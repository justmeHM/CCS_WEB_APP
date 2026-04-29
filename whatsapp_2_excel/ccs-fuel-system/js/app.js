/**
 * js/app.js
 * Application bootstrap — the single entry point.
 * Runs after all modules and pages are loaded.
 *
 * Responsibility:
 *   1. Check auth gate
 *   2. Build layout (sidebar, topbar)
 *   3. Navigate to default page
 *   4. Start autosave loop
 *   5. Register auth screen HTML
 *   6. Kick off guided tour (first visit)
 */

'use strict';

(function () {
  // ── Register auth screens HTML ──────────────────────────────────────────
  function _buildAuthScreens() {
    const loginScreen  = document.getElementById('loginScreen');
    const signupScreen = document.getElementById('signupScreen');

    if (loginScreen) {
      loginScreen.innerHTML = `
        <div class="auth-card" style="width:100%;max-width:420px;">
          <button class="auth-back-btn" onclick="CCS.Auth.showLanding()">
            <i class="fa-regular fa-arrow-left"></i> Back
          </button>
          <h2 class="auth-title">Welcome back</h2>
          <p class="auth-subtitle">Sign in to your CCS account</p>
          <div class="auth-error" id="loginError"></div>
          <div class="auth-field">
            <label class="auth-label">Email</label>
            <input type="email" class="auth-input" id="loginEmail" placeholder="name@ccszambia.com"
                   autocomplete="email" onkeydown="if(event.key==='Enter')CCS.Auth.doLogin()">
            <div class="auth-domain-hint"><i class="fa-regular fa-info-circle"></i> Must be @ccszambia.com</div>
          </div>
          <div class="auth-field">
            <label class="auth-label">Password</label>
            <div class="pw-wrapper">
              <input type="password" class="auth-input" id="loginPassword" placeholder="••••••••"
                     autocomplete="current-password" onkeydown="if(event.key==='Enter')CCS.Auth.doLogin()">
              <button class="pw-toggle" onclick="CCS.Auth.togglePw('loginPassword',this)" type="button">
                <i class="fa-regular fa-eye"></i>
              </button>
            </div>
          </div>
          <button class="auth-btn" id="loginBtn" data-label="Sign In" onclick="CCS.Auth.doLogin()">Sign In</button>
          <div class="auth-switch">Don't have an account? <a onclick="CCS.Auth.showSignup()">Create one</a></div>
        </div>`;
    }

    if (signupScreen) {
      signupScreen.innerHTML = `
        <div class="auth-card" style="width:100%;max-width:420px;">
          <button class="auth-back-btn" onclick="CCS.Auth.showLanding()">
            <i class="fa-regular fa-arrow-left"></i> Back
          </button>
          <h2 class="auth-title">Create account</h2>
          <p class="auth-subtitle">Join CCS Fuel System</p>
          <div class="auth-error" id="signupError"></div>
          <div class="auth-field">
            <label class="auth-label">Email</label>
            <input type="email" class="auth-input" id="signupEmail" placeholder="name@ccszambia.com"
                   autocomplete="email">
            <div class="auth-domain-hint"><i class="fa-regular fa-info-circle"></i> Must be @ccszambia.com</div>
          </div>
          <div class="auth-field">
            <label class="auth-label">Password</label>
            <div class="pw-wrapper">
              <input type="password" class="auth-input" id="signupPassword" placeholder="Min 8 characters"
                     autocomplete="new-password">
              <button class="pw-toggle" onclick="CCS.Auth.togglePw('signupPassword',this)" type="button">
                <i class="fa-regular fa-eye"></i>
              </button>
            </div>
          </div>
          <div class="auth-field">
            <label class="auth-label">Confirm Password</label>
            <div class="pw-wrapper">
              <input type="password" class="auth-input" id="signupConfirm" placeholder="Repeat password"
                     autocomplete="new-password" onkeydown="if(event.key==='Enter')CCS.Auth.doSignup()">
              <button class="pw-toggle" onclick="CCS.Auth.togglePw('signupConfirm',this)" type="button">
                <i class="fa-regular fa-eye"></i>
              </button>
            </div>
          </div>
          <button class="auth-btn" id="signupBtn" data-label="Create Account" onclick="CCS.Auth.doSignup()">Create Account</button>
          <div class="auth-switch">Already have an account? <a onclick="CCS.Auth.showLogin()">Sign in</a></div>
          <p class="text-xs mt-4 text-center" style="color:rgba(255,255,255,0.4);">
            The first registered account automatically becomes admin.
          </p>
        </div>`;
    }
  }

  // ── Link up remaining page modules ──────────────────────────────────────
  // All-pages.js defines multiple pages on CCS.Pages.
  // The pages from dedicated files (dashboard.js, orders.js, daily.js) are
  // already attached. Remaining pages are in all-pages.js which also uses
  // CCS.Pages = CCS.Pages || {} so they all coexist.

  // ── Autosave loop ───────────────────────────────────────────────────────
  let _autosaveInterval;
  function startAutosave(intervalMs = 60000) {
    clearInterval(_autosaveInterval);
    _autosaveInterval = setInterval(() => {
      CCS.Layout.save();
    }, intervalMs);
  }

  // ── App init ─────────────────────────────────────────────────────────────
  function init() {
    CCS.Layout.init();
    CCS.Router.go('dashboard', { skipTransition: true });
    startAutosave();
    CCS.Notifications.refresh();
    // Start tour after a brief delay so page renders first
    setTimeout(() => CCS.Tour.start(), 1500);
  }

  // ── Boot ─────────────────────────────────────────────────────────────────
  function boot() {
    _buildAuthScreens();
    const authed = CCS.Auth.gate();
    if (authed) init();
  }

  // Expose init so Auth.enterApp can call it after login/signup
  CCS.App = { init, boot };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
