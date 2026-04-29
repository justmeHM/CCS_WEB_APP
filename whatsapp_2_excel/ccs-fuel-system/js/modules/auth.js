/**
 * js/modules/auth.js
 * Authentication: session management, login, signup, admin checks.
 * All user records live in a separate localStorage key from the main DB.
 */

'use strict';

(function () {
  const USERS_KEY   = 'ccs_auth_users_v1';
  const SESSION_KEY = 'ccs_auth_session_v1';
  const ALLOWED_DOMAIN = 'ccszambia.com';

  // ── Persistence helpers ──────────────────────────────────────────────────
  function getUsers()       { try { return JSON.parse(localStorage.getItem(USERS_KEY)) || []; } catch { return []; } }
  function saveUsers(users) { localStorage.setItem(USERS_KEY, JSON.stringify(users)); }
  function getSession()     { try { return JSON.parse(localStorage.getItem(SESSION_KEY)); } catch { return null; } }
  function setSession(email){ localStorage.setItem(SESSION_KEY, JSON.stringify({ email, at: Date.now() })); }
  function clearSession()   { localStorage.removeItem(SESSION_KEY); }

  function isAdmin() {
    const session = getSession();
    if (!session) return false;
    return getUsers().find(u => u.email === session.email)?.isAdmin || false;
  }

  function validateDomain(email) {
    return email.endsWith('@' + ALLOWED_DOMAIN);
  }

  // ── UI helpers ────────────────────────────────────────────────────────────
  function showScreen(id) {
    document.querySelectorAll('.auth-screen').forEach(s => s.classList.remove('active'));
    const target = document.getElementById(id);
    if (target) target.classList.add('active');
  }

  function showError(formId, msg) {
    const el = document.getElementById(formId + 'Error');
    if (!el) return;
    el.textContent = msg;
    el.classList.add('visible');
  }

  function clearError(formId) {
    const el = document.getElementById(formId + 'Error');
    if (el) { el.textContent = ''; el.classList.remove('visible'); }
  }

  function setLoading(btnId, loading) {
    const btn = document.getElementById(btnId);
    if (!btn) return;
    btn.disabled = loading;
    btn.textContent = loading ? 'Please wait…' : btn.dataset.label;
  }

  function togglePw(inputId, btn) {
    const input = document.getElementById(inputId);
    if (!input) return;
    const show = input.type === 'password';
    input.type = show ? 'text' : 'password';
    btn.innerHTML = show ? '<i class="fa-regular fa-eye-slash"></i>' : '<i class="fa-regular fa-eye"></i>';
  }

  // ── Enter the app after successful auth ───────────────────────────────────
  function enterApp(user) {
    document.getElementById('authOverlay')?.classList.add('hidden');
    const initial  = user.email.charAt(0).toUpperCase();
    const namePart = user.email.split('@')[0];

    CCS.dom.html('authUserAvatarSm',  initial);
    CCS.dom.html('authUserPillName',  namePart);
    CCS.dom.html('authDropdownName',  namePart);
    CCS.dom.html('authDropdownEmail', user.email);

    if (user.isAdmin) {
      CCS.dom.show('authAdminMenuItem');
      CCS.dom.show('sidebarAdminBtn');
    }
  }

  // ── Landing screen ────────────────────────────────────────────────────────
  function renderLanding() {
    const el = document.getElementById('landingScreen');
    if (!el) return;
    el.innerHTML = `
      <div style="text-align:center;color:white;max-width:680px;padding:var(--space-8) var(--space-6);">
        <div style="display:inline-flex;align-items:center;justify-content:center;width:72px;height:72px;
             border-radius:var(--radius-2xl);background:linear-gradient(135deg,var(--accent-600),var(--accent-800));
             margin-bottom:var(--space-5);box-shadow:0 12px 32px rgba(196,30,58,0.4);">
          <i class="fa-regular fa-gas-pump" style="font-size:1.75rem;color:white;"></i>
        </div>
        <h1 style="font-size:var(--text-4xl);font-weight:800;letter-spacing:-0.04em;margin-bottom:var(--space-3);">
          CCS Fuel System
        </h1>
        <p style="font-size:var(--text-lg);color:rgba(255,255,255,0.7);margin-bottom:var(--space-8);line-height:var(--leading-relaxed);">
          Enterprise fuel allocation &amp; technician management platform for CCS Zambia.
        </p>
        <div style="display:flex;gap:var(--space-3);justify-content:center;flex-wrap:wrap;">
          <button class="btn btn-primary btn-lg" onclick="CCS.Auth.showLogin()">
            <i class="fa-regular fa-arrow-right-to-bracket"></i> Sign In
          </button>
          <button class="btn btn-secondary btn-lg" onclick="CCS.Auth.showSignup()">
            <i class="fa-regular fa-user-plus"></i> Create Account
          </button>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:var(--space-4);margin-top:var(--space-8);">
          ${[
            ['fa-chart-line',  'Live Dashboard',          'Real-time KPIs across all regions'],
            ['fa-whatsapp fa-brands', 'WhatsApp Parser',  'Paste field reports to auto-enter data'],
            ['fa-file-excel',  'Excel Automation',        'Write xlsx without opening Excel'],
            ['fa-users',       'Technician Management',   'Allocate fuel and track targets'],
          ].map(([icon, title, desc]) => `
            <div style="background:rgba(255,255,255,0.07);border-radius:var(--radius-xl);padding:var(--space-4);text-align:left;">
              <i class="fa-regular ${icon}" style="font-size:1.25rem;color:var(--accent-300);margin-bottom:var(--space-2);display:block;"></i>
              <div style="font-weight:600;margin-bottom:4px;font-size:var(--text-sm);">${title}</div>
              <div style="font-size:var(--text-xs);color:rgba(255,255,255,0.55);">${desc}</div>
            </div>`).join('')}
        </div>
      </div>`;
  }

  // ── Login ─────────────────────────────────────────────────────────────────
  async function doLogin() {
    const email    = document.getElementById('loginEmail')?.value.trim().toLowerCase();
    const password = document.getElementById('loginPassword')?.value;
    clearError('login');

    if (!email || !validateDomain(email)) return showError('login', 'Enter a valid @ccszambia.com email.');
    if (!password) return showError('login', 'Password is required.');

    const users = getUsers();
    const user  = users.find(u => u.email === email);
    if (!user) return showError('login', 'No account found for this email.');

    const hash = await CCS.utils.sha256(password);
    if (hash !== user.passwordHash) return showError('login', 'Incorrect password.');

    setSession(email);
    enterApp(user);
    CCS.App?.init();
  }

  // ── Signup ────────────────────────────────────────────────────────────────
  async function doSignup() {
    const email   = document.getElementById('signupEmail')?.value.trim().toLowerCase();
    const pw      = document.getElementById('signupPassword')?.value;
    const confirm = document.getElementById('signupConfirm')?.value;
    clearError('signup');

    if (!email || !validateDomain(email)) return showError('signup', 'Use a valid @ccszambia.com email.');
    if (pw.length < 8)                    return showError('signup', 'Password must be at least 8 characters.');
    if (pw !== confirm)                   return showError('signup', 'Passwords do not match.');

    const users = getUsers();
    if (users.find(u => u.email === email)) return showError('signup', 'An account with this email already exists.');

    const hash       = await CCS.utils.sha256(pw);
    const isFirst    = users.length === 0;
    const newUser    = { email, passwordHash: hash, isAdmin: isFirst, createdAt: new Date().toISOString() };
    users.push(newUser);
    saveUsers(users);
    setSession(email);
    enterApp(newUser);
    CCS.App?.init();
  }

  // ── Logout ────────────────────────────────────────────────────────────────
  function doLogout() {
    clearSession();
    document.getElementById('authOverlay')?.classList.remove('hidden');
    showScreen('landingScreen');
    ['loginEmail','loginPassword'].forEach(id => { const el = document.getElementById(id); if (el) el.value = ''; });
  }

  // ── Auth gate (called on page load) ──────────────────────────────────────
  function gate() {
    const session = getSession();
    if (session) {
      const user = getUsers().find(u => u.email === session.email);
      if (user) { enterApp(user); return true; }
    }
    document.getElementById('authOverlay')?.classList.remove('hidden');
    renderLanding();
    showScreen('landingScreen');
    return false;
  }

  // ── Admin: add / toggle / delete user ────────────────────────────────────
  async function adminAddUser(email, password, makeAdmin) {
    if (!email || !validateDomain(email)) return CCS.Toast.show('Enter a valid @ccszambia.com email', 'error');
    if (password.length < 8)             return CCS.Toast.show('Password must be at least 8 characters', 'warning');
    const users = getUsers();
    if (users.find(u => u.email === email)) return CCS.Toast.show('User already exists', 'warning');
    const hash = await CCS.utils.sha256(password);
    users.push({ email, passwordHash: hash, isAdmin: !!makeAdmin, createdAt: new Date().toISOString() });
    saveUsers(users);
    CCS.Toast.show('User added: ' + email, 'success');
  }

  function adminToggleRole(idx) {
    const users = getUsers();
    if (!users[idx]) return;
    users[idx].isAdmin = !users[idx].isAdmin;
    saveUsers(users);
    CCS.Toast.show((users[idx].isAdmin ? 'Admin granted to ' : 'Admin revoked from ') + users[idx].email);
  }

  function adminDeleteUser(idx) {
    const users = getUsers();
    if (!users[idx]) return false;
    const email = users[idx].email;
    users.splice(idx, 1);
    saveUsers(users);
    CCS.Toast.show('User removed: ' + email);
    return true;
  }

  // ── Dropdown toggle ───────────────────────────────────────────────────────
  function toggleDropdown() { document.getElementById('authUserDropdown')?.classList.toggle('open'); }
  function closeDropdown()  { document.getElementById('authUserDropdown')?.classList.remove('open'); }

  document.addEventListener('click', e => {
    const pill = document.getElementById('authUserPill');
    const dd   = document.getElementById('authUserDropdown');
    if (dd && pill && !pill.contains(e.target)) closeDropdown();
  });

  // ── Public API ────────────────────────────────────────────────────────────
  CCS.Auth = {
    gate,
    doLogin,
    doSignup,
    doLogout,
    toggleDropdown,
    closeDropdown,
    togglePw,
    showLogin:  () => showScreen('loginScreen'),
    showSignup: () => showScreen('signupScreen'),
    showLanding:() => { renderLanding(); showScreen('landingScreen'); },
    clearError,
    isAdmin,
    getUsers,
    saveUsers,
    getSession,
    adminAddUser,
    adminToggleRole,
    adminDeleteUser,
  };
})();
