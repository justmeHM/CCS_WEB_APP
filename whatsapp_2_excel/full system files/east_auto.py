<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=yes" />
  <meta name="theme-color" content="#C41E3A" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <title>CCS Fuel System · Enterprise</title>
  
  <!-- Preload critical assets -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preconnect" href="https://cdn.tailwindcss.com" />
  
  <!-- Core dependencies -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/xlsx/dist/xlsx.full.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js"></script>
  
  <!-- Typography - Industry standard SF Pro with fallbacks -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
  
  <!-- Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  
  <style>
    /* ===== DESIGN SYSTEM - INDUSTRY STANDARD ===== */
    :root {
      /* Typography - Modular Scale (1.25 ratio) */
      --text-xs: 0.75rem;     /* 12px */
      --text-sm: 0.875rem;    /* 14px */
      --text-base: 1rem;      /* 16px */
      --text-lg: 1.125rem;    /* 18px */
      --text-xl: 1.25rem;     /* 20px */
      --text-2xl: 1.5rem;     /* 24px */
      --text-3xl: 2rem;       /* 32px */
      --text-4xl: 2.5rem;     /* 40px */
      
      /* Line heights */
      --leading-tight: 1.2;
      --leading-normal: 1.5;
      --leading-relaxed: 1.75;
      
      /* Font families */
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
      --font-mono: 'JetBrains Mono', 'SF Mono', monospace;
      
      /* Spacing - 8px grid system */
      --space-1: 0.25rem;  /* 4px */
      --space-2: 0.5rem;   /* 8px */
      --space-3: 0.75rem;  /* 12px */
      --space-4: 1rem;     /* 16px */
      --space-5: 1.5rem;   /* 24px */
      --space-6: 2rem;     /* 32px */
      --space-8: 3rem;     /* 48px */
      --space-10: 4rem;    /* 64px */
      --space-12: 5rem;    /* 80px */
      
      /* Border radius */
      --radius-sm: 0.375rem;   /* 6px */
      --radius-md: 0.5rem;     /* 8px */
      --radius-lg: 0.75rem;    /* 12px */
      --radius-xl: 1rem;       /* 16px */
      --radius-2xl: 1.5rem;    /* 24px */
      --radius-full: 9999px;
      
      /* Primary palette - refined corporate */
      --primary-900: #0A1A2F;
      --primary-800: #122B45;
      --primary-700: #1E3A5A;
      --primary-600: #2B4A70;
      --primary-500: #3A5B85;
      --primary-400: #4F73A0;
      
      /* Accent - sophisticated crimson */
      --accent-900: #7A1F2D;
      --accent-800: #9B2C3A;
      --accent-700: #B43A48;
      --accent-600: #C41E3A;
      --accent-500: #D43B54;
      --accent-400: #E35D72;
      --accent-300: #EC8A9B;
      --accent-200: #F5C0C8;
      --accent-100: #FAEAEC;
      --accent-50:  #FDF5F6;
      
      /* Status colors - standardized semantics */
      --status-success: #16a34a;
      --status-success-bg: #22c55e20;
      --status-warning: #d97706;
      --status-warning-bg: #f59e0b20;
      --status-danger: #dc2626;
      --status-danger-bg: #ef444420;
      --status-info: #2563eb;
      --status-info-bg: #3b82f620;
      --status-unassigned: #6b7280;
      --status-unassigned-bg: #9ca3af20;
      
      /* Neutrals - premium */
      --neutral-50: #F9FAFC;
      --neutral-100: #F2F5F9;
      --neutral-200: #E9EEF3;
      --neutral-300: #DCE3EB;
      --neutral-400: #B8C3D1;
      --neutral-500: #8F9BAE;
      --neutral-600: #667085;
      --neutral-700: #475467;
      --neutral-800: #2C3A4B;
      --neutral-900: #1A2634;
      
      /* Glass effects */
      --glass-bg: rgba(255, 255, 255, 0.72);
      --glass-border: rgba(255, 255, 255, 0.5);
      --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
      
      /* Shadows - consistent elevation */
      --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.05);
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.04);
      --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.08);
      --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.12);
      --shadow-xl: 0 24px 64px rgba(0, 0, 0, 0.16);
      
      /* Animation timings */
      --transition-fast: 150ms;
      --transition-base: 250ms;
      --transition-slow: 350ms;
      --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
      --ease-out: cubic-bezier(0.4, 0, 0.2, 1);
      --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ===== TYPOGRAPHY UTILITIES ===== */
    .text-xs { font-size: var(--text-xs); line-height: var(--leading-normal); }
    .text-sm { font-size: var(--text-sm); line-height: var(--leading-normal); }
    .text-base { font-size: var(--text-base); line-height: var(--leading-normal); }
    .text-lg { font-size: var(--text-lg); line-height: var(--leading-tight); }
    .text-xl { font-size: var(--text-xl); line-height: var(--leading-tight); }
    .text-2xl { font-size: var(--text-2xl); line-height: var(--leading-tight); }
    .text-3xl { font-size: var(--text-3xl); line-height: var(--leading-tight); }
    .text-4xl { font-size: var(--text-4xl); line-height: var(--leading-tight); }
    
    .font-light { font-weight: 300; }
    .font-normal { font-weight: 400; }
    .font-medium { font-weight: 500; }
    .font-semibold { font-weight: 600; }
    .font-bold { font-weight: 700; }
    
    .tracking-tight { letter-spacing: -0.02em; }
    .tracking-normal { letter-spacing: 0; }
    .tracking-wide { letter-spacing: 0.02em; }
    
    .font-mono { font-family: var(--font-mono); }
    
    /* ===== SPACING UTILITIES ===== */
    .p-1 { padding: var(--space-1); }
    .p-2 { padding: var(--space-2); }
    .p-3 { padding: var(--space-3); }
    .p-4 { padding: var(--space-4); }
    .p-5 { padding: var(--space-5); }
    .p-6 { padding: var(--space-6); }
    
    .px-1 { padding-left: var(--space-1); padding-right: var(--space-1); }
    .px-2 { padding-left: var(--space-2); padding-right: var(--space-2); }
    .px-3 { padding-left: var(--space-3); padding-right: var(--space-3); }
    .px-4 { padding-left: var(--space-4); padding-right: var(--space-4); }
    .px-5 { padding-left: var(--space-5); padding-right: var(--space-5); }
    .px-6 { padding-left: var(--space-6); padding-right: var(--space-6); }
    
    .py-1 { padding-top: var(--space-1); padding-bottom: var(--space-1); }
    .py-2 { padding-top: var(--space-2); padding-bottom: var(--space-2); }
    .py-3 { padding-top: var(--space-3); padding-bottom: var(--space-3); }
    .py-4 { padding-top: var(--space-4); padding-bottom: var(--space-4); }
    .py-5 { padding-top: var(--space-5); padding-bottom: var(--space-5); }
    .py-6 { padding-top: var(--space-6); padding-bottom: var(--space-6); }
    
    .m-1 { margin: var(--space-1); }
    .m-2 { margin: var(--space-2); }
    .m-3 { margin: var(--space-3); }
    .m-4 { margin: var(--space-4); }
    
    .mt-1 { margin-top: var(--space-1); }
    .mt-2 { margin-top: var(--space-2); }
    .mt-3 { margin-top: var(--space-3); }
    .mt-4 { margin-top: var(--space-4); }
    .mt-5 { margin-top: var(--space-5); }
    .mt-6 { margin-top: var(--space-6); }
    
    .mb-1 { margin-bottom: var(--space-1); }
    .mb-2 { margin-bottom: var(--space-2); }
    .mb-3 { margin-bottom: var(--space-3); }
    .mb-4 { margin-bottom: var(--space-4); }
    .mb-5 { margin-bottom: var(--space-5); }
    .mb-6 { margin-bottom: var(--space-6); }
    
    .gap-1 { gap: var(--space-1); }
    .gap-2 { gap: var(--space-2); }
    .gap-3 { gap: var(--space-3); }
    .gap-4 { gap: var(--space-4); }
    .gap-5 { gap: var(--space-5); }
    
    /* ===== LAYOUT UTILITIES ===== */
    .flex { display: flex; }
    .flex-col { flex-direction: column; }
    .flex-wrap { flex-wrap: wrap; }
    .items-center { align-items: center; }
    .items-start { align-items: flex-start; }
    .items-end { align-items: flex-end; }
    .justify-between { justify-content: space-between; }
    .justify-end { justify-content: flex-end; }
    .justify-center { justify-content: center; }
    .flex-1 { flex: 1; }
    
    .grid { display: grid; }
    .grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
    .grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
    .grid-cols-4 { grid-template-columns: repeat(4, 1fr); }
    .grid-cols-5 { grid-template-columns: repeat(5, 1fr); }
    
    .w-full { width: 100%; }
    .h-full { height: 100%; }
    .text-center { text-align: center; }
    .text-left { text-align: left; }
    .text-right { text-align: right; }
    
    /* ===== ANIMATIONS - SPRING PHYSICS ===== */
    @keyframes spring-pop {
      0% { transform: scale(0.9); opacity: 0; }
      40% { transform: scale(1.02); }
      70% { transform: scale(0.99); }
      100% { transform: scale(1); opacity: 1; }
    }
    
    @keyframes spring-slide {
      0% { transform: translateY(20px) scale(0.95); opacity: 0; }
      40% { transform: translateY(-2px) scale(1.01); }
      70% { transform: translateY(2px) scale(0.99); }
      100% { transform: translateY(0) scale(1); opacity: 1; }
    }
    
    @keyframes spring-scale {
      0% { transform: scale(0.95); opacity: 0; }
      50% { transform: scale(1.02); }
      100% { transform: scale(1); opacity: 1; }
    }
    
    @keyframes shimmer {
      0% { transform: translateX(-100%); }
      100% { transform: translateX(100%); }
    }
    
    @keyframes pulse-subtle {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.8; }
    }
    
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
    
    @keyframes slideUp {
      from { transform: translateY(20px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
      from { transform: translateX(20px); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes toastProgress {
      from { width: 100%; }
      to { width: 0%; }
    }
    
    @keyframes autosavePulse {
      0% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.6); opacity: 0.5; }
      100% { transform: scale(1); opacity: 1; }
    }
    
    @keyframes amberPulse {
      0%, 100% { box-shadow: 0 0 0 0 rgba(212,122,62,0.45); }
      50% { box-shadow: 0 0 0 7px rgba(212,122,62,0); }
    }
    
    @keyframes pageEnter {
      from { opacity: 0; transform: translateY(12px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pageExit {
      from { opacity: 1; transform: translateY(0); }
      to { opacity: 0; transform: translateY(-8px); }
    }
    
    .animate-spring-pop { animation: spring-pop 0.4s var(--ease-spring) both; }
    .animate-spring-slide { animation: spring-slide 0.4s var(--ease-spring) both; }
    .animate-fade-in { animation: fadeIn 0.3s var(--ease-out) both; }
    .animate-slide-up { animation: slideUp 0.4s var(--ease-out) both; }
    .animate-slide-right { animation: slideInRight 0.3s var(--ease-out) both; }
    
    .page-entering { animation: pageEnter 0.32s var(--ease-out) both; }
    .page-exiting { animation: pageExit 0.18s var(--ease-in-out) both; pointer-events: none; }

    /* ===== RESET & BASE ===== */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    *:focus-visible {
      outline: 2px solid var(--accent-600);
      outline-offset: 2px;
      border-radius: var(--radius-sm);
    }
    
    body {
      font-family: var(--font-sans);
      font-size: var(--text-base);
      line-height: var(--leading-normal);
      background: linear-gradient(135deg, var(--neutral-50) 0%, var(--neutral-100) 100%);
      color: var(--neutral-900);
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    
    /* ===== TYPOGRAPHY ELEMENTS ===== */
    h1, h2, h3, h4, h5, h6 {
      font-family: var(--font-sans);
      font-weight: 600;
      letter-spacing: -0.02em;
      line-height: var(--leading-tight);
    }
    
    h1 { font-size: var(--text-3xl); }
    h2 { font-size: var(--text-2xl); }
    h3 { font-size: var(--text-xl); }
    h4 { font-size: var(--text-lg); }
    
    /* ===== CARDS & ELEVATION ===== */
    .card {
      background: white;
      border-radius: var(--radius-xl);
      padding: var(--space-5);
      box-shadow: var(--shadow-sm);
      transition: transform var(--transition-base) var(--ease-spring),
                  box-shadow var(--transition-base) var(--ease-out),
                  border-color var(--transition-base) var(--ease-out);
      border: 1px solid var(--neutral-200);
      position: relative;
      overflow: hidden;
    }
    
    .card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 2px;
      background: linear-gradient(90deg, var(--accent-600), var(--accent-400));
      opacity: 0;
      transition: opacity var(--transition-base) var(--ease-out);
    }
    
    .card:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: var(--neutral-300);
    }
    
    .card:hover::before {
      opacity: 1;
    }
    
    .card-glass {
      background: var(--glass-bg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--glass-border);
      box-shadow: var(--glass-shadow);
    }
    
    /* ===== BUTTONS ===== */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: var(--space-2);
      padding: var(--space-3) var(--space-5);
      border-radius: var(--radius-full);
      font-family: var(--font-sans);
      font-weight: 500;
      font-size: var(--text-sm);
      border: none;
      cursor: pointer;
      transition: all var(--transition-base) var(--ease-spring);
      position: relative;
      overflow: hidden;
      white-space: nowrap;
    }
    
    .btn::after {
      content: '';
      position: absolute;
      top: 50%;
      left: 50%;
      width: 0;
      height: 0;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.3);
      transform: translate(-50%, -50%);
      transition: width 0.6s, height 0.6s;
    }
    
    .btn:active::after {
      width: 300px;
      height: 300px;
    }
    
    .btn-primary {
      background: linear-gradient(135deg, var(--accent-700), var(--accent-600));
      color: white;
      box-shadow: 0 4px 12px rgba(196, 30, 58, 0.3);
    }
    
    .btn-primary:hover {
      transform: translateY(-1px);
      box-shadow: 0 8px 20px rgba(196, 30, 58, 0.4);
    }
    
    .btn-primary:active {
      transform: translateY(0);
    }
    
    .btn-secondary {
      background: white;
      color: var(--neutral-800);
      border: 1px solid var(--neutral-300);
      box-shadow: var(--shadow-xs);
    }
    
    .btn-secondary:hover {
      background: var(--neutral-50);
      border-color: var(--neutral-400);
      transform: translateY(-1px);
      box-shadow: var(--shadow-sm);
    }
    
    .btn-ghost {
      background: transparent;
      color: var(--neutral-700);
    }
    
    .btn-ghost:hover {
      background: var(--neutral-100);
    }
    
    .btn-sm {
      padding: var(--space-2) var(--space-4);
      font-size: var(--text-xs);
    }
    
    .btn-lg {
      padding: var(--space-4) var(--space-6);
      font-size: var(--text-base);
    }
    
    .btn-icon {
      width: 40px;
      height: 40px;
      padding: 0;
      border-radius: var(--radius-full);
    }
    
    /* ===== INPUTS ===== */
    .input-group {
      position: relative;
      margin-bottom: var(--space-4);
    }
    
    .input-wrapper {
      position: relative;
    }
    
    .input-field {
      width: 100%;
      padding: var(--space-4) var(--space-4) var(--space-2);
      border: 1.5px solid var(--neutral-200);
      border-radius: var(--radius-lg);
      font-family: var(--font-sans);
      font-size: var(--text-sm);
      background: white;
      transition: border-color var(--transition-fast) var(--ease-out),
                  box-shadow var(--transition-fast) var(--ease-out);
      outline: none;
    }
    
    .input-field:focus {
      border-color: var(--accent-600);
      box-shadow: 0 0 0 4px rgba(196, 30, 58, 0.1);
    }
    
    .input-field.error {
      border-color: var(--status-danger);
    }
    
    .input-field.error:focus {
      box-shadow: 0 0 0 4px rgba(220, 38, 38, 0.1);
    }
    
    .input-field.success {
      border-color: var(--status-success);
    }
    
    .input-field.success:focus {
      box-shadow: 0 0 0 4px rgba(22, 163, 74, 0.1);
    }
    
    .input-label {
      position: absolute;
      left: var(--space-4);
      top: var(--space-4);
      font-size: var(--text-sm);
      color: var(--neutral-500);
      transition: all var(--transition-fast) var(--ease-out);
      pointer-events: none;
      background: white;
      padding: 0 var(--space-1);
    }
    
    .input-field:focus ~ .input-label,
    .input-field:not(:placeholder-shown) ~ .input-label {
      transform: translateY(-20px) scale(0.85);
      color: var(--accent-600);
      font-weight: 500;
    }
    
    .input-field::placeholder {
      color: transparent;
    }
    
    /* Validation icons */
    .input-wrapper::after {
      content: '';
      position: absolute;
      right: var(--space-3);
      top: 50%;
      transform: translateY(-50%);
      width: 20px;
      height: 20px;
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      opacity: 0;
      transition: opacity var(--transition-fast) var(--ease-out);
    }
    
    .input-wrapper.has-error::after {
      opacity: 1;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23dc2626'%3E%3Cpath d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z'/%3E%3C/svg%3E");
    }
    
    .input-wrapper.has-success::after {
      opacity: 1;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%2316a34a'%3E%3Cpath d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z'/%3E%3C/svg%3E");
    }
    
    /* ===== SELECT ===== */
    .select-wrapper {
      position: relative;
    }
    
    .select-wrapper::after {
      content: '\f107';
      font-family: 'Font Awesome 6 Free';
      font-weight: 900;
      position: absolute;
      right: var(--space-4);
      top: 50%;
      transform: translateY(-50%);
      color: var(--neutral-500);
      pointer-events: none;
    }
    
    .select-field {
      width: 100%;
      padding: var(--space-3) var(--space-4);
      border: 1.5px solid var(--neutral-200);
      border-radius: var(--radius-lg);
      font-family: var(--font-sans);
      font-size: var(--text-sm);
      background: white;
      appearance: none;
      cursor: pointer;
      transition: all var(--transition-fast) var(--ease-out);
    }
    
    .select-field:focus {
      border-color: var(--accent-600);
      box-shadow: 0 0 0 4px rgba(196, 30, 58, 0.1);
      outline: none;
    }
    
    /* ===== BADGES ===== */
    .badge {
      display: inline-flex;
      align-items: center;
      padding: var(--space-1) var(--space-3);
      border-radius: var(--radius-full);
      font-family: var(--font-sans);
      font-weight: 500;
      font-size: var(--text-xs);
      letter-spacing: 0.02em;
      line-height: 1.4;
      gap: var(--space-1);
      white-space: nowrap;
    }
    
    .badge-success {
      background: var(--status-success-bg);
      color: var(--status-success);
      border: 1px solid var(--status-success);
    }
    
    .badge-warning {
      background: var(--status-warning-bg);
      color: var(--status-warning);
      border: 1px solid var(--status-warning);
    }
    
    .badge-danger {
      background: var(--status-danger-bg);
      color: var(--status-danger);
      border: 1px solid var(--status-danger);
    }
    
    .badge-info {
      background: var(--status-info-bg);
      color: var(--status-info);
      border: 1px solid var(--status-info);
    }
    
    .badge-neutral {
      background: var(--status-unassigned-bg);
      color: var(--status-unassigned);
      border: 1px solid var(--status-unassigned);
    }
    
    /* ===== MODALS ===== */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(26, 38, 52, 0.6);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      opacity: 0;
      visibility: hidden;
      transition: all var(--transition-base) var(--ease-out);
    }
    
    .modal-overlay.active {
      opacity: 1;
      visibility: visible;
    }
    
    .modal-container {
      background: white;
      border-radius: var(--radius-2xl);
      box-shadow: var(--shadow-xl);
      width: 90%;
      max-width: 500px;
      max-height: 90vh;
      overflow-y: auto;
      transform: scale(0.95) translateY(20px);
      transition: all var(--transition-slow) var(--ease-spring);
    }
    
    .modal-overlay.active .modal-container {
      transform: scale(1) translateY(0);
      animation: spring-pop 0.4s var(--ease-spring);
    }
    
    .modal-header {
      padding: var(--space-5) var(--space-6);
      border-bottom: 1px solid var(--neutral-200);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    
    .modal-body {
      padding: var(--space-6);
    }
    
    .modal-footer {
      padding: var(--space-4) var(--space-6);
      border-top: 1px solid var(--neutral-200);
      display: flex;
      gap: var(--space-3);
      justify-content: flex-end;
    }
    
    /* ===== PAGE HEADER ===== */
    .page-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: var(--space-4);
      flex-wrap: wrap;
    }
    #autoDropZone:hover {
      border-color: var(--accent-600) !important;
      background: var(--accent-50);
    }

    /* ===== TABLES ===== */
    .table-container {
      border-radius: var(--radius-lg);
      border: 1px solid var(--neutral-200);
      overflow: auto;
      background: white;
    }
    
    .table {
      width: 100%;
      border-collapse: collapse;
      font-size: var(--text-sm);
    }
    
    .table th {
      background: var(--neutral-50);
      padding: var(--space-4) var(--space-4);
      text-align: left;
      font-family: var(--font-sans);
      font-weight: 600;
      font-size: var(--text-xs);
      letter-spacing: 0.02em;
      text-transform: uppercase;
      color: var(--neutral-600);
      border-bottom: 1px solid var(--neutral-200);
      position: sticky;
      top: 0;
      backdrop-filter: blur(8px);
    }
    
    .table td {
      padding: var(--space-4) var(--space-4);
      border-bottom: 1px solid var(--neutral-200);
      color: var(--neutral-800);
    }
    
    .table tbody tr {
      transition: background var(--transition-fast) var(--ease-out);
    }
    
    .table tbody tr:hover {
      background: var(--neutral-50);
    }
    
    .table tbody tr:last-child td {
      border-bottom: none;
    }
    
    /* Mobile table cards */
    @media (max-width: 768px) {
      .table-container {
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
      }
      
      .table {
        min-width: 600px;
      }
      
      .mobile-table-cards {
        display: block;
      }
      
      .mobile-table-cards .table-row {
        display: block;
        background: white;
        border-radius: var(--radius-lg);
        padding: var(--space-4);
        margin-bottom: var(--space-3);
        border: 1px solid var(--neutral-200);
      }
      
      .mobile-table-cards .table-cell {
        display: flex;
        justify-content: space-between;
        padding: var(--space-2) 0;
        border-bottom: 1px solid var(--neutral-100);
      }
      
      .mobile-table-cards .table-cell:last-child {
        border-bottom: none;
      }
      
      .mobile-table-cards .cell-label {
        font-weight: 500;
        color: var(--neutral-600);
        font-size: var(--text-xs);
      }
      
      .mobile-table-cards .cell-value {
        font-weight: 600;
      }
    }
    
    /* ===== SORTABLE TABLE HEADERS ===== */
    .table th.sortable {
      cursor: pointer;
      user-select: none;
      transition: background var(--transition-fast), color var(--transition-fast);
    }
    
    .table th.sortable:hover {
      background: var(--neutral-100);
      color: var(--neutral-900);
    }
    
    .table th.sortable .sort-icon {
      display: inline-block;
      margin-left: var(--space-1);
      opacity: 0.3;
      transition: opacity var(--transition-fast), transform var(--transition-fast);
      font-style: normal;
    }
    
    .table th.sortable.sort-asc .sort-icon {
      opacity: 1;
    }
    
    .table th.sortable.sort-desc .sort-icon {
      opacity: 1;
      transform: rotate(180deg);
    }
    
    /* ===== PROGRESS BARS ===== */
    .progress-bar {
      height: 8px;
      background: var(--neutral-200);
      border-radius: var(--radius-full);
      overflow: hidden;
      position: relative;
    }
    
    .progress-fill {
      height: 100%;
      border-radius: var(--radius-full);
      transition: width var(--transition-slow) var(--ease-spring);
      position: relative;
      overflow: hidden;
      background: linear-gradient(90deg, var(--accent-600), var(--accent-400));
    }
    
    .progress-fill::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
      transform: translateX(-100%);
      animation: shimmer 1.5s infinite;
    }
    
    .progress-fill.success {
      background: linear-gradient(90deg, #22c55e, #16a34a);
    }
    
    .progress-fill.warning {
      background: linear-gradient(90deg, #f59e0b, #d97706);
    }
    
    .progress-fill.danger {
      background: linear-gradient(90deg, #ef4444, #dc2626);
    }
    
    /* ===== SKELETON LOADING ===== */
    .skeleton {
      background: linear-gradient(
        90deg,
        var(--neutral-200) 25%,
        var(--neutral-300) 37%,
        var(--neutral-200) 50%
      );
      background-size: 200% 100%;
      animation: shimmer 1.5s infinite linear;
      border-radius: var(--radius-md);
      position: relative;
      overflow: hidden;
    }
    
    .skeleton::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.4),
        transparent
      );
      transform: translateX(-100%);
      animation: shimmer 2s infinite;
    }
    
    .skeleton-text {
      height: 1rem;
      margin-bottom: 0.5rem;
    }
    
    .skeleton-title {
      height: 1.5rem;
      width: 60%;
      margin-bottom: 1rem;
    }
    
    .skeleton-avatar {
      width: 40px;
      height: 40px;
      border-radius: 50%;
    }
    
    .skeleton-hero {
      height: 160px;
      border-radius: var(--radius-2xl);
      margin-bottom: var(--space-6);
    }
    
    .skeleton-kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: var(--space-4);
      margin-bottom: var(--space-6);
    }
    
    .skeleton-card {
      height: 120px;
      border-radius: var(--radius-xl);
    }
    
    .skeleton-card.tall { height: 200px; }
    .skeleton-card.short { height: 48px; }
    
    /* ===== TOAST NOTIFICATIONS ===== */
    .toast-container {
      position: fixed;
      bottom: var(--space-6);
      right: var(--space-6);
      z-index: 9999;
      display: flex;
      flex-direction: column;
      gap: var(--space-2);
      pointer-events: none;
      max-width: 360px;
    }
    
    .toast {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      padding: var(--space-3) var(--space-4);
      border-radius: var(--radius-lg);
      background: white;
      box-shadow: var(--shadow-lg);
      border: 1px solid var(--neutral-200);
      font-size: var(--text-sm);
      font-weight: 500;
      color: var(--neutral-900);
      pointer-events: all;
      position: relative;
      overflow: hidden;
      min-width: 280px;
      animation: spring-slide 0.35s var(--ease-spring) both;
      border-left: 4px solid var(--neutral-300);
    }
    
    .toast.removing {
      animation: slideOut 0.25s var(--ease-in-out) forwards;
    }
    
    @keyframes slideOut {
      from { opacity: 1; transform: translateX(0) scale(1); max-height: 80px; margin-bottom: 0; }
      to { opacity: 0; transform: translateX(120%) scale(0.9); max-height: 0; margin-bottom: -8px; }
    }
    
    .toast.success { border-left-color: var(--status-success); }
    .toast.error { border-left-color: var(--status-danger); }
    .toast.warning { border-left-color: var(--status-warning); }
    .toast.info { border-left-color: var(--status-info); }
    
    .toast-icon {
      font-size: var(--text-lg);
      flex-shrink: 0;
    }
    
    .toast-msg {
      flex: 1;
      line-height: 1.4;
    }
    
    .toast-close {
      background: none;
      border: none;
      cursor: pointer;
      color: var(--neutral-400);
      font-size: var(--text-base);
      padding: var(--space-1);
      border-radius: var(--radius-sm);
      transition: color var(--transition-fast);
      flex-shrink: 0;
    }
    
    .toast-close:hover {
      color: var(--neutral-700);
    }
    
    .toast-progress {
      position: absolute;
      bottom: 0;
      left: 0;
      height: 3px;
      animation: toastProgress linear forwards;
      opacity: 0.7;
    }
    
    .toast.success .toast-progress { background: var(--status-success); }
    .toast.error .toast-progress { background: var(--status-danger); }
    .toast.warning .toast-progress { background: var(--status-warning); }
    .toast.info .toast-progress { background: var(--status-info); }
    
    /* ===== HELP TOOLTIPS ===== */
    .help-tooltip {
      position: relative;
      display: inline-block;
      margin-left: var(--space-1);
    }
    
    .help-tooltip i {
      color: var(--neutral-400);
      cursor: help;
      transition: color var(--transition-fast);
      font-size: var(--text-sm);
    }
    
    .help-tooltip:hover i {
      color: var(--accent-600);
    }
    
    .help-tooltip:hover .tooltip-content {
      display: block;
      animation: fadeIn var(--transition-fast) var(--ease-out);
    }
    
    .tooltip-content {
      display: none;
      position: absolute;
      bottom: 100%;
      left: 50%;
      transform: translateX(-50%);
      width: 200px;
      padding: var(--space-3);
      background: white;
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-lg);
      border: 1px solid var(--neutral-200);
      z-index: 1000;
      font-size: var(--text-xs);
      pointer-events: none;
      margin-bottom: var(--space-2);
    }
    
    .tooltip-content h4 {
      font-weight: 600;
      margin-bottom: var(--space-1);
      font-size: var(--text-xs);
    }
    
    .tooltip-content p {
      color: var(--neutral-600);
      line-height: 1.4;
    }
    
    .tooltip-content::after {
      content: '';
      position: absolute;
      top: 100%;
      left: 50%;
      transform: translateX(-50%);
      border-width: 6px;
      border-style: solid;
      border-color: white transparent transparent transparent;
    }
    
    /* ===== FLOATING ACTION BUTTON ===== */
    .fab-container {
      position: fixed;
      bottom: 80px;
      right: 24px;
      z-index: 1000;
    }
    
    .fab-main {
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent-600), var(--accent-500));
      color: white;
      border: none;
      box-shadow: 0 4px 12px rgba(196, 30, 58, 0.3);
      cursor: pointer;
      transition: transform var(--transition-base) var(--ease-spring);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: var(--text-xl);
    }
    
    .fab-main:hover {
      transform: scale(1.1) rotate(90deg);
    }
    
    .fab-main:active {
      transform: scale(0.95);
    }
    
    .fab-menu {
      position: absolute;
      bottom: 70px;
      right: 0;
      display: none;
      flex-direction: column;
      gap: var(--space-2);
    }
    
    .fab-menu.open {
      display: flex;
      animation: slideUp var(--transition-base) var(--ease-out);
    }
    
    .fab-item {
      display: flex;
      align-items: center;
      gap: var(--space-2);
      padding: var(--space-2) var(--space-4);
      background: white;
      border: 1px solid var(--neutral-200);
      border-radius: var(--radius-full);
      box-shadow: var(--shadow-md);
      white-space: nowrap;
      cursor: pointer;
      transition: all var(--transition-fast) var(--ease-out);
      font-size: var(--text-sm);
    }
    
    .fab-item:hover {
      transform: translateX(-4px);
      border-color: var(--accent-400);
      background: var(--accent-50);
    }
    
    .fab-item i {
      color: var(--accent-600);
    }
    
    /* ===== KEYBOARD SHORTCUTS ===== */
    .kbd {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: var(--space-1) var(--space-2);
      background: var(--neutral-100);
      border: 1px solid var(--neutral-300);
      border-radius: var(--radius-sm);
      font-family: var(--font-mono);
      font-size: var(--text-xs);
      color: var(--neutral-700);
      box-shadow: 0 2px 0 var(--neutral-300);
    }
    
    .shortcut-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: var(--space-4);
    }
    
    .shortcut-item {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      padding: var(--space-2);
      background: var(--neutral-50);
      border-radius: var(--radius-md);
    }
    
    .shortcut-item .kbd {
      min-width: 48px;
      text-align: center;
    }
    
    /* ===== EMPTY STATES ===== */
    .empty-state {
      text-align: center;
      padding: var(--space-12) var(--space-6);
      background: white;
      border-radius: var(--radius-xl);
      border: 2px dashed var(--neutral-300);
    }
    
    .empty-state.enhanced {
      padding: var(--space-8);
    }
    
    .empty-illustration {
      width: 120px;
      height: 120px;
      margin: 0 auto var(--space-4);
    }
    
    .empty-illustration svg {
      width: 100%;
      height: 100%;
    }
    
    /* ===== SIDEBAR ===== */
    .app-container {
      display: flex;
      min-height: 100vh;
    }
    
    .sidebar {
      width: 260px;
      background: white;
      border-right: 1px solid var(--neutral-200);
      padding: var(--space-5) var(--space-4);
      position: fixed;
      top: 0;
      left: 0;
      bottom: 0;
      overflow-y: auto;
      overflow-x: hidden;
      transition: width var(--transition-base) var(--ease-out);
      z-index: 100;
      display: flex;
      flex-direction: column;
    }
    
    .sidebar.collapsed {
      width: 72px;
    }
    
    .sidebar-logo {
      padding: var(--space-3) var(--space-2);
      margin-bottom: var(--space-5);
      border-bottom: 1px solid var(--neutral-200);
      display: flex;
      align-items: center;
      gap: var(--space-3);
    }
    
    .sidebar-logo-mark {
      width: 34px;
      height: 34px;
      border-radius: var(--radius-lg);
      background: linear-gradient(135deg, var(--accent-700), var(--accent-600));
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 700;
      font-size: var(--text-sm);
      flex-shrink: 0;
    }

    .sidebar-logo-text {
      overflow: hidden;
      transition: opacity var(--transition-base) var(--ease-out), max-width var(--transition-base) var(--ease-out);
      max-width: 200px;
    }

    .sidebar.collapsed .sidebar-logo-text {
      opacity: 0;
      max-width: 0;
    }
    
    .sidebar-logo h1 {
      font-size: var(--text-lg);
      font-weight: 700;
      color: var(--neutral-900);
      white-space: nowrap;
    }

    .sidebar-logo .logo-sub {
      font-size: var(--text-xs);
      color: var(--neutral-500);
      font-weight: 400;
      white-space: nowrap;
      margin-top: 1px;
    }

    /* Nav section groups */
    .nav-group {
      margin-bottom: var(--space-5);
    }

    .nav-group-label {
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--neutral-400);
      padding: 0 var(--space-3);
      margin-bottom: var(--space-2);
      white-space: nowrap;
      overflow: hidden;
      transition: opacity var(--transition-base);
    }

    .sidebar.collapsed .nav-group-label {
      opacity: 0;
    }
    
    .nav-item {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      padding: var(--space-3) var(--space-3);
      border-radius: var(--radius-lg);
      color: var(--neutral-600);
      font-weight: 500;
      font-size: var(--text-sm);
      transition: all var(--transition-fast) var(--ease-out);
      margin-bottom: 2px;
      cursor: pointer;
      border: none;
      background: transparent;
      width: 100%;
      text-align: left;
      position: relative;
    }
    
    .nav-item:hover {
      background: var(--neutral-100);
      color: var(--neutral-900);
    }
    
    .nav-item.active {
      background: linear-gradient(135deg, var(--accent-50), var(--accent-100));
      color: var(--accent-700);
      box-shadow: 0 2px 8px rgba(196, 30, 58, 0.08);
    }

    .nav-item.active i {
      color: var(--accent-600);
    }
    
    .nav-item i {
      width: 20px;
      font-size: var(--text-base);
      flex-shrink: 0;
      text-align: center;
      color: var(--neutral-500);
      transition: color var(--transition-fast);
    }

    .nav-item:hover i {
      color: var(--neutral-800);
    }

    .nav-item span {
      white-space: nowrap;
      overflow: hidden;
      transition: opacity var(--transition-base), max-width var(--transition-base);
      max-width: 200px;
    }
    
    .sidebar.collapsed .nav-item span {
      opacity: 0;
      max-width: 0;
    }

    /* Tooltip for collapsed nav */
    .sidebar.collapsed .nav-item::after {
      content: attr(data-tooltip);
      position: absolute;
      left: calc(100% + 12px);
      top: 50%;
      transform: translateY(-50%);
      background: var(--neutral-900);
      color: white;
      font-size: var(--text-xs);
      font-weight: 500;
      padding: var(--space-1) var(--space-3);
      border-radius: var(--radius-md);
      white-space: nowrap;
      pointer-events: none;
      opacity: 0;
      transition: opacity var(--transition-fast);
      z-index: 200;
    }

    .sidebar.collapsed .nav-item:hover::after {
      opacity: 1;
    }

    /* ===== BREADCRUMB ===== */
    .breadcrumb {
      display: flex;
      align-items: center;
      gap: var(--space-2);
      font-size: var(--text-xs);
      color: var(--neutral-500);
      margin-bottom: var(--space-5);
      padding: var(--space-2) 0;
      flex-wrap: wrap;
    }

    .breadcrumb-item {
      display: flex;
      align-items: center;
      gap: var(--space-2);
    }

    .breadcrumb-item a, .breadcrumb-item span {
      color: var(--neutral-500);
      font-weight: 500;
      cursor: pointer;
      transition: color var(--transition-fast);
    }

    .breadcrumb-item a:hover {
      color: var(--accent-600);
    }

    .breadcrumb-item.current span {
      color: var(--neutral-900);
      font-weight: 600;
      cursor: default;
    }

    .breadcrumb-sep {
      color: var(--neutral-300);
      font-size: var(--text-xs);
    }

    body.dark-mode .breadcrumb-item.current span {
      color: #c9d1d9;
    }
    
    /* ===== MAIN CONTENT ===== */
    .main-content {
      flex: 1;
      margin-left: 260px;
      padding: var(--space-5) var(--space-6);
      transition: margin-left var(--transition-base) var(--ease-out);
      min-width: 0;
    }
    
    .main-content.expanded {
      margin-left: 72px;
    }
    
    /* ===== TOP BAR - STREAMLINED ===== */
    .top-bar {
      background: var(--glass-bg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--glass-border);
      padding: var(--space-3) var(--space-5);
      position: sticky;
      top: 0;
      z-index: 90;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: var(--space-4);
      margin-bottom: var(--space-2);
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow-sm);
    }

    /* ===== COMMAND PALETTE ===== */
    .cmd-overlay {
      position: fixed;
      inset: 0;
      background: rgba(26, 38, 52, 0.55);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      z-index: 9998;
      display: flex;
      align-items: flex-start;
      justify-content: center;
      padding-top: 15vh;
      opacity: 0;
      visibility: hidden;
      transition: all var(--transition-base) var(--ease-out);
    }

    .cmd-overlay.active {
      opacity: 1;
      visibility: visible;
    }

    .cmd-palette {
      background: white;
      border-radius: var(--radius-2xl);
      box-shadow: var(--shadow-xl);
      width: 90%;
      max-width: 560px;
      overflow: hidden;
      transform: scale(0.96) translateY(-8px);
      transition: all var(--transition-base) var(--ease-spring);
      border: 1px solid var(--neutral-200);
    }

    .cmd-overlay.active .cmd-palette {
      transform: scale(1) translateY(0);
    }

    .cmd-input-wrap {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      padding: var(--space-4) var(--space-5);
      border-bottom: 1px solid var(--neutral-200);
    }

    .cmd-input-wrap i {
      color: var(--neutral-500);
      font-size: var(--text-lg);
      flex-shrink: 0;
    }

    .cmd-input {
      flex: 1;
      border: none;
      outline: none;
      font-size: var(--text-base);
      font-family: var(--font-sans);
      background: transparent;
      color: var(--neutral-900);
    }

    .cmd-input::placeholder {
      color: var(--neutral-400);
    }

    .cmd-kbd-hint {
      font-size: var(--text-xs);
      color: var(--neutral-400);
      white-space: nowrap;
    }

    .cmd-body {
      max-height: 380px;
      overflow-y: auto;
    }

    .cmd-section-label {
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--neutral-400);
      padding: var(--space-3) var(--space-5) var(--space-1);
    }

    .cmd-item {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      padding: var(--space-3) var(--space-5);
      cursor: pointer;
      transition: background var(--transition-fast);
      border: none;
      background: none;
      width: 100%;
      text-align: left;
    }

    .cmd-item:hover, .cmd-item.selected {
      background: var(--neutral-50);
    }

    .cmd-item-icon {
      width: 32px;
      height: 32px;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--neutral-100);
      color: var(--neutral-600);
      font-size: var(--text-sm);
      flex-shrink: 0;
    }

    .cmd-item.action .cmd-item-icon {
      background: var(--accent-100);
      color: var(--accent-600);
    }

    .cmd-item-text {
      flex: 1;
      min-width: 0;
    }

    .cmd-item-label {
      font-size: var(--text-sm);
      font-weight: 500;
      color: var(--neutral-900);
    }

    .cmd-item-sub {
      font-size: var(--text-xs);
      color: var(--neutral-500);
      margin-top: 1px;
    }

    .cmd-item-tag {
      font-size: var(--text-xs);
      color: var(--neutral-500);
      background: var(--neutral-100);
      padding: 2px 8px;
      border-radius: var(--radius-full);
    }

    .cmd-footer {
      display: flex;
      align-items: center;
      gap: var(--space-4);
      padding: var(--space-3) var(--space-5);
      border-top: 1px solid var(--neutral-200);
      background: var(--neutral-50);
    }

    .cmd-footer-hint {
      display: flex;
      align-items: center;
      gap: var(--space-1);
      font-size: var(--text-xs);
      color: var(--neutral-500);
    }

    body.dark-mode .cmd-palette {
      background: #161b22;
      border-color: #30363d;
    }
    body.dark-mode .cmd-input-wrap {
      border-color: #30363d;
    }
    body.dark-mode .cmd-input {
      color: #c9d1d9;
    }
    body.dark-mode .cmd-item:hover, body.dark-mode .cmd-item.selected {
      background: #21262d;
    }
    body.dark-mode .cmd-item-icon {
      background: #21262d;
      color: #8b949e;
    }
    body.dark-mode .cmd-item-label {
      color: #c9d1d9;
    }
    body.dark-mode .cmd-footer {
      background: #0d1117;
      border-color: #30363d;
    }

    /* ===== DESTRUCTIVE CONFIRM INPUT ===== */
    .danger-confirm-wrap {
      margin-top: var(--space-4);
    }

    .danger-confirm-wrap .confirm-phrase {
      font-size: var(--text-sm);
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--status-danger);
      background: var(--status-danger-bg);
      padding: var(--space-2) var(--space-3);
      border-radius: var(--radius-md);
      display: inline-block;
      margin: var(--space-2) 0 var(--space-3);
      letter-spacing: 0.04em;
    }

    .danger-confirm-input {
      width: 100%;
      padding: var(--space-3) var(--space-4);
      border: 1.5px solid var(--neutral-200);
      border-radius: var(--radius-lg);
      font-family: var(--font-mono);
      font-size: var(--text-sm);
      font-weight: 600;
      letter-spacing: 0.04em;
      transition: border-color var(--transition-fast);
      outline: none;
    }

    .danger-confirm-input:focus {
      border-color: var(--status-danger);
      box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
    }

    .danger-confirm-input.matched {
      border-color: var(--status-success);
      box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.1);
    }

    /* tour-backdrop moved above */

    .tour-spotlight {
      position: absolute;
      border-radius: var(--radius-lg);
      box-shadow: 0 0 0 9999px rgba(26, 38, 52, 0.7);
      transition: all var(--transition-slow) var(--ease-out);
      pointer-events: none;
    }

    .tour-tooltip {
      position: fixed;
      background: white;
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow-xl);
      padding: var(--space-5);
      max-width: 320px;
      z-index: 9991;
      border: 1px solid var(--neutral-200);
      animation: spring-pop 0.3s var(--ease-spring);
      pointer-events: all;
    }

    .tour-step-indicator {
      font-size: var(--text-xs);
      color: var(--neutral-400);
      font-weight: 600;
      margin-bottom: var(--space-2);
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }

    .tour-title {
      font-size: var(--text-base);
      font-weight: 600;
      color: var(--neutral-900);
      margin-bottom: var(--space-2);
    }

    .tour-desc {
      font-size: var(--text-sm);
      color: var(--neutral-600);
      line-height: 1.6;
      margin-bottom: var(--space-4);
    }

    .tour-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: var(--space-3);
    }

    /* ===== DENSITY TOGGLE ===== */
    .table-density-compact .table td,
    .table-density-compact .table th {
      padding: var(--space-2) var(--space-3);
    }

    .table-density-comfortable .table td,
    .table-density-comfortable .table th {
      padding: var(--space-5) var(--space-4);
    }

    .density-toggle {
      display: flex;
      align-items: center;
      gap: 2px;
      background: var(--neutral-100);
      border-radius: var(--radius-lg);
      padding: 3px;
    }

    .density-btn {
      padding: 4px 10px;
      border-radius: var(--radius-md);
      border: none;
      background: transparent;
      font-size: var(--text-xs);
      font-weight: 500;
      color: var(--neutral-500);
      cursor: pointer;
      transition: all var(--transition-fast);
    }

    .density-btn.active {
      background: white;
      color: var(--neutral-900);
      box-shadow: var(--shadow-xs);
    }

    body.dark-mode .density-btn.active {
      background: #30363d;
      color: #c9d1d9;
    }

    /* ===== COLUMN CHOOSER ===== */
    .col-chooser-wrap {
      position: relative;
      display: inline-block;
    }
    .col-chooser-btn {
      display: inline-flex;
      align-items: center;
      gap: var(--space-1);
      padding: 4px 10px;
      border-radius: var(--radius-md);
      border: 1px solid var(--neutral-200);
      background: white;
      font-size: var(--text-xs);
      font-weight: 500;
      color: var(--neutral-600);
      cursor: pointer;
      transition: all var(--transition-fast);
    }
    .col-chooser-btn:hover {
      background: var(--neutral-50);
      border-color: var(--neutral-300);
      color: var(--neutral-900);
    }
    .col-chooser-dropdown {
      position: absolute;
      top: calc(100% + 6px);
      right: 0;
      background: white;
      border: 1px solid var(--neutral-200);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-lg);
      z-index: 500;
      min-width: 200px;
      padding: var(--space-2) 0;
      display: none;
      animation: spring-scale 0.2s var(--ease-spring) both;
    }
    .col-chooser-dropdown.open { display: block; }
    .col-chooser-header {
      padding: var(--space-2) var(--space-4);
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--neutral-400);
      border-bottom: 1px solid var(--neutral-100);
      margin-bottom: var(--space-1);
    }
    .col-chooser-item {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      padding: var(--space-2) var(--space-4);
      font-size: var(--text-xs);
      font-weight: 500;
      color: var(--neutral-700);
      cursor: pointer;
      user-select: none;
      transition: background var(--transition-fast);
    }
    .col-chooser-item:hover { background: var(--neutral-50); }
    .col-chooser-item input[type="checkbox"] {
      width: 14px; height: 14px;
      accent-color: var(--accent-600);
      cursor: pointer;
    }
    body.dark-mode .col-chooser-btn {
      background: #21262d; border-color: #30363d; color: #8b949e;
    }
    body.dark-mode .col-chooser-dropdown {
      background: #161b22; border-color: #30363d;
    }
    body.dark-mode .col-chooser-item { color: #c9d1d9; }
    body.dark-mode .col-chooser-item:hover { background: #21262d; }

    /* ===== INLINE FIELD VALIDATION ===== */
    .field-hint {
      font-size: var(--text-xs);
      color: var(--neutral-500);
      margin-top: var(--space-1);
      display: flex;
      align-items: center;
      gap: var(--space-1);
      min-height: 18px;
    }

    .field-hint.error { color: var(--status-danger); }
    .field-hint.success { color: var(--status-success); }
    .field-hint.warning { color: var(--status-warning); }

    /* What's New badge in sidebar */
    .whats-new-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 18px;
      height: 18px;
      border-radius: var(--radius-full);
      background: var(--accent-600);
      color: white;
      font-size: 10px;
      font-weight: 700;
      padding: 0 4px;
      margin-left: auto;
      flex-shrink: 0;
    }

    .sidebar.collapsed .whats-new-badge {
      display: none;
    }
    
    .search-bar {
      display: flex;
      align-items: center;
      gap: var(--space-2);
      background: white;
      border: 1px solid var(--neutral-200);
      border-radius: var(--radius-full);
      padding: var(--space-2) var(--space-4);
      width: 300px;
      transition: all var(--transition-base) var(--ease-out);
      position: relative;
    }
    
    .search-bar:focus-within {
      border-color: var(--accent-600);
      box-shadow: 0 0 0 4px rgba(196, 30, 58, 0.1);
      width: 350px;
    }
    
    .search-bar input {
      border: none;
      outline: none;
      background: transparent;
      width: 100%;
      font-size: var(--text-sm);
    }
    
    .search-bar i {
      color: var(--neutral-500);
    }
    
    /* ===== STATS GRID ===== */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: var(--space-4);
      margin-bottom: var(--space-6);
    }
    
    .stat-tile {
      background: white;
      border-radius: var(--radius-xl);
      padding: var(--space-5);
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--neutral-200);
      transition: all var(--transition-base) var(--ease-spring);
      position: relative;
      overflow: hidden;
    }
    
    .stat-tile::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, var(--accent-600), var(--accent-400));
      opacity: 0;
      transition: opacity var(--transition-base) var(--ease-out);
    }
    
    .stat-tile:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }
    
    .stat-tile:hover::before {
      opacity: 1;
    }
    
    .stat-label {
      font-size: var(--text-xs);
      font-weight: 500;
      color: var(--neutral-600);
      margin-bottom: var(--space-2);
      display: flex;
      align-items: center;
      gap: var(--space-2);
      text-transform: uppercase;
      letter-spacing: 0.02em;
    }
    
    .stat-value {
      font-family: var(--font-mono);
      font-size: var(--text-2xl);
      font-weight: 700;
      color: var(--neutral-900);
      line-height: var(--leading-tight);
    }
    
    .stat-trend {
      display: flex;
      align-items: center;
      gap: var(--space-1);
      font-size: var(--text-xs);
      margin-top: var(--space-2);
    }
    
    .trend-up { color: var(--status-success); }
    .trend-down { color: var(--status-danger); }
    
    /* ===== DASHBOARD KPI CARDS ===== */
    .dashboard-kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: var(--space-4);
      margin-bottom: var(--space-6);
    }
    
    .kpi-card {
      background: white;
      border-radius: var(--radius-xl);
      padding: var(--space-5);
      border: 1px solid var(--neutral-200);
      box-shadow: var(--shadow-sm);
      transition: all var(--transition-base) var(--ease-spring);
      position: relative;
      overflow: hidden;
      cursor: pointer;
    }
    
    .kpi-card:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }
    
    .kpi-icon {
      width: 44px;
      height: 44px;
      border-radius: var(--radius-lg);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: var(--text-lg);
      margin-bottom: var(--space-3);
    }
    
    .kpi-value {
      font-family: var(--font-mono);
      font-size: var(--text-2xl);
      font-weight: 700;
      line-height: 1;
      margin-bottom: 4px;
    }
    
    .kpi-label {
      font-size: var(--text-xs);
      color: var(--neutral-600);
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.02em;
    }
    
    .kpi-trend {
      font-size: var(--text-xs);
      margin-top: var(--space-2);
      display: flex;
      align-items: center;
      gap: 4px;
    }
    
    .target-bar-wrap {
      margin-top: var(--space-3);
    }
    
    .target-bar-label {
      font-size: var(--text-xs);
      color: var(--neutral-500);
      margin-bottom: var(--space-1);
      display: flex;
      justify-content: space-between;
    }
    
    .target-bar {
      height: 6px;
      background: var(--neutral-200);
      border-radius: var(--radius-full);
      overflow: hidden;
    }
    
    .target-bar-fill {
      height: 100%;
      border-radius: var(--radius-full);
      background: linear-gradient(90deg, var(--accent-600), var(--accent-400));
      transition: width var(--transition-slow) var(--ease-spring);
    }
    
    /* ===== DASHBOARD HERO ===== */
    .dashboard-hero {
      background: linear-gradient(135deg, var(--primary-800) 0%, var(--accent-800) 100%);
      border-radius: var(--radius-2xl);
      padding: var(--space-8);
      color: white;
      margin-bottom: var(--space-6);
      position: relative;
      overflow: hidden;
    }
    
    .dashboard-hero::after {
      content: '';
      position: absolute;
      top: -40%;
      right: -10%;
      width: 300px;
      height: 300px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
    }
    
    .dashboard-hero::before {
      content: '';
      position: absolute;
      bottom: -30%;
      left: 40%;
      width: 200px;
      height: 200px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.04);
    }
    
    .dashboard-hero .hero-content {
      position: relative;
      z-index: 1;
    }
    
    /* ===== TECH AVATAR ===== */
    .tech-avatar {
      width: 40px;
      height: 40px;
      border-radius: var(--radius-full);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 600;
      flex-shrink: 0;
    }
    
    .tech-avatar[data-color="0"] { background: #e8f3ef; color: #2e6b4e; }
    .tech-avatar[data-color="1"] { background: #f0f7fc; color: #3a6b8f; }
    .tech-avatar[data-color="2"] { background: #faeaec; color: #9b2c3a; }
    .tech-avatar[data-color="3"] { background: #fcf5eb; color: #b45f2a; }
    .tech-avatar[data-color="4"] { background: #f0ebfc; color: #6b3a9b; }
    .tech-avatar[data-color="5"] { background: #ebf5fc; color: #3a809b; }
    .tech-avatar[data-color="6"] { background: #fcebf5; color: #9b3a7a; }
    .tech-avatar[data-color="7"] { background: #f5fceb; color: #5a9b3a; }
    
    /* ===== ORDER CARDS ===== */
    .order-card {
      background: white;
      border-radius: var(--radius-xl);
      border: 1px solid var(--neutral-200);
      margin-bottom: var(--space-4);
      overflow: hidden;
      transition: all var(--transition-base) var(--ease-spring);
    }
    
    .order-card:hover {
      border-color: var(--neutral-300);
      box-shadow: var(--shadow-md);
    }
    
    .order-card.nearly-full {
      border-color: var(--status-warning) !important;
      animation: amberPulse 2s infinite;
    }
    
    .order-header {
      padding: var(--space-4) var(--space-5);
      display: flex;
      align-items: center;
      gap: var(--space-4);
      cursor: pointer;
      transition: background var(--transition-fast) var(--ease-out);
    }
    
    .order-header:hover {
      background: var(--neutral-50);
    }
    
    .order-status-indicator {
      width: 4px;
      height: 40px;
      border-radius: var(--radius-full);
    }
    
    .status-open { background: var(--status-success); }
    .status-closed { background: var(--status-warning); }
    .status-over { background: var(--status-danger); }
    .status-unassigned { background: var(--status-unassigned); }
    
    .order-info {
      flex: 1;
    }
    
    .order-title {
      font-weight: 600;
      font-size: var(--text-lg);
      color: var(--neutral-900);
      margin-bottom: var(--space-1);
    }
    
    .order-meta {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      font-size: var(--text-xs);
      color: var(--neutral-600);
    }
    
    .order-meta i {
      font-size: var(--text-xs);
      color: var(--neutral-400);
    }
    
    .order-stats {
      display: flex;
      align-items: center;
      gap: var(--space-4);
    }
    
    .order-progress {
      width: 120px;
    }
    
    .order-chevron {
      color: var(--neutral-400);
      transition: transform var(--transition-base) var(--ease-spring);
    }
    
    .order-chevron.expanded {
      transform: rotate(180deg);
    }
    
    .order-body {
      padding: var(--space-5);
      border-top: 1px solid var(--neutral-200);
      background: var(--neutral-50);
    }
    
    /* ===== TECH ALLOCATION ROWS ===== */
    .tech-alloc-row {
      display: flex;
      align-items: center;
      gap: var(--space-4);
      padding: var(--space-3);
      background: white;
      border-radius: var(--radius-lg);
      border: 1px solid var(--neutral-200);
      margin-bottom: var(--space-2);
      transition: all var(--transition-fast) var(--ease-out);
      cursor: grab;
    }
    
    .tech-alloc-row:active {
      cursor: grabbing;
    }
    
    .tech-alloc-row.drag-over {
      border-color: var(--accent-500) !important;
      background: var(--accent-50) !important;
      transform: scale(1.01);
    }
    
    .supply-log-row:hover {
      border-color: var(--neutral-300) !important;
      box-shadow: var(--shadow-sm);
      transform: translateX(2px);
    }
    
    .supply-log-row.drag-over {
      border-color: var(--accent-500) !important;
      background: var(--accent-50) !important;
      transform: scale(1.01);
    }
    
    .supply-log-row:active {
      cursor: grabbing;
    }
    
    .tech-alloc-row:hover {
      border-color: var(--neutral-300);
      box-shadow: var(--shadow-sm);
    }
    
    .drag-handle {
      color: var(--neutral-300);
      cursor: grab;
      padding: 0 var(--space-1);
      font-size: var(--text-base);
      flex-shrink: 0;
      transition: color var(--transition-fast);
    }
    
    .tech-alloc-row:hover .drag-handle {
      color: var(--neutral-400);
    }
    
    .tech-details {
      flex: 1;
    }
    
    .tech-name {
      font-weight: 600;
      color: var(--neutral-900);
      margin-bottom: var(--space-1);
      font-size: var(--text-sm);
    }
    
    .tech-plate {
      font-size: var(--text-xs);
      color: var(--neutral-600);
    }
    
    .tech-stats {
      display: flex;
      align-items: center;
      gap: var(--space-2);
      margin-top: var(--space-1);
    }
    
    .stat-badge {
      padding: var(--space-1) var(--space-2);
      background: var(--neutral-100);
      border-radius: var(--radius-sm);
      font-size: var(--text-xs);
      font-weight: 500;
    }
    
    /* ===== LEADERBOARD ===== */
    .leaderboard-card {
      display: flex;
      align-items: center;
      gap: var(--space-4);
      padding: var(--space-4);
      background: white;
      border-radius: var(--radius-xl);
      border: 1px solid var(--neutral-200);
      margin-bottom: var(--space-3);
      transition: all var(--transition-base) var(--ease-spring);
      cursor: pointer;
    }
    
    .leaderboard-card:hover {
      transform: translateX(4px);
      border-color: var(--accent-600);
      box-shadow: var(--shadow-md);
    }
    
    .rank-badge {
      width: 48px;
      height: 48px;
      border-radius: var(--radius-full);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: var(--text-lg);
    }
    
    .rank-1 { background: linear-gradient(135deg, #FFD700, #FFC800); color: #7D5E00; }
    .rank-2 { background: linear-gradient(135deg, #E0E0E0, #D0D0D0); color: #5E5E5E; }
    .rank-3 { background: linear-gradient(135deg, #CD7F32, #B87333); color: #5E3A1A; }
    
    .lb-bar-container {
      flex: 1;
      height: 6px;
      background: var(--neutral-200);
      border-radius: var(--radius-full);
      overflow: hidden;
    }
    
    .lb-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--accent-600), var(--accent-400));
      border-radius: var(--radius-full);
      transition: width var(--transition-slow) var(--ease-spring);
    }
    
    /* ===== NOTIFICATIONS ===== */
    .notif-bell {
      position: relative;
      cursor: pointer;
    }
    
    .notif-badge {
      position: absolute;
      top: -4px;
      right: -4px;
      width: 16px;
      height: 16px;
      background: var(--status-danger);
      color: white;
      border-radius: 50%;
      font-size: 0.6rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 2px solid white;
    }
    
    .notif-dropdown {
      position: absolute;
      top: calc(100% + 8px);
      right: 0;
      width: 320px;
      background: white;
      border: 1px solid var(--neutral-200);
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow-lg);
      z-index: 999;
      overflow: hidden;
      display: none;
    }
    
    .notif-dropdown.open {
      display: block;
      animation: slideUp var(--transition-base) var(--ease-out);
    }
    
    .notif-item {
      display: flex;
      gap: var(--space-3);
      padding: var(--space-3) var(--space-4);
      border-bottom: 1px solid var(--neutral-100);
      transition: background var(--transition-fast);
      cursor: pointer;
    }
    
    .notif-item:hover {
      background: var(--neutral-50);
    }
    
    .notif-icon {
      width: 32px;
      height: 32px;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: var(--text-sm);
      flex-shrink: 0;
    }
    
    .notif-text {
      flex: 1;
    }
    
    .notif-title {
      font-size: var(--text-xs);
      font-weight: 600;
      color: var(--neutral-800);
    }
    
    .notif-desc {
      font-size: var(--text-xs);
      color: var(--neutral-500);
      margin-top: 1px;
    }
    
    /* ===== AUTOSAVE INDICATOR ===== */
    .autosave-indicator {
      display: inline-flex;
      align-items: center;
      gap: var(--space-1);
      font-size: var(--text-xs);
      color: var(--neutral-400);
      transition: all var(--transition-base) var(--ease-out);
      opacity: 0;
      transform: translateY(2px);
      pointer-events: none;
      white-space: nowrap;
    }
    
    .autosave-indicator.visible {
      opacity: 1;
      transform: translateY(0);
    }
    
    .autosave-indicator.unsaved {
      color: var(--status-warning);
      opacity: 1;
      transform: translateY(0);
    }
    
    .autosave-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--status-success);
      animation: autosavePulse 1.5s var(--ease-out) 1;
    }
    
    .autosave-indicator.unsaved .autosave-dot {
      background: var(--status-warning);
      animation: none;
    }
    
    /* ===== CONTEXT MENU ===== */
    .context-menu {
      position: fixed;
      background: white;
      border: 1px solid var(--neutral-200);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-lg);
      z-index: 10000;
      min-width: 190px;
      padding: var(--space-1) 0;
      display: none;
      animation: spring-scale var(--transition-base) var(--ease-spring) both;
      transform-origin: top left;
    }
    
    .context-menu.active {
      display: block;
    }
    
    .context-menu-item {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      padding: var(--space-2) var(--space-4);
      font-size: var(--text-xs);
      font-weight: 500;
      color: var(--neutral-700);
      cursor: pointer;
      transition: background var(--transition-fast), color var(--transition-fast);
      border: none;
      background: none;
      width: 100%;
      text-align: left;
    }
    
    .context-menu-item:hover {
      background: var(--neutral-50);
      color: var(--neutral-900);
    }
    
    .context-menu-item.danger {
      color: var(--status-danger);
    }
    
    .context-menu-item.danger:hover {
      background: var(--status-danger-bg);
    }
    
    .context-menu-item i {
      width: 16px;
      text-align: center;
    }
    
    .context-menu-separator {
      height: 1px;
      background: var(--neutral-200);
      margin: var(--space-1) 0;
    }
    
    /* ===== ORDER GROUP HEADERS ===== */
    .order-group-header {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      padding: var(--space-3) var(--space-4);
      background: var(--neutral-50);
      border-radius: var(--radius-lg);
      margin-bottom: var(--space-2);
      cursor: pointer;
      border: 1px solid var(--neutral-200);
      transition: all var(--transition-fast);
      user-select: none;
    }
    
    .order-group-header:hover {
      border-color: var(--neutral-300);
      box-shadow: var(--shadow-sm);
    }
    
    .order-group-title {
      font-weight: 700;
      font-size: var(--text-sm);
      flex: 1;
    }
    
    .order-group-chevron {
      transition: transform var(--transition-base) var(--ease-spring);
      color: var(--neutral-400);
    }
    
    .order-group-chevron.collapsed {
      transform: rotate(-90deg);
    }
    
    /* ===== ORDERS STICKY BAR ===== */
    .orders-sticky-bar {
      position: sticky;
      top: 0;
      z-index: 50;
      background: var(--glass-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-lg);
      padding: var(--space-3) var(--space-5);
      display: flex;
      align-items: center;
      gap: var(--space-5);
      margin-bottom: var(--space-4);
      box-shadow: var(--shadow-sm);
      flex-wrap: wrap;
    }
    
    .sticky-stat {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
    }
    
    .sticky-stat-label {
      font-size: 0.68rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--neutral-500);
    }
    
    .sticky-stat-value {
      font-family: var(--font-mono);
      font-size: var(--text-sm);
      font-weight: 700;
      color: var(--neutral-900);
    }
    
    .sticky-divider {
      width: 1px;
      height: 32px;
      background: var(--neutral-200);
    }
    
    /* ===== INLINE EDIT ===== */
    .inline-editable {
      cursor: pointer;
      border-radius: var(--radius-sm);
      padding: 1px var(--space-1);
      transition: background var(--transition-fast);
    }
    
    .inline-editable:hover {
      background: var(--accent-50);
      outline: 1px dashed var(--accent-400);
    }
    
    .inline-edit-input {
      width: 72px;
      padding: var(--space-1) var(--space-2);
      border: 1.5px solid var(--accent-600);
      border-radius: var(--radius-sm);
      font-family: var(--font-mono);
      font-size: var(--text-xs);
      background: white;
      text-align: center;
    }
    
    /* ===== DATE CHECKBOX ===== */
    .date-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
      gap: var(--space-2);
      max-height: 400px;
      overflow-y: auto;
      padding: var(--space-2);
    }
    
    .date-checkbox {
      display: flex;
      align-items: center;
      gap: var(--space-2);
      padding: var(--space-2);
      background: var(--neutral-50);
      border-radius: var(--radius-md);
      border: 1px solid var(--neutral-200);
      transition: all var(--transition-fast);
    }
    
    .date-checkbox:hover {
      background: white;
      border-color: var(--accent-600);
    }
    
    .date-checkbox input[type="checkbox"] {
      width: 16px;
      height: 16px;
      accent-color: var(--accent-600);
    }
    
    /* ===== UNASSIGNED COMMENT SECTION ===== */
    .unassign-comment-section {
      margin-top: var(--space-3);
      padding: var(--space-3);
      background: var(--neutral-50);
      border-radius: var(--radius-md);
      border-left: 3px solid var(--status-unassigned);
    }
    
    .unassign-comment-display {
      display: flex;
      align-items: center;
      gap: var(--space-2);
      padding: var(--space-2);
      background: var(--neutral-50);
      border-radius: var(--radius-sm);
      font-size: var(--text-xs);
    }
    
    /* ===== MOBILE BOTTOM NAV ===== */
    .mobile-bottom-nav {
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: white;
      border-top: 1px solid var(--neutral-200);
      padding: var(--space-2) var(--space-2) calc(var(--space-2) + env(safe-area-inset-bottom));
      z-index: 200;
      justify-content: space-around;
      box-shadow: 0 -4px 20px rgba(0,0,0,0.08);
    }
    
    .mobile-nav-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
      padding: var(--space-2) var(--space-3);
      border-radius: var(--radius-md);
      color: var(--neutral-500);
      font-size: 0.65rem;
      font-weight: 500;
      border: none;
      background: transparent;
      cursor: pointer;
      transition: all var(--transition-fast);
      min-width: 52px;
    }
    
    .mobile-nav-item i {
      font-size: var(--text-lg);
    }
    
    .mobile-nav-item.active {
      color: var(--accent-600);
      background: var(--accent-50);
    }
    
    .mobile-nav-item.active i {
      transform: translateY(-2px);
    }
    
    /* ===== FOOTER STATUS BAR ===== */
    .footer-status-bar {
      border-top: 1px solid var(--neutral-200);
      border-bottom: 1px solid var(--neutral-200);
      padding: var(--space-2) 0;
      display: flex;
      justify-content: center;
      gap: var(--space-8);
      font-size: var(--text-xs);
      color: var(--neutral-600);
      background: white;
      position: sticky;
      bottom: 0;
      z-index: 90;
    }
    
    .status-item {
      display: flex;
      align-items: center;
      gap: var(--space-2);
    }
    
    .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }
    
    .status-dot.online {
      background: var(--status-success);
    }
    
    .status-dot.offline {
      background: var(--status-danger);
    }
    
    /* ===== ORDER PICKER CARDS ===== */
    .order-picker-card {
      cursor: pointer;
      border: 2px solid var(--neutral-200);
      border-radius: var(--radius-lg);
      padding: var(--space-3);
      margin-bottom: var(--space-2);
      background: white;
      transition: all var(--transition-fast) var(--ease-out);
    }
    
    .order-picker-card:hover {
      border-color: var(--accent-400);
      transform: translateX(2px);
    }
    
    .order-picker-card.selected {
      border-color: var(--accent-600);
      background: var(--accent-50);
    }
    
    /* ===== DARK MODE ===== */
    body.dark-mode {
      background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
      color: #e6edf3;
    }
    
    body.dark-mode .sidebar,
    body.dark-mode .card,
    body.dark-mode .stat-tile,
    body.dark-mode .order-card,
    body.dark-mode .tech-alloc-row,
    body.dark-mode .leaderboard-card,
    body.dark-mode .modal-container,
    body.dark-mode .table-container,
    body.dark-mode .kpi-card,
    body.dark-mode .search-bar,
    body.dark-mode .input-field,
    body.dark-mode .select-field,
    body.dark-mode .toast,
    body.dark-mode .context-menu,
    body.dark-mode .notif-dropdown,
    body.dark-mode .footer-status-bar,
    body.dark-mode .mobile-bottom-nav,
    body.dark-mode .order-group-header,
    body.dark-mode .date-checkbox {
      background: #161b22;
      border-color: #21262d;
      color: #c9d1d9;
    }

    body.dark-mode .sidebar-logo-mark {
      background: linear-gradient(135deg, var(--accent-800), var(--accent-700));
    }

    body.dark-mode .sidebar-logo h1 { color: #e6edf3; }
    body.dark-mode .logo-sub { color: #8b949e; }
    body.dark-mode .nav-group-label { color: #6e7681; }
    body.dark-mode .nav-item { color: #8b949e; }
    body.dark-mode .nav-item:hover { background: #21262d; color: #c9d1d9; }
    body.dark-mode .nav-item:hover i { color: #c9d1d9; }
    body.dark-mode .nav-item.active { background: rgba(228,160,172,0.15); color: #f4a7b5; }
    body.dark-mode .nav-item.active i { color: #f4a7b5; }
    body.dark-mode .nav-item::after { background: #e6edf3; color: #161b22; }

    body.dark-mode .breadcrumb-item a,
    body.dark-mode .breadcrumb-item span { color: #6e7681; }
    body.dark-mode .breadcrumb-sep { color: #30363d; }

    body.dark-mode .density-toggle { background: #21262d; }
    body.dark-mode .density-btn { color: #6e7681; }
    body.dark-mode .density-btn.active { background: #30363d; color: #c9d1d9; }

    body.dark-mode .whats-new-badge { background: var(--accent-700); }
    
    body.dark-mode .top-bar {
      background: rgba(22,27,34,0.9);
      border-color: #21262d;
    }

    body.dark-mode .input-field,
    body.dark-mode .select-field {
      background: #0d1117;
      border-color: #30363d;
      color: #c9d1d9;
    }

    body.dark-mode .table th {
      background: #0d1117;
      color: #8b949e;
      border-color: #21262d;
    }

    body.dark-mode .table td {
      color: #c9d1d9;
      border-color: #21262d;
    }

    body.dark-mode .table tbody tr:hover {
      background: #21262d;
    }
    
    body.dark-mode .btn-secondary {
      background: #21262d;
      border-color: #30363d;
      color: #c9d1d9;
    }
    
    body.dark-mode .btn-secondary:hover {
      background: #30363d;
    }
    
    body.dark-mode .order-body {
      background: #0d1117;
    }
    
    body.dark-mode .input-label {
      background: #161b22;
      color: #8b949e;
    }
    
    body.dark-mode .kbd {
      background: #21262d;
      border-color: #30363d;
      color: #c9d1d9;
    }

    body.dark-mode #autoLog {
      background: #0d1117;
      color: #79c0ff;
      border-color: #21262d;
    }

    body.dark-mode #tmQuickResult {
      background: #161b22;
      border-color: #21262d;
    }

    body.dark-mode #autoDropZone {
      border-color: #30363d;
      background: #0d1117;
    }

    body.dark-mode #autoDropZone:hover {
      border-color: var(--accent-400) !important;
      background: rgba(196,30,58,0.08);
    }

    body.dark-mode #autoXlsxDropZone {
      border-color: #30363d;
      background: #0d1117;
    }

    body.dark-mode #autoXlsxDropZone:hover {
      border-color: var(--status-success) !important;
      background: rgba(22,163,74,0.08);
    }

    /* Dynamic modals appended to body inherit these rules automatically
       via body.dark-mode .modal-container — but ensure label/subtitle text too */
    body.dark-mode #propagationModal .modal-body p,
    body.dark-mode #propagationModal .modal-body ul,
    body.dark-mode #bulkTechModal .modal-body p {
      color: #8b949e;
    }
    body.dark-mode #propagationModal .card,
    body.dark-mode #bulkTechModal .card {
      background: #0d1117;
      border-color: #21262d;
    }
    body.dark-mode #bulkTechModal label {
      background: #0d1117;
      color: #c9d1d9;
    }

    /* ===== RESPONSIVE BREAKPOINTS ===== */
    @media (max-width: 1024px) {
      .grid-cols-4 {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    
    @media (max-width: 768px) {
      .sidebar {
        transform: translateX(-100%);
        width: 260px;
      }
      
      .sidebar.mobile-open {
        transform: translateX(0);
      }
      
      .main-content {
        margin-left: 0;
      }
      
      .main-content.expanded {
        margin-left: 0;
      }
      
      .top-bar {
        flex-direction: column;
        gap: var(--space-3);
      }
      
      .search-bar {
        width: 100%;
      }
      
      .search-bar:focus-within {
        width: 100%;
      }
      
      .mobile-bottom-nav {
        display: flex;
      }
      
      .main-content {
        padding-bottom: 80px;
      }
      
      .footer-status-bar {
        flex-wrap: wrap;
        gap: var(--space-4);
        padding: var(--space-2) var(--space-3);
      }
      
      .stats-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      
      .dashboard-kpi-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    
    @media (max-width: 480px) {
      .stats-grid {
        grid-template-columns: 1fr;
      }
      
      .dashboard-kpi-grid {
        grid-template-columns: 1fr;
      }
      
      .order-header {
        flex-direction: column;
        align-items: flex-start;
      }
      
      .order-stats {
        width: 100%;
        flex-direction: row;
        justify-content: space-between;
      }
      
      .order-progress {
        width: 80px;
      }
      
      .kpi-value {
        font-size: var(--text-xl);
      }
      
      .modal-container {
        width: 96%;
      }
      
      .grid-cols-2, .grid-cols-3, .grid-cols-4 {
        grid-template-columns: 1fr;
      }
      
      .shortcut-grid {
        grid-template-columns: 1fr;
      }
      
      .fab-container {
        bottom: 70px;
        right: 16px;
      }
    }
    
    /* ===== PRINT STYLES ===== */
    @media print {
      .sidebar, .top-bar, .btn, .fab-container, .mobile-bottom-nav, .footer-status-bar {
        display: none;
      }
      
      .main-content {
        margin-left: 0;
      }
      
      .card {
        break-inside: avoid;
        border: 1px solid #000;
      }
    }
    
    /* ===== TOP BAR RESPONSIVE BREAKPOINTS ===== */
    @media (max-width: 900px) {
      .top-bar {
        flex-wrap: wrap;
        gap: var(--space-2);
        padding: var(--space-2) var(--space-3);
      }
      .top-bar > div:first-child {
        max-width: 100% !important;
        flex: 1 1 200px;
      }
      .top-bar .topbar-right {
        flex-wrap: wrap;
        gap: var(--space-2);
      }
      .topbar-region-label {
        display: none;
      }
    }
    @media (max-width: 640px) {
      .top-bar {
        padding: var(--space-2);
      }
      .autosave-indicator {
        display: none !important;
      }
      .topbar-right {
        gap: var(--space-1) !important;
      }
      .top-bar .kbd {
        display: none;
      }
    }
    /* ===== ONBOARDING TOUR — enhanced backdrop ===== */
    .tour-backdrop {
      position: fixed;
      inset: 0;
      z-index: 9990;
      pointer-events: none;
      background: rgba(26, 38, 52, 0.55);
    }
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }
  </style>
</head>
<body>
  <!-- Developer Credit - Fixed Footer Position -->
  <div class="footer-status-bar">
    <div class="status-item">
      <span class="status-dot online" id="systemStatusDot"></span>
      <span id="systemStatusText">System Online</span>
      <span style="margin-left: 150px; font-weight: 500;">
        System Developed By Harrison Mwewa · Call/WhatsApp: 0770435328 & 0778847177
      </span>
    </div>
    <div class="status-item">
      <i class="fa-regular fa-clock"></i>
      <span id="footerSystemTime"></span>
    </div>
    <div class="status-item">
      <i class="fa-regular fa-server"></i>
      <span id="footerActiveRegion">Region: -</span>
    </div>
    <div class="status-item">
      <i class="fa-regular fa-rotate"></i>
      <span id="footerAutosave">Autosave Active</span>
    </div>
  </div>

  <div class="app-container">
    <!-- Sidebar -->
    <aside class="sidebar" id="sidebar" role="navigation" aria-label="Main navigation">
      <div class="sidebar-logo">
        <div class="sidebar-logo-mark">C</div>
        <div class="sidebar-logo-text">
          <h1>CCS Fuel</h1>
          <div class="logo-sub">Enterprise System</div>
        </div>
      </div>
      
      <!-- MAIN NAV GROUP -->
      <div class="nav-group" role="group" aria-label="Main pages">
        <div class="nav-group-label" aria-hidden="true">Main</div>
        <button class="nav-item" onclick="setPage('dashboard', this)" data-tooltip="Dashboard">
          <i class="fa-regular fa-gauge-high"></i>
          <span>Dashboard</span>
        </button>
        <button class="nav-item active" onclick="setPage('daily', this)" data-tooltip="Daily">
          <i class="fa-regular fa-calendar"></i>
          <span>Daily</span>
        </button>
        <button class="nav-item" onclick="setPage('orders', this)" data-tooltip="Orders">
          <i class="fa-regular fa-file-lines"></i>
          <span>Orders</span>
        </button>
        <button class="nav-item" onclick="setPage('regions', this)" data-tooltip="Regions">
          <i class="fa-regular fa-building"></i>
          <span>Regions</span>
        </button>
        <button class="nav-item" onclick="setPage('reports', this)" data-tooltip="Reports">
          <i class="fa-regular fa-chart-bar"></i>
          <span>Reports</span>
        </button>
        <button class="nav-item" onclick="setPage('leaderboard', this)" data-tooltip="Leaderboard">
          <i class="fa-regular fa-trophy"></i>
          <span>Leaderboard</span>
        </button>
        <button class="nav-item" onclick="setPage('cycles', this)" data-tooltip="Cycle History">
          <i class="fa-regular fa-rotate"></i>
          <span>Cycle History</span>
        </button>
        <button class="nav-item" onclick="setPage('technicians', this)" data-tooltip="Tech Manager">
          <i class="fa-regular fa-id-card"></i>
          <span>Tech Manager</span>
        </button>
        <button class="nav-item" onclick="setPage('automation', this)" data-tooltip="Automation">
          <i class="fa-regular fa-robot"></i>
          <span>Automation</span>
        </button>
      </div>

      <!-- QUICK ACTIONS GROUP -->
      <div class="nav-group" role="group" aria-label="Quick actions">
        <div class="nav-group-label" aria-hidden="true">Quick Actions</div>
        <button class="nav-item" onclick="openWhatsAppImport()" data-tooltip="Import Orders">
          <i class="fa-brands fa-whatsapp"></i>
          <span>Import Orders</span>
        </button>
        <button class="nav-item" onclick="openDailyAutoImport()" data-tooltip="Auto Daily Entry">
          <i class="fa-regular fa-file-excel"></i>
          <span>Auto Daily Entry</span>
        </button>
        <button class="nav-item" onclick="openWatchedPersonsModal()" data-tooltip="Watch List">
          <i class="fa-regular fa-eye"></i>
          <span>Watch List</span>
        </button>
      </div>

      <!-- BOTTOM CONTROLS - push to bottom -->
      <div style="margin-top:auto; padding-top: var(--space-4); border-top: 1px solid var(--neutral-200); display:flex; flex-direction:column; gap:2px;">
        <button class="nav-item" onclick="openEndCycleModal()" data-tooltip="End Cycle" style="color:var(--accent-600);">
          <i class="fa-regular fa-flag-checkered"></i>
          <span>End Cycle</span>
        </button>
        <button class="nav-item" onclick="openWhatsNewModal()" data-tooltip="What's New">
          <i class="fa-regular fa-sparkles"></i>
          <span>What's New</span>
          <span class="whats-new-badge">10</span>
        </button>
        <button class="nav-item" onclick="startOnboardingTour()" data-tooltip="Help Tour">
          <i class="fa-regular fa-circle-question"></i>
          <span>Help Tour</span>
        </button>
        <div class="nav-item" onclick="toggleDarkMode()" id="darkModeBtn" data-tooltip="Dark Mode">
          <i class="fa-regular fa-moon"></i>
          <span>Dark Mode</span>
        </div>
        <div class="nav-item" onclick="toggleSidebar()" data-tooltip="Expand" id="sidebarToggleBtn">
          <i class="fa-regular fa-chevron-left" id="sidebarToggleIcon"></i>
          <span>Collapse</span>
        </div>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="main-content" id="mainContent" role="main" aria-label="Page content">
      <!-- Top Bar - Streamlined -->
      <div class="top-bar">
        <!-- Left: Search -->
        <div style="position:relative;flex:1;min-width:0;max-width:420px;">
          <div class="search-bar" onclick="openCommandPalette()" style="cursor:pointer;" title="Search or press Ctrl+K">
            <i class="fa-regular fa-magnifying-glass"></i>
            <input type="text" placeholder="Search orders, technicians… (Ctrl+K)" id="globalSearch" oninput="handleGlobalSearch()" autocomplete="off">
            <span class="kbd" style="font-size:11px;opacity:0.6;white-space:nowrap;">Ctrl K</span>
          </div>
          <div id="searchDropdown" style="display:none;position:absolute;top:calc(100% + 6px);left:0;right:0;background:white;border:1px solid var(--neutral-200);border-radius:var(--radius-lg);box-shadow:var(--shadow-lg);z-index:999;max-height:380px;overflow-y:auto;"></div>
        </div>

        <!-- Right: Notifications + User -->
        <div class="flex items-center gap-3 topbar-right">
          <!-- Notifications Bell -->
          <div class="notif-bell btn btn-icon btn-ghost" id="notifBellBtn" onclick="toggleNotifications()" style="position:relative;" aria-label="Notifications" role="button" tabindex="0">
            <i class="fa-regular fa-bell"></i>
            <span class="notif-badge" id="notifBadge" style="display:none;">0</span>
          </div>
          <div class="notif-dropdown" id="notifDropdown" role="dialog" aria-label="Notifications panel">
            <div class="p-3 border-b border-neutral-100 flex items-center justify-between">
              <span class="font-bold text-sm">Notifications</span>
              <button class="btn btn-ghost btn-sm" onclick="clearNotifications()">Clear all</button>
            </div>
            <div id="notifList"><div class="p-6 text-center text-neutral-400 text-sm">No notifications</div></div>
          </div>

          <!-- Autosave Indicator (compact) -->
          <div class="autosave-indicator" id="autosaveIndicator" aria-live="polite">
            <div class="autosave-dot"></div>
            <span id="autosaveText">Saved</span>
          </div>

          <!-- User / Region pill -->
          <div style="display:flex;align-items:center;gap:var(--space-2);background:var(--neutral-100);border-radius:var(--radius-full);padding:4px 4px 4px 12px;">
            <span style="font-size:var(--text-xs);font-weight:500;color:var(--neutral-600);white-space:nowrap;" class="topbar-region-label">Region</span>
            <div class="select-wrapper" style="width:150px;">
              <select class="select-field" id="regionSelect" onchange="changeRegion()" style="background:white;border-radius:var(--radius-full);padding:6px 32px 6px 12px;font-size:var(--text-xs);"></select>
            </div>
          </div>
        </div>
      </div>

      <!-- Breadcrumb Row -->
      <div class="breadcrumb" id="pageBreadcrumb" aria-label="Breadcrumb">
        <div class="breadcrumb-item">
          <span onclick="setPage('dashboard',null)" style="cursor:pointer;"><i class="fa-regular fa-house" style="font-size:11px;"></i></span>
        </div>
        <span class="breadcrumb-sep"><i class="fa-regular fa-chevron-right" style="font-size:9px;"></i></span>
        <div class="breadcrumb-item current" id="breadcrumbCurrent">
          <span>Daily</span>
        </div>
        <span style="margin-left:auto;font-size:var(--text-xs);color:var(--neutral-400);" id="breadcrumbRegionPill"></span>
      </div>

      <!-- Dynamic Page Content -->
      <div id="pageContent"></div>
    </main>
  </div>

  <!-- Mobile Bottom Nav -->
  <nav class="mobile-bottom-nav" id="mobileBottomNav">
    <button class="mobile-nav-item" onclick="mobileNav('dashboard', this)"><i class="fa-regular fa-gauge-high"></i><span>Home</span></button>
    <button class="mobile-nav-item active" onclick="mobileNav('daily', this)"><i class="fa-regular fa-calendar"></i><span>Daily</span></button>
    <button class="mobile-nav-item" onclick="mobileNav('orders', this)"><i class="fa-regular fa-file-lines"></i><span>Orders</span></button>
    <button class="mobile-nav-item" onclick="mobileNav('technicians', this)"><i class="fa-regular fa-id-card"></i><span>Techs</span></button>
    <button class="mobile-nav-item" onclick="mobileNav('automation', this)"><i class="fa-regular fa-robot"></i><span>Auto</span></button>
    <button class="mobile-nav-item" onclick="mobileNav('reports', this)"><i class="fa-regular fa-chart-bar"></i><span>Reports</span></button>
    <button class="mobile-nav-item" onclick="mobileNav('cycles', this)"><i class="fa-regular fa-rotate"></i><span>Cycles</span></button>
  </nav>

  <!-- Floating Action Button -->
  <div class="fab-container">
    <button class="fab-main" onclick="toggleFabMenu()" id="fabMain">
      <i class="fa-regular fa-plus"></i>
    </button>
    <div class="fab-menu" id="fabMenu">
      <button class="fab-item" onclick="toggleFabMenu(); fabGoAddEntry()">
        <i class="fa-regular fa-calendar-plus"></i>
        <span>Add Entry</span>
      </button>
      <button class="fab-item" onclick="toggleFabMenu(); fabGoCreateOrder()">
        <i class="fa-regular fa-file-lines"></i>
        <span>Create Order</span>
      </button>
      <button class="fab-item" onclick="toggleFabMenu(); fabGoSummary()">
        <i class="fa-regular fa-chart-pie"></i>
        <span>Summary</span>
      </button>
      <button class="fab-item" onclick="toggleFabMenu(); openTargetModal()">
        <i class="fa-regular fa-bullseye"></i>
        <span>Set Target</span>
      </button>
      <button class="fab-item" style="background:linear-gradient(135deg,#0d6efd,#0a58ca);color:white;" onclick="toggleFabMenu(); openWhatsAppImport()">
        <i class="fa-brands fa-whatsapp"></i>
        <span>Import WhatsApp</span>
      </button>
      <button class="fab-item" style="background:linear-gradient(135deg,#198754,#146c43);color:white;" onclick="toggleFabMenu(); openDailyAutoImport()">
        <i class="fa-regular fa-file-excel"></i>
        <span>Auto Daily Entry</span>
      </button>
    </div>
  </div>

  <!-- ===== AUTOMATION MODALS ===== -->

  <!-- Daily History CRUD Modal -->
  <div class="modal-overlay" id="dailyHistoryModal">
    <div class="modal-container" style="max-width:820px;max-height:92vh;overflow-y:auto;">
      <div class="modal-header">
        <div>
          <h3 class="text-xl font-semibold" id="historyModalTitle">Day Detail</h3>
          <p class="text-sm mt-1" style="color:var(--neutral-500);">View, edit or delete entries for this day</p>
        </div>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('dailyHistoryModal')"><i class="fa-regular fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <input type="hidden" id="historyModalDate">
        <div id="historyModalEntries"></div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="historyGoToDate(document.getElementById('historyModalDate').value)">
          <i class="fa-regular fa-calendar"></i> Load in Daily Entry
        </button>
        <button class="btn btn-primary" onclick="closeModal('dailyHistoryModal')">
          <i class="fa-regular fa-check"></i> Done
        </button>
      </div>
    </div>
  </div>

  <!-- WhatsApp Order Import Modal -->
  <div class="modal-overlay" id="whatsappImportModal">
    <div class="modal-container" style="max-width:780px;max-height:92vh;overflow-y:auto;">
      <div class="modal-header">
        <div>
          <h3 class="text-xl font-semibold" style="color:var(--status-info);">📲 WhatsApp Order Import</h3>
          <p class="text-sm mt-1" style="color:var(--neutral-500);">Paste or upload a WhatsApp export (.txt) to automatically create orders</p>
        </div>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('whatsappImportModal')"><i class="fa-regular fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <!-- Step indicator -->
        <div class="flex gap-2 mb-5" id="waImportSteps">
          <div class="badge badge-info" id="waStep1Badge">1 · Paste Text</div>
          <div class="badge badge-neutral" id="waStep2Badge">2 · Review Orders</div>
          <div class="badge badge-neutral" id="waStep3Badge">3 · Import</div>
        </div>

        <!-- Step 1: Input -->
        <div id="waStep1">
          <p class="text-sm mb-3" style="color:var(--neutral-600);">Export the WhatsApp chat as a .txt file and either paste the content below or upload the file directly. The system will automatically find all MERU OTP messages and extract the order details.</p>

          <!-- Date range filter -->
          <div class="card mb-3" style="background:var(--neutral-50);padding:var(--space-3);">
            <div class="text-sm font-semibold mb-2" style="color:var(--neutral-700);">
              <i class="fa-regular fa-calendar-range"></i> Date Filter <span style="font-weight:400;color:var(--neutral-500);">— only import orders within this date range</span>
            </div>
            <div class="flex gap-3 items-center flex-wrap">
              <div>
                <label class="text-xs font-semibold" style="color:var(--neutral-500);">FROM DATE</label>
                <input type="date" class="input-field mt-1" id="waDateFrom" style="width:160px;padding:8px 12px;">
              </div>
              <div>
                <label class="text-xs font-semibold" style="color:var(--neutral-500);">TO DATE</label>
                <input type="date" class="input-field mt-1" id="waDateTo" style="width:160px;padding:8px 12px;" value="${new Date().toISOString().slice(0,10)}">
              </div>
              <button class="btn btn-ghost btn-sm mt-3" onclick="document.getElementById('waDateFrom').value='';document.getElementById('waDateTo').value='';" style="color:var(--neutral-500);">
                <i class="fa-regular fa-xmark"></i> Clear filter (import all dates)
              </button>
            </div>
          </div>

          <div class="flex gap-2 mb-3">
            <label class="btn btn-secondary btn-sm cursor-pointer">
              <i class="fa-regular fa-folder-open"></i> Upload .txt File
              <input type="file" accept=".txt" style="display:none;" onchange="waHandleFileUpload(event)">
            </label>
            <button class="btn btn-ghost btn-sm" onclick="document.getElementById('waTextInput').value='';document.getElementById('waTextInput').focus()">
              <i class="fa-regular fa-eraser"></i> Clear
            </button>
          </div>
          <textarea id="waTextInput" class="input-field" rows="8" style="resize:vertical;min-height:150px;font-family:var(--font-mono);font-size:0.78rem;" placeholder="Paste WhatsApp export text here...
Example:
08/03/2026, 09:27 - +260 977860459: Dear Customer, 75915165 is the OTP to complete the fuel consumption at MERU stations..."></textarea>
          <div class="flex justify-end mt-4">
            <button class="btn btn-primary" onclick="waParseTxt()"><i class="fa-regular fa-magnifying-glass"></i> Parse Messages</button>
          </div>
        </div>

        <!-- Step 2: Review -->
        <div id="waStep2" style="display:none;">
          <div id="waParseSummary" class="card mb-4" style="background:var(--neutral-50);"></div>
          <div id="waOrdersPreview"></div>
          <div class="flex justify-between mt-4">
            <button class="btn btn-secondary" onclick="waBackToStep1()"><i class="fa-regular fa-arrow-left"></i> Back</button>
            <button class="btn btn-primary" onclick="waConfirmImport()" id="waImportBtn"><i class="fa-regular fa-file-import"></i> Import Selected Orders</button>
          </div>
        </div>

        <!-- Step 3: Result -->
        <div id="waStep3" style="display:none;">
          <div id="waImportResult"></div>
          <div class="flex justify-end mt-4">
            <button class="btn btn-primary" onclick="closeModal('whatsappImportModal'); renderPageWithTransition(currentPage)"><i class="fa-regular fa-check"></i> Done</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Auto Daily Entry Import Modal -->
  <div class="modal-overlay" id="dailyAutoImportModal">
    <div class="modal-container" style="max-width:720px;max-height:92vh;overflow-y:auto;">
      <div class="modal-header">
        <div>
          <h3 class="text-xl font-semibold" style="color:var(--status-success);">📊 Auto Daily Entry Import</h3>
          <p class="text-sm mt-1" style="color:var(--neutral-500);">Upload an Excel file with technician supply data to auto-fill daily entries (oldest order first)</p>
        </div>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('dailyAutoImportModal')"><i class="fa-regular fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <div class="card mb-4" style="background:var(--status-info-bg);border:1px solid var(--status-info);">
          <div class="text-sm" style="color:var(--status-info);">
            <strong>📋 Excel Format Required:</strong> Your file must have these columns:<br>
            <code style="background:rgba(0,0,0,0.07);padding:2px 6px;border-radius:4px;font-size:0.75rem;">Technician | Date | Total Supplied</code><br>
            <span style="color:var(--neutral-600);margin-top:4px;display:block;">Date format: DD/MM/YYYY or YYYY-MM-DD. Supply system will fill oldest orders first.</span>
          </div>
        </div>

        <!-- Template download -->
        <div class="flex gap-2 mb-4">
          <button class="btn btn-secondary btn-sm" onclick="downloadDailyImportTemplate()">
            <i class="fa-regular fa-file-excel"></i> Download Template
          </button>
          <label class="btn btn-primary btn-sm cursor-pointer">
            <i class="fa-regular fa-folder-open"></i> Upload Excel File
            <input type="file" accept=".xlsx,.xls,.csv" style="display:none;" onchange="dailyAutoHandleFile(event)">
          </label>
        </div>

        <div id="dailyAutoPreview" style="display:none;">
          <div id="dailyAutoSummary" class="card mb-3" style="background:var(--neutral-50);"></div>
          <div id="dailyAutoEntriesPreview" class="mb-4"></div>
          <div class="flex justify-between">
            <button class="btn btn-secondary btn-sm" onclick="document.getElementById('dailyAutoPreview').style.display='none'">
              <i class="fa-regular fa-arrow-left"></i> Back
            </button>
            <button class="btn btn-primary" onclick="dailyAutoConfirmImport()">
              <i class="fa-regular fa-file-import"></i> Apply Entries
            </button>
          </div>
        </div>

        <div id="dailyAutoResult" style="display:none;"></div>
      </div>
    </div>
  </div>

  <!-- Watched Persons / Notification Config Modal -->
  <div class="modal-overlay" id="watchedPersonsModal">
    <div class="modal-container" style="max-width:560px;">
      <div class="modal-header">
        <div>
          <h3 class="text-xl font-semibold" style="color:var(--status-warning);">👁️ WhatsApp Watch List</h3>
          <p class="text-sm mt-1" style="color:var(--neutral-500);">Get notified when these people post during WhatsApp import</p>
        </div>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('watchedPersonsModal')"><i class="fa-regular fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <p class="text-sm mb-3" style="color:var(--neutral-600);">Add names exactly as they appear in the WhatsApp export (the sender name before the colon). Partial matches work — e.g. "John IHS" matches "~John IHS👨🏽‍🔧".</p>
        <div class="card mb-4" style="background:var(--status-info-bg);border:1px solid var(--status-info);padding:var(--space-3);">
          <p class="text-xs" style="color:var(--status-info);"><i class="fa-regular fa-calendar-clock"></i> <strong>Recency filter active:</strong> Only messages from the <strong>last 3 days</strong> will appear in watch list alerts. Older messages are automatically ignored.</p>
        </div>
        <div class="flex gap-2 mb-4">
          <div class="input-group flex-1" style="margin-bottom:0;">
            <input type="text" class="input-field" id="watchPersonInput" placeholder=" " onkeydown="if(event.key==='Enter')addWatchedPerson()">
            <label class="input-label">Person to watch (name)</label>
          </div>
          <button class="btn btn-primary" onclick="addWatchedPerson()"><i class="fa-regular fa-plus"></i> Add</button>
        </div>
        <div id="watchedPersonsList"></div>
        <div class="card mt-4" style="background:var(--status-warning-bg);border:1px solid var(--status-warning);">
          <p class="text-sm" style="color:var(--status-warning);"><strong>⚡ How it works:</strong> When you import a WhatsApp .txt, the system scans every message. If a watched person posted anything, you'll see a ⚠️ notification panel in the import results with their exact messages highlighted.</p>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-primary" onclick="saveWatchedPersons()"><i class="fa-regular fa-check"></i> Save</button>
      </div>
    </div>
  </div>

  <!-- End Cycle Modal -->
  <div class="modal-overlay" id="endCycleModal">
    <div class="modal-container" style="max-width: 520px;">
      <div class="modal-header">
        <div>
          <h3 class="text-xl font-semibold">🏁 End Current Cycle</h3>
          <p class="text-sm mt-1" style="color:var(--neutral-500);">All data will be archived. A fresh cycle will begin.</p>
        </div>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('endCycleModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <div class="card mb-4" style="background:#fff8f8;border:1px solid var(--status-danger);border-left:4px solid var(--status-danger);">
          <div class="flex items-center gap-3">
            <span style="font-size:1.75rem;">⚠️</span>
            <div>
              <div class="font-semibold" style="color:var(--status-danger);">This action is irreversible</div>
              <div class="text-sm mt-1" style="color:var(--neutral-600);">Orders, daily logs, and allocations will be archived to Cycle History. The new cycle will start fresh with the same regions and technicians.</div>
            </div>
          </div>
        </div>
        <div id="endCycleSummaryCard" class="card mb-4" style="background:var(--neutral-50);"></div>
        <div class="mb-4">
          <label class="block text-sm font-semibold mb-2">Name the <strong>new</strong> cycle</label>
          <input type="text" class="input-field" id="newCycleName" placeholder="e.g. FEBRUARY CYCLE" style="text-transform:uppercase;font-weight:600;font-size:1rem;letter-spacing:0.03em;">
          <p class="text-xs mt-1" style="color:var(--neutral-500);">Give the new cycle a clear name so it's easy to identify later.</p>
        </div>
        <!-- Destructive confirmation -->
        <div class="danger-confirm-wrap">
          <p class="text-sm font-semibold" style="color:var(--neutral-700);">To confirm, type the current cycle name below:</p>
          <div class="confirm-phrase" id="endCycleConfirmPhrase">INITIAL CYCLE</div>
          <input type="text" class="danger-confirm-input" id="endCycleConfirmInput" placeholder="Type cycle name to confirm…" oninput="checkEndCycleConfirm()" autocomplete="off">
          <div class="field-hint" id="endCycleConfirmHint" style="margin-top:6px;"></div>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal('endCycleModal')">Cancel</button>
        <button class="btn btn-primary" id="endCycleConfirmBtn" onclick="confirmEndCycle()" disabled style="background:linear-gradient(135deg,var(--accent-800),var(--accent-600));opacity:0.5;cursor:not-allowed;">
          <i class="fa-regular fa-flag-checkered"></i> End Cycle &amp; Start New
        </button>
      </div>
    </div>
  </div>

  <!-- View Past Cycle Modal -->
  <div class="modal-overlay" id="viewCycleModal">
    <div id="viewCycleModalContainer" class="modal-container" style="max-width:960px;width:95vw;max-height:92vh;overflow-y:auto;transition:all 0.3s ease;">
      <div class="modal-header" style="position:sticky;top:0;background:white;z-index:10;border-bottom:1px solid var(--neutral-200);">
        <div style="flex:1;min-width:0;">
          <h3 class="text-xl font-semibold" id="viewCycleTitle">Cycle Details</h3>
          <p class="text-sm mt-1" style="color:var(--neutral-500);" id="viewCycleSubtitle"></p>
        </div>
        <div style="display:flex;align-items:center;gap:8px;flex-shrink:0;">
          <button class="btn btn-secondary btn-sm" id="cycleExpandBtn" onclick="toggleCycleFullscreen()" title="Expand to fullscreen">
            <i class="fa-regular fa-expand" id="cycleExpandIcon"></i>
            <span id="cycleExpandLabel">Expand</span>
          </button>
          <button class="btn btn-icon btn-ghost" onclick="closeModal('viewCycleModal')">
            <i class="fa-regular fa-xmark"></i>
          </button>
        </div>
      </div>
      <div class="modal-body" id="viewCycleContent" style="padding:var(--space-5);"></div>
      <div class="modal-footer" style="position:sticky;bottom:0;background:white;z-index:10;border-top:1px solid var(--neutral-200);">
        <button class="btn btn-secondary" onclick="closeModal('viewCycleModal')">Close</button>
        <button class="btn btn-secondary" id="cycleEditBtn" onclick="openCycleEditor(window._viewingCycleIdx)">
          <i class="fa-regular fa-pen-to-square"></i> Edit Cycle
        </button>
        <button class="btn btn-primary" onclick="exportCycleData(window._viewingCycleIdx)">
          <i class="fa-regular fa-download"></i> Export to Excel
        </button>
      </div>
    </div>
  </div>

  <!-- Cycle Editor Modal -->
  <div class="modal-overlay" id="cycleEditorModal">
    <div id="cycleEditorContainer" class="modal-container" style="max-width:980px;width:96vw;max-height:94vh;overflow-y:auto;transition:all 0.3s ease;">
      <div class="modal-header" style="position:sticky;top:0;background:white;z-index:10;border-bottom:1px solid var(--neutral-200);">
        <div style="flex:1;min-width:0;">
          <h3 class="text-xl font-semibold" id="cycleEditorTitle">Edit Cycle</h3>
          <p class="text-sm mt-1" style="color:var(--status-warning);" id="cycleEditorSubtitle"></p>
        </div>
        <div style="display:flex;gap:8px;align-items:center;flex-shrink:0;">
          <button class="btn btn-secondary btn-sm" id="cycleEditorExpandBtn" onclick="toggleCycleEditorFullscreen()" title="Expand">
            <i class="fa-regular fa-expand" id="cycleEditorExpandIcon"></i>
          </button>
          <button class="btn btn-icon btn-ghost" onclick="closeModal('cycleEditorModal')">
            <i class="fa-regular fa-xmark"></i>
          </button>
        </div>
      </div>
      <div class="modal-body" id="cycleEditorContent" style="padding:var(--space-5);"></div>
      <div class="modal-footer" style="position:sticky;bottom:0;background:white;z-index:10;border-top:1px solid var(--neutral-200);">
        <button class="btn btn-secondary" onclick="closeModal('cycleEditorModal')">Cancel</button>
        <button class="btn btn-primary" onclick="saveCycleEdits()">
          <i class="fa-regular fa-floppy-disk"></i> Save All Changes
        </button>
      </div>
    </div>
  </div>

  <!-- ===== COMMAND PALETTE ===== -->
  <div class="cmd-overlay" id="cmdOverlay" role="dialog" aria-modal="true" aria-label="Command palette">
    <div class="cmd-palette" id="cmdPalette">
      <div class="cmd-input-wrap">
        <i class="fa-regular fa-magnifying-glass"></i>
        <input type="text" class="cmd-input" id="cmdInput" placeholder="Search pages, actions, technicians…" autocomplete="off" aria-label="Command palette search">
        <span class="cmd-kbd-hint"><span class="kbd" style="font-size:10px;">ESC</span> to close</span>
      </div>
      <div class="cmd-body" id="cmdBody" role="listbox"></div>
      <div class="cmd-footer">
        <span class="cmd-footer-hint"><span class="kbd" style="font-size:10px;">↑↓</span> navigate</span>
        <span class="cmd-footer-hint"><span class="kbd" style="font-size:10px;">↵</span> select</span>
        <span class="cmd-footer-hint"><span class="kbd" style="font-size:10px;">Ctrl K</span> toggle</span>
      </div>
    </div>
  </div>

  <!-- ===== ONBOARDING TOUR ===== -->
  <div class="tour-backdrop" id="tourBackdrop" style="display:none;">
    <div class="tour-spotlight" id="tourSpotlight"></div>
  </div>
  <div class="tour-tooltip" id="tourTooltip" style="display:none;">
    <div class="tour-step-indicator" id="tourStepIndicator">Step 1 of 6</div>
    <div class="tour-title" id="tourTitle"></div>
    <div class="tour-desc" id="tourDesc"></div>
    <div class="tour-actions">
      <button class="btn btn-ghost btn-sm" onclick="endTour()">Skip tour</button>
      <div style="display:flex;gap:var(--space-2);">
        <button class="btn btn-secondary btn-sm" id="tourPrevBtn" onclick="tourPrev()">Back</button>
        <button class="btn btn-primary btn-sm" id="tourNextBtn" onclick="tourNext()">Next →</button>
      </div>
    </div>
  </div>

  <!-- ===== WHAT'S NEW MODAL ===== -->
  <div class="modal-overlay" id="whatsNewModal">
    <div class="modal-container" style="max-width:520px;">
      <div class="modal-header">
        <h3 class="text-xl font-semibold"><i class="fa-regular fa-sparkles" style="color:var(--accent-600);margin-right:8px;"></i>What's New</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('whatsNewModal')"><i class="fa-regular fa-xmark"></i></button>
      </div>
      <div class="modal-body" style="padding:0;">
        <div style="padding:var(--space-5) var(--space-6);">
          <div style="display:flex;align-items:center;gap:var(--space-3);margin-bottom:var(--space-5);">
            <span class="badge badge-success">Latest</span>
            <span class="text-sm font-semibold">v2.0 — UI Redesign</span>
            <span class="text-xs" style="color:var(--neutral-400);margin-left:auto;">${new Date().toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'})}</span>
          </div>
          <div style="display:flex;flex-direction:column;gap:var(--space-4);">
            <div style="display:flex;gap:var(--space-3);"><div style="width:28px;height:28px;border-radius:var(--radius-md);background:var(--accent-100);display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="fa-regular fa-sidebar" style="color:var(--accent-600);font-size:12px;"></i></div><div><div class="font-semibold text-sm">Improved Sidebar Navigation</div><div class="text-xs" style="color:var(--neutral-500);margin-top:2px;">Navigation grouped into Main and Quick Actions with tooltip labels when collapsed.</div></div></div>
            <div style="display:flex;gap:var(--space-3);"><div style="width:28px;height:28px;border-radius:var(--radius-md);background:var(--status-info-bg);display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="fa-regular fa-magnifying-glass" style="color:var(--status-info);font-size:12px;"></i></div><div><div class="font-semibold text-sm">Command Palette (Ctrl+K)</div><div class="text-xs" style="color:var(--neutral-500);margin-top:2px;">Quick access to any page, action, or search result from anywhere in the app.</div></div></div>
            <div style="display:flex;gap:var(--space-3);"><div style="width:28px;height:28px;border-radius:var(--radius-md);background:var(--status-success-bg);display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="fa-regular fa-shield" style="color:var(--status-success);font-size:12px;"></i></div><div><div class="font-semibold text-sm">Safer End Cycle Confirmation</div><div class="text-xs" style="color:var(--neutral-500);margin-top:2px;">Now requires typing the cycle name before confirming — prevents accidental data loss.</div></div></div>
            <div style="display:flex;gap:var(--space-3);"><div style="width:28px;height:28px;border-radius:var(--radius-md);background:var(--status-warning-bg);display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="fa-regular fa-map-pin" style="color:var(--status-warning);font-size:12px;"></i></div><div><div class="font-semibold text-sm">Breadcrumb Navigation</div><div class="text-xs" style="color:var(--neutral-500);margin-top:2px;">Page location and region always visible below the top bar.</div></div></div>
            <div style="display:flex;gap:var(--space-3);"><div style="width:28px;height:28px;border-radius:var(--radius-md);background:var(--neutral-100);display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="fa-regular fa-table-columns" style="color:var(--neutral-600);font-size:12px;"></i></div><div><div class="font-semibold text-sm">Table Density Toggle</div><div class="text-xs" style="color:var(--neutral-500);margin-top:2px;">Switch between Compact, Default and Comfortable row density in data tables.</div></div></div>
          </div>
        </div>
        <div style="padding:var(--space-4) var(--space-6);background:var(--neutral-50);border-top:1px solid var(--neutral-200);">
          <button class="btn btn-secondary btn-sm" onclick="startOnboardingTour();closeModal('whatsNewModal')"><i class="fa-regular fa-circle-play"></i> Take a quick tour</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Container -->
  <div class="toast-container" id="toastContainer"></div>

  <!-- Context Menu -->
  <div class="context-menu" id="contextMenu"></div>

  <!-- Keyboard Shortcuts Modal -->
  <div class="modal-overlay" id="shortcutsModal">
    <div class="modal-container" style="max-width: 500px;">
      <div class="modal-header">
        <h3 class="text-xl font-semibold">Keyboard Shortcuts</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('shortcutsModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <div class="shortcut-grid">
          <div class="shortcut-item">
            <span class="kbd">K</span>
            <span>Search</span>
          </div>
          <div class="shortcut-item">
            <span class="kbd">S</span>
            <span>Save (Daily page)</span>
          </div>
          <div class="shortcut-item">
            <span class="kbd">ESC</span>
            <span>Close modal / clear search</span>
          </div>
          <div class="shortcut-item">
            <span class="kbd">B</span>
            <span>Toggle sidebar</span>
          </div>
          <div class="shortcut-item">
            <span class="kbd">D</span>
            <span>Go to Dashboard</span>
          </div>
          <div class="shortcut-item">
            <span class="kbd">O</span>
            <span>Go to Orders</span>
          </div>
          <div class="shortcut-item">
            <span class="kbd">L</span>
            <span>Go to Leaderboard</span>
          </div>
          <div class="shortcut-item">
            <span class="kbd">/</span>
            <span>Show this menu</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Edit Modal -->
  <div class="modal-overlay" id="editModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="text-xl font-semibold">Edit Entry</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('editModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <div class="input-group">
          <input type="number" class="input-field" id="editSupplied" placeholder=" ">
          <label class="input-label">Litres Supplied</label>
        </div>
        <div class="input-group" id="editCommentGroup" style="display: none;">
          <input type="text" class="input-field" id="editComment" placeholder=" ">
          <label class="input-label">Comment</label>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal('editModal')">Cancel</button>
        <button class="btn btn-primary" onclick="saveEditEntry()">Save Changes</button>
      </div>
    </div>
  </div>

  <!-- Overage Modal -->
  <div class="modal-overlay" id="overageModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="text-xl font-semibold">Overage Comment</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('overageModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <div class="text-sm mb-4" id="overageMeta"></div>
        <div class="input-group">
          <input type="text" class="input-field" id="overageComment" placeholder=" ">
          <label class="input-label">Reason for overage</label>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal('overageModal')">Cancel</button>
        <button class="btn btn-primary" onclick="saveOverageComment()">Save</button>
      </div>
    </div>
  </div>

  <!-- Summary Modal -->
  <div class="modal-overlay" id="summaryModal">
    <div class="modal-container" style="max-width: 980px;">
      <div class="modal-header">
        <h3 class="text-xl font-semibold" id="summaryModalTitle">Summary Report</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('summaryModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <div class="stats-grid grid-cols-4 mb-4">
          <div class="stat-tile">
            <div class="stat-label">Total Ordered (Assigned)</div>
            <div class="stat-value" id="summaryTotalOrdered">0L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Total Supplied (All Time)</div>
            <div class="stat-value text-success-700" id="summaryTotalSupplied">0L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Balance (Assigned)</div>
            <div class="stat-value text-error-700" id="summaryBalance">0L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Entries This Day</div>
            <div class="stat-value" id="summaryEntries">0</div>
          </div>
        </div>

        <!-- Per-Technician Open Order Totals -->
        <div id="summaryTechBreakdown"></div>

        <!-- Daily Entries Table -->
        <h4 class="text-lg font-semibold mt-5 mb-3" style="display:flex;align-items:center;gap:8px;">
          <i class="fa-regular fa-calendar-day" style="color:var(--accent-600);"></i>
          Daily Entries
        </h4>
        <div class="table-container">
          <table class="table">
            <thead>
              <tr>
                <th>Date</th>
                <th>Technician</th>
                <th>Order</th>
                <th>Supplied</th>
                <th>Type</th>
              </tr>
            </thead>
            <tbody id="summaryTableBody"></tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

  <!-- Tech History Modal -->
  <div class="modal-overlay" id="techHistoryModal">
    <div class="modal-container" style="max-width: 600px;">
      <div class="modal-header">
        <h3 class="text-xl font-semibold" id="techHistoryTitle">Technician History</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('techHistoryModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <div class="stats-grid grid-cols-3 mb-4">
          <div class="stat-tile">
            <div class="stat-label">Total (Allocated)</div>
            <div class="stat-value" id="techTotal">0L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Days Active</div>
            <div class="stat-value" id="techDays">0</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Orders</div>
            <div class="stat-value" id="techOrders">0</div>
          </div>
        </div>
        <div id="techHistoryList"></div>
      </div>
    </div>
  </div>

  <!-- Rename Modal -->
  <div class="modal-overlay" id="renameModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="text-xl font-semibold" id="renameTitle">Rename</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('renameModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <div class="input-group">
          <input type="text" class="input-field" id="renameInput" placeholder=" ">
          <label class="input-label">New Name</label>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal('renameModal')">Cancel</button>
        <button class="btn btn-primary" onclick="confirmRename()">Rename</button>
      </div>
    </div>
  </div>

  <!-- Clone Modal -->
  <div class="modal-overlay" id="cloneModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="text-xl font-semibold">Clone Order</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('cloneModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <div class="card mb-4">
          <div id="clonePreview"></div>
        </div>
        <div class="input-group">
          <input type="text" class="input-field" id="cloneOrderNo" placeholder=" ">
          <label class="input-label">New Order Number</label>
        </div>
        <div class="input-group">
          <input type="date" class="input-field" id="cloneOrderDate">
          <label class="input-label">Order Date</label>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal('cloneModal')">Cancel</button>
        <button class="btn btn-primary" onclick="confirmClone()">Create Clone</button>
      </div>
    </div>
  </div>

  <!-- Multi-Date Summary Modal -->
  <div class="modal-overlay" id="multiDateModal">
    <div class="modal-container" style="max-width: 800px;">
      <div class="modal-header">
        <h3 class="text-xl font-semibold">Multi-Date Summary</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('multiDateModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <div class="stats-grid grid-cols-3 mb-6" id="multiDateStats">
          <div class="stat-tile">
            <div class="stat-label">Selected Dates</div>
            <div class="stat-value" id="selectedDatesCount">0</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Total Supplied (Allocated)</div>
            <div class="stat-value" id="multiDateTotal">0L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Total Entries</div>
            <div class="stat-value" id="multiDateEntries">0</div>
          </div>
        </div>

        <div class="mb-4">
          <div class="flex items-center justify-between mb-3">
            <h4 class="text-lg font-semibold">Select Dates</h4>
            <div class="flex gap-2">
              <button class="btn btn-secondary btn-sm" onclick="selectAllDates(true)"><i class="fa-regular fa-check-double"></i> Select All</button>
              <button class="btn btn-secondary btn-sm" onclick="selectAllDates(false)"><i class="fa-regular fa-xmark"></i> Clear All</button>
            </div>
          </div>
          <div class="date-grid" id="dateGrid"></div>
        </div>

        <div class="flex gap-2 justify-end">
          <button class="btn btn-secondary" onclick="closeModal('multiDateModal')">Cancel</button>
          <button class="btn btn-primary" onclick="generateMultiDateSummary()">Generate Summary</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Multi-Date Results Modal -->
  <div class="modal-overlay" id="multiDateResultsModal">
    <div class="modal-container" style="max-width: 1000px;">
      <div class="modal-header">
        <h3 class="text-xl font-semibold">Multi-Date Summary Results</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('multiDateResultsModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <div id="multiDateResults"></div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal('multiDateResultsModal')">Close</button>
        <button class="btn btn-primary" onclick="exportMultiDateSummary()">Export to Excel</button>
      </div>
    </div>
  </div>

  <!-- Monthly Target Modal -->
  <div class="modal-overlay" id="targetModal">
    <div class="modal-container" style="max-width:420px;">
      <div class="modal-header">
        <h3 class="text-xl font-semibold">Set Monthly Target</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('targetModal')"><i class="fa-regular fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <p class="text-sm mb-4">Set a monthly litre target for <strong id="targetRegionLabel"></strong>. This appears on your dashboard as a progress tracker.</p>
        <div class="input-group">
          <input type="number" class="input-field" id="targetInput" placeholder=" " min="1">
          <label class="input-label">Monthly Litres Target</label>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal('targetModal')">Cancel</button>
        <button class="btn btn-primary" onclick="saveMonthlyTarget()"><i class="fa-regular fa-check"></i> Save Target</button>
      </div>
    </div>
  </div>

  <!-- Technician Targets Modal -->
  <div class="modal-overlay" id="techTargetModal">
    <div class="modal-container" style="max-width:520px;">
      <div class="modal-header">
        <h3 class="text-xl font-semibold">Technician Monthly Targets</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('techTargetModal')"><i class="fa-regular fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <p class="text-sm mb-4">Set monthly litre targets for each technician. These show as progress bars on the leaderboard.</p>
        <div id="techTargetBody"></div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal('techTargetModal')">Cancel</button>
        <button class="btn btn-primary" onclick="saveTechTargets()"><i class="fa-regular fa-check"></i> Save Targets</button>
      </div>
    </div>
  </div>

  <!-- Unassigned Order Comment Modal -->
  <div class="modal-overlay" id="unassignedCommentModal">
    <div class="modal-container" style="max-width: 500px;">
      <div class="modal-header">
        <h3 class="text-xl font-semibold" id="unassignedCommentTitle">Add Comment to Unassigned Order</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('unassignedCommentModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <div class="card mb-4" id="unassignedOrderPreview"></div>
        <div class="input-group">
          <textarea class="input-field" id="unassignedComment" rows="3" placeholder=" " style="resize: vertical; min-height: 80px;"></textarea>
          <label class="input-label">Comment / Notes</label>
        </div>
        <p class="text-sm text-neutral-500 mt-2">Add any notes about this unassigned order (reason for no allocation, special instructions, etc.)</p>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal('unassignedCommentModal')">Cancel</button>
        <button class="btn btn-primary" onclick="saveUnassignedComment()">Save Comment</button>
      </div>
    </div>
  </div>

  <!-- Order Detail Modal -->
  <div class="modal-overlay" id="orderDetailModal">
    <div class="modal-container" style="max-width: 680px;">
      <div class="modal-header">
        <h3 class="text-xl font-semibold" id="orderDetailTitle">Order Detail</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('orderDetailModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body" id="orderDetailContent"></div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal('orderDetailModal')">Close</button>
        <button class="btn btn-primary" id="orderDetailGoBtn">
          <i class="fa-regular fa-arrow-up-right-from-square"></i> Go to Orders Page
        </button>
      </div>
    </div>
  </div>

  <!-- Edit Order Modal -->
  <div class="modal-overlay" id="editOrderModal">
    <div class="modal-container" style="max-width: 500px;">
      <div class="modal-header">
        <h3 class="text-xl font-semibold" id="editOrderModalTitle">Edit Order</h3>
        <button class="btn btn-icon btn-ghost" onclick="closeModal('editOrderModal')">
          <i class="fa-regular fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body" id="editOrderModalBody"></div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal('editOrderModal')">Cancel</button>
        <button class="btn btn-primary" onclick="saveOrderEdits()">Save Changes</button>
      </div>
    </div>
  </div>

  <script>
    // ===== DATA LAYER =====
    const KEY = 'ccs_fuel_orders_v6';
    const DEFAULT = {
      currentRegion: 'New CCS',
      currentCycleName: 'INITIAL CYCLE',
      currentCycleStartDate: new Date().toISOString().slice(0,10),
      cycles: [],
      regions: { 'New CCS': { technicians: [], technicianPlates: {}, orders: {}, dailyLog: {}, monthlyTarget: null, techMonthlyTargets: {}, unassignedComments: {} } }
    };

    let DB = JSON.parse(localStorage.getItem(KEY)) || structuredClone(DEFAULT);
    let currentEditingOrder = null;

    // Ensure DB has cycle fields (migration for existing data)
    if (!DB.cycles) DB.cycles = [];
    if (!DB.currentCycleName) DB.currentCycleName = 'INITIAL CYCLE';
    if (!DB.currentCycleStartDate) DB.currentCycleStartDate = new Date().toISOString().slice(0,10);

    // Ensure each region has required objects
    Object.values(DB.regions).forEach(r => {
      if (!r.unassignedComments) r.unassignedComments = {};
      if (!r.techMonthlyTargets) r.techMonthlyTargets = {};
    });

    // ===== ANIMATED NUMBER COUNTER WITH SPRING EASING =====
    function animateCounter(el, target, suffix = '', duration = 800) {
      if (!el) return;
      
      const start = parseFloat(el.textContent.replace(/[^0-9.-]/g, '')) || 0;
      const startTime = performance.now();
      suffix = suffix || '';
      
      if (el._animationFrame) {
        cancelAnimationFrame(el._animationFrame);
      }
      
      function easeOutCubic(t) {
        return 1 - Math.pow(1 - t, 3);
      }
      
      function easeOutElastic(t) {
        return Math.sin(-13 * (t + 1) * Math.PI/2) * Math.pow(2, -10 * t) + 1;
      }
      
      function animate(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        const eased = progress < 0.8 
          ? easeOutCubic(progress / 0.8) * 0.8
          : 0.8 + easeOutElastic((progress - 0.8) / 0.2) * 0.2;
        
        const current = start + (target - start) * eased;
        
        if (Number.isInteger(target)) {
          el.textContent = Math.round(current).toLocaleString() + suffix;
        } else {
          el.textContent = current.toFixed(1).toLocaleString() + suffix;
        }
        
        if (progress < 1) {
          el._animationFrame = requestAnimationFrame(animate);
        } else {
          el.textContent = (Number.isInteger(target) 
            ? target.toLocaleString() 
            : target.toFixed(1).toLocaleString()) + suffix;
          
          el.style.transition = 'background-color 0.3s';
          el.style.backgroundColor = 'var(--accent-100)';
          setTimeout(() => {
            el.style.backgroundColor = '';
          }, 300);
        }
      }
      
      el._animationFrame = requestAnimationFrame(animate);
    }

    // ===== AUTOSAVE INDICATOR =====
    let _autosaveTimer = null;
    function save() {
      localStorage.setItem(KEY, JSON.stringify(DB));
      _showAutosave();
    }
    
    function _showAutosave() {
      const el = document.getElementById('autosaveIndicator');
      const txt = document.getElementById('autosaveText');
      if (!el) return;
      el.classList.remove('unsaved');
      el.classList.add('visible');
      if (txt) txt.textContent = 'Saved';
      const dot = el.querySelector('.autosave-dot');
      if (dot) { dot.replaceWith(dot.cloneNode(true)); }
      clearTimeout(_autosaveTimer);
      _autosaveTimer = setTimeout(() => el.classList.remove('visible'), 2500);
      
      // Update footer
      setAutosaveStatus('saved');
    }
    
    function _markUnsaved() {
      const el = document.getElementById('autosaveIndicator');
      const txt = document.getElementById('autosaveText');
      if (!el) return;
      clearTimeout(_autosaveTimer);
      el.classList.add('unsaved', 'visible');
      if (txt) txt.textContent = 'Unsaved changes';
      setAutosaveStatus('saving');
    }

    // ===== TOAST QUEUE SYSTEM =====
    const toastQueue = [];
    let isProcessingToast = false;
    const MAX_TOASTS = 3;

    function showToast(message, type = 'success', duration = 3500) {
      toastQueue.push({ message, type, duration });
      if (!isProcessingToast) {
        processToastQueue();
      }
    }

    function processToastQueue() {
      if (toastQueue.length === 0) {
        isProcessingToast = false;
        return;
      }

      isProcessingToast = true;
      const { message, type, duration } = toastQueue.shift();
      const container = document.getElementById('toastContainer');
      
      const existing = container.querySelectorAll('.toast:not(.removing)');
      if (existing.length >= MAX_TOASTS) {
        const oldest = existing[0];
        removeToast(oldest);
      }

      const icons = {
        success: 'fa-circle-check',
        error: 'fa-circle-xmark',
        warning: 'fa-triangle-exclamation',
        info: 'fa-circle-info',
      };

      const toast = document.createElement('div');
      toast.className = `toast ${type}`;
      toast.innerHTML = `
        <i class="fa-regular ${icons[type] || icons.info} toast-icon"></i>
        <span class="toast-msg">${message}</span>
        <button class="toast-close" onclick="this.closest('.toast') && removeToast(this.closest('.toast'))">
          <i class="fa-regular fa-xmark"></i>
        </button>
        <div class="toast-progress" style="animation-duration:${duration}ms;"></div>
      `;

      container.appendChild(toast);
      const timer = setTimeout(() => {
        removeToast(toast);
        setTimeout(processToastQueue, 300);
      }, duration);
      toast._timer = timer;
    }

    function removeToast(toast) {
      if (!toast || toast.classList.contains('removing')) return;
      clearTimeout(toast._timer);
      toast.classList.add('removing');
      setTimeout(() => {
        toast.remove();
      }, 260);
    }

    // ===== TECH AVATAR COLOR HELPER =====
    function techColor(name) {
      let hash = 0;
      for (let i = 0; i < name.length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash);
      return Math.abs(hash) % 8;
    }
    
    function techAvatarHtml(name, extra) {
      const c = techColor(name);
      return `<div class="tech-avatar" data-color="${c}" ${extra||''}>${name.charAt(0).toUpperCase()}</div>`;
    }

    // ===== DARK MODE =====
    function toggleDarkMode() {
      document.body.classList.toggle('dark-mode');
      const isDark = document.body.classList.contains('dark-mode');
      localStorage.setItem('ccs_dark_mode', isDark ? '1' : '0');
      const btn = document.getElementById('darkModeBtn');
      if (btn) btn.innerHTML = isDark
        ? '<i class="fa-regular fa-sun"></i><span>Light Mode</span>'
        : '<i class="fa-regular fa-moon"></i><span>Dark Mode</span>';
    }

    // ===== NOTIFICATIONS =====
    let _notifData = [];
    
    function buildNotifications() {
      _notifData = [];
      Object.entries(DB.regions).forEach(([rName, r]) => {
        Object.keys(r.orders).forEach(orderNo => {
          const order = r.orders[orderNo];
          if (Object.keys(order.allocations || {}).length === 0) {
            if (!r.unassignedComments || !r.unassignedComments[orderNo]) {
              _notifData.push({ 
                type: 'info', 
                icon: '📝', 
                bg: 'var(--status-info-bg)', 
                title: `Unassigned Order Needs Comment`, 
                desc: `${orderNo} · ${rName}`, 
                action: () => openUnassignedCommentModal(orderNo, rName) 
              });
            }
          }
        });
        
        Object.values(r.orders).forEach(o => {
          const balance = o.totalLiters - o.suppliedTotal;
          const progress = o.totalLiters > 0 ? (o.suppliedTotal / o.totalLiters) * 100 : 0;
          if (progress >= 90 && progress < 100) {
            _notifData.push({ 
              type: 'warn', 
              icon: '⚠️', 
              bg: 'var(--status-warning-bg)', 
              title: `Order ${o.orderNo} nearly full`, 
              desc: `${progress.toFixed(0)}% used · ${balance}L remaining · ${rName}`, 
              action: () => openOrderDetailModal(o.orderNo, rName) 
            });
          }
          
          Object.entries(o.allocations || {}).forEach(([tech, alloc]) => {
            const supplied = Object.values(r.dailyLog).flat().filter(e => e.orderNo === o.orderNo && e.technician === tech).reduce((s,e)=>s+e.supplied,0);
            if (supplied > alloc) {
              _notifData.push({ 
                type: 'error', 
                icon: '🔴', 
                bg: 'var(--status-danger-bg)', 
                title: `Overage: ${tech} on ${o.orderNo}`, 
                desc: `${(supplied-alloc).toFixed(1)}L over allocation · ${rName}`, 
                action: () => openOrderDetailModal(o.orderNo, rName) 
              });
            }
          });
        });
        
        const threeDaysAgo = new Date(Date.now() - 3*86400000).toISOString().slice(0,10);
        r.technicians.forEach(t => {
          const lastActive = Object.entries(r.dailyLog).filter(([date]) => date >= threeDaysAgo).some(([,entries]) => entries.some(e => e.technician === t));
          const hasAnyActivity = Object.values(r.dailyLog).flat().some(e => e.technician === t);
          if (!lastActive && hasAnyActivity) {
            _notifData.push({ 
              type: 'info', 
              icon: '👤', 
              bg: 'var(--status-info-bg)', 
              title: `${t} inactive 3+ days`, 
              desc: `No supply entries in the last 3 days · ${rName}`, 
              action: null 
            });
          }
        });
      });
      return _notifData;
    }

    function renderNotifications() {
      buildNotifications();
      runSmartAlerts();
      const badge = document.getElementById('notifBadge');
      const list = document.getElementById('notifList');
      if (!badge || !list) return;
      
      if (_notifData.length === 0) {
        badge.style.display = 'none';
        list.innerHTML = '<div class="p-6 text-center text-neutral-400"><i class="fa-regular fa-bell-slash text-2xl block mb-2"></i>No notifications</div>';
        return;
      }
      
      badge.style.display = 'flex';
      badge.textContent = _notifData.length;
      
      list.innerHTML = _notifData.map((n,i) => `
        <div class="notif-item" onclick="_notifData[${i}].action && _notifData[${i}].action(); closeNotifications();">
          <div class="notif-icon" style="background:${n.bg};">${n.icon}</div>
          <div class="notif-text">
            <div class="notif-title">${n.title}</div>
            <div class="notif-desc">${n.desc}</div>
          </div>
        </div>
      `).join('');
    }

    function toggleNotifications() {
      const dd = document.getElementById('notifDropdown');
      if (!dd) return;
      dd.classList.toggle('open');
      if (dd.classList.contains('open')) renderNotifications();
    }
    
    function closeNotifications() {
      const dd = document.getElementById('notifDropdown');
      if (dd) dd.classList.remove('open');
    }
    
    function clearNotifications() {
      _notifData = [];
      const badge = document.getElementById('notifBadge');
      const list = document.getElementById('notifList');
      if (badge) badge.style.display = 'none';
      if (list) list.innerHTML = '<div class="p-6 text-center text-neutral-400">No notifications</div>';
      closeNotifications();
    }

    // ===== MODAL MANAGEMENT WITH FOCUS TRAP =====
    const _focusTrapHandlers = new Map();
    
    function openModal(modalId) {
      const overlay = document.getElementById(modalId);
      if (!overlay) return;
      overlay.classList.add('active');
      overlay._triggerEl = document.activeElement;

      // Set ARIA dialog attributes
      overlay.setAttribute('role', 'dialog');
      overlay.setAttribute('aria-modal', 'true');
      // Try to find a heading to use as the accessible label
      const heading = overlay.querySelector('h2, h3, h4, [id$="Title"], [id$="title"]');
      if (heading) {
        if (!heading.id) heading.id = modalId + '_label';
        overlay.setAttribute('aria-labelledby', heading.id);
      }

      requestAnimationFrame(() => {
        const focusable = overlay.querySelectorAll(
          'button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
        );
        if (focusable.length) focusable[0].focus();

        const trapHandler = (e) => {
          if (e.key !== 'Tab') return;
          const focusableArr = Array.from(overlay.querySelectorAll(
            'button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
          ));
          if (!focusableArr.length) return;
          const first = focusableArr[0];
          const last = focusableArr[focusableArr.length - 1];
          
          if (e.shiftKey) {
            if (document.activeElement === first) {
              e.preventDefault();
              last.focus();
            }
          } else {
            if (document.activeElement === last) {
              e.preventDefault();
              first.focus();
            }
          }
        };
        
        document.addEventListener('keydown', trapHandler);
        _focusTrapHandlers.set(modalId, trapHandler);
      });
    }

    function closeModal(modalId) {
      const overlay = document.getElementById(modalId);
      if (!overlay) return;
      overlay.classList.remove('active');
      const handler = _focusTrapHandlers.get(modalId);
      if (handler) {
        document.removeEventListener('keydown', handler);
        _focusTrapHandlers.delete(modalId);
      }
      if (overlay._triggerEl && typeof overlay._triggerEl.focus === 'function') {
        requestAnimationFrame(() => overlay._triggerEl.focus());
      }
      // Reset fullscreen state for cycle modal
      if (modalId === 'viewCycleModal') {
        const container = document.getElementById('viewCycleModalContainer');
        const icon      = document.getElementById('cycleExpandIcon');
        const label     = document.getElementById('cycleExpandLabel');
        if (container) {
          container.dataset.fullscreen = '0';
          container.style.maxWidth   = '960px';
          container.style.width      = '95vw';
          container.style.maxHeight  = '92vh';
          container.style.height     = '';
          container.style.borderRadius = '';
          overlay.style.alignItems   = '';
        }
        if (icon)  icon.className   = 'fa-regular fa-expand';
        if (label) label.textContent = 'Expand';
      }
      // Reset fullscreen state for cycle editor modal
      if (modalId === 'cycleEditorModal') {
        const container = document.getElementById('cycleEditorContainer');
        const icon      = document.getElementById('cycleEditorExpandIcon');
        if (container) {
          container.dataset.fullscreen = '0';
          container.style.cssText = 'max-width:980px;width:96vw;max-height:94vh;overflow-y:auto;transition:all 0.3s ease;';
          overlay.style.alignItems = '';
        }
        if (icon) icon.className = 'fa-regular fa-expand';
      }
    }

    // ===== FLOATING ACTION BUTTON =====
    function toggleFabMenu() {
      const menu = document.getElementById('fabMenu');
      if (menu) menu.classList.toggle('open');
    }

    function fabGoAddEntry() {
      if (currentPage !== 'daily') {
        setPage('daily', null);
        setTimeout(() => addDailyEntry(), 400);
      } else {
        addDailyEntry();
      }
    }

    function fabGoCreateOrder() {
      if (currentPage !== 'orders') {
        setPage('orders', null);
        setTimeout(() => { 
          const form = document.getElementById('orderForm');
          if (form && form.style.display === 'none') toggleOrderForm();
        }, 400);
      } else {
        const form = document.getElementById('orderForm');
        if (form && form.style.display === 'none') toggleOrderForm();
      }
    }

    function fabGoSummary() {
      if (currentPage !== 'daily') {
        setPage('daily', null);
        setTimeout(() => openSummaryModal(), 400);
      } else {
        openSummaryModal();
      }
    }

    // ===== MOBILE NAV =====
    function mobileNav(page, el) {
      document.querySelectorAll('.mobile-nav-item').forEach(b => b.classList.remove('active'));
      if (el) el.classList.add('active');
      setPage(page, null);
      toggleFabMenu();
    }

    // ===== PAGE TRANSITION SYSTEM =====
    function setPage(page, el) {
      document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
        item.removeAttribute('aria-current');
      });
      if (el) {
        el.classList.add('active');
        el.setAttribute('aria-current', 'page');
      }
      if (typeof updateBreadcrumb === 'function') updateBreadcrumb(page);
      renderPageWithTransition(page);
    }

    function renderPageWithTransition(page) {
      currentPage = page;
      if (typeof updateBreadcrumb === 'function') updateBreadcrumb(page);
      const content = document.getElementById('pageContent');
      
      if (content.children.length > 0 && !content.classList.contains('page-entering')) {
        content.classList.add('page-exiting');
        setTimeout(() => {
          content.classList.remove('page-exiting');
          renderPageContent(page, content);
        }, 180);
      } else {
        renderPageContent(page, content);
      }
    }

    function renderPageContent(page, container) {
      container.innerHTML = buildSkeleton(page);
      container.classList.add('page-entering');
      
      document.querySelectorAll('.nav-item').forEach(item => {
        if (item.textContent.toLowerCase().includes(page)) item.classList.add('active');
      });

      setTimeout(() => {
        container.classList.remove('page-entering');
        
        switch(page) {
          case 'dashboard':  renderDashboardPage(container); break;
          case 'daily':      renderDailyPage(container); break;
          case 'orders':     renderOrdersPage(container); break;
          case 'regions':    renderRegionsPage(container); break;
          case 'reports':    renderReportsPage(container); break;
          case 'leaderboard':renderLeaderboardPage(container); break;
          case 'cycles':       renderCyclesPage(container); break;
          case 'technicians':  renderTechniciansPage(container); break;
          case 'automation':   renderAutomationPage(container); break;
        }
        
        container.classList.add('page-entering');
      }, 300);
    }

    function buildSkeleton(page) {
      if (page === 'dashboard') {
        return `<div>
          <div class="skeleton skeleton-hero"></div>
          <div class="skeleton-kpi-grid">${Array(6).fill('<div class="skeleton skeleton-card"></div>').join('')}</div>
          <div class="grid grid-cols-2 gap-4 mb-4">
            <div class="skeleton skeleton-card tall"></div>
            <div class="skeleton skeleton-card tall"></div>
          </div>
          <div class="skeleton skeleton-card tall" style="height:220px;"></div>
        </div>`;
      }
      if (page === 'orders') {
        return `<div>
          <div class="skeleton-kpi-grid grid-cols-5">${Array(5).fill('<div class="skeleton skeleton-card" style="height:90px;"></div>').join('')}</div>
          <div class="skeleton skeleton-card short mb-4"></div>
          ${Array(5).fill('<div class="skeleton skeleton-card short mb-2"></div>').join('')}
        </div>`;
      }
      if (page === 'daily') {
        return `<div>
          <div class="skeleton-kpi-grid grid-cols-3">${Array(3).fill('<div class="skeleton skeleton-card" style="height:110px;"></div>').join('')}</div>
          <div class="skeleton skeleton-card short mb-4"></div>
          ${Array(6).fill('<div class="skeleton skeleton-card short mb-2"></div>').join('')}
        </div>`;
      }
      if (page === 'leaderboard') {
        return `<div>
          <div class="skeleton-kpi-grid grid-cols-3">${Array(3).fill('<div class="skeleton skeleton-card" style="height:110px;"></div>').join('')}</div>
          ${Array(5).fill('<div class="skeleton skeleton-card short mb-2"></div>').join('')}
        </div>`;
      }
      if (page === 'technicians') {
        return `<div>
          <div class="skeleton skeleton-card" style="height:48px;margin-bottom:1.5rem;border-radius:var(--radius-xl);"></div>
          <div class="skeleton-kpi-grid grid-cols-4 mb-4">${Array(4).fill('<div class="skeleton skeleton-card" style="height:88px;"></div>').join('')}</div>
          <div class="skeleton skeleton-card short mb-4"></div>
          ${Array(8).fill('<div class="skeleton skeleton-card" style="height:44px;margin-bottom:0.5rem;border-radius:var(--radius-md);"></div>').join('')}
        </div>`;
      }
      if (page === 'automation') {
        return `<div>
          <div class="skeleton skeleton-card" style="height:48px;margin-bottom:1.5rem;border-radius:var(--radius-xl);"></div>
          <div class="grid grid-cols-2 gap-4 mb-4">
            <div class="skeleton skeleton-card tall" style="height:280px;"></div>
            <div class="skeleton skeleton-card tall" style="height:280px;"></div>
          </div>
        </div>`;
      }
      return `<div class="skeleton skeleton-card tall"></div>`;
    }

    // ===== SVG EMPTY STATE ILLUSTRATIONS =====
    function renderEmptyState(type, actionText, action) {
      const illustrations = {
        orders: {
          svg: '<svg class="empty-illustration" viewBox="0 0 120 120" fill="none"><rect x="20" y="15" width="80" height="90" rx="8" fill="var(--neutral-200)"/><rect x="32" y="35" width="56" height="6" rx="3" fill="var(--neutral-300)"/><rect x="32" y="50" width="40" height="6" rx="3" fill="var(--neutral-300)"/><rect x="32" y="65" width="48" height="6" rx="3" fill="var(--neutral-300)"/><circle cx="85" cy="80" r="18" fill="var(--accent-100)"/><path d="M78 80h14M85 73v14" stroke="var(--accent-600)" stroke-width="2.5"/></svg>',
          title: 'No orders yet',
          description: 'Create your first order to start tracking fuel allocation'
        },
        daily: {
          svg: '<svg class="empty-illustration" viewBox="0 0 120 120" fill="none"><rect x="15" y="25" width="90" height="80" rx="8" fill="var(--neutral-200)"/><rect x="15" y="35" width="90" height="12" fill="var(--accent-100)"/><circle cx="38" cy="18" r="7" fill="var(--neutral-300)"/><circle cx="82" cy="18" r="7" fill="var(--neutral-300)"/><rect x="27" y="57" width="16" height="14" rx="3" fill="var(--neutral-300)"/><rect x="52" y="57" width="16" height="14" rx="3" fill="var(--accent-200)"/><rect x="77" y="57" width="16" height="14" rx="3" fill="var(--neutral-300)"/></svg>',
          title: 'No entries for this date',
          description: 'Add entries above to start tracking fuel supply'
        },
        leaderboard: {
          svg: '<svg class="empty-illustration" viewBox="0 0 120 120" fill="none"><rect x="20" y="55" width="22" height="50" rx="4" fill="var(--neutral-300)"/><rect x="49" y="30" width="22" height="75" rx="4" fill="var(--accent-200)"/><rect x="78" y="70" width="22" height="35" rx="4" fill="var(--neutral-300)"/><path d="M58 20l2.5 5 5.5.8-4 3.9.9 5.5L58 33l-4.9 2.6.9-5.5-4-3.9 5.5-.8z" fill="#FFD700"/></svg>',
          title: 'No data available',
          description: 'Start adding allocated supply entries to see the leaderboard'
        },
        tech: {
          svg: '<svg class="empty-illustration" viewBox="0 0 120 120" fill="none"><circle cx="60" cy="42" r="22" fill="var(--neutral-200)"/><path d="M20 95c0-22 18-36 40-36s40 14 40 36" stroke="var(--neutral-300)" stroke-width="8" stroke-linecap="round" fill="none"/></svg>',
          title: 'No technicians',
          description: 'Add technicians to this region to get started'
        }
      };
      
      const ill = illustrations[type] || illustrations.daily;
      
      return `
        <div class="empty-state enhanced">
          <div class="empty-illustration">${ill.svg}</div>
          <h3 class="text-lg font-semibold mt-4">${ill.title}</h3>
          <p class="text-sm text-neutral-500 mt-2 mb-4">${ill.description}</p>
          <button class="btn btn-primary" onclick="${action}">
            <i class="fa-regular fa-plus"></i> ${actionText}
          </button>
        </div>
      `;
    }

    // ===== MONTHLY TARGET MODAL =====
    function openTargetModal() {
      const region = DB.regions[DB.currentRegion];
      document.getElementById('targetInput').value = region.monthlyTarget || '';
      const lbl = document.getElementById('targetRegionLabel');
      if (lbl) lbl.textContent = DB.currentRegion;
      openModal('targetModal');
    }
    
    function saveMonthlyTarget() {
      const val = parseFloat(document.getElementById('targetInput').value);
      if (!val || val <= 0) return showToast('Please enter a valid target', 'warning');
      DB.regions[DB.currentRegion].monthlyTarget = val;
      save();
      closeModal('targetModal');
      renderPageWithTransition('dashboard');
      showToast('Monthly target set to ' + val + 'L');
    }

    // ===== TECHNICIAN MONTHLY TARGETS =====
    function openTechTargetModal() {
      const region = DB.regions[DB.currentRegion];
      if (!region.techMonthlyTargets) region.techMonthlyTargets = {};
      let rows = '';
      region.technicians.forEach(t => {
        const cur = region.techMonthlyTargets[t] || '';
        rows += `<div class="target-tech-row flex items-center gap-3 py-3 border-b border-neutral-100">
          ${techAvatarHtml(t)}
          <div style="flex:1;"><div class="font-semibold">${t}</div></div>
          <div class="flex items-center gap-2">
            <input type="number" class="input-field" style="width:110px;padding:8px 10px;" id="techTarget_${t.replace(/\s/g,'_')}" value="${cur}" placeholder="Litres/month">
          </div>
        </div>`;
      });
      document.getElementById('techTargetBody').innerHTML = rows || '<p class="text-neutral-500 p-4 text-center">No technicians found. Add technicians in Regions first.</p>';
      openModal('techTargetModal');
    }
    
    function saveTechTargets() {
      const region = DB.regions[DB.currentRegion];
      if (!region.techMonthlyTargets) region.techMonthlyTargets = {};
      region.technicians.forEach(t => {
        const el = document.getElementById('techTarget_' + t.replace(/\s/g,'_'));
        if (el) {
          const val = parseFloat(el.value);
          if (val > 0) region.techMonthlyTargets[t] = val;
          else delete region.techMonthlyTargets[t];
        }
      });
      save();
      closeModal('techTargetModal');
      showToast('Technician targets saved');
      if (currentPage === 'leaderboard') renderPageWithTransition('leaderboard');
    }

    // ===== UNASSIGN ORDER FUNCTIONS =====
    function unassignFuel(orderNo, tech) {
      const region = DB.regions[DB.currentRegion];
      const order = region.orders[orderNo];
      
      if (!order || !order.allocations || !order.allocations[tech]) {
        return showToast('Allocation not found', 'error');
      }

      if (!confirm(`Remove ${tech} from order ${orderNo}? This will free up ${order.allocations[tech]}L.`)) return;

      const supplied = Object.values(region.dailyLog).flat()
        .filter(e => e.orderNo === orderNo && e.technician === tech && !e.unallocated)
        .reduce((s, e) => s + e.supplied, 0);

      if (supplied > 0) {
        Object.values(region.dailyLog).forEach(entries => {
          entries.forEach(e => {
            if (e.orderNo === orderNo && e.technician === tech && !e.unallocated) {
              e.unallocated = true;
              e.comment = `Converted from allocated to unallocated (was part of ${order.allocations[tech]}L allocation)`;
              e.orderNo = undefined;
            }
          });
        });
        
        order.suppliedTotal = Math.max(0, order.suppliedTotal - supplied);
      }

      const allocAmount = order.allocations[tech];
      delete order.allocations[tech];

      if (Object.keys(order.allocations || {}).length === 0) {
        if (!region.unassignedComments) region.unassignedComments = {};
        region.unassignedComments[orderNo] = `Previously assigned to ${tech} (${allocAmount}L) - now unassigned`;
      }

      if (order.overageComments && order.overageComments[tech]) {
        delete order.overageComments[tech];
      }

      save();
      renderOrdersList();
      showToast(`Unassigned ${tech} from order ${orderNo}`, 'info');
    }

    // ===== REASSIGN FUEL TO ANOTHER TECHNICIAN =====
    function reassignFuel(orderNo, fromTech, toTech) {
      if (!toTech) return;
      
      const region = DB.regions[DB.currentRegion];
      const order = region.orders[orderNo];
      
      if (!order || !order.allocations || !order.allocations[fromTech]) {
        return showToast('Source allocation not found', 'error');
      }

      if (!region.technicians.includes(toTech)) {
        return showToast('Target technician not found', 'error');
      }

      if (order.allocations[toTech]) {
        return showToast('Target technician already has allocation for this order', 'warning');
      }

      if (fromTech === toTech) return;

      const allocAmount = order.allocations[fromTech];
      
      order.allocations[toTech] = allocAmount;
      delete order.allocations[fromTech];

      const suppliedEntries = [];
      Object.entries(region.dailyLog).forEach(([date, entries]) => {
        entries.forEach((e, idx) => {
          if (e.orderNo === orderNo && e.technician === fromTech && !e.unallocated) {
            suppliedEntries.push({ date, idx, entry: e });
          }
        });
      });

      if (suppliedEntries.length > 0) {
        if (confirm(`${suppliedEntries.length} supply entries found for ${fromTech}. Reassign them to ${toTech}?`)) {
          suppliedEntries.forEach(({ date, idx, entry }) => {
            entry.technician = toTech;
          });
        }
      }

      if (order.overageComments && order.overageComments[fromTech]) {
        order.overageComments[toTech] = order.overageComments[fromTech];
        delete order.overageComments[fromTech];
      }

      save();
      renderOrdersList();
      showToast(`Reassigned ${allocAmount}L from ${fromTech} to ${toTech}`, 'success');
    }

    // ===== EDIT ORDER DETAILS =====
    function editOrder(orderNo) {
      currentEditingOrder = orderNo;
      const region = DB.regions[DB.currentRegion];
      const order = region.orders[orderNo];
      
      if (!order) return;

      document.getElementById('editOrderModalTitle').textContent = `Edit Order: ${orderNo}`;
      
      const modalContent = `
        <div class="mb-4">
          <label class="block text-sm font-medium mb-2">Order Number</label>
          <input type="text" class="input-field" id="editOrderNo" value="${order.orderNo}" placeholder="Order Number">
        </div>
        <div class="mb-4">
          <label class="block text-sm font-medium mb-2">Vehicle Plate</label>
          <input type="text" class="input-field" id="editVehiclePlate" value="${order.vehiclePlate || ''}" placeholder="Vehicle Plate">
        </div>
        <div class="mb-4">
          <label class="block text-sm font-medium mb-2">Total Litres</label>
          <input type="number" class="input-field" id="editTotalLiters" value="${order.totalLiters}" placeholder="Total Litres" min="0" step="0.1">
        </div>
        <div class="mb-4">
          <label class="block text-sm font-medium mb-2">Order Date</label>
          <input type="date" class="input-field" id="editOrderDate" value="${order.createdDate || new Date().toISOString().slice(0, 10)}">
        </div>
        <div class="mb-4">
          <label class="block text-sm font-medium mb-2">Status</label>
          <div class="select-wrapper">
            <select class="select-field" id="editOrderStatus">
              <option value="OPEN" ${order.status === 'OPEN' ? 'selected' : ''}>OPEN</option>
              <option value="CLOSED" ${order.status === 'CLOSED' ? 'selected' : ''}>CLOSED</option>
            </select>
          </div>
        </div>
      `;

      document.getElementById('editOrderModalBody').innerHTML = modalContent;
      openModal('editOrderModal');
    }

    function saveOrderEdits() {
      if (!currentEditingOrder) return;
      
      const region = DB.regions[DB.currentRegion];
      const originalOrder = region.orders[currentEditingOrder];
      
      const newOrderNo = document.getElementById('editOrderNo').value.trim();
      const vehiclePlate = document.getElementById('editVehiclePlate').value.trim();
      const totalLiters = parseFloat(document.getElementById('editTotalLiters').value);
      const orderDate = document.getElementById('editOrderDate').value;
      const status = document.getElementById('editOrderStatus').value;

      if (!newOrderNo || !vehiclePlate || !totalLiters || totalLiters <= 0) {
        return showToast('Please fill all required fields with valid values', 'warning');
      }

      if (newOrderNo !== currentEditingOrder && region.orders[newOrderNo]) {
        return showToast('Order number already exists', 'error');
      }

      const newSuppliedTotal = Math.min(originalOrder.suppliedTotal, totalLiters);
      const suppliedReduction = originalOrder.suppliedTotal - newSuppliedTotal;

      if (suppliedReduction > 0) {
        if (!confirm(`Reducing total liters will reduce supplied total by ${suppliedReduction}L. Continue?`)) {
          return;
        }
      }

      if (newOrderNo !== currentEditingOrder) {
        region.orders[newOrderNo] = {
          ...originalOrder,
          orderNo: newOrderNo,
          vehiclePlate,
          totalLiters,
          suppliedTotal: newSuppliedTotal,
          status,
          createdDate: orderDate
        };

        Object.values(region.dailyLog).forEach(entries => {
          entries.forEach(e => {
            if (e.orderNo === currentEditingOrder) {
              e.orderNo = newOrderNo;
            }
          });
        });

        if (region.unassignedComments && region.unassignedComments[currentEditingOrder]) {
          region.unassignedComments[newOrderNo] = region.unassignedComments[currentEditingOrder];
          delete region.unassignedComments[currentEditingOrder];
        }

        delete region.orders[currentEditingOrder];
      } else {
        originalOrder.vehiclePlate = vehiclePlate;
        originalOrder.totalLiters = totalLiters;
        originalOrder.suppliedTotal = newSuppliedTotal;
        originalOrder.status = status;
        originalOrder.createdDate = orderDate;
      }

      const order = region.orders[newOrderNo];
      const totalAllocated = Object.values(order.allocations || {}).reduce((s, v) => s + v, 0);
      
      if (totalAllocated > totalLiters) {
        const excess = totalAllocated - totalLiters;
        if (!confirm(`Total allocations (${totalAllocated}L) exceed new order total (${totalLiters}L) by ${excess}L. Reduce allocations proportionally?`)) {
          return;
        }
        
        const allocEntries = Object.entries(order.allocations || {});
        const reductionFactor = totalLiters / totalAllocated;
        
        allocEntries.forEach(([tech, alloc]) => {
          order.allocations[tech] = Math.floor(alloc * reductionFactor * 100) / 100;
        });
      }

      save();
      closeModal('editOrderModal');
      currentEditingOrder = null;
      renderOrdersList();
      showToast('Order updated successfully');
    }
        // ===== UNASSIGNED ORDER COMMENT FUNCTIONS =====
    function openUnassignedCommentModal(orderNo, regionName) {
      const rName = regionName || DB.currentRegion;
      const region = DB.regions[rName];
      const order = region.orders[orderNo];
      if (!order) return;
      
      unassignedContext = { orderNo, region: rName };
      
      document.getElementById('unassignedOrderPreview').innerHTML = `
        <div class="text-sm">
          <strong>Order:</strong> ${order.orderNo}<br>
          <strong>Vehicle:</strong> ${order.vehiclePlate}<br>
          <strong>Total:</strong> ${order.totalLiters}L<br>
          <strong>Status:</strong> <span class="badge badge-neutral">Unassigned</span>
        </div>
      `;
      
      document.getElementById('unassignedComment').value = region.unassignedComments?.[orderNo] || '';
      openModal('unassignedCommentModal');
    }
    
    function saveUnassignedComment() {
      if (!unassignedContext) return;
      
      const { orderNo, region } = unassignedContext;
      const comment = document.getElementById('unassignedComment').value.trim();
      
      const r = DB.regions[region];
      if (!r) return;
      
      if (!r.unassignedComments) r.unassignedComments = {};
      r.unassignedComments[orderNo] = comment;
      
      save();
      closeModal('unassignedCommentModal');
      renderOrdersList();
      showToast('Comment saved for unassigned order');
    }
    
    function deleteUnassignedComment(orderNo, regionName) {
      const rName = regionName || DB.currentRegion;
      const region = DB.regions[rName];
      if (!region) return;
      
      if (!confirm('Delete comment for this unassigned order?')) return;
      
      if (region.unassignedComments && region.unassignedComments[orderNo]) {
        delete region.unassignedComments[orderNo];
        save();
        renderOrdersList();
        showToast('Comment deleted');
      }
    }

    // ===== INLINE EDIT FOR DAILY LOG =====
    function startInlineEdit(el, date, idx) {
      const region = DB.regions[DB.currentRegion];
      const entry = region.dailyLog[date] ? region.dailyLog[date][idx] : null;
      if (!entry) return;
      const cur = entry.supplied;
      const input = document.createElement('input');
      input.type = 'number';
      input.className = 'inline-edit-input';
      input.value = cur;
      input.min = '0';
      el.replaceWith(input);
      input.focus();
      input.select();
      
      function commit() {
        const newVal = parseFloat(input.value);
        if (!isNaN(newVal) && newVal > 0 && newVal !== cur) {
          const diff = newVal - entry.supplied;
          if (!entry.unallocated && entry.orderNo && region.orders[entry.orderNo]) {
            region.orders[entry.orderNo].suppliedTotal += diff;
          }
          entry.supplied = newVal;
          save();
          showToast('Entry updated', 'success', 1500);
          loadDailyLog();
        } else {
          loadDailyLog();
        }
      }
      
      input.addEventListener('blur', commit);
      input.addEventListener('keydown', e => { 
        if(e.key === 'Enter') commit(); 
        if(e.key === 'Escape') loadDailyLog(); 
      });
    }

    // ===== EDIT ENTRY MODAL (editModal) =====
    // State for the edit modal
    let _editCtx = null; // { date, idx }

    function openEditModal(date, idx) {
      const region = DB.regions[DB.currentRegion];
      const entry = region.dailyLog[date]?.[idx];
      if (!entry) return showToast('Entry not found', 'error');
      _editCtx = { date, idx };
      const sup = document.getElementById('editSupplied');
      const cmt = document.getElementById('editComment');
      const cmtGroup = document.getElementById('editCommentGroup');
      if (sup) sup.value = entry.supplied;
      if (cmt) cmt.value = entry.comment || '';
      if (cmtGroup) cmtGroup.style.display = 'block';
      openModal('editModal');
    }

    function saveEditEntry() {
      if (!_editCtx) return closeModal('editModal');
      const { date, idx } = _editCtx;
      const region = DB.regions[DB.currentRegion];
      const entry = region.dailyLog[date]?.[idx];
      if (!entry) { closeModal('editModal'); return showToast('Entry not found', 'error'); }

      const sup = document.getElementById('editSupplied');
      const cmt = document.getElementById('editComment');
      const parsed = parseFloat(sup?.value);
      if (isNaN(parsed) || parsed < 0) return showToast('Invalid value', 'error');

      if (!entry.unallocated && entry.orderNo) {
        const order = region.orders[entry.orderNo];
        if (order) {
          order.suppliedTotal = order.suppliedTotal - entry.supplied + parsed;
          order.status = order.suppliedTotal >= order.totalLiters ? 'CLOSED' : 'OPEN';
        }
      }
      entry.supplied = parsed;
      if (cmt) entry.comment = cmt.value.trim() || undefined;
      _editCtx = null;
      save();
      closeModal('editModal');
      showToast('Entry updated', 'success');
      if (currentPage === 'daily') loadDailyLog();
      if (typeof renderDailyHistory === 'function') renderDailyHistory();
    }
    let tableSortState = {
      dailyLog: { field: 'default', direction: 'asc' },
      orders: { field: 'default', direction: 'asc' },
      history: { field: 'default', direction: 'asc' }
    };

    function sortTable(tableId, data, field, direction, renderFunction) {
      const sorted = [...data].sort((a, b) => {
        let va = a[field];
        let vb = b[field];
        
        if (typeof va === 'string') va = va.toLowerCase();
        if (typeof vb === 'string') vb = vb.toLowerCase();
        
        if (va < vb) return direction === 'asc' ? -1 : 1;
        if (va > vb) return direction === 'asc' ? 1 : -1;
        return 0;
      });
      
      tableSortState[tableId] = { field, direction };
      renderFunction(sorted);
    }

    // ===== DAILY PAGE =====
    function renderDailyPage(container) {
      const today = new Date().toISOString().slice(0, 10);
      
      container.innerHTML = `
        <div class="stats-grid">
          <div class="stat-tile">
            <div class="stat-label">
              <i class="fa-regular fa-calendar"></i> Date
            </div>
            <input type="date" class="input-field mt-2" id="dailyDate" value="${today}">
          </div>
          <div class="stat-tile">
            <div class="stat-label">
              <i class="fa-regular fa-chart-line"></i> Today's Stats
            </div>
            <div class="flex justify-between items-center">
              <span class="text-sm">Ordered (Assigned):</span>
              <span class="stat-value text-2xl" id="dailyOrdered">L</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-sm">Supplied (All):</span>
              <span class="stat-value text-2xl text-success-700" id="dailySupplied">0L</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-sm">Balance (Assigned):</span>
              <span class="stat-value text-2xl text-danger-700" id="dailyBalance">0L</span>
            </div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">
              <i class="fa-regular fa-clock"></i> Quick Actions
            </div>
            <div class="flex gap-2">
              <button class="btn btn-primary btn-sm" onclick="loadDailyLog()">
                <i class="fa-regular fa-rotate-right"></i> Load
              </button>
              <button class="btn btn-secondary btn-sm" onclick="openSummaryModal()">
                <i class="fa-regular fa-chart-pie"></i> Summary
              </button>
              <button class="btn btn-info btn-sm" onclick="openMultiDateModal()">
                <i class="fa-regular fa-calendar-plus"></i> Multi-Date
              </button>
            </div>
          </div>
        </div>

        <div class="card mb-4">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold">Daily Entries</h3>
            <div class="flex gap-2">
              <button class="btn btn-secondary btn-sm" onclick="addDailyEntry()">
                <i class="fa-regular fa-plus"></i> Add Entry
              </button>
              <button class="btn btn-primary btn-sm" onclick="saveDaily()">
                <i class="fa-regular fa-floppy-disk"></i> Save
              </button>
            </div>
          </div>
          <div id="dailyEntriesContainer"></div>
        </div>

        <div class="card">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold">Supply Log</h3>
            <div class="flex items-center gap-2">
              <span class="badge badge-info" id="entryCount">0 entries</span>
              <span id="dailyDensityToggle"></span>
              <span id="dailyColChooser"></span>
            </div>
          </div>
          <div id="dailyLogContainer"></div>
        </div>

        <div class="card mt-4">
          <h3 class="text-lg font-semibold mb-4">History</h3>
          <div id="dailyHistoryContainer"></div>
        </div>
      `;

      loadDailyLog();
      renderDailyHistory();
      const dtEl = document.getElementById('dailyDensityToggle');
      if (dtEl) dtEl.innerHTML = renderDensityToggle();
      const dcEl = document.getElementById('dailyColChooser');
      if (dcEl) dcEl.innerHTML = renderColChooser('daily');
      setTimeout(() => { applyColVisibility('daily'); updateColChooserBtn('daily'); }, 50);
    }

    function loadDailyLog() {
      const date = document.getElementById('dailyDate').value;
      if (!date) return showToast('Please select a date', 'warning');
      
      const region = DB.regions[DB.currentRegion];
      const entries = region.dailyLog[date] || [];
      
      const assignedOrders = Object.values(region.orders).filter(o => Object.keys(o.allocations || {}).length > 0);
      const totalOrderedAssigned = assignedOrders.reduce((s, o) => s + o.totalLiters, 0);
      const totalSuppliedAssigned = assignedOrders.reduce((s, o) => s + o.suppliedTotal, 0);
      
      const dailySupplied = entries.reduce((s, e) => s + e.supplied, 0);
      
      animateCounter(document.getElementById('dailyOrdered'), totalOrderedAssigned, 'L');
      animateCounter(document.getElementById('dailySupplied'), dailySupplied, 'L');
      animateCounter(document.getElementById('dailyBalance'), totalOrderedAssigned - totalSuppliedAssigned, 'L');
      
      document.getElementById('entryCount').textContent = entries.length + ' entries';
      
      renderDailyLog(entries, date);
    }

    function renderDailyLog(entries, dateVal) {
      const container = document.getElementById('dailyLogContainer');
      if (!container) return;
      
      if (!entries.length) {
        container.innerHTML = renderEmptyState('daily', 'Add Entry', 'addDailyEntry()');
        return;
      }

      let sorted = [...entries.map((e, i) => ({...e, _origIdx: i}))];
      const sortState = tableSortState.dailyLog;
      
      if (sortState.field !== 'default') {
        sorted.sort((a, b) => {
          let va = a[sortState.field];
          let vb = b[sortState.field];
          if (typeof va === 'string') va = va.toLowerCase();
          if (typeof vb === 'string') vb = vb.toLowerCase();
          if (va < vb) return sortState.direction === 'asc' ? -1 : 1;
          if (va > vb) return sortState.direction === 'asc' ? 1 : -1;
          return 0;
        });
      }

      const mkSortBtn = (field, label) => {
        const active = sortState.field === field;
        const icon = active ? (sortState.direction === 'asc' ? '↑' : '↓') : '↕';
        return `<button onclick="sortDailyLog('${field}')" style="
          background:${active ? 'var(--accent-50)' : 'var(--neutral-100)'};
          border:1px solid ${active ? 'var(--accent-300)' : 'var(--neutral-200)'};
          color:${active ? 'var(--accent-700)' : 'var(--neutral-600)'};
          border-radius:var(--radius-full);padding:4px 12px;font-size:0.72rem;
          font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:4px;
          letter-spacing:0.02em;transition:all 150ms;">
          ${label} <span>${icon}</span>
        </button>`;
      };

      // Totals summary bar
      const totalSupplied = sorted.reduce((s, e) => s + e.supplied, 0);
      const allocCount = sorted.filter(e => !e.unallocated).length;
      const unallocCount = sorted.filter(e => e.unallocated).length;

      let rowsHtml = '';
      sorted.forEach((entry, idx) => {
        const origIdx = entry._origIdx;
        const isUnalloc = entry.unallocated;
        const c = techColor(entry.technician);
        const colorMap = ['#3D8662','#4F86B0','#C23B4C','#D47A3E','#6b3a9b','#3a809b','#9b3a7a','#5a9b3a'];
        const accentColor = colorMap[c];
        
        rowsHtml += `
          <div class="supply-log-row" draggable="true" data-idx="${origIdx}" data-date="${dateVal}"
               ondragstart="dragStart(event, ${origIdx})" ondragover="dragOver(event)" 
               ondrop="dragDrop(event)" ondragleave="dragLeave(event)"
               style="display:flex;align-items:center;gap:12px;padding:10px 14px;
                      background:white;border-radius:var(--radius-lg);
                      border:1px solid var(--neutral-200);margin-bottom:6px;
                      border-left:3px solid ${accentColor};
                      transition:all 150ms;cursor:grab;position:relative;overflow:hidden;">
            <span class="drag-handle" style="color:var(--neutral-300);font-size:0.85rem;flex-shrink:0;">
              <i class="fa-regular fa-grip-dots-vertical"></i>
            </span>
            ${techAvatarHtml(entry.technician, `style="width:34px;height:34px;font-size:0.8rem;flex-shrink:0;"`)}
            <div style="flex:1;min-width:0;">
              <div data-col="daily-technician" style="font-weight:700;font-size:0.85rem;color:var(--neutral-900);display:flex;align-items:center;gap:6px;">
                ${entry.technician}
                ${entry.autoImported ? `<span style="font-size:0.65rem;font-weight:700;padding:1px 6px;border-radius:var(--radius-full);background:var(--status-info-bg);color:var(--status-info);border:1px solid var(--status-info);letter-spacing:0.04em;">🤖 AUTO</span>` : ''}
              </div>
              <div style="font-size:0.72rem;color:var(--neutral-500);margin-top:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
                <span data-col="daily-order">${isUnalloc
                  ? `<span style="color:var(--status-warning);font-weight:600;">⚠ Unallocated</span>`
                  : `<i class="fa-regular fa-file-lines" style="margin-right:3px;"></i>${entry.orderNo}`
                }</span>
                <span data-col="daily-comment">${entry.comment ? ' · 💬 ' + entry.comment : ''}</span>
                <span data-col="daily-site">${entry.siteId ? `<span style="margin-left:4px;padding:0 4px;background:var(--neutral-100);border-radius:2px;font-family:var(--font-mono);font-size:0.65rem;">${entry.siteId}</span>` : ''}</span>
                ${entry.dgHoursUsed > 0 ? `<span style="margin-left:4px;color:var(--status-info);">⚡ ${entry.dgHoursUsed}h</span>` : ''}
                ${entry.dieselConsumed > 0 ? `<span style="margin-left:4px;color:var(--status-warning);">🔥 ${entry.dieselConsumed}L used</span>` : ''}
              </div>
            </div>
            <span data-col="daily-type" class="badge ${isUnalloc ? 'badge-warning' : 'badge-success'}" style="font-size:0.65rem;flex-shrink:0;">${isUnalloc ? 'Unalloc' : 'Alloc'}</span>
            <span data-col="daily-supplied" class="inline-editable" title="Click to edit"
              onclick="startInlineEdit(this,'${dateVal}',${origIdx})"
              style="font-family:var(--font-mono);font-weight:700;font-size:0.9rem;
                     padding:4px 10px;border-radius:var(--radius-full);cursor:pointer;
                     background:${isUnalloc ? 'var(--status-warning-bg)' : 'var(--status-success-bg)'};
                     color:${isUnalloc ? 'var(--status-warning)' : 'var(--status-success)'};
                     border:1px solid ${isUnalloc ? 'rgba(217,119,6,0.2)' : 'rgba(22,163,74,0.2)'};
                     white-space:nowrap;flex-shrink:0;">${entry.supplied}L</span>
            <button class="btn btn-icon btn-ghost btn-sm" onclick="deleteDailyEntry('${dateVal}',${origIdx})"
              style="width:30px;height:30px;flex-shrink:0;color:var(--neutral-400);">
              <i class="fa-regular fa-trash"></i>
            </button>
          </div>
        `;
      });

      container.innerHTML = `
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;flex-wrap:wrap;gap:8px;">
          <div style="display:flex;gap:6px;align-items:center;">
            <span style="font-size:0.72rem;font-weight:600;color:var(--neutral-500);text-transform:uppercase;letter-spacing:0.04em;">Sort:</span>
            ${mkSortBtn('technician','Technician')}
            ${mkSortBtn('supplied','Litres')}
          </div>
          <div style="display:flex;gap:8px;align-items:center;">
            ${allocCount > 0 ? `<span style="font-size:0.72rem;font-weight:600;padding:3px 10px;border-radius:var(--radius-full);background:var(--status-success-bg);color:var(--status-success);">✓ ${allocCount} allocated</span>` : ''}
            ${unallocCount > 0 ? `<span style="font-size:0.72rem;font-weight:600;padding:3px 10px;border-radius:var(--radius-full);background:var(--status-warning-bg);color:var(--status-warning);">⚠ ${unallocCount} unallocated</span>` : ''}
            <span style="font-family:var(--font-mono);font-weight:700;font-size:0.85rem;padding:3px 12px;border-radius:var(--radius-full);background:var(--accent-50);color:var(--accent-700);border:1px solid var(--accent-200);">${totalSupplied}L total</span>
          </div>
        </div>
        <div id="supplyLogRows">${rowsHtml}</div>`;
      applyColVisibility('daily');
    }

    function sortDailyLog(field) {
      const sortState = tableSortState.dailyLog;
      if (sortState.field === field) {
        sortState.direction = sortState.direction === 'asc' ? 'desc' : 'asc';
      } else {
        sortState.field = field;
        sortState.direction = 'asc';
      }
      loadDailyLog();
    }

    // ===== DRAG AND DROP FOR DAILY LOG =====
    let dragSrcIdx = null;
    
    function dragStart(e, idx) {
      dragSrcIdx = idx;
      e.dataTransfer.effectAllowed = 'move';
      e.target.classList.add('dragging');
    }
    
    function dragOver(e) {
      e.preventDefault();
      e.dataTransfer.dropEffect = 'move';
      const row = e.target.closest('[data-idx]');
      if (row) row.classList.add('drag-over');
    }
    
    function dragLeave(e) {
      const row = e.target.closest('[data-idx]');
      if (row) row.classList.remove('drag-over');
    }
    
    function dragDrop(e) {
      e.preventDefault();
      const row = e.target.closest('[data-idx]');
      if (row) row.classList.remove('drag-over');
      
      const destIdx = parseInt(row?.dataset.idx);
      const dateVal = row?.dataset.date;
      
      if (dragSrcIdx === null || isNaN(destIdx) || dragSrcIdx === destIdx || !dateVal) return;
      
      const region = DB.regions[DB.currentRegion];
      const log = region.dailyLog[dateVal];
      if (!log) return;
      
      const [moved] = log.splice(dragSrcIdx, 1);
      log.splice(destIdx, 0, moved);
      dragSrcIdx = null;
      
      save();
      loadDailyLog();
      showToast('Entry reordered', 'info', 1500);
    }

    function addDailyEntry() {
      const container = document.getElementById('dailyEntriesContainer');
      const id = 'entry_' + Date.now();
      _markUnsaved();
      
      const region = DB.regions[DB.currentRegion];
      let techOptions = '<option value="">Select technician</option>';
      region.technicians.forEach(t => {
        techOptions += `<option value="${t}">${t}</option>`;
      });
      
      const card = document.createElement('div');
      card.className = 'card';
      card.id = id;
      card.innerHTML = `
        <div class="flex justify-end mb-2">
          <button class="btn btn-icon btn-ghost btn-sm" onclick="this.closest('.card').remove()">
            <i class="fa-regular fa-xmark"></i>
          </button>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div class="select-wrapper">
            <select class="select-field" onchange="techSelected(this, '${id}')">
              ${techOptions}
            </select>
          </div>
          <div class="input-group">
            <input type="number" class="input-field" id="supplied_${id}" placeholder=" ">
            <label class="input-label">Litres</label>
          </div>
        </div>
        <div class="grid grid-cols-4 gap-2 mt-2" id="details_${id}">
          <div class="text-sm">Order: <span id="orderNo_${id}">—</span></div>
          <div class="text-sm">Vehicle: <span id="vehicle_${id}">—</span></div>
          <div class="text-sm">Allocated: <span id="allocated_${id}">—</span></div>
          <div class="text-sm">Remaining: <span id="remaining_${id}">—</span></div>
        </div>
        <div id="orderPickerSection_${id}"></div>
        <div id="commentSection_${id}" style="display: none; margin-top: var(--space-2);">
          <div class="input-group">
            <input type="text" class="input-field" id="comment_${id}" placeholder=" ">
            <label class="input-label">Comment (required for unallocated)</label>
          </div>
        </div>
      `;
      
      container.appendChild(card);
    }

    function renderOrderPicker(cardId, tech, selectedOrderNo) {
      const region = DB.regions[DB.currentRegion];
      const section = document.getElementById(`orderPickerSection_${cardId}`);
      if (!section) return;

      const assignedOrders = Object.values(region.orders).filter(o =>
        o.status === 'OPEN' && o.allocations && o.allocations[tech]
      );

      if (assignedOrders.length === 0) return;

      const existingSearch = section.querySelector('.order-picker-search')?.value || '';
      const existingSort = section.querySelector('.order-picker-sort')?.value || 'date-desc';

      let filtered = assignedOrders.filter(o => {
        const q = existingSearch.toLowerCase();
        return !q ||
          o.orderNo.toLowerCase().includes(q) ||
          (o.vehiclePlate || '').toLowerCase().includes(q) ||
          (o.createdDate || '').includes(q);
      });

      filtered = [...filtered].sort((a, b) => {
        switch (existingSort) {
          case 'date-desc': return (b.createdDate || '').localeCompare(a.createdDate || '');
          case 'date-asc':  return (a.createdDate || '').localeCompare(b.createdDate || '');
          case 'litres-desc': return b.totalLiters - a.totalLiters;
          case 'litres-asc':  return a.totalLiters - b.totalLiters;
          case 'balance-desc': return (b.totalLiters - b.suppliedTotal) - (a.totalLiters - a.suppliedTotal);
          case 'balance-asc':  return (a.totalLiters - a.suppliedTotal) - (b.totalLiters - b.suppliedTotal);
          case 'order-asc':    return a.orderNo.localeCompare(b.orderNo);
          default: return 0;
        }
      });

      let cardsHtml = '';
      filtered.forEach(o => {
        const techSupplied = Object.values(region.dailyLog).flat()
          .filter(e => e.orderNo === o.orderNo && e.technician === tech && !e.unallocated)
          .reduce((s, e) => s + e.supplied, 0);
        const techRemaining = o.allocations[tech] - techSupplied;
        const orderBalance = o.totalLiters - o.suppliedTotal;
        const pct = o.totalLiters > 0 ? Math.min(100, (o.suppliedTotal / o.totalLiters) * 100) : 0;
        const isSelected = o.orderNo === selectedOrderNo;
        const formattedDate = o.createdDate
          ? new Date(o.createdDate).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
          : '—';

        cardsHtml += `
          <div class="order-picker-card ${isSelected ? 'selected' : ''}"
               onclick="selectOrderCard('${cardId}', '${tech}', '${o.orderNo}', this)">
            <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:6px;">
              <div style="display:flex;align-items:center;gap:8px;">
                <span style="font-weight:700;font-size:0.95rem;">${isSelected ? '✓ ' : ''}${o.orderNo}</span>
                <span class="badge badge-neutral">${o.vehiclePlate}</span>
                <span class="badge badge-info">📅 ${formattedDate}</span>
              </div>
              <span class="badge ${orderBalance <= 0 ? 'badge-warning' : 'badge-success'}">
                ${orderBalance <= 0 ? 'Closed' : 'Open'}
              </span>
            </div>
            <div class="grid grid-cols-4 gap-1 mt-2 text-xs">
              <div style="background:var(--info-100);border-radius:6px;padding:4px;text-align:center;">
                <div class="text-neutral-500 text-2xs">Total</div>
                <div class="font-mono font-bold">${o.totalLiters}L</div>
              </div>
              <div style="background:var(--success-100);border-radius:6px;padding:4px;text-align:center;">
                <div class="text-neutral-500 text-2xs">Your Alloc</div>
                <div class="font-mono font-bold">${o.allocations[tech]}L</div>
              </div>
              <div style="background:var(--accent-100);border-radius:6px;padding:4px;text-align:center;">
                <div class="text-neutral-500 text-2xs">You Supplied</div>
                <div class="font-mono font-bold">${techSupplied}L</div>
              </div>
              <div style="background:${techRemaining <= 0 ? 'var(--warning-100)' : 'var(--neutral-100)'};border-radius:6px;padding:4px;text-align:center;">
                <div class="text-neutral-500 text-2xs">Your Balance</div>
                <div class="font-mono font-bold">${Math.max(0, techRemaining)}L</div>
              </div>
            </div>
            <div class="mt-1 h-1 bg-neutral-200 rounded-full overflow-hidden">
              <div style="height:100%;width:${pct}%;background:${pct >= 90 ? 'var(--warning-600)' : pct >= 60 ? 'var(--success-600)' : 'var(--info-600)'};border-radius:999px;"></div>
            </div>
          </div>
        `;
      });

      if (!filtered.length) {
        cardsHtml = `<div class="p-3 text-center text-neutral-400 text-sm">No orders match your filter.</div>`;
      }

      section.innerHTML = `
        <div style="margin-top:10px;padding:10px;background:var(--neutral-50);border-radius:var(--radius-lg);border:1px solid var(--neutral-200);">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;flex-wrap:wrap;gap:6px;">
            <span style="font-size:0.8rem;font-weight:600;">
              <i class="fa-regular fa-file-lines" style="color:var(--accent-600);margin-right:4px;"></i>
              Select Order <span style="color:var(--neutral-400);font-weight:400;">(${filtered.length} shown)</span>
            </span>
            <div style="display:flex;gap:6px;flex-wrap:wrap;">
              <input type="text" class="input-field order-picker-search" placeholder="🔍 Search…"
                style="padding:6px 10px;font-size:0.8rem;width:180px;" value="${existingSearch}"
                oninput="renderOrderPicker('${cardId}','${tech}','${selectedOrderNo || ''}')">
              <div class="select-wrapper" style="width:140px;">
                <select class="select-field order-picker-sort" style="padding:6px 10px;font-size:0.8rem;"
                  onchange="renderOrderPicker('${cardId}','${tech}','${selectedOrderNo || ''}')">
                  <option value="date-desc" ${existingSort==='date-desc'?'selected':''}>📅 Newest</option>
                  <option value="date-asc"  ${existingSort==='date-asc'?'selected':''}>📅 Oldest</option>
                  <option value="litres-desc" ${existingSort==='litres-desc'?'selected':''}>💧 Litres ↓</option>
                  <option value="order-asc"    ${existingSort==='order-asc'?'selected':''}>🔤 Order No</option>
                </select>
              </div>
            </div>
          </div>
          <div style="max-height:300px;overflow-y:auto;" id="orderPickerList_${cardId}">
            ${cardsHtml}
          </div>
        </div>
      `;
    }

    function selectOrderCard(cardId, tech, orderNo, clickedEl) {
      const region = DB.regions[DB.currentRegion];
      const order = region.orders[orderNo];
      const card = document.getElementById(cardId);
      if (!order || !card) return;

      const techSupplied = Object.values(region.dailyLog).flat()
        .filter(e => e.orderNo === order.orderNo && e.technician === tech && !e.unallocated)
        .reduce((s, e) => s + e.supplied, 0);
      const remaining = order.allocations[tech] - techSupplied;

      card.querySelector(`#orderNo_${cardId}`).textContent = order.orderNo;
      card.querySelector(`#vehicle_${cardId}`).textContent = order.vehiclePlate;
      card.querySelector(`#allocated_${cardId}`).textContent = order.allocations[tech] + 'L';
      card.querySelector(`#remaining_${cardId}`).textContent = Math.max(0, remaining) + 'L';
      card.querySelector(`#commentSection_${cardId}`).style.display = 'none';
      card.dataset.orderNo = order.orderNo;
      card.dataset.unallocated = 'false';

      renderOrderPicker(cardId, tech, orderNo);
    }

    function techSelected(select, cardId) {
      const tech = select.value;
      const card = document.getElementById(cardId);
      const region = DB.regions[DB.currentRegion];

      card.querySelector(`#orderNo_${cardId}`).textContent = '—';
      card.querySelector(`#vehicle_${cardId}`).textContent = '—';
      card.querySelector(`#allocated_${cardId}`).textContent = '—';
      card.querySelector(`#remaining_${cardId}`).textContent = '—';
      card.querySelector(`#commentSection_${cardId}`).style.display = 'none';
      card.querySelector(`#orderPickerSection_${cardId}`).innerHTML = '';
      delete card.dataset.orderNo;
      delete card.dataset.unallocated;

      if (!tech) return;

      const assignedOrders = Object.values(region.orders).filter(o =>
        o.status === 'OPEN' && o.allocations && o.allocations[tech]
      );

      if (assignedOrders.length === 0) {
        card.querySelector(`#orderNo_${cardId}`).textContent = 'Unallocated';
        card.querySelector(`#vehicle_${cardId}`).textContent = '—';
        card.querySelector(`#allocated_${cardId}`).textContent = '0L';
        card.querySelector(`#remaining_${cardId}`).textContent = '—';
        card.querySelector(`#commentSection_${cardId}`).style.display = 'block';
        card.dataset.unallocated = 'true';
      } else if (assignedOrders.length === 1) {
        selectOrderCard(cardId, tech, assignedOrders[0].orderNo, null);
        renderOrderPicker(cardId, tech, assignedOrders[0].orderNo);
      } else {
        renderOrderPicker(cardId, tech, '');
      }
    }

    function saveDaily() {
      const date = document.getElementById('dailyDate').value;
      if (!date) return showToast('Please select a date', 'warning');
      
      const region = DB.regions[DB.currentRegion];
      if (!region.dailyLog[date]) region.dailyLog[date] = [];
      
      const cards = document.querySelectorAll('#dailyEntriesContainer .card');
      let saved = 0;
      let skipped = 0;
      
      cards.forEach(card => {
        const tech = card.querySelector('select').value;
        const supplied = parseFloat(card.querySelector('input[type="number"]').value);
        const isUnalloc = card.dataset.unallocated === 'true';
        
        if (!tech || !supplied || supplied <= 0) return;
        
        if (isUnalloc) {
          const comment = card.querySelector('input[type="text"]')?.value;
          if (!comment) {
            skipped++;
            card.querySelector('input[type="text"]')?.classList.add('error');
            return;
          }
          region.dailyLog[date].push({
            technician: tech,
            supplied,
            comment,
            unallocated: true
          });
          saved++;
        } else {
          const orderNo = card.dataset.orderNo;
          if (!orderNo) return;
          
          const order = region.orders[orderNo];
          if (!order || order.status === 'CLOSED') return;
          
          region.dailyLog[date].push({
            orderNo,
            technician: tech,
            supplied
          });
          
          order.suppliedTotal += supplied;
          saved++;
        }
      });
      
      Object.values(region.orders).forEach(o => {
        if (o.suppliedTotal >= o.totalLiters) o.status = 'CLOSED';
      });
      
      save();
      showToast(`Saved ${saved} entries${skipped ? `, ${skipped} skipped` : ''}`);
      
      document.getElementById('dailyEntriesContainer').innerHTML = '';
      loadDailyLog();
      renderDailyHistory();
      
      checkForOverages();
    }

    function checkForOverages() {
      const region = DB.regions[DB.currentRegion];
      
      Object.entries(region.orders).forEach(([orderNo, order]) => {
        Object.entries(order.allocations || {}).forEach(([tech, alloc]) => {
          const supplied = Object.values(region.dailyLog).flat()
            .filter(e => e.orderNo === orderNo && e.technician === tech)
            .reduce((s, e) => s + e.supplied, 0);
            
          if (supplied > alloc && !(order.overageComments && order.overageComments[tech])) {
            openOverageComment(orderNo, tech);
          }
        });
      });
    }

    function deleteDailyEntry(date, idx) {
      if (!confirm('Delete this entry?')) return;
      
      const region = DB.regions[DB.currentRegion];
      const entry = region.dailyLog[date][idx];
      
      if (!entry.unallocated && entry.orderNo) {
        const order = region.orders[entry.orderNo];
        if (order) {
          order.suppliedTotal -= entry.supplied;
        }
      }
      
      region.dailyLog[date].splice(idx, 1);
      if (region.dailyLog[date].length === 0) {
        delete region.dailyLog[date];
      }
      
      save();
      loadDailyLog();
      renderDailyHistory();
      showToast('Entry deleted', 'info', 1500);
    }

    function renderDailyHistory() {
      const container = document.getElementById('dailyHistoryContainer');
      if (!container) return;
      
      const region = DB.regions[DB.currentRegion];
      const dates = Object.keys(region.dailyLog).sort().reverse().slice(0, 30);
      
      if (!dates.length) {
        container.innerHTML = renderEmptyState('daily', 'Add Entry', 'addDailyEntry()');
        return;
      }
      
      let html = '';
      dates.forEach(date => {
        const entries = region.dailyLog[date];
        const total = entries.reduce((s, e) => s + e.supplied, 0);
        const allocTotal = entries.filter(e => !e.unallocated).reduce((s, e) => s + e.supplied, 0);
        const unallocTotal = entries.filter(e => e.unallocated).reduce((s, e) => s + e.supplied, 0);
        const autoCount = entries.filter(e => e.autoImported).length;
        const dateLabel = new Date(date + 'T12:00:00').toLocaleDateString('en-GB', { weekday: 'short', day: '2-digit', month: 'short', year: 'numeric' });

        html += `
          <div class="tech-alloc-row" style="cursor:pointer;border-radius:var(--radius-lg);padding:12px 14px;background:white;border:1px solid var(--neutral-200);margin-bottom:6px;transition:all 150ms;" 
               onmouseenter="this.style.borderColor='var(--accent-300)'" 
               onmouseleave="this.style.borderColor='var(--neutral-200)'"
               onclick="openDailyHistoryModal('${date}')">
            <div class="tech-avatar" style="background:var(--status-info-bg);color:var(--status-info);flex-shrink:0;">
              <i class="fa-regular fa-calendar-days"></i>
            </div>
            <div class="tech-details" style="flex:1;">
              <div class="tech-name">${dateLabel}</div>
              <div class="tech-plate" style="display:flex;gap:8px;flex-wrap:wrap;margin-top:2px;">
                <span>${entries.length} entr${entries.length===1?'y':'ies'}</span>
                <span style="color:var(--status-success);">✓ ${allocTotal}L allocated</span>
                ${unallocTotal > 0 ? `<span style="color:var(--status-warning);">⚠ ${unallocTotal}L unalloc</span>` : ''}
                ${autoCount > 0 ? `<span style="color:var(--status-info);">🤖 ${autoCount} auto</span>` : ''}
              </div>
            </div>
            <div class="tech-stats" style="display:flex;align-items:center;gap:8px;">
              <span style="font-family:var(--font-mono);font-weight:700;font-size:0.9rem;padding:4px 12px;border-radius:var(--radius-full);background:var(--accent-50);color:var(--accent-700);border:1px solid var(--accent-200);">${total}L</span>
              <button class="btn btn-primary btn-sm" onclick="event.stopPropagation();openDailyHistoryModal('${date}')">
                <i class="fa-regular fa-eye"></i> View & Edit
              </button>
            </div>
          </div>
        `;
      });
      
      container.innerHTML = html;
    }

    // ===== DAILY HISTORY CRUD MODAL =====
    function openDailyHistoryModal(date) {
      const dateLabel = new Date(date + 'T12:00:00').toLocaleDateString('en-GB', { weekday: 'long', day: '2-digit', month: 'long', year: 'numeric' });
      document.getElementById('historyModalTitle').textContent = dateLabel;
      document.getElementById('historyModalDate').value = date;
      renderHistoryModalEntries(date);
      openModal('dailyHistoryModal');
    }

    function renderHistoryModalEntries(date) {
      const region = DB.regions[DB.currentRegion];
      const entries = region.dailyLog[date] || [];
      const container = document.getElementById('historyModalEntries');

      if (!entries.length) {
        container.innerHTML = `<div style="text-align:center;padding:2rem;color:var(--neutral-400);">No entries for this date.</div>`;
        return;
      }

      const total = entries.reduce((s, e) => s + e.supplied, 0);
      const allocTotal = entries.filter(e => !e.unallocated).reduce((s, e) => s + e.supplied, 0);
      const unallocTotal = entries.filter(e => e.unallocated).reduce((s, e) => s + e.supplied, 0);

      let html = `
        <div style="display:flex;gap:12px;flex-wrap:wrap;margin-bottom:14px;padding:10px 14px;background:var(--neutral-50);border-radius:var(--radius-lg);border:1px solid var(--neutral-200);">
          <span class="badge badge-neutral">${entries.length} entries</span>
          <span class="badge badge-success">✓ ${allocTotal}L allocated</span>
          ${unallocTotal > 0 ? `<span class="badge badge-warning">⚠ ${unallocTotal}L unallocated</span>` : ''}
          <span style="font-family:var(--font-mono);font-weight:700;font-size:0.85rem;padding:3px 12px;border-radius:var(--radius-full);background:var(--accent-50);color:var(--accent-700);border:1px solid var(--accent-200);">${total}L total</span>
        </div>
        <div class="table-container" style="max-height:420px;overflow-y:auto;">
          <table class="table">
            <thead>
              <tr>
                <th>#</th>
                <th>Technician</th>
                <th>Order No</th>
                <th>Supplied</th>
                <th>Type</th>
                <th>Comment</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>`;

      entries.forEach((entry, idx) => {
        const typeBadge = entry.unallocated
          ? `<span class="badge badge-warning">Unalloc</span>`
          : `<span class="badge badge-success">Allocated</span>`;
        const autoBadge = entry.autoImported
          ? `<span style="font-size:0.65rem;font-weight:700;padding:1px 5px;border-radius:var(--radius-full);background:var(--status-info-bg);color:var(--status-info);border:1px solid var(--status-info);">🤖 AUTO</span>`
          : '';

        html += `<tr id="hrow_${date}_${idx}">
          <td class="text-xs font-mono" style="color:var(--neutral-400);">${idx+1}</td>
          <td>
            <div style="font-weight:600;font-size:0.85rem;">${entry.technician}</div>
            ${autoBadge}
            ${entry.siteId ? `<div class="font-mono text-xs mt-1" style="color:var(--neutral-400);">${entry.siteId}</div>` : ''}
          </td>
          <td class="font-mono">${entry.orderNo || '—'}</td>
          <td>
            <span style="font-family:var(--font-mono);font-weight:700;padding:3px 10px;border-radius:var(--radius-full);
              background:${entry.unallocated?'var(--status-warning-bg)':'var(--status-success-bg)'};
              color:${entry.unallocated?'var(--status-warning)':'var(--status-success)'};
              border:1px solid ${entry.unallocated?'rgba(217,119,6,0.25)':'rgba(22,163,74,0.25)'};">
              ${entry.supplied}L
            </span>
          </td>
          <td>${typeBadge}</td>
          <td class="text-xs" style="color:var(--neutral-600);">
            ${entry.fuelFound > 0 ? `<div>Found: <strong>${entry.fuelFound}L</strong></div>` : ''}
            ${entry.supplier ? `<div>${entry.supplier}</div>` : ''}
            ${entry.cph > 0 ? `<div>CPH: ${entry.cph}</div>` : ''}
            ${entry.dgHoursUsed > 0 ? `<div style="color:var(--status-info);">⚡ ${entry.dgHoursUsed}h DG</div>` : ''}
            ${!entry.fuelFound && !entry.supplier && !entry.cph ? (entry.comment || '—') : (entry.comment ? `<div style="color:var(--neutral-400);">${entry.comment}</div>` : '')}
          </td>
          <td>
            <div class="flex gap-1">
              <button class="btn btn-secondary btn-sm" onclick="historyEditEntry('${date}', ${idx})" title="Edit">
                <i class="fa-regular fa-pen"></i>
              </button>
              <button class="btn btn-sm" style="background:var(--status-danger-bg);color:var(--status-danger);border:1px solid var(--status-danger);" onclick="historyDeleteEntry('${date}', ${idx})" title="Delete">
                <i class="fa-regular fa-trash"></i>
              </button>
            </div>
          </td>
        </tr>`;
      });

      html += `</tbody></table></div>`;
      container.innerHTML = html;
    }

    function historyEditEntry(date, idx) {
      const region = DB.regions[DB.currentRegion];
      const entry = region.dailyLog[date]?.[idx];
      if (!entry) return showToast('Entry not found', 'error');

      const newSupplied = prompt(`Edit supplied litres for ${entry.technician}${entry.orderNo ? ' (Order: ' + entry.orderNo + ')' : ''}:`, entry.supplied);
      if (newSupplied === null) return;
      const parsed = parseFloat(newSupplied);
      if (isNaN(parsed) || parsed < 0) return showToast('Invalid value', 'error');

      // Adjust order running total
      if (!entry.unallocated && entry.orderNo) {
        const order = region.orders[entry.orderNo];
        if (order) {
          order.suppliedTotal = order.suppliedTotal - entry.supplied + parsed;
          order.status = order.suppliedTotal >= order.totalLiters ? 'CLOSED' : 'OPEN';
        }
      }

      // Allow editing comment too
      const newComment = prompt('Comment (optional, leave blank for none):', entry.comment || '');
      if (newComment !== null) entry.comment = newComment.trim() || undefined;

      entry.supplied = parsed;
      save();
      renderHistoryModalEntries(date);
      renderDailyHistory();
      showToast('Entry updated', 'success');
    }

    function historyDeleteEntry(date, idx) {
      const region = DB.regions[DB.currentRegion];
      const entry = region.dailyLog[date]?.[idx];
      if (!entry) return showToast('Entry not found', 'error');

      if (!confirm(`Delete entry: ${entry.technician} — ${entry.supplied}L${entry.orderNo ? ' (Order ' + entry.orderNo + ')' : ''}?`)) return;

      // Reverse order total
      if (!entry.unallocated && entry.orderNo) {
        const order = region.orders[entry.orderNo];
        if (order) {
          order.suppliedTotal = Math.max(0, order.suppliedTotal - entry.supplied);
          order.status = order.suppliedTotal >= order.totalLiters ? 'CLOSED' : 'OPEN';
        }
      }

      region.dailyLog[date].splice(idx, 1);
      if (region.dailyLog[date].length === 0) delete region.dailyLog[date];
      save();

      // If the date is now gone, close modal
      if (!region.dailyLog[date]) {
        closeModal('dailyHistoryModal');
        renderDailyHistory();
        showToast('Entry deleted — date removed (no more entries)', 'info');
        return;
      }

      renderHistoryModalEntries(date);
      renderDailyHistory();
      showToast('Entry deleted', 'info');
    }

    function historyGoToDate(date) {
      closeModal('dailyHistoryModal');
      const dateEl = document.getElementById('dailyDate');
      if (dateEl) {
        dateEl.value = date;
        loadDailyLog();
        dateEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

    // ===== OVERAGE FUNCTIONS =====
    function openOverageComment(orderNo, tech) {
      const region = DB.regions[DB.currentRegion];
      const order = region.orders[orderNo];
      
      const alloc = order.allocations[tech] || 0;
      const supplied = Object.values(region.dailyLog).flat()
        .filter(e => e.orderNo === orderNo && e.technician === tech)
        .reduce((s, e) => s + e.supplied, 0);
      
      overageContext = { orderNo, tech };
      
      document.getElementById('overageMeta').innerHTML = `
        <strong>${tech}</strong> supplied <strong class="text-danger-700">${supplied}L</strong> 
        against allocation of <strong>${alloc}L</strong> 
        (${(supplied - alloc).toFixed(1)}L over)
      `;
      
      document.getElementById('overageComment').value = order.overageComments?.[tech] || '';
      openModal('overageModal');
    }

    function saveOverageComment() {
      if (!overageContext) return;
      
      const { orderNo, tech } = overageContext;
      const comment = document.getElementById('overageComment').value.trim();
      
      if (!comment) return showToast('Please enter a comment', 'warning');
      
      const region = DB.regions[DB.currentRegion];
      const order = region.orders[orderNo];
      
      if (!order.overageComments) order.overageComments = {};
      order.overageComments[tech] = comment;
      
      save();
      closeModal('overageModal');
      renderOrdersList();
      showToast('Overage comment saved');
    }

    // ===== ORDERS PAGE =====
    let orderFilterStatus = 'all';

    function renderOrdersPage(container) {
      container.innerHTML = `
        <div class="stats-grid">
          <div class="stat-tile">
            <div class="stat-label">Total Ordered (Assigned)</div>
            <div class="stat-value" id="ordersTotalOrderedAssigned">0L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Total Supplied (Allocated)</div>
            <div class="stat-value text-success-700" id="ordersTotalSuppliedAssigned">0L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Balance (Assigned)</div>
            <div class="stat-value text-danger-700" id="ordersTotalBalanceAssigned">0L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Open Orders</div>
            <div class="stat-value" id="ordersOpenCount">0</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label text-warning-800"><i class="fa-regular fa-clipboard"></i> Unassigned Orders</div>
            <div class="stat-value text-warning-700" id="ordersUnassignedCount">0</div>
            <div class="text-sm mt-1" id="ordersUnassignedDetail"></div>
          </div>
        </div>

        <div class="card mb-4">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold">Create Order</h3>
            <button class="btn btn-primary btn-sm" onclick="toggleOrderForm()">
              <i class="fa-regular fa-chevron-down" id="orderFormChevron"></i>
            </button>
          </div>
          <div id="orderForm" style="display: none;">
            <div class="grid grid-cols-2 gap-4">
              <div class="input-group">
                <input type="text" class="input-field" id="orderNo" placeholder=" "
                  data-validate="order-no" oninput="liveValidate(this)">
                <label class="input-label">Order Number</label>
                <div class="field-hint" id="orderNoHint"></div>
              </div>
              <div class="input-group">
                <input type="text" class="input-field" id="vehiclePlate" placeholder=" " list="knownPlatesList"
                  data-validate="plate" oninput="liveValidate(this)">
                <label class="input-label">Vehicle Plate</label>
                <div class="field-hint" id="vehiclePlateHint"></div>
                <datalist id="knownPlatesList"></datalist>
              </div>
              <div class="input-group">
                <input type="number" class="input-field" id="totalLiters" placeholder=" "
                  data-validate="positive-number" oninput="liveValidate(this)">
                <label class="input-label">Total Litres</label>
                <div class="field-hint" id="totalLitersHint"></div>
              </div>
              <div class="input-group">
                <input type="date" class="input-field" id="orderDate">
                <label class="input-label">Order Date</label>
              </div>
            </div>
            <button class="btn btn-primary w-full mt-4" onclick="createOrder()">
              <i class="fa-regular fa-check"></i> Create Order
            </button>
          </div>
        </div>

        <div class="card mb-4">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold">Allocate Fuel</h3>
          </div>
          <div class="grid grid-cols-3 gap-4">
            <div class="select-wrapper">
              <select class="select-field" id="allocOrder" onchange="liveValidate(document.getElementById('allocAmount'))"></select>
            </div>
            <div class="select-wrapper">
              <select class="select-field" id="allocTech" onchange="liveValidate(document.getElementById('allocAmount'))"></select>
            </div>
            <div class="input-group">
              <input type="number" class="input-field" id="allocAmount" placeholder=" "
                data-validate="alloc-amount" oninput="liveValidate(this)">
              <label class="input-label">Litres</label>
              <div class="field-hint" id="allocAmountHint"></div>
            </div>
          </div>
          <button class="btn btn-primary w-full mt-4" onclick="allocateFuel()">
            <i class="fa-regular fa-link"></i> Allocate
          </button>
        </div>

        <div class="card">
          <div class="flex items-center justify-between mb-4">
            <div style="display:flex;align-items:center;gap:12px;">
              <h3 class="text-lg font-semibold">All Orders</h3>
              <span id="ordersRowCount" class="text-xs" style="color:var(--neutral-400);font-weight:500;"></span>
            </div>
            <div class="flex gap-2 flex-wrap items-center">
              <div class="flex gap-1 mr-2">
                <button class="btn btn-sm ${orderFilterStatus === 'all' ? 'btn-primary' : 'btn-secondary'}" onclick="setOrderFilter('all')">All</button>
                <button class="btn btn-sm ${orderFilterStatus === 'open' ? 'btn-primary' : 'btn-secondary'}" onclick="setOrderFilter('open')">Open</button>
                <button class="btn btn-sm ${orderFilterStatus === 'closed' ? 'btn-primary' : 'btn-secondary'}" onclick="setOrderFilter('closed')">Closed</button>
                <button class="btn btn-sm ${orderFilterStatus === 'assigned' ? 'btn-primary' : 'btn-secondary'}" onclick="setOrderFilter('assigned')">Assigned</button>
                <button class="btn btn-sm ${orderFilterStatus === 'unassigned' ? 'btn-primary' : 'btn-secondary'}" onclick="setOrderFilter('unassigned')">Unassigned</button>
              </div>
              <div class="select-wrapper" style="width: 140px;">
                <select class="select-field" id="orderFilterTech" onchange="renderOrdersList()">
                  <option value="">All Techs</option>
                </select>
              </div>
              <input type="date" class="input-field" style="width: 140px;" id="orderFilterFrom" onchange="renderOrdersList()">
              <input type="date" class="input-field" style="width: 140px;" id="orderFilterTo" onchange="renderOrdersList()">
              ${renderDensityToggle()}
              ${renderColChooser('orders')}
            </div>
          </div>
          <div id="ordersListContainer"></div>
        </div>
      `;

      updateOrderStats();
      populateAllocOrder();
      populateAllocTech();
      populateVehiclePlateDatalist();
      renderOrdersList();
      setTimeout(() => { applyColVisibility('orders'); updateColChooserBtn('orders'); }, 50);
    }

    function setOrderFilter(filter) {
      orderFilterStatus = filter;
      renderOrdersList();
    }

    function toggleOrderForm() {
      const form = document.getElementById('orderForm');
      const chevron = document.getElementById('orderFormChevron');
      if (!form) return;
      const isHidden = form.style.display === 'none';
      form.style.display = isHidden ? 'block' : 'none';
      if (chevron) chevron.style.transform = isHidden ? 'rotate(180deg)' : '';
    }

    function populateVehiclePlateDatalist() {
      const region = DB.regions[DB.currentRegion];
      const dl = document.getElementById('knownPlatesList');
      const vpField = document.getElementById('vehiclePlate');
      if (!dl || !vpField) return;
      
      const plates = new Set();
      Object.values(region.technicianPlates || {}).forEach(p => { if(p) plates.add(p); });
      Object.values(region.orders || {}).forEach(o => { if(o.vehiclePlate) plates.add(o.vehiclePlate); });
      
      dl.innerHTML = [...plates].map(p => `<option value="${p}">`).join('');
      
      if (!vpField.value && region.lastUsedPlate) {
        vpField.value = region.lastUsedPlate;
      }
    }

    function createOrder() {
      const orderNo = document.getElementById('orderNo').value.trim();
      const vehiclePlate = document.getElementById('vehiclePlate').value.trim();
      const totalLiters = parseFloat(document.getElementById('totalLiters').value);
      const orderDate = document.getElementById('orderDate').value || new Date().toISOString().slice(0, 10);
      
      if (!orderNo || !vehiclePlate || !totalLiters) {
        return showToast('Please fill all fields', 'warning');
      }
      
      const region = DB.regions[DB.currentRegion];
      
      if (region.orders[orderNo]) {
        return showToast('Order number already exists', 'error');
      }
      
      region.orders[orderNo] = {
        orderNo,
        vehiclePlate,
        totalLiters,
        suppliedTotal: 0,
        allocations: {},
        status: 'OPEN',
        createdDate: orderDate
      };
      
      region.lastUsedPlate = vehiclePlate;
      
      save();
      showToast('Order created successfully');
      
      document.getElementById('orderNo').value = '';
      document.getElementById('vehiclePlate').value = region.lastUsedPlate || '';
      document.getElementById('totalLiters').value = '';
      document.getElementById('orderDate').value = '';
      // Clear live-validation hints
      ['orderNoHint','vehiclePlateHint','totalLitersHint'].forEach(id => {
        const el = document.getElementById(id);
        if (el) { el.textContent = ''; el.className = 'field-hint'; }
      });
      ['orderNo','vehiclePlate','totalLiters'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.borderColor = '';
      });
      
      updateOrderStats();
      populateAllocOrder();
      renderOrdersList();
    }

    function populateAllocOrder() {
      const sel = document.getElementById('allocOrder');
      if (!sel) return;
      
      sel.innerHTML = '<option value="">Select order</option>';
      const region = DB.regions[DB.currentRegion];
      Object.values(region.orders)
        .filter(o => o.status === 'OPEN' && Object.keys(o.allocations || {}).length < Object.keys(region.technicians).length)
        .sort((a, b) => {
          // Carried orders last, then oldest first within each group
          if (a.carriedFromCycle && !b.carriedFromCycle) return 1;
          if (!a.carriedFromCycle && b.carriedFromCycle) return -1;
          return (a.createdDate || '').localeCompare(b.createdDate || '');
        })
        .forEach(o => {
          const opt = document.createElement('option');
          opt.value = o.orderNo;
          opt.textContent = o.carriedFromCycle
            ? `[OLD] ${o.orderNo} (${o.vehiclePlate})`
            : `${o.orderNo} (${o.vehiclePlate})`;
          sel.appendChild(opt);
        });
    }

    function populateAllocTech() {
      const sel = document.getElementById('allocTech');
      if (!sel) return;
      
      sel.innerHTML = '<option value="">Select technician</option>';
      DB.regions[DB.currentRegion].technicians.forEach(t => {
        const opt = document.createElement('option');
        opt.value = t;
        opt.textContent = t;
        sel.appendChild(opt);
      });
    }

    function allocateFuel() {
      const orderNo = document.getElementById('allocOrder').value;
      const tech = document.getElementById('allocTech').value;
      const amount = parseFloat(document.getElementById('allocAmount').value);
      
      if (!orderNo || !tech || !amount) {
        return showToast('Please fill all fields', 'warning');
      }
      
      const region = DB.regions[DB.currentRegion];
      const order = region.orders[orderNo];
      
      if (!order) return showToast('Order not found', 'error');
      
      if (order.allocations[tech]) {
        return showToast('Technician already allocated to this order', 'warning');
      }
      
      const totalAllocated = Object.values(order.allocations).reduce((s, v) => s + v, 0);
      if (totalAllocated + amount > order.totalLiters) {
        return showToast('Allocation exceeds order total', 'error');
      }
      
      order.allocations[tech] = amount;
      
      if (region.unassignedComments && region.unassignedComments[orderNo]) {
        delete region.unassignedComments[orderNo];
      }
      
      save();
      
      showToast(`${amount}L allocated to ${tech}`);
      document.getElementById('allocAmount').value = '';
      populateAllocOrder();
      renderOrdersList();
    }

    function updateOrderStats() {
      const region = DB.regions[DB.currentRegion];
      // Only count current-cycle orders (not carried-over from old cycle)
      const orders = Object.values(region.orders).filter(o => !o.carriedFromCycle);
      
      const assignedOrders = orders.filter(o => Object.keys(o.allocations || {}).length > 0);
      const unassignedOrders = orders.filter(o => Object.keys(o.allocations || {}).length === 0);
      
      const totalOrderedAssigned = assignedOrders.reduce((s, o) => s + o.totalLiters, 0);
      const totalSuppliedAssigned = assignedOrders.reduce((s, o) => s + o.suppliedTotal, 0);
      
      const totalOrderedUnassigned = unassignedOrders.reduce((s, o) => s + o.totalLiters, 0);
      
      const openOrders = assignedOrders.filter(o => (o.totalLiters - o.suppliedTotal) > 0);
      
      animateCounter(document.getElementById('ordersTotalOrderedAssigned'), totalOrderedAssigned, 'L');
      animateCounter(document.getElementById('ordersTotalSuppliedAssigned'), totalSuppliedAssigned, 'L');
      animateCounter(document.getElementById('ordersTotalBalanceAssigned'), totalOrderedAssigned - totalSuppliedAssigned, 'L');
      animateCounter(document.getElementById('ordersOpenCount'), openOrders.length, '');
      animateCounter(document.getElementById('ordersUnassignedCount'), unassignedOrders.length, '');
      
      document.getElementById('ordersUnassignedDetail').textContent = `${unassignedOrders.length} orders · ${totalOrderedUnassigned}L total`;
    }

    function renderOrdersList() {
      const container = document.getElementById('ordersListContainer');
      if (!container) return;
      
      const region = DB.regions[DB.currentRegion];
      let orders = Object.values(region.orders);

      // Auto-remove carried orders that are now closed (balance <= 0)
      // They should no longer appear anywhere once closed
      let needsSave = false;
      orders.forEach(o => {
        if (o.carriedFromCycle && (o.totalLiters - o.suppliedTotal) <= 0) {
          delete region.orders[o.orderNo];
          needsSave = true;
        }
      });
      if (needsSave) {
        save();
        orders = Object.values(region.orders);
      }

      // Split into current-cycle and carried (old cycle) orders
      const currentCycleOrders = orders.filter(o => !o.carriedFromCycle);
      const carriedOrders = orders.filter(o => !!o.carriedFromCycle);

      // For filtering/display, apply status filter to current-cycle orders only
      // Carried orders are always shown (they are always open by definition)
      let filteredCurrentOrders = currentCycleOrders.filter(o => {
        const balance = o.totalLiters - o.suppliedTotal;
        const hasAllocations = Object.keys(o.allocations || {}).length > 0;
        
        switch(orderFilterStatus) {
          case 'open':    return balance > 0 && hasAllocations;
          case 'closed':  return balance <= 0 && hasAllocations;
          case 'assigned': return hasAllocations;
          case 'unassigned': return !hasAllocations;
          default:        return true;
        }
      });
      
      const techFilter = document.getElementById('orderFilterTech')?.value;
      if (techFilter) {
        filteredCurrentOrders = filteredCurrentOrders.filter(o => Object.keys(o.allocations || {}).includes(techFilter));
      }
      
      const fromDate = document.getElementById('orderFilterFrom')?.value;
      const toDate = document.getElementById('orderFilterTo')?.value;
      if (fromDate) filteredCurrentOrders = filteredCurrentOrders.filter(o => o.createdDate >= fromDate);
      if (toDate) filteredCurrentOrders = filteredCurrentOrders.filter(o => o.createdDate <= toDate);
      
      const techSelect = document.getElementById('orderFilterTech');
      if (techSelect) {
        const currentValue = techSelect.value;
        techSelect.innerHTML = '<option value="">All Techs</option>';
        region.technicians.forEach(t => {
          const opt = document.createElement('option');
          opt.value = t; opt.textContent = t; techSelect.appendChild(opt);
        });
        techSelect.value = currentValue;
      }

      // Update row count badge
      const rowCountEl = document.getElementById('ordersRowCount');
      if (rowCountEl) {
        const total = orders.length;
        const shown = filteredCurrentOrders.length + carriedOrders.length;
        rowCountEl.textContent = shown === total ? `${total} order${total !== 1 ? 's' : ''}` : `${shown} of ${total} orders`;
      }
      
      if (!filteredCurrentOrders.length && !carriedOrders.length) {
        container.innerHTML = renderEmptyState('orders', 'Create Order', 'toggleOrderForm()');
        return;
      }
      
      // Sort current orders
      filteredCurrentOrders.sort((a, b) => {
        const aOpen = a.status !== 'CLOSED' && (a.totalLiters - a.suppliedTotal) > 0;
        const bOpen = b.status !== 'CLOSED' && (b.totalLiters - b.suppliedTotal) > 0;
        if (aOpen && !bOpen) return -1;
        if (!aOpen && bOpen) return 1;
        if (aOpen && bOpen) return (a.createdDate || '').localeCompare(b.createdDate || '');
        return (b.createdDate || '').localeCompare(a.createdDate || '');
      });

      // Sort carried orders oldest first
      carriedOrders.sort((a, b) => (a.createdDate || '').localeCompare(b.createdDate || ''));
      
      const assignedOrders = filteredCurrentOrders.filter(o => Object.keys(o.allocations || {}).length > 0);
      const unassignedOrders = filteredCurrentOrders.filter(o => Object.keys(o.allocations || {}).length === 0);
      
      const groups = { 
        Unassigned: unassignedOrders,
        Overage: [], 
        Open: [], 
        Closed: [] 
      };
      
      assignedOrders.forEach(order => {
        const balance = order.totalLiters - order.suppliedTotal;
        const hasOverage = Object.entries(order.allocations || {}).some(([tech, alloc]) => {
          const supplied = Object.values(region.dailyLog).flat().filter(e => e.orderNo === order.orderNo && e.technician === tech).reduce((s, e) => s + e.supplied, 0);
          return supplied > alloc;
        });
        if (hasOverage) groups.Overage.push(order);
        else if (balance <= 0) groups.Closed.push(order);
        else groups.Open.push(order);
      });
      
      const groupConfig = [
        { key: 'Unassigned', label: 'Unassigned',      color: 'var(--status-unassigned)', badge: 'badge-neutral', icon: '📋', collapsedByDefault: true  },
        { key: 'Overage',    label: 'Overage',          color: 'var(--status-danger)',     badge: 'badge-danger',  icon: '🔴', collapsedByDefault: false },
        { key: 'Open',       label: 'Open (Assigned)',  color: 'var(--status-success)',    badge: 'badge-success', icon: '🟢', collapsedByDefault: false },
        { key: 'Closed',     label: 'Closed',           color: 'var(--status-warning)',    badge: 'badge-warning', icon: '🟡', collapsedByDefault: true  },
      ];
      
      let html = '';
      
      const totalOpen = groups.Open.length + groups.Overage.length;
      const openBalance = [...groups.Open, ...groups.Overage].reduce((s,o)=>s+(o.totalLiters-o.suppliedTotal),0);
      const openSupplied = [...groups.Open, ...groups.Overage].reduce((s,o)=>s+o.suppliedTotal,0);
      const openOrdered = [...groups.Open, ...groups.Overage].reduce((s,o)=>s+o.totalLiters,0);
      const unassignedTotal = groups.Unassigned.reduce((s,o)=>s+o.totalLiters,0);
      
      html += `<div class="orders-sticky-bar">
        <div class="sticky-stat"><div class="sticky-stat-label">Open Orders</div><div class="sticky-stat-value">${totalOpen}</div></div>
        <div class="sticky-divider"></div>
        <div class="sticky-stat"><div class="sticky-stat-label">Unassigned</div><div class="sticky-stat-value">${unassignedOrders.length}</div></div>
        <div class="sticky-divider"></div>
        <div class="sticky-stat"><div class="sticky-stat-label">Ordered (Assigned)</div><div class="sticky-stat-value">${openOrdered}L</div></div>
        <div class="sticky-divider"></div>
        <div class="sticky-stat"><div class="sticky-stat-label">Supplied</div><div class="sticky-stat-value text-success-700">${openSupplied}L</div></div>
        <div class="sticky-divider"></div>
        <div class="sticky-stat"><div class="sticky-stat-label">Balance (Assigned)</div><div class="sticky-stat-value text-danger-700">${openBalance}L</div></div>
        ${groups.Overage.length > 0 ? '<div class="sticky-divider"></div><div class="sticky-stat"><div class="sticky-stat-label text-danger-700">Overages</div><div class="sticky-stat-value text-danger-700">'+groups.Overage.length+'</div></div>' : ''}
        ${carriedOrders.length > 0 ? `<div class="sticky-divider"></div><div class="sticky-stat"><div class="sticky-stat-label" style="color:var(--status-warning);">Carried Over</div><div class="sticky-stat-value" style="color:var(--status-warning);">${carriedOrders.length}</div></div>` : ''}
      </div>`;

      // ── CARRIED-OVER ORDERS FROM OLD CYCLE (shown first, clearly separated) ──
      if (carriedOrders.length > 0) {

        // Read current carried-filter state from module-level vars
        const carriedTechFilter  = window._carriedTechFilter  || '';
        const carriedDateFrom    = window._carriedDateFrom    || '';
        const carriedDateTo      = window._carriedDateTo      || '';

        // Apply filters to carriedOrders
        let visibleCarried = carriedOrders.filter(o => {
          if (carriedTechFilter && !Object.keys(o.allocations || {}).includes(carriedTechFilter)) return false;
          if (carriedDateFrom   && (o.createdDate || '') < carriedDateFrom) return false;
          if (carriedDateTo     && (o.createdDate || '') > carriedDateTo)   return false;
          return true;
        });

        // Collect all techs across all carried orders for the dropdown
        const carriedTechSet = new Set();
        carriedOrders.forEach(o => Object.keys(o.allocations || {}).forEach(t => carriedTechSet.add(t)));
        const carriedTechOptions = [...carriedTechSet].sort().map(t =>
          `<option value="${t}" ${carriedTechFilter === t ? 'selected' : ''}>${t}</option>`
        ).join('');

        // Group the (filtered) carried orders by source cycle
        const cycleGroups = {};
        visibleCarried.forEach(o => {
          const key = o.carriedFromCycle || 'Previous Cycle';
          if (!cycleGroups[key]) cycleGroups[key] = [];
          cycleGroups[key].push(o);
        });

        const totalCarriedBalance = carriedOrders.reduce((s,o)=>s+(o.totalLiters-o.suppliedTotal),0);

        html += `<div style="border:2px solid var(--status-warning);border-radius:var(--radius-lg);overflow:hidden;margin-bottom:var(--space-4);">
          <div style="background:linear-gradient(135deg,#7a3e00,#b45a00);color:white;padding:var(--space-3) var(--space-4);display:flex;align-items:center;gap:var(--space-3);">
            <span style="font-size:1.1rem;">⏳</span>
            <div style="flex:1;">
              <div style="font-weight:700;font-size:0.95rem;letter-spacing:0.03em;">CARRIED-OVER ORDERS — PREVIOUS CYCLE</div>
              <div style="font-size:0.72rem;opacity:0.85;margin-top:2px;">These orders were still open when the last cycle ended. NOT counted in ${DB.currentCycleName} totals. Auto-removed once fully supplied.</div>
            </div>
            <span style="background:rgba(255,255,255,0.2);padding:3px 10px;border-radius:999px;font-size:0.75rem;font-weight:700;">${carriedOrders.length} order${carriedOrders.length!==1?'s':''} · ${totalCarriedBalance}L outstanding</span>
          </div>
          <div style="background:rgba(122,62,0,0.06);border-bottom:1px solid rgba(217,119,6,0.25);padding:10px var(--space-4);display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
            <span style="font-size:0.72rem;font-weight:700;color:#92400e;text-transform:uppercase;letter-spacing:0.06em;white-space:nowrap;"><i class="fa-regular fa-filter"></i> Filter</span>
            <div style="position:relative;min-width:150px;flex:1;max-width:200px;">
              <select id="carriedTechFilter" onchange="applyCarriedFilters()" style="width:100%;padding:5px 28px 5px 10px;border:1px solid rgba(217,119,6,0.4);border-radius:var(--radius-md);font-size:0.78rem;background:white;color:var(--neutral-800);appearance:none;cursor:pointer;">
                <option value="">All Technicians</option>
                ${carriedTechOptions}
              </select>
              <i class="fa-regular fa-chevron-down" style="position:absolute;right:8px;top:50%;transform:translateY(-50%);pointer-events:none;font-size:0.65rem;color:#92400e;"></i>
            </div>
            <div style="display:flex;align-items:center;gap:5px;flex:1;max-width:175px;">
              <label style="font-size:0.7rem;color:#92400e;font-weight:600;white-space:nowrap;">From</label>
              <input type="date" id="carriedDateFrom" value="${carriedDateFrom}" onchange="applyCarriedFilters()"
                style="flex:1;padding:5px 8px;border:1px solid rgba(217,119,6,0.4);border-radius:var(--radius-md);font-size:0.78rem;background:white;color:var(--neutral-800);">
            </div>
            <div style="display:flex;align-items:center;gap:5px;flex:1;max-width:175px;">
              <label style="font-size:0.7rem;color:#92400e;font-weight:600;white-space:nowrap;">To</label>
              <input type="date" id="carriedDateTo" value="${carriedDateTo}" onchange="applyCarriedFilters()"
                style="flex:1;padding:5px 8px;border:1px solid rgba(217,119,6,0.4);border-radius:var(--radius-md);font-size:0.78rem;background:white;color:var(--neutral-800);">
            </div>
            ${(carriedTechFilter || carriedDateFrom || carriedDateTo) ? `
            <button onclick="clearCarriedFilters()" style="padding:5px 12px;border:1px solid rgba(217,119,6,0.5);border-radius:var(--radius-md);background:rgba(255,255,255,0.7);color:#92400e;font-size:0.72rem;font-weight:600;cursor:pointer;white-space:nowrap;">
              <i class="fa-regular fa-xmark"></i> Clear
            </button>` : ''}
            <span style="font-size:0.72rem;color:#b45a00;margin-left:auto;white-space:nowrap;">${visibleCarried.length} of ${carriedOrders.length} shown</span>
          </div>
          <div style="background:rgba(180,90,0,0.04);padding:var(--space-3);">
          ${visibleCarried.length === 0 ? `
            <div style="text-align:center;padding:24px;color:#b45a00;font-size:0.85rem;">
              <i class="fa-regular fa-filter" style="font-size:1.5rem;display:block;margin-bottom:8px;opacity:0.5;"></i>
              No carried orders match the current filters.
              <br><button onclick="clearCarriedFilters()" style="margin-top:8px;padding:4px 12px;border:1px solid rgba(217,119,6,0.4);border-radius:999px;background:white;color:#92400e;font-size:0.75rem;cursor:pointer;">Clear Filters</button>
            </div>` : ''}`;

        Object.entries(cycleGroups).forEach(([cycleName, cOrders]) => {
          const gId = 'carried_group_' + cycleName.replace(/\s+/g,'_');
          html += `<div class="order-group-header" onclick="toggleOrderGroup('${gId}')" style="border-color:var(--status-warning);background:rgba(217,119,6,0.08);margin-bottom:var(--space-2);">
            <span style="font-size:0.9rem;">🔄</span>
            <span class="order-group-title" style="color:#92400e;">From: ${cycleName}</span>
            <span class="badge badge-warning">${cOrders.length}</span>
            <span style="font-size:0.72rem;color:var(--status-warning);margin-left:auto;margin-right:var(--space-2);">Balance: ${cOrders.reduce((s,o)=>s+(o.totalLiters-o.suppliedTotal),0)}L remaining</span>
            <i class="fa-regular fa-chevron-down order-group-chevron" id="chevg_${gId}"></i>
          </div>
          <div id="${gId}" class="order-group-body">`;

          cOrders.forEach(order => {
            const balance = order.totalLiters - order.suppliedTotal;
            const progress = order.totalLiters > 0 ? (order.suppliedTotal / order.totalLiters) * 100 : 0;
            const isNearly = progress >= 90 && progress < 100;
            const allocEntries = Object.entries(order.allocations || {});

            // Per-tech supply breakdown for follow-up
            let techRowsHtml = '';
            allocEntries.forEach(([tech, alloc]) => {
              const techSupplied = Object.values(region.dailyLog).flat()
                .filter(e => e.orderNo === order.orderNo && e.technician === tech)
                .reduce((s, e) => s + e.supplied, 0);
              const techRemaining = alloc - techSupplied;
              const techPct = alloc > 0 ? Math.min(100, (techSupplied / alloc) * 100) : 0;
              const plate = region.technicianPlates?.[tech] || '—';
              const isOver = techSupplied > alloc;
              techRowsHtml += `
                <div style="display:flex;align-items:center;gap:10px;padding:8px 10px;background:rgba(255,255,255,0.7);border-radius:var(--radius-md);margin-bottom:6px;border:1px solid rgba(217,119,6,0.2);">
                  <div style="width:32px;height:32px;border-radius:50%;background:rgba(217,119,6,0.15);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.78rem;color:#92400e;flex-shrink:0;">${tech.charAt(0).toUpperCase()}</div>
                  <div style="flex:1;min-width:0;">
                    <div style="font-weight:600;font-size:0.82rem;color:var(--neutral-800);">${tech}</div>
                    <div style="font-size:0.7rem;color:var(--neutral-500);">🚗 ${plate}</div>
                    <div style="margin-top:4px;">
                      <div style="height:5px;background:var(--neutral-200);border-radius:999px;overflow:hidden;">
                        <div style="height:100%;width:${techPct}%;background:${isOver ? 'var(--status-danger)' : techPct >= 90 ? 'var(--status-warning)' : 'var(--status-success)'};border-radius:999px;transition:width 0.6s;"></div>
                      </div>
                    </div>
                  </div>
                  <div style="text-align:right;flex-shrink:0;">
                    <div style="font-size:0.75rem;font-weight:700;color:${isOver ? 'var(--status-danger)' : 'var(--neutral-700)'};">${techSupplied}/${alloc}L</div>
                    <div style="font-size:0.68rem;color:${techRemaining > 0 ? 'var(--status-warning)' : 'var(--status-success)'};">
                      ${isOver ? `+${(techSupplied-alloc).toFixed(1)}L over` : techRemaining > 0 ? `${techRemaining}L outstanding` : '✓ Complete'}
                    </div>
                  </div>
                </div>`;
            });

            // Recent supply history for this order
            const supplyHistory = [];
            Object.entries(region.dailyLog).sort((a,b)=>b[0].localeCompare(a[0])).forEach(([date, entries]) => {
              entries.forEach(e => {
                if (e.orderNo === order.orderNo) supplyHistory.push({ date, ...e });
              });
            });
            const histHtml = supplyHistory.length === 0
              ? `<div style="font-size:0.75rem;color:var(--neutral-400);font-style:italic;padding:6px 0;">No supply entries recorded yet.</div>`
              : supplyHistory.slice(0, 8).map(e => `
                  <div style="display:flex;justify-content:space-between;align-items:center;padding:4px 8px;font-size:0.74rem;border-bottom:1px solid var(--neutral-100);">
                    <span style="color:var(--neutral-500);">${e.date}</span>
                    <span style="font-weight:600;color:var(--neutral-700);">${e.technician}</span>
                    <span style="font-weight:700;color:var(--status-success);font-family:var(--font-mono);">+${e.supplied}L</span>
                  </div>`).join('') + (supplyHistory.length > 8 ? `<div style="font-size:0.7rem;color:var(--neutral-400);padding:4px 8px;">…and ${supplyHistory.length - 8} more entries</div>` : '');

            const cardId = 'carried_detail_' + order.orderNo.replace(/[^a-zA-Z0-9]/g,'_');

            html += `<div class="order-card${isNearly ? ' nearly-full' : ''}" data-order-no="${order.orderNo}" style="border-left:4px solid var(--status-warning);margin-bottom:10px;">
              <!-- CLICKABLE HEADER — opens full detail -->
              <div class="order-header" onclick="toggleCarriedDetail('${cardId}')" style="cursor:pointer;">
                <div class="order-status-indicator" style="background:var(--status-warning);width:10px;height:10px;border-radius:50%;flex-shrink:0;"></div>
                <div class="order-info" style="flex:1;">
                  <div class="order-title" style="display:flex;align-items:center;gap:6px;">
                    ${order.orderNo}
                    <span style="font-size:0.65rem;background:rgba(217,119,6,0.18);color:#92400e;border-radius:999px;padding:1px 7px;font-weight:700;letter-spacing:0.04em;">OLD CYCLE</span>
                    <span style="font-size:0.65rem;color:var(--neutral-400);">From: ${order.carriedFromCycle}</span>
                  </div>
                  <div class="order-meta">
                    <span><i class="fa-regular fa-truck"></i> ${order.vehiclePlate}</span>
                    <span><i class="fa-regular fa-calendar"></i> ${order.createdDate || '—'}</span>
                    <span><i class="fa-regular fa-users"></i> ${allocEntries.length} tech${allocEntries.length!==1?'s':''}: ${allocEntries.map(([t])=>t).join(', ')}</span>
                  </div>
                </div>
                <div class="order-stats">
                  <div class="order-progress">
                    <div class="progress-bar">
                      <div class="progress-fill warning" style="width:${progress}%;"></div>
                    </div>
                    <div class="text-sm text-center mt-1">${order.suppliedTotal}/${order.totalLiters}L</div>
                  </div>
                  <span class="badge badge-warning">${balance}L remaining</span>
                </div>
                <i class="fa-regular fa-chevron-down order-chevron" id="chev_carried_${order.orderNo.replace(/[^a-zA-Z0-9]/g,'_')}" style="transition:transform 0.25s;"></i>
              </div>

              <!-- FULL DETAIL PANEL (collapsed by default) -->
              <div id="${cardId}" style="display:none;" class="order-body">
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px;">
                  <div style="background:var(--neutral-50);border-radius:var(--radius-md);padding:10px;border:1px solid var(--neutral-200);">
                    <div style="font-size:0.7rem;color:var(--neutral-500);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:4px;">Order</div>
                    <div style="font-weight:700;font-family:var(--font-mono);">${order.orderNo}</div>
                  </div>
                  <div style="background:var(--neutral-50);border-radius:var(--radius-md);padding:10px;border:1px solid var(--neutral-200);">
                    <div style="font-size:0.7rem;color:var(--neutral-500);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:4px;">Vehicle</div>
                    <div style="font-weight:700;font-family:var(--font-mono);">${order.vehiclePlate}</div>
                  </div>
                  <div style="background:var(--neutral-50);border-radius:var(--radius-md);padding:10px;border:1px solid var(--neutral-200);">
                    <div style="font-size:0.7rem;color:var(--neutral-500);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:4px;">Created</div>
                    <div style="font-weight:600;">${order.createdDate || '—'}</div>
                  </div>
                  <div style="background:rgba(217,119,6,0.08);border-radius:var(--radius-md);padding:10px;border:1px solid rgba(217,119,6,0.25);">
                    <div style="font-size:0.7rem;color:#92400e;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:4px;">Outstanding</div>
                    <div style="font-weight:700;color:#b45a00;font-family:var(--font-mono);">${balance}L</div>
                  </div>
                  <div style="background:var(--neutral-50);border-radius:var(--radius-md);padding:10px;border:1px solid var(--neutral-200);">
                    <div style="font-size:0.7rem;color:var(--neutral-500);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:4px;">Total Ordered</div>
                    <div style="font-weight:600;font-family:var(--font-mono);">${order.totalLiters}L</div>
                  </div>
                  <div style="background:var(--status-success-bg);border-radius:var(--radius-md);padding:10px;border:1px solid var(--status-success);">
                    <div style="font-size:0.7rem;color:var(--status-success);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:4px;">Already Supplied</div>
                    <div style="font-weight:700;color:var(--status-success);font-family:var(--font-mono);">${order.suppliedTotal}L</div>
                  </div>
                </div>

                <!-- Overall progress bar -->
                <div style="margin-bottom:14px;">
                  <div style="display:flex;justify-content:space-between;font-size:0.72rem;color:var(--neutral-500);margin-bottom:4px;">
                    <span>Overall Progress</span><span style="font-weight:700;">${progress.toFixed(1)}%</span>
                  </div>
                  <div style="height:8px;background:var(--neutral-200);border-radius:999px;overflow:hidden;">
                    <div style="height:100%;width:${progress}%;background:var(--status-warning);border-radius:999px;transition:width 0.8s;"></div>
                  </div>
                </div>

                <!-- Tech allocations & outstanding per tech -->
                <div style="margin-bottom:14px;">
                  <div style="font-size:0.78rem;font-weight:700;color:var(--neutral-700);margin-bottom:8px;display:flex;align-items:center;gap:6px;">
                    <i class="fa-regular fa-users" style="color:var(--status-warning);"></i> Technician Breakdown
                  </div>
                  ${techRowsHtml || '<div style="font-size:0.75rem;color:var(--neutral-400);font-style:italic;">No technicians allocated.</div>'}
                </div>

                <!-- Supply history -->
                <div style="margin-bottom:14px;">
                  <div style="font-size:0.78rem;font-weight:700;color:var(--neutral-700);margin-bottom:6px;display:flex;align-items:center;gap:6px;">
                    <i class="fa-regular fa-clock-rotate-left" style="color:var(--status-info);"></i> Supply History
                  </div>
                  <div style="border:1px solid var(--neutral-200);border-radius:var(--radius-md);overflow:hidden;background:white;">
                    ${histHtml}
                  </div>
                </div>

                <!-- Action buttons -->
                <div style="display:flex;gap:8px;justify-content:flex-end;padding-top:10px;border-top:1px solid var(--neutral-100);">
                  <button class="btn btn-secondary btn-sm" onclick="editOrder('${order.orderNo}')">
                    <i class="fa-regular fa-pen-to-square"></i> Edit Order
                  </button>
                  <button class="btn btn-secondary btn-sm" onclick="deleteOrder('${order.orderNo}')">
                    <i class="fa-regular fa-trash"></i> Remove
                  </button>
                </div>
              </div>
            </div>`;
          });

          html += `</div>`; // close group body
        });

        html += `</div></div></div>`; // close: content area + filter bar wrapper + outer border panel
      }

      // ── CURRENT CYCLE ORDERS ──
      if (filteredCurrentOrders.length > 0) {
        groupConfig.forEach(g => {
          const gOrders = groups[g.key];
          if (gOrders.length === 0) return;
          const gId = 'group_' + g.key;

          // Persist user-expanded state across re-renders
          const stateKey = '_grpOpen_' + g.key;
          // If user has explicitly toggled, honour it; otherwise use collapsedByDefault
          const isOpen = (window[stateKey] !== undefined) ? window[stateKey] : !g.collapsedByDefault;

          // Summary line shown inside the header when collapsed
          const summaryText = g.key === 'Closed'
            ? `${gOrders.length} closed order${gOrders.length!==1?'s':''} · ${gOrders.reduce((s,o)=>s+o.suppliedTotal,0)}L supplied`
            : g.key === 'Unassigned'
            ? `${gOrders.length} unassigned order${gOrders.length!==1?'s':''} · ${gOrders.reduce((s,o)=>s+o.totalLiters,0)}L total`
            : '';

          html += `<div class="order-group-header" onclick="toggleOrderGroup('${gId}')">
            <span style="font-size:1rem;">${g.icon}</span>
            <span class="order-group-title" style="color:${g.color};">${g.label}</span>
            <span class="badge ${g.badge}">${gOrders.length}</span>
            ${g.collapsedByDefault && !isOpen && summaryText
              ? `<span style="font-size:0.72rem;color:var(--neutral-400);margin-left:4px;">${summaryText}</span>`
              : ''}
            ${g.collapsedByDefault
              ? `<span style="font-size:0.68rem;color:${g.color};opacity:0.8;margin-left:auto;margin-right:8px;font-weight:600;">${isOpen ? 'Click to hide' : 'Click to show'}</span>`
              : ''}
            <i class="fa-regular fa-chevron-down order-group-chevron${isOpen ? '' : ' collapsed'}" id="chevg_${gId}"></i>
          </div>
          <div id="${gId}" class="order-group-body" style="display:${isOpen ? 'block' : 'none'};">`;

          // Only render card HTML when the group is open (lazy rendering for performance)
          if (isOpen) {
            gOrders.forEach(order => {
              const balance = order.totalLiters - order.suppliedTotal;
              const progress = (order.suppliedTotal / order.totalLiters) * 100;
              const isNearly = progress >= 90 && progress < 100;
              const hasAllocations = Object.keys(order.allocations || {}).length > 0;
              const hasOverage = g.key === 'Overage';
              
              let statusClass, statusText, statusBadge;
              if (!hasAllocations) {
                statusClass = 'status-unassigned';
                statusText = 'Unassigned';
                statusBadge = 'badge-neutral';
              } else if (hasOverage) {
                statusClass = 'status-over';
                statusText = 'Overage';
                statusBadge = 'badge-danger';
              } else if (balance <= 0) {
                statusClass = 'status-closed';
                statusText = 'Closed';
                statusBadge = 'badge-warning';
              } else {
                statusClass = 'status-open';
                statusText = 'Open';
                statusBadge = 'badge-success';
              }
              
              const nearlyClass = isNearly ? ' nearly-full' : '';
              
              html += `<div class="order-card${nearlyClass}" data-order-no="${order.orderNo}">
                <div class="order-header" onclick="toggleOrderBody('${order.orderNo}')">
                  <div class="order-status-indicator ${statusClass}"></div>
                  <div class="order-info">
                    <div class="order-title">${order.orderNo}</div>
                    <div class="order-meta">
                      <span data-col="orders-vehicle"><i class="fa-regular fa-truck"></i> ${order.vehiclePlate}</span>
                      <span data-col="orders-date"><i class="fa-regular fa-calendar"></i> ${order.createdDate || '—'}</span>
                      <span data-col="orders-techs"><i class="fa-regular fa-users"></i> ${hasAllocations ? Object.keys(order.allocations || {}).length + ' techs' : 'Unassigned'}</span>
                      ${isNearly ? '<span class="text-warning-700 font-semibold">⚠️ Nearly full</span>' : ''}
                    </div>
                  </div>
                  <div class="order-stats">
                    <div data-col="orders-progress" class="order-progress">
                      <div class="progress-bar">
                        <div class="progress-fill ${!hasAllocations ? '' : (progress >= 100 ? 'warning' : isNearly ? 'warning' : progress >= 75 ? 'success' : 'info')}" style="width: ${hasAllocations ? progress : 0}%;"></div>
                      </div>
                      <div class="text-sm text-center mt-1">
                        <span data-col="orders-supplied">${order.suppliedTotal}</span>/<span data-col="orders-total">${order.totalLiters}</span>L
                        (<span data-col="orders-balance">${balance}L left</span>)
                      </div>
                    </div>
                    <span data-col="orders-status" class="badge ${statusBadge}">${statusText}</span>
                  </div>
                  <i class="fa-regular fa-chevron-down order-chevron" id="chev_${order.orderNo}"></i>
                </div>
                <div class="order-body" id="body_${order.orderNo}" style="display: none;">
                  ${renderOrderDetails(order)}
                </div>
              </div>`;
            });
          }
          
          html += '</div>';
        });
      } else if (carriedOrders.length === 0) {
        html += renderEmptyState('orders', 'Create Order', 'toggleOrderForm()');
      }
      
      container.innerHTML = html;
      applyColVisibility('orders');
    }

    function toggleOrderGroup(gId) {
      const body = document.getElementById(gId);
      const chev = document.getElementById('chevg_' + gId);
      if (!body) return;
      const isHidden = body.style.display === 'none';
      const nowOpen = isHidden;
      body.style.display = nowOpen ? 'block' : 'none';
      if (chev) chev.classList.toggle('collapsed', !nowOpen);

      // Persist state for lazy groups (Unassigned / Closed)
      const key = gId.replace('group_', '');
      const stateKey = '_grpOpen_' + key;
      window[stateKey] = nowOpen;

      // Lazy-render: if opening a collapsed group that has no cards yet, re-render the list
      // so cards get injected. Only needed for groups that were hidden by default.
      if (nowOpen && body.children.length === 0) {
        renderOrdersList();
      }
    }

    function toggleOrderBody(orderNo) {
      const body = document.getElementById(`body_${orderNo}`);
      const chev = document.getElementById(`chev_${orderNo}`);
      
      if (body.style.display === 'none') {
        body.style.display = 'block';
        chev.style.transform = 'rotate(180deg)';
      } else {
        body.style.display = 'none';
        chev.style.transform = 'rotate(0)';
      }
    }

    function toggleCycleFullscreen() {
      const container = document.getElementById('viewCycleModalContainer');
      const icon      = document.getElementById('cycleExpandIcon');
      const label     = document.getElementById('cycleExpandLabel');
      const overlay   = document.getElementById('viewCycleModal');
      if (!container) return;

      const isFullscreen = container.dataset.fullscreen === '1';
      if (isFullscreen) {
        // Restore
        container.dataset.fullscreen = '0';
        container.style.maxWidth   = '960px';
        container.style.width      = '95vw';
        container.style.maxHeight  = '92vh';
        container.style.height     = '';
        container.style.borderRadius = '';
        overlay.style.alignItems   = '';
        icon.className  = 'fa-regular fa-expand';
        label.textContent = 'Expand';
      } else {
        // Fullscreen
        container.dataset.fullscreen = '1';
        container.style.maxWidth   = '100vw';
        container.style.width      = '100vw';
        container.style.maxHeight  = '100vh';
        container.style.height     = '100vh';
        container.style.borderRadius = '0';
        overlay.style.alignItems   = 'flex-start';
        icon.className  = 'fa-regular fa-compress';
        label.textContent = 'Compress';
      }
    }

    function toggleCarriedDetail(cardId) {
      const panel = document.getElementById(cardId);
      if (!panel) return;
      // chevron id is 'chev_carried_' + the safe orderNo suffix stored in cardId
      const suffix = cardId.replace('carried_detail_', '');
      const chev = document.getElementById('chev_carried_' + suffix);
      const isHidden = panel.style.display === 'none';
      panel.style.display = isHidden ? 'block' : 'none';
      if (chev) chev.style.transform = isHidden ? 'rotate(180deg)' : 'rotate(0deg)';
    }

    function applyCarriedFilters() {
      window._carriedTechFilter = document.getElementById('carriedTechFilter')?.value || '';
      window._carriedDateFrom   = document.getElementById('carriedDateFrom')?.value   || '';
      window._carriedDateTo     = document.getElementById('carriedDateTo')?.value     || '';
      renderOrdersList();
    }

    function clearCarriedFilters() {
      window._carriedTechFilter = '';
      window._carriedDateFrom   = '';
      window._carriedDateTo     = '';
      renderOrdersList();
    }

    function renderOrderDetails(order) {
      const region = DB.regions[DB.currentRegion];
      let html = '<div class="mb-4">';
      
      const hasAllocations = Object.keys(order.allocations || {}).length > 0;
      
      if (hasAllocations) {
        const allocEntries = Object.entries(order.allocations || {});
        allocEntries.forEach(([tech, alloc]) => {
          const supplied = Object.values(region.dailyLog).flat()
            .filter(e => e.orderNo === order.orderNo && e.technician === tech)
            .reduce((s, e) => s + e.supplied, 0);
          const remaining = alloc - supplied;
          const isOver = supplied > alloc;
          
          html += `
            <div class="tech-alloc-row" draggable="true" data-tech="${tech}" data-order="${order.orderNo}"
                 ondragstart="allocDragStart(event,'${order.orderNo}','${tech}')"
                 ondragover="allocDragOver(event)" ondrop="allocDrop(event)" ondragleave="allocDragLeave(event)">
              <span class="drag-handle"><i class="fa-regular fa-grip-dots-vertical"></i></span>
              ${techAvatarHtml(tech)}
              <div class="tech-details">
                <div class="tech-name">${tech}</div>
                <div class="tech-plate">${region.technicianPlates[tech] || '—'}</div>
                <div class="tech-stats">
                  <span class="stat-badge" style="background: var(--info-100); color: var(--info-700);">Alloc: ${alloc}L</span>
                  <span class="stat-badge" style="background: var(--success-100); color: var(--success-700);">Supplied: ${supplied}L</span>
                  <span class="stat-badge" style="background: ${isOver ? 'var(--danger-100)' : 'var(--warning-100)'}; color: ${isOver ? 'var(--danger-700)' : 'var(--warning-700)'};">${isOver ? '+' + (supplied - alloc).toFixed(1) + 'L over' : remaining + 'L left'}</span>
                </div>
                ${order.overageComments && order.overageComments[tech] ? `<div class="text-sm mt-1 text-danger-700">💬 ${order.overageComments[tech]}</div>` : ''}
                
                <div class="flex gap-2 mt-2">
                  <button class="btn btn-ghost btn-sm text-danger-700" onclick="unassignFuel('${order.orderNo}', '${tech}')">
                    <i class="fa-regular fa-user-slash"></i> Unassign
                  </button>
                  <div class="select-wrapper" style="width: 140px;">
                    <select class="select-field btn-sm" onchange="reassignFuel('${order.orderNo}', '${tech}', this.value); this.value='';">
                      <option value="">Reassign to...</option>
                      ${region.technicians.filter(t => t !== tech && !order.allocations[t]).map(t => `<option value="${t}">${t}</option>`).join('')}
                    </select>
                  </div>
                </div>
              </div>
              <div class="flex gap-2">
                <button class="btn btn-icon btn-ghost btn-sm" onclick="editAllocation('${order.orderNo}', '${tech}')">
                  <i class="fa-regular fa-pen"></i>
                </button>
              </div>
            </div>
          `;
        });
      } else {
        const comment = region.unassignedComments?.[order.orderNo] || '';
        html += `
          <div class="unassign-comment-section">
            <div class="flex items-center justify-between mb-2">
              <span class="font-semibold">Unassigned Order Notes</span>
              <div class="flex gap-2">
                <button class="btn btn-ghost btn-sm" onclick="openUnassignedCommentModal('${order.orderNo}')">
                  <i class="fa-regular fa-pen"></i> ${comment ? 'Edit' : 'Add'} Comment
                </button>
                ${comment ? `
                <button class="btn btn-ghost btn-sm text-danger-700" onclick="deleteUnassignedComment('${order.orderNo}')">
                  <i class="fa-regular fa-trash"></i>
                </button>` : ''}
              </div>
            </div>
            ${comment ? `
            <div class="unassign-comment-display">
              <i class="fa-regular fa-message"></i>
              <span>${comment}</span>
            </div>` : `
            <div class="text-neutral-400 text-sm italic p-2">No comment added yet. Click "Add Comment" to add notes.</div>`}
          </div>
        `;
      }
      
      html += `
        <div class="mt-4 pt-4 border-t border-neutral-200">
          <div class="flex gap-2 justify-end">
            <button class="btn btn-secondary btn-sm" onclick="cloneOrder('${order.orderNo}')">
              <i class="fa-regular fa-copy"></i> Clone
            </button>
            <button class="btn btn-secondary btn-sm" onclick="editOrderDate('${order.orderNo}')">
              <i class="fa-regular fa-pen"></i> Edit Date
            </button>
            <button class="btn btn-primary btn-sm" onclick="editOrder('${order.orderNo}')">
              <i class="fa-regular fa-pen-to-square"></i> Edit Order
            </button>
            <button class="btn btn-secondary btn-sm" onclick="deleteOrder('${order.orderNo}')">
              <i class="fa-regular fa-trash"></i> Delete
            </button>
          </div>
        </div>
      `;
      return html;
    }

    // ===== ALLOCATION DRAG AND DROP =====
    let allocDragSrcTech = null;
    
    function allocDragStart(e, orderNo, tech) {
      allocDragSrcTech = tech;
      e.dataTransfer.effectAllowed = 'move';
      e.dataTransfer.setData('text/plain', tech);
    }
    
    function allocDragOver(e) {
      e.preventDefault();
      e.dataTransfer.dropEffect = 'move';
      const row = e.target.closest('.tech-alloc-row[data-tech]');
      if (row) row.classList.add('drag-over');
    }
    
    function allocDragLeave(e) {
      const row = e.target.closest('.tech-alloc-row[data-tech]');
      if (row) row.classList.remove('drag-over');
    }
    
    function allocDrop(e) {
      e.preventDefault();
      const row = e.target.closest('.tech-alloc-row[data-tech]');
      if (row) row.classList.remove('drag-over');
      
      const destTech = row?.dataset.tech;
      const orderNo = row?.dataset.order;
      
      if (!allocDragSrcTech || allocDragSrcTech === destTech || !orderNo) return;
      
      const region = DB.regions[DB.currentRegion];
      const order = region.orders[orderNo];
      if (!order) return;
      
      const entries = Object.entries(order.allocations);
      const srcIdx = entries.findIndex(([k]) => k === allocDragSrcTech);
      const destIdx = entries.findIndex(([k]) => k === destTech);
      
      if (srcIdx < 0 || destIdx < 0) return;
      
      const [moved] = entries.splice(srcIdx, 1);
      entries.splice(destIdx, 0, moved);
      order.allocations = Object.fromEntries(entries);
      
      allocDragSrcTech = null;
      save();
      renderOrdersList();
      showToast('Allocation order updated', 'info', 1500);
    }

    function editAllocation(orderNo, tech) {
      const region = DB.regions[DB.currentRegion];
      const order = region.orders[orderNo];
      const newAlloc = prompt('Enter new allocation amount (litres):', order.allocations[tech]);
      
      if (newAlloc === null) return;
      
      const amount = parseFloat(newAlloc);
      if (isNaN(amount) || amount < 0) return showToast('Please enter a valid number', 'warning');
      
      const otherTotal = Object.entries(order.allocations)
        .filter(([t]) => t !== tech)
        .reduce((s, [,v]) => s + v, 0);
      
      if (otherTotal + amount > order.totalLiters) {
        return showToast('Total allocations would exceed order total', 'error');
      }
      
      order.allocations[tech] = amount;
      save();
      renderOrdersList();
      showToast('Allocation updated', 'success', 1500);
    }

    function editOrderDate(orderNo) {
      const region = DB.regions[DB.currentRegion];
      const order = region.orders[orderNo];
      const newDate = prompt('Enter new date (YYYY-MM-DD):', order.createdDate);
      
      if (newDate) {
        order.createdDate = newDate;
        save();
        renderOrdersList();
        showToast('Order date updated', 'success', 1500);
      }
    }

    function deleteOrder(orderNo) {
      if (!confirm(`Delete order ${orderNo}?`)) return;
      
      const region = DB.regions[DB.currentRegion];
      
      Object.keys(region.dailyLog).forEach(date => {
        region.dailyLog[date] = region.dailyLog[date].filter(e => e.orderNo !== orderNo);
      });
      
      if (region.unassignedComments && region.unassignedComments[orderNo]) {
        delete region.unassignedComments[orderNo];
      }
      
      delete region.orders[orderNo];
      save();
      
      renderOrdersList();
      updateOrderStats();
      populateAllocOrder();
      showToast('Order deleted', 'info', 1500);
    }

    function cloneOrder(orderNo) {
      cloneSource = orderNo;
      const region = DB.regions[DB.currentRegion];
      const order = region.orders[orderNo];
      
      document.getElementById('clonePreview').innerHTML = `
        <div class="text-sm">
          <strong>Source:</strong> ${order.orderNo}<br>
          <strong>Vehicle:</strong> ${order.vehiclePlate}<br>
          <strong>Total:</strong> ${order.totalLiters}L<br>
          <strong>Allocations:</strong> ${Object.keys(order.allocations).length} technicians
        </div>
      `;
      
      document.getElementById('cloneOrderDate').value = new Date().toISOString().slice(0, 10);
      openModal('cloneModal');
    }

    function confirmClone() {
      if (!cloneSource) return;
      
      const region = DB.regions[DB.currentRegion];
      const source = region.orders[cloneSource];
      const newOrderNo = document.getElementById('cloneOrderNo').value.trim();
      const newDate = document.getElementById('cloneOrderDate').value;
      
      if (!newOrderNo) return showToast('Please enter new order number', 'warning');
      
      if (region.orders[newOrderNo]) {
        return showToast('Order number already exists', 'error');
      }
      
      region.orders[newOrderNo] = {
        orderNo: newOrderNo,
        vehiclePlate: source.vehiclePlate,
        totalLiters: source.totalLiters,
        suppliedTotal: 0,
        allocations: { ...source.allocations },
        status: 'OPEN',
        createdDate: newDate
      };
      
      save();
      closeModal('cloneModal');
      renderOrdersList();
      showToast('Order cloned successfully');
    }

    // ===== REGIONS PAGE =====
    function renderRegionsPage(container) {
      container.innerHTML = `
        <div class="stats-grid">
          <div class="stat-tile">
            <div class="stat-label">Total Regions</div>
            <div class="stat-value" id="regionCount">0</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Total Technicians</div>
            <div class="stat-value" id="techCount">0</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Total Orders</div>
            <div class="stat-value" id="regionOrderCount">0</div>
          </div>
        </div>

        <div class="card mb-4">
          <h3 class="text-lg font-semibold mb-4">Regions</h3>
          <div class="flex gap-2 mb-4">
            <div class="input-group flex-1">
              <input type="text" class="input-field" id="newRegion" placeholder=" ">
              <label class="input-label">New Region Name</label>
            </div>
            <button class="btn btn-primary" onclick="addRegion()">Add Region</button>
          </div>
          <div id="regionsList"></div>
        </div>

        <div class="card">
          <h3 class="text-lg font-semibold mb-4">Technicians</h3>
          <div class="grid grid-cols-2 gap-4 mb-4">
            <div class="input-group">
              <input type="text" class="input-field" id="techName" placeholder=" " list="techNameSuggestions" autocomplete="off"
                data-validate="required" oninput="liveValidate(this)">
              <label class="input-label">Technician Name</label>
              <div class="field-hint" id="techNameHint"></div>
              <datalist id="techNameSuggestions">
                ${[...TECH_MANAGER.allTechs].sort().map(t=>`<option value="${t}">`).join('')}
              </datalist>
            </div>
            <div class="input-group">
              <input type="text" class="input-field" id="techPlate" placeholder=" "
                data-validate="plate" oninput="liveValidate(this)">
              <label class="input-label">Vehicle Plate (optional)</label>
              <div class="field-hint" id="techPlateHint"></div>
            </div>
          </div>
          <button class="btn btn-primary w-full mb-2" onclick="addTechnician()">
            Add Technician
          </button>
          <button class="btn btn-secondary w-full mb-4" onclick="openBulkTechImportModal()">
            <i class="fa-regular fa-users-gear"></i> Bulk Import from Master Data
          </button>
          <div id="techListContainer"></div>
        </div>
      `;

      renderRegionsList();
      renderTechList();
      updateRegionStats();
    }

    function renderRegionsList() {
      const container = document.getElementById('regionsList');
      if (!container) return;
      
      let html = '';
      Object.keys(DB.regions).forEach(r => {
        const isCurrent = r === DB.currentRegion;
        const techCount = DB.regions[r].technicians.length;
        const orderCount = Object.keys(DB.regions[r].orders).length;
        
        html += `
          <div class="tech-alloc-row">
            <div class="tech-avatar" style="background: var(--accent-100); color: var(--accent-700);">
              <i class="fa-regular fa-building"></i>
            </div>
            <div class="tech-details">
              <div class="tech-name">${r} ${isCurrent ? '(Current)' : ''}</div>
              <div class="tech-plate">${techCount} technicians · ${orderCount} orders</div>
            </div>
            <div class="tech-stats">
              <button class="btn btn-icon btn-ghost btn-sm" onclick="openRenameRegion('${r}')">
                <i class="fa-regular fa-pen"></i>
              </button>
              <button class="btn btn-icon btn-ghost btn-sm" onclick="deleteRegion('${r}')">
                <i class="fa-regular fa-trash"></i>
              </button>
              ${!isCurrent ? 
                `<button class="btn btn-secondary btn-sm" onclick="switchRegion('${r}')">Switch</button>` : 
                ''}
            </div>
          </div>
        `;
      });
      
      container.innerHTML = html;
      document.getElementById('regionCount').textContent = Object.keys(DB.regions).length;
    }

    function renderTechList() {
      const container = document.getElementById('techListContainer');
      if (!container) return;
      
      const region = DB.regions[DB.currentRegion];
      
      if (!region.technicians.length) {
        container.innerHTML = renderEmptyState('tech', 'Add Technician', 'addTechnician()');
        return;
      }
      
      let html = '';
      region.technicians.forEach(t => {
        const tc = techColor(t);
        html += `
          <div class="tech-alloc-row">
            ${techAvatarHtml(t)}
            <div class="tech-details">
              <div class="tech-name">${t}</div>
              <div class="tech-plate">${region.technicianPlates[t] || '—'}</div>
            </div>
            <div class="tech-stats">
              <button class="btn btn-icon btn-ghost btn-sm" onclick="openRenameTech('${t}')">
                <i class="fa-regular fa-pen"></i>
              </button>
              <button class="btn btn-icon btn-ghost btn-sm" onclick="deleteTech('${t}')">
                <i class="fa-regular fa-trash"></i>
              </button>
            </div>
          </div>
        `;
      });
      
      container.innerHTML = html;
    }

    function updateRegionStats() {
      let totalTechs = 0;
      let totalOrders = 0;
      
      Object.values(DB.regions).forEach(r => {
        totalTechs += r.technicians.length;
        totalOrders += Object.keys(r.orders).length;
      });
      
      animateCounter(document.getElementById('techCount'), totalTechs, '');
      animateCounter(document.getElementById('regionOrderCount'), totalOrders, '');
    }

    function addRegion() {
      const name = document.getElementById('newRegion').value.trim();
      if (!name) return showToast('Please enter a region name', 'warning');
      
      if (DB.regions[name]) return showToast('Region already exists', 'error');
      
      DB.regions[name] = { technicians: [], technicianPlates: {}, orders: {}, dailyLog: {}, monthlyTarget: null, techMonthlyTargets: {}, unassignedComments: {} };
      document.getElementById('newRegion').value = '';
      
      save();
      renderRegionsList();
      populateRegions();
      showToast('Region added');
    }

    function switchRegion(name) {
      DB.currentRegion = name;
      save();
      populateRegions();
      renderPageWithTransition(currentPage);
      showToast(`Switched to ${name}`);
    }

    function deleteRegion(name) {
      if (Object.keys(DB.regions).length <= 1) {
        return showToast('Cannot delete the only region', 'warning');
      }
      
      if (!confirm(`Delete region ${name}?`)) return;
      
      delete DB.regions[name];
      
      if (DB.currentRegion === name) {
        DB.currentRegion = Object.keys(DB.regions)[0];
      }
      
      save();
      renderRegionsList();
      populateRegions();
      showToast('Region deleted', 'info', 1500);
    }

    function openRenameRegion(name) {
      renameContext = { type: 'region', name };
      document.getElementById('renameTitle').textContent = `Rename Region: ${name}`;
      document.getElementById('renameInput').value = name;
      openModal('renameModal');
    }

    function openRenameTech(name) {
      renameContext = { type: 'tech', name };
      document.getElementById('renameTitle').textContent = `Rename Technician: ${name}`;
      document.getElementById('renameInput').value = name;
      openModal('renameModal');
    }

    function confirmRename() {
      if (!renameContext) return;
      
      const newName = document.getElementById('renameInput').value.trim();
      if (!newName) return showToast('Please enter a name', 'warning');
      
      if (renameContext.type === 'region') {
        const oldName = renameContext.name;
        if (newName === oldName) {
          closeModal('renameModal');
          return;
        }
        
        if (DB.regions[newName]) return showToast('Region already exists', 'error');
        
        DB.regions[newName] = DB.regions[oldName];
        delete DB.regions[oldName];
        
        if (DB.currentRegion === oldName) {
          DB.currentRegion = newName;
        }
      } else {
        const oldName = renameContext.name;
        
        Object.values(DB.regions).forEach(r => {
          const idx = r.technicians.indexOf(oldName);
          if (idx !== -1) {
            r.technicians[idx] = newName;
          }
          
          if (r.technicianPlates[oldName]) {
            r.technicianPlates[newName] = r.technicianPlates[oldName];
            delete r.technicianPlates[oldName];
          }
          
          Object.values(r.orders).forEach(o => {
            if (o.allocations && o.allocations[oldName]) {
              o.allocations[newName] = o.allocations[oldName];
              delete o.allocations[oldName];
            }
            
            if (o.overageComments && o.overageComments[oldName]) {
              o.overageComments[newName] = o.overageComments[oldName];
              delete o.overageComments[oldName];
            }
          });
          
          Object.values(r.dailyLog).forEach(entries => {
            entries.forEach(e => {
              if (e.technician === oldName) e.technician = newName;
            });
          });
        });
      }
      
      save();
      closeModal('renameModal');
      renderPageWithTransition(currentPage);
      showToast('Renamed successfully');
    }

    function addTechnician() {
      const name = document.getElementById('techName').value.trim();
      const plate = document.getElementById('techPlate').value.trim();
      
      if (!name) return showToast('Please enter a technician name', 'warning');
      
      const region = DB.regions[DB.currentRegion];
      
      if (region.technicians.includes(name)) {
        return showToast('Technician already exists', 'error');
      }
      
      region.technicians.push(name);
      if (plate) region.technicianPlates[name] = plate;
      
      document.getElementById('techName').value = '';
      document.getElementById('techPlate').value = '';
      
      save();
      renderTechList();
      populateAllocTech();
      showToast('Technician added');
    }

    function deleteTech(name) {
      if (!confirm(`Remove technician ${name}?`)) return;
      
      const region = DB.regions[DB.currentRegion];
      
      region.technicians = region.technicians.filter(t => t !== name);
      delete region.technicianPlates[name];
      
      Object.values(region.orders).forEach(o => {
        delete o.allocations[name];
      });
      
      save();
      renderTechList();
      populateAllocTech();
      showToast('Technician removed', 'info', 1500);
    }

    // ===== REPORTS PAGE =====
    function renderReportsPage(container) {
      const region = DB.regions[DB.currentRegion];
      
      const now = new Date();
      const days = Array.from({length:14}, (_,i) => {
        const d = new Date(now); d.setDate(d.getDate()-13+i);
        return d.toISOString().slice(0,10);
      });
      
      const chartData = days.map(d => {
        const entries = region.dailyLog[d] || [];
        return entries.filter(e => !e.unallocated).reduce((s, e) => s + e.supplied, 0);
      });
      const hasChartData = chartData.some(v=>v>0);

      const techTotals = {};
      Object.values(region.dailyLog).flat().forEach(e => {
        if (!e.unallocated) techTotals[e.technician] = (techTotals[e.technician]||0)+e.supplied;
      });
      const techNames = Object.keys(techTotals).sort((a,b)=>techTotals[b]-techTotals[a]).slice(0,8);
      const hasTechData = techNames.length > 0;

      // Compute propagated field totals
      const allEntries = Object.values(region.dailyLog).flat();
      const totalDgHours    = allEntries.reduce((s,e) => s + (e.dgHoursUsed    || 0), 0);
      const totalDieselUsed = allEntries.reduce((s,e) => s + (e.dieselConsumed || 0), 0);
      const sitesWithData   = new Set(allEntries.filter(e=>e.siteId).map(e=>e.siteId.toUpperCase())).size;
      const hasPropagated   = totalDgHours > 0 || totalDieselUsed > 0;

      container.innerHTML = `
        <div class="stats-grid">
          <div class="stat-tile">
            <div class="stat-label">Export Options</div>
            <div class="flex gap-2 mt-2">
              <button class="btn btn-primary btn-sm" onclick="exportOrders()">
                <i class="fa-regular fa-file-excel"></i> Excel
              </button>
              <button class="btn btn-secondary btn-sm" onclick="backupData()">
                <i class="fa-regular fa-cloud-arrow-up"></i> Backup
              </button>
              <button class="btn btn-secondary btn-sm" onclick="openTargetModal()">
                <i class="fa-regular fa-bullseye"></i> Monthly Target
              </button>
            </div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Unallocated Total</div>
            <div class="stat-value text-warning-700" id="unallocTotal">0L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label" style="color:var(--status-info);">⚡ DG Hours Used</div>
            <div class="stat-value" style="color:var(--status-info);">${totalDgHours > 0 ? totalDgHours.toFixed(1)+'h' : '—'}</div>
            <div class="text-xs mt-1" style="color:var(--neutral-400);">${sitesWithData} sites tracked</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label" style="color:var(--status-warning);">🔥 Diesel Consumed</div>
            <div class="stat-value" style="color:var(--status-warning);">${totalDieselUsed > 0 ? totalDieselUsed.toFixed(0)+'L' : '—'}</div>
            <div class="text-xs mt-1" style="color:var(--neutral-400);">
              ${hasPropagated
                ? `<button class="btn btn-ghost btn-sm" style="font-size:10px;padding:2px 8px;" onclick="openPropagationModal()">Run again</button>`
                : `<button class="btn btn-ghost btn-sm" style="font-size:10px;padding:2px 8px;" onclick="openPropagationModal()">Run propagation</button>`}
            </div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Restore Backup</div>
            <label class="btn btn-secondary btn-sm mt-2 cursor-pointer">
              <i class="fa-regular fa-folder-open"></i> Choose File
              <input type="file" accept=".json" style="display: none;" onchange="restoreData(event)">
            </label>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-4 mb-4">
          <div class="card">
            <h3 class="text-lg font-semibold mb-4">Allocated Supply — Last 14 Days</h3>
            ${hasChartData
              ? `<div class="chart-wrapper"><canvas id="supplyChart" height="180"></canvas></div>`
              : `<div class="chart-empty-state">${renderEmptyState('daily', 'Add Entry', 'setPage(\'daily\', null)')}</div>`
            }
          </div>
          <div class="card">
            <h3 class="text-lg font-semibold mb-4">Technician Totals (Allocated Only)</h3>
            ${hasTechData
              ? `<div class="chart-wrapper"><canvas id="techChart" height="180"></canvas></div>`
              : `<div class="chart-empty-state">${renderEmptyState('leaderboard', 'View Leaderboard', 'setPage(\'leaderboard\', null)')}</div>`
            }
          </div>
        </div>

        <div class="card mb-4">
          <h3 class="text-lg font-semibold mb-4">Unallocated Supply Log (Not Tracked in Balance)</h3>
          <div id="unallocReportContainer"></div>
        </div>
      `;

      renderUnallocReport();

      if (hasChartData && document.getElementById('supplyChart')) {
        new Chart(document.getElementById('supplyChart'), {
          type: 'bar',
          data: {
            labels: days.map(d => new Date(d).toLocaleDateString('en-GB',{day:'2-digit',month:'short'})),
            datasets: [{
              label: 'Litres Supplied (Allocated)',
              data: chartData,
              backgroundColor: 'rgba(196,30,58,0.18)',
              borderColor: 'rgba(196,30,58,0.8)',
              borderWidth: 1.5,
              borderRadius: 6,
              borderSkipped: false,
            }]
          },
          options: {
            animation: { duration: 900, easing: 'easeInOutQuart' },
            responsive: true, maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                backgroundColor: 'rgba(26,38,52,0.92)',
                titleColor: '#fff', bodyColor: '#e2e8f0',
                padding: 10, cornerRadius: 8,
                callbacks: { label: ctx => ` ${ctx.raw}L allocated supply` }
              }
            },
            scales: {
              x: { grid: { display: false }, ticks: { font: { size: 11 } } },
              y: { grid: { color: 'rgba(0,0,0,0.05)' }, ticks: { callback: v => v + 'L' } }
            }
          }
        });
      }

      if (hasTechData && document.getElementById('techChart')) {
        const palette = ['#3D8662','#4F86B0','#C23B4C','#D47A3E','#6b3a9b','#3a809b','#9b3a7a','#5a9b3a'];
        new Chart(document.getElementById('techChart'), {
          type: 'doughnut',
          data: {
            labels: techNames,
            datasets: [{
              data: techNames.map(t => techTotals[t]),
              backgroundColor: palette.slice(0, techNames.length).map(c => c + 'cc'),
              borderColor: palette.slice(0, techNames.length),
              borderWidth: 2,
            }]
          },
          options: {
            animation: { animateRotate: true, duration: 900, easing: 'easeInOutQuart' },
            responsive: true, maintainAspectRatio: false,
            plugins: {
              legend: { position: 'right', labels: { font: { size: 12 }, boxWidth: 12 } },
              tooltip: {
                backgroundColor: 'rgba(26,38,52,0.92)',
                titleColor: '#fff', bodyColor: '#e2e8f0',
                padding: 10, cornerRadius: 8,
                callbacks: { label: ctx => ` ${ctx.label}: ${ctx.raw}L (allocated)` }
              }
            }
          }
        });
      }
    }

    function renderUnallocReport() {
      const container = document.getElementById('unallocReportContainer');
      if (!container) return;
      
      const region = DB.regions[DB.currentRegion];
      const entries = [];
      let total = 0;
      
      Object.entries(region.dailyLog).forEach(([date, dayEntries]) => {
        dayEntries.filter(e => e.unallocated).forEach(e => {
          entries.push({ date, ...e });
          total += e.supplied;
        });
      });
      
      animateCounter(document.getElementById('unallocTotal'), total, 'L');
      
      if (!entries.length) {
        container.innerHTML = `
          <div class="empty-state">
            <i class="fa-regular fa-circle-check text-3xl"></i>
            <h3 class="text-lg font-semibold mt-4">No unallocated entries</h3>
            <p class="text-sm text-neutral-500 mt-2">All fuel supplies are properly allocated</p>
          </div>
        `;
        return;
      }
      
      entries.sort((a, b) => b.date.localeCompare(a.date));
      
      let html = '';
      entries.forEach(e => {
        html += `
          <div class="tech-alloc-row">
            <div class="tech-avatar" style="background: var(--warning-100); color: var(--warning-700);">
              <i class="fa-regular fa-triangle-exclamation"></i>
            </div>
            <div class="tech-details">
              <div class="tech-name">${e.technician}</div>
              <div class="tech-plate">${e.date} · ${e.comment || 'No comment'}</div>
            </div>
            <div class="tech-stats">
              <span class="stat-badge" style="background: var(--warning-100); color: var(--warning-700);">
                ${e.supplied}L
              </span>
            </div>
          </div>
        `;
      });
      
      container.innerHTML = html;
    }

    // ===== LEADERBOARD PAGE =====
    function renderLeaderboardPage(container) {
      container.innerHTML = `
        <div class="stats-grid">
          <div class="stat-tile">
            <div class="stat-label">Top Technician</div>
            <div class="stat-value text-2xl" id="topPerformer">—</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Total Allocated</div>
            <div class="stat-value text-success-700" id="leaderboardTotal">0L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Active Techs</div>
            <div class="stat-value" id="activeTechs">0</div>
          </div>
        </div>

        <div class="card">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold">Technician Leaderboard</h3>
            <div class="flex gap-2 flex-wrap items-center">
              <button class="btn btn-secondary btn-sm" onclick="openTechTargetModal()">
                <i class="fa-regular fa-bullseye"></i> Set Targets
              </button>
              <div class="select-wrapper" style="width: 140px;">
                <select class="select-field" id="lbRegionFilter" onchange="renderLeaderboardList()">
                  <option value="">All Regions</option>
                </select>
              </div>
              <div class="select-wrapper" style="width: 140px;">
                <select class="select-field" id="lbDateFilter" onchange="renderLeaderboardList()">
                  <option value="0">All Time</option>
                  <option value="7">Last 7 Days</option>
                  <option value="30">Last 30 Days</option>
                  <option value="90">Last 90 Days</option>
                </select>
              </div>
              <span id="lbDensityToggle"></span>
            </div>
          </div>
          <div id="leaderboardListContainer"></div>
        </div>
      `;

      populateLbRegionFilter();
      renderLeaderboardList();
      const lbDt = document.getElementById('lbDensityToggle');
      if (lbDt) lbDt.innerHTML = renderDensityToggle();
    }

    function populateLbRegionFilter() {
      const sel = document.getElementById('lbRegionFilter');
      if (!sel) return;
      
      const current = sel.value;
      sel.innerHTML = '<option value="">All Regions</option>';
      Object.keys(DB.regions).forEach(r => {
        const opt = document.createElement('option');
        opt.value = r;
        opt.textContent = r;
        sel.appendChild(opt);
      });
      if (current) sel.value = current;
    }

    function renderLeaderboardList() {
      const container = document.getElementById('leaderboardListContainer');
      if (!container) return;
      
      const regionFilter = document.getElementById('lbRegionFilter')?.value;
      const dayFilter = parseInt(document.getElementById('lbDateFilter')?.value) || 0;
      const cutoff = dayFilter ? new Date(Date.now() - dayFilter * 86400000).toISOString().slice(0, 10) : null;
      
      const techData = {};
      let totalLitres = 0;
      
      Object.entries(DB.regions).forEach(([rName, r]) => {
        if (regionFilter && rName !== regionFilter) return;
        
        Object.entries(r.dailyLog).forEach(([date, entries]) => {
          if (cutoff && date < cutoff) return;
          
          entries.forEach(e => {
            if (!e.unallocated) {
              if (!techData[e.technician]) {
                techData[e.technician] = { litres: 0, region: rName };
              }
              techData[e.technician].litres += e.supplied;
              totalLitres += e.supplied;
            }
          });
        });
      });
      
      const sorted = Object.entries(techData).sort((a, b) => b[1].litres - a[1].litres);
      
      animateCounter(document.getElementById('leaderboardTotal'), totalLitres, 'L');
      animateCounter(document.getElementById('activeTechs'), sorted.length, '');
      
      document.getElementById('topPerformer').textContent = sorted[0]?.[0] || '—';
      
      if (!sorted.length) {
        container.innerHTML = renderEmptyState('leaderboard', 'Add Entries', 'setPage(\'daily\', null)');
        return;
      }
      
      const max = sorted[0][1].litres;
      
      let html = '';
      sorted.forEach(([tech, data], idx) => {
        const percentage = (data.litres / max) * 100;
        const rankClass = idx === 0 ? 'rank-1' : idx === 1 ? 'rank-2' : idx === 2 ? 'rank-3' : '';
        
        const techTarget = Object.values(DB.regions).reduce((t, r) => t || (r.techMonthlyTargets && r.techMonthlyTargets[tech]), null);
        const targetPctLb = techTarget ? Math.min(100, (data.litres/techTarget)*100) : null;
        const colorLb = techColor(tech);
        
        html += `
          <div class="leaderboard-card" onclick="openTechHistory('${tech}')">
            <div class="rank-badge ${rankClass}">${idx + 1}</div>
            <div class="tech-details" style="flex: 1;">
              <div class="tech-name flex items-center gap-2">
                ${techAvatarHtml(tech, 'style="width:28px;height:28px;font-size:0.75rem;"')}
                ${tech}
              </div>
              <div class="tech-plate"> ${data.region}</div>
              <div class="lb-bar-container mt-2">
                <div class="lb-bar-fill" style="width: ${percentage}%;"></div>
              </div>
              ${targetPctLb !== null ? `<div class="mt-1 text-xs text-neutral-500">Target: <span class="font-semibold ${targetPctLb>=100?'text-success-700':'text-warning-700'};">${targetPctLb.toFixed(0)}%</span> of ${techTarget}L</div>` : ''}
            </div>
            <div class="stat-value text-xl">${data.litres.toFixed(1)}L</div>
          </div>
        `;
      });
      
      container.innerHTML = html;
    }

    function openTechHistory(tech) {
      const entries = [];
      
      Object.entries(DB.regions).forEach(([rName, r]) => {
        Object.entries(r.dailyLog).forEach(([date, dayEntries]) => {
          dayEntries.filter(e => e.technician === tech).forEach(e => {
            entries.push({ ...e, date, region: rName });
          });
        });
      });
      
      entries.sort((a, b) => b.date.localeCompare(a.date));
      
      const allocatedEntries = entries.filter(e => !e.unallocated);
      const totalAllocated = allocatedEntries.reduce((s, e) => s + e.supplied, 0);
      const days = new Set(allocatedEntries.map(e => e.date)).size;
      const orders = new Set(allocatedEntries.filter(e => e.orderNo).map(e => e.orderNo)).size;
      
      document.getElementById('techHistoryTitle').textContent = `${tech} - History (Allocated Only)`;
      animateCounter(document.getElementById('techTotal'), totalAllocated, 'L');
      animateCounter(document.getElementById('techDays'), days, '');
      animateCounter(document.getElementById('techOrders'), orders, '');
      
      let html = '';
      entries.forEach(e => {
        html += `
          <div class="tech-alloc-row">
            ${techAvatarHtml(e.technician, e.unallocated ? 'style="background:var(--warning-100);color:var(--warning-700);"' : '')}
            <div class="tech-details">
              <div class="tech-name">${new Date(e.date).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })}</div>
              <div class="tech-plate">
                ${e.unallocated ? 'Unallocated' : 'Order: ' + e.orderNo} ·  ${e.region}
                ${e.comment ? ' · 💬 ' + e.comment : ''}
              </div>
            </div>
            <div class="tech-stats">
              <span class="stat-badge" style="background: ${e.unallocated ? 'var(--warning-100)' : 'var(--success-100)'}; color: ${e.unallocated ? 'var(--warning-700)' : 'var(--success-700)'};">
                ${e.supplied}L ${e.unallocated ? '(Unallocated)' : ''}
              </span>
            </div>
          </div>
        `;
      });
      
      document.getElementById('techHistoryList').innerHTML = html;
      openModal('techHistoryModal');
    }

    // ===== SUMMARY MODAL =====
    function openSummaryModal() {
      const date = document.getElementById('dailyDate').value;
      if (!date) return showToast('Please select a date', 'warning');

      const region = DB.regions[DB.currentRegion];
      const entries = region.dailyLog[date] || [];

      const assignedOrders = Object.values(region.orders).filter(o => Object.keys(o.allocations || {}).length > 0);
      const totalOrderedAssigned = assignedOrders.reduce((s, o) => s + o.totalLiters, 0);
      const totalSuppliedAssigned = assignedOrders.reduce((s, o) => s + o.suppliedTotal, 0);
      const balanceAssigned = totalOrderedAssigned - totalSuppliedAssigned;

      const titleEl = document.getElementById('summaryModalTitle');
      if (titleEl) titleEl.textContent = 'Summary Report — ' + new Date(date).toLocaleDateString('en-GB', { weekday: 'long', day: '2-digit', month: 'long', year: 'numeric' });

      animateCounter(document.getElementById('summaryTotalOrdered'), totalOrderedAssigned, 'L');
      animateCounter(document.getElementById('summaryTotalSupplied'), totalSuppliedAssigned, 'L');
      animateCounter(document.getElementById('summaryBalance'), balanceAssigned, 'L');
      animateCounter(document.getElementById('summaryEntries'), entries.length, '');

      const techStats = {};
      const openOrders = Object.values(region.orders).filter(o =>
        Object.keys(o.allocations || {}).length > 0 && (o.totalLiters - o.suppliedTotal) > 0
      );

      openOrders.forEach(order => {
        Object.entries(order.allocations || {}).forEach(([tech, alloc]) => {
          if (!techStats[tech]) {
            techStats[tech] = { totalAllocated: 0, suppliedAllTime: 0, suppliedToday: 0, orders: [] };
          }
          const techSuppliedOnOrder = Object.values(region.dailyLog).flat()
            .filter(e => e.orderNo === order.orderNo && e.technician === tech && !e.unallocated)
            .reduce((s, e) => s + e.supplied, 0);

          techStats[tech].totalAllocated += alloc;
          techStats[tech].suppliedAllTime += techSuppliedOnOrder;
          techStats[tech].orders.push({ orderNo: order.orderNo, alloc, supplied: techSuppliedOnOrder });
        });
      });

      entries.filter(e => !e.unallocated).forEach(e => {
        if (techStats[e.technician]) {
          techStats[e.technician].suppliedToday += e.supplied;
        } else {
          techStats[e.technician] = techStats[e.technician] || { totalAllocated: 0, suppliedAllTime: 0, suppliedToday: 0, orders: [] };
          techStats[e.technician].suppliedToday += e.supplied;
        }
      });

      const sortedTechs = Object.entries(techStats).sort((a, b) => b[1].totalAllocated - a[1].totalAllocated);

      let techBreakdownHtml = '';
      if (sortedTechs.length > 0) {
        techBreakdownHtml = `
          <h4 class="text-lg font-semibold mb-3" style="display:flex;align-items:center;gap:8px;">
            <i class="fa-regular fa-users" style="color:var(--accent-600);"></i>
            Technician Open Order Totals
          </h4>
          <div class="table-container mb-2">
            <table class="table">
              <thead>
                <tr>
                  <th>Technician</th>
                  <th style="text-align:right;">Total Orders </th>
                  <th style="text-align:right;">Supplied Today </th>
                  <th style="text-align:right;">Total Supplied </th>
                  <th style="text-align:right;">Balance </th>
                </tr>
              </thead>
              <tbody>
        `;

        sortedTechs.forEach(([tech, s], i) => {
          const balance = s.totalAllocated - s.suppliedAllTime;
          const pct = s.totalAllocated > 0 ? Math.min(100, (s.suppliedAllTime / s.totalAllocated) * 100) : 0;
          const barColor = pct >= 100 ? 'var(--warning-600)' : pct >= 75 ? 'var(--success-600)' : pct >= 40 ? 'var(--info-600)' : 'var(--accent-500)';
          const c = techColor(tech);

          techBreakdownHtml += `
            <tr>
              <td>
                <div style="display:flex;align-items:center;gap:8px;">
                  ${techAvatarHtml(tech, 'style="width:30px;height:30px;font-size:0.8rem;"')}
                  <div>
                    <div style="font-weight:700;">${tech}</div>
                    <div style="font-size:0.7rem;color:var(--neutral-500);">${s.orders.length} open order${s.orders.length !== 1 ? 's' : ''}</div>
                    <div style="margin-top:4px;height:5px;background:var(--neutral-200);border-radius:999px;width:120px;overflow:hidden;">
                      <div style="height:100%;width:${pct}%;background:${barColor};border-radius:999px;"></div>
                    </div>
                  </div>
                </div>
              </td>
              <td style="text-align:right;"><span class="font-mono font-bold">${s.totalAllocated.toLocaleString()}L</span></td>
              <td style="text-align:right;"><span class="font-mono font-bold ${s.suppliedToday > 0 ? 'text-accent-700' : 'text-neutral-400'}">${s.suppliedToday > 0 ? '' : ''}${s.suppliedToday.toLocaleString()}L</span></td>
              <td style="text-align:right;"><span class="font-mono font-bold text-success-700">${s.suppliedAllTime.toLocaleString()}L</span></td>
              <td style="text-align:right;"><span class="font-mono font-bold ${balance <= 0 ? 'text-warning-700' : 'text-danger-700'}">${balance.toLocaleString()}L</span></td>
            </tr>
          `;
        });

        techBreakdownHtml += '</tbody></table></div>';
      } else {
        techBreakdownHtml = `<div class="p-4 text-neutral-400 text-sm">No open order allocations found for technicians.</div>`;
      }

      document.getElementById('summaryTechBreakdown').innerHTML = techBreakdownHtml;

      let html = '';
      entries.forEach(e => {
        html += `
          <tr>
            <td>${e.date || date}</td>
            <td>${e.technician}</td>
            <td>${e.orderNo || 'Unallocated'}</td>
            <td>${e.supplied}L</td>
            <td>
              <span class="badge ${e.unallocated ? 'badge-warning' : 'badge-success'}">
                ${e.unallocated ? 'Unallocated' : 'Allocated'}
              </span>
            </td>
          </tr>
        `;
      });

      document.getElementById('summaryTableBody').innerHTML = html || '<tr><td colspan="5" style="text-align:center;color:var(--neutral-400);">No entries for this date</td></tr>';
      openModal('summaryModal');
    }

    // ===== MULTI-DATE SUMMARY =====
    let multiDateSelection = [];

    function openMultiDateModal() {
      const region = DB.regions[DB.currentRegion];
      const dates = Object.keys(region.dailyLog).sort().reverse();
      
      let gridHtml = '';
      dates.forEach(date => {
        const checked = multiDateSelection.includes(date) ? 'checked' : '';
        gridHtml += `
          <label class="date-checkbox">
            <input type="checkbox" value="${date}" ${checked} onchange="updateMultiDateSelection(this)">
            ${new Date(date).toLocaleDateString('en-GB')}
          </label>
        `;
      });
      
      document.getElementById('dateGrid').innerHTML = gridHtml;
      updateMultiDateStats();
      openModal('multiDateModal');
    }

    function updateMultiDateSelection(checkbox) {
      if (checkbox.checked) {
        multiDateSelection.push(checkbox.value);
      } else {
        multiDateSelection = multiDateSelection.filter(d => d !== checkbox.value);
      }
      updateMultiDateStats();
    }

    function updateMultiDateStats() {
      const region = DB.regions[DB.currentRegion];
      let totalSupplied = 0;
      let totalEntries = 0;
      
      multiDateSelection.forEach(date => {
        const entries = region.dailyLog[date] || [];
        totalSupplied += entries.filter(e => !e.unallocated).reduce((s, e) => s + e.supplied, 0);
        totalEntries += entries.length;
      });
      
      document.getElementById('selectedDatesCount').textContent = multiDateSelection.length;
      animateCounter(document.getElementById('multiDateTotal'), totalSupplied, 'L');
      animateCounter(document.getElementById('multiDateEntries'), totalEntries, '');
    }

    function selectAllDates(select) {
      const checkboxes = document.querySelectorAll('#dateGrid input[type="checkbox"]');
      checkboxes.forEach(cb => {
        cb.checked = select;
        if (select) {
          if (!multiDateSelection.includes(cb.value)) multiDateSelection.push(cb.value);
        } else {
          multiDateSelection = [];
        }
      });
      updateMultiDateStats();
    }

    function generateMultiDateSummary() {
      if (multiDateSelection.length === 0) {
        return showToast('Please select at least one date', 'warning');
      }
      
      const region = DB.regions[DB.currentRegion];
      const allEntries = [];
      const techTotals = {};
      const unallocEntries = [];
      
      multiDateSelection.sort().forEach(date => {
        const entries = region.dailyLog[date] || [];
        entries.forEach(entry => {
          allEntries.push({ date, ...entry });
          
          if (entry.unallocated) {
            unallocEntries.push({ date, ...entry });
          } else {
            if (!techTotals[entry.technician]) {
              techTotals[entry.technician] = { total: 0, orders: {} };
            }
            techTotals[entry.technician].total += entry.supplied;
            if (entry.orderNo) {
              techTotals[entry.technician].orders[entry.orderNo] = (techTotals[entry.technician].orders[entry.orderNo] || 0) + entry.supplied;
            }
          }
        });
      });
      
      const assignedOrders = Object.values(region.orders).filter(o => Object.keys(o.allocations || {}).length > 0);
      const totalOrderedAssigned = assignedOrders.reduce((s, o) => s + o.totalLiters, 0);
      const totalSuppliedAssigned = allEntries.filter(e => !e.unallocated).reduce((s, e) => s + e.supplied, 0);
      const balanceAssigned = totalOrderedAssigned - totalSuppliedAssigned;
      
      let resultsHtml = `
        <div class="stats-grid grid-cols-4 mb-6">
          <div class="stat-tile">
            <div class="stat-label">Dates Selected</div>
            <div class="stat-value">${multiDateSelection.length}</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Total Ordered (Assigned)</div>
            <div class="stat-value">${totalOrderedAssigned}L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Total Supplied (Allocated)</div>
            <div class="stat-value text-success-700">${totalSuppliedAssigned}L</div>
          </div>
          <div class="stat-tile">
            <div class="stat-label">Balance (Assigned)</div>
            <div class="stat-value text-danger-700">${balanceAssigned}L</div>
          </div>
        </div>
      `;
      
      resultsHtml += '<h4 class="text-lg font-semibold mt-4 mb-3">Technician Breakdown (Allocated Only)</h4>';
      
      if (Object.keys(techTotals).length > 0) {
        resultsHtml += '<div class="table-container">';
        resultsHtml += '<table class="table"><thead><tr><th>Technician</th><th>Total Supplied</th><th>Orders</th></tr></thead><tbody>';
        
        Object.entries(techTotals).sort((a, b) => b[1].total - a[1].total).forEach(([tech, data]) => {
          const orderList = Object.entries(data.orders).map(([order, litres]) => `${order}: ${litres}L`).join(', ');
          resultsHtml += `
            <tr>
              <td><strong>${tech}</strong></td>
              <td>${data.total}L</td>
              <td><small>${orderList}</small></td>
            </tr>
          `;
        });
        
        resultsHtml += '</tbody></table></div>';
      } else {
        resultsHtml += '<div class="empty-state"><p>No allocated entries found</p></div>';
      }
      
      if (unallocEntries.length > 0) {
        resultsHtml += '<h4 class="text-lg font-semibold mt-4 mb-3">Unallocated Entries (Not Tracked in Balance)</h4>';
        resultsHtml += '<div class="table-container">';
        resultsHtml += '<table class="table"><thead><tr><th>Date</th><th>Technician</th><th>Litres</th><th>Comment</th></tr></thead><tbody>';
        
        unallocEntries.forEach(e => {
          resultsHtml += `
            <tr>
              <td>${new Date(e.date).toLocaleDateString('en-GB')}</td>
              <td>${e.technician}</td>
              <td>${e.supplied}L</td>
              <td><small>${e.comment || '—'}</small></td>
            </tr>
          `;
        });
        
        resultsHtml += '</tbody></table></div>';
      }
      
      document.getElementById('multiDateResults').innerHTML = resultsHtml;
      closeModal('multiDateModal');
      openModal('multiDateResultsModal');
    }

    function exportMultiDateSummary() {
      const region = DB.regions[DB.currentRegion];
      const wb = XLSX.utils.book_new();
      
      const summaryData = [['Date', 'Technician', 'Order', 'Supplied', 'Type', 'Comment']];
      multiDateSelection.sort().forEach(date => {
        const entries = region.dailyLog[date] || [];
        entries.forEach(e => {
          summaryData.push([date, e.technician, e.orderNo || 'Unallocated', e.supplied, e.unallocated ? 'Unallocated' : 'Allocated', e.comment || '']);
        });
      });
      
      XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet(summaryData), 'Multi-Date Summary');
      XLSX.writeFile(wb, `CCS_Summary_${multiDateSelection.length}_dates.xlsx`);
      showToast('Summary exported successfully');
    }

    // ===== BACKUP FUNCTIONS =====
    let autoBackupTimer = null;
    
    function startAutoBackup() {
      if (autoBackupTimer) clearInterval(autoBackupTimer);
      autoBackupTimer = setInterval(() => {
        performAutoBackup();
      }, 21600000); // 6 hours
      setTimeout(() => {
        performAutoBackup();
      }, 5000);
    }
    
    function performAutoBackup() {
      const json = JSON.stringify(DB, null, 2);
      const blob = new Blob([json], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `CCS_AutoBackup_${new Date().toISOString().slice(0, 19).replace(/:/g, '-')}.json`;
      a.click();
      URL.revokeObjectURL(url);
      localStorage.setItem('ccs_last_auto_backup', new Date().toISOString());
      renderBackupStatus();
      if (!document.hidden) {
        showToast('Auto-backup completed', 'info', 2000);
      }
    }

    function backupData() {
      const json = JSON.stringify(DB, null, 2);
      const blob = new Blob([json], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `CCS_Backup_${new Date().toISOString().slice(0, 10)}.json`;
      a.click();
      URL.revokeObjectURL(url);
      
      localStorage.setItem('ccs_last_backup', new Date().toISOString());
      renderBackupStatus();
      showToast('Manual backup created successfully');
    }

    function restoreData(event) {
      const file = event.target.files[0];
      if (!file) return;
      
      const reader = new FileReader();
      reader.onload = e => {
        try {
          const parsed = JSON.parse(e.target.result);
          if (!parsed.regions || !parsed.currentRegion) {
            return showToast('Invalid backup file', 'error');
          }
          
          Object.values(parsed.regions).forEach(r => {
            if (!r.unassignedComments) r.unassignedComments = {};
          });
          
          if (!confirm('This will replace all current data. Continue?')) return;
          
          DB = parsed;
          save();
          renderPageWithTransition(currentPage);
          populateRegions();
          showToast('Data restored successfully');
        } catch {
          showToast('Failed to read backup file', 'error');
        }
      };
      reader.readAsText(file);
      event.target.value = '';
    }

    function renderBackupStatus() {
      const indicator = document.getElementById('backupIndicator');
      if (!indicator) return;
      
      const lastManual = localStorage.getItem('ccs_last_backup');
      const lastAuto = localStorage.getItem('ccs_last_auto_backup');
      const lastBackup = lastAuto || lastManual;
      
      if (!lastBackup) {
        indicator.innerHTML = '<i class="fa-regular fa-cloud"></i><span>No backup</span>';
        indicator.className = 'badge badge-warning';
        return;
      }
      
      const last = new Date(lastBackup);
      const daysSince = Math.floor((Date.now() - last) / 86400000);
      const hoursSince = Math.floor((Date.now() - last) / 3600000);
      
      if (daysSince >= 7) {
        indicator.innerHTML = `<i class="fa-regular fa-cloud-exclamation"></i><span>Backup ${daysSince}d ago</span>`;
        indicator.className = 'badge badge-warning';
      } else if (hoursSince >= 24) {
        indicator.innerHTML = `<i class="fa-regular fa-cloud"></i><span>Backup ${Math.floor(hoursSince/24)}d ago</span>`;
        indicator.className = 'badge badge-info';
      } else if (hoursSince >= 1) {
        indicator.innerHTML = `<i class="fa-regular fa-cloud-check"></i><span>Backup ${hoursSince}h ago</span>`;
        indicator.className = 'badge badge-success';
      } else {
        indicator.innerHTML = `<i class="fa-regular fa-cloud-check"></i><span>Backed up just now</span>`;
        indicator.className = 'badge badge-success';
      }
    }

    // ===== SEARCH KEYBOARD NAVIGATION =====
    let searchKeyIdx = -1;
    let searchItems = [];
    let searchTimeout = null;

    function handleGlobalSearch() {
      clearTimeout(searchTimeout);
      searchKeyIdx = -1;
      
      const query = document.getElementById('globalSearch').value.toLowerCase().trim();
      const dd = document.getElementById('searchDropdown');

      if (!query) {
        dd.style.display = 'none';
        return;
      }

      searchTimeout = setTimeout(() => {
        const results = [];

        Object.entries(DB.regions).forEach(([rName, r]) => {
          Object.values(r.orders).forEach(o => {
            if (o.orderNo.toLowerCase().includes(query) ||
                (o.vehiclePlate || '').toLowerCase().includes(query)) {
              results.push({ type: 'order', region: rName, data: o });
            }
          });
          r.technicians.forEach(t => {
            if (t.toLowerCase().includes(query)) {
              results.push({ type: 'tech', region: rName, data: { name: t, plate: r.technicianPlates[t] || '' } });
            }
          });
          Object.entries(r.dailyLog).forEach(([date, entries]) => {
            entries.forEach(e => {
              if ((e.technician || '').toLowerCase().includes(query) ||
                  (e.orderNo || '').toLowerCase().includes(query)) {
                results.push({ type: 'log', region: rName, data: { ...e, date } });
              }
            });
          });
        });

        // Also search TECH_MANAGER master data for site IDs and technician names
        if (query.length >= 3) {
          const tmHits = TECH_MANAGER.getAllAssignments().filter(r =>
            r.siteId.toLowerCase().includes(query) || r.techName.toLowerCase().includes(query)
          ).slice(0, 6);
          tmHits.forEach(hit => {
            const regionLabels = { nrw:'NRW', eastern:'Eastern', old_cbt:'Old CBT', new_cbt:'New CBT' };
            results.push({ type: 'site', region: regionLabels[hit.region]||hit.region, data: { siteId: hit.siteId, techName: hit.techName, region: hit.region } });
          });
        }

        showSearchResults(results, query);
      }, 250);
    }

    function showSearchResults(results, query) {
      const dd = document.getElementById('searchDropdown');
      if (!dd) return;

      if (!results.length) {
        dd.innerHTML = `<div class="p-4 text-center text-neutral-400">No results for "<strong>${query}</strong>"</div>`;
        dd.style.display = 'block';
        return;
      }

      const hl = (text) => {
        const safe = String(text).replace(/[<>&"]/g, c => ({'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'}[c]));
        const re = new RegExp('(' + query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
        return safe.replace(re, '<mark style="background:#fef08a;border-radius:2px;padding:0 1px;">$1</mark>');
      };

      const icons = { order: '📄', tech: '👤', log: '📝', site: '📡' };
      const labels = { order: 'Order', tech: 'Technician', log: 'Log Entry', site: 'Site Assignment' };

      const groups = {};
      results.forEach(r => {
        if (!groups[r.type]) groups[r.type] = [];
        groups[r.type].push(r);
      });

      let html = '';
      const MAX_PER_GROUP = 5;
      searchItems = [];

      ['order', 'tech', 'log', 'site'].forEach(type => {
        if (!groups[type]) return;
        const items = groups[type].slice(0, MAX_PER_GROUP);
        html += `<div class="px-3 py-1.5 text-xs font-bold uppercase text-neutral-400 bg-neutral-50 border-b border-neutral-100">${icons[type]} ${labels[type]}s</div>`;
        
        items.forEach(res => {
          const itemId = 'sr_' + Math.random().toString(36).substr(2, 9);
          searchItems.push({ id: itemId, result: res });
          
          if (type === 'order') {
            const o = res.data;
            const hasAllocations = Object.keys(o.allocations || {}).length > 0;
            const status = !hasAllocations ? '#8f9bae' : (o.status === 'OPEN' ? '#16a34a' : '#d97706');
            html += `<div id="${itemId}" class="sr-item px-3 py-2.5 cursor-pointer border-b border-neutral-100 flex items-center gap-2.5" onclick="searchGoTo('order','${res.region}','${o.orderNo}')">
              <span class="text-lg">📄</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-sm">${hl(o.orderNo)} <span class="text-xs font-bold" style="color:${status};">${!hasAllocations ? 'Unassigned' : o.status}</span></div>
                <div class="text-xs text-neutral-500">${hl(o.vehiclePlate || '')} · ${o.totalLiters}L · ${res.region}</div>
              </div>
            </div>`;
          } else if (type === 'tech') {
            const t = res.data;
            html += `<div id="${itemId}" class="sr-item px-3 py-2.5 cursor-pointer border-b border-neutral-100 flex items-center gap-2.5" onclick="searchGoTo('tech','${res.region}','${t.name}')">
              <span class="text-lg">👤</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-sm">${hl(t.name)}</div>
                <div class="text-xs text-neutral-500">${t.plate ? hl(t.plate) + ' · ' : ''}${res.region}</div>
              </div>
            </div>`;
          } else if (type === 'log') {
            const e = res.data;
            const entryType = e.unallocated ? '⚠️ Unallocated' : '✅ Allocated';
            html += `<div id="${itemId}" class="sr-item px-3 py-2.5 cursor-pointer border-b border-neutral-100 flex items-center gap-2.5" onclick="searchGoTo('log','${res.region}','${e.date}')">
              <span class="text-lg">📝</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-sm">${hl(e.technician)} — ${hl(e.orderNo || 'Unallocated')}</div>
                <div class="text-xs text-neutral-500">${e.date} · ${e.supplied}L · ${entryType} · ${res.region}</div>
              </div>
            </div>`;
          } else if (type === 'site') {
            const s = res.data;
            html += `<div id="${itemId}" class="sr-item px-3 py-2.5 cursor-pointer border-b border-neutral-100 flex items-center gap-2.5" onclick="searchGoToSite(this)">
              <span class="sr-site-id" style="display:none">${s.siteId}</span>
              <span class="text-lg">📡</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-sm">${hl(s.siteId)}</div>
                <div class="text-xs text-neutral-500">${hl(s.techName)} · ${res.region}</div>
              </div>
            </div>`;
          }
        });

        if (groups[type].length > MAX_PER_GROUP) {
          html += `<div class="px-3 py-1.5 text-xs text-neutral-400 bg-neutral-50">+${groups[type].length - MAX_PER_GROUP} more ${labels[type].toLowerCase()}s</div>`;
        }
      });

      dd.innerHTML = html;
      dd.style.display = 'block';
      
      searchItems = searchItems.map((item, index) => ({ ...item, index }));
    }

    function handleSearchKeydown(e) {
      const dd = document.getElementById('searchDropdown');
      if (!dd || dd.style.display === 'none' || searchItems.length === 0) return;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        searchKeyIdx = Math.min(searchKeyIdx + 1, searchItems.length - 1);
        updateSearchHighlight();
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        searchKeyIdx = Math.max(searchKeyIdx - 1, 0);
        updateSearchHighlight();
      } else if (e.key === 'Enter' && searchKeyIdx >= 0) {
        e.preventDefault();
        const item = searchItems[searchKeyIdx];
        if (item) {
          const el = document.getElementById(item.id);
          if (el) el.click();
        }
      }
    }

    function updateSearchHighlight() {
      searchItems.forEach((item, i) => {
        const el = document.getElementById(item.id);
        if (el) {
          el.classList.toggle('keyboard-active', i === searchKeyIdx);
          if (i === searchKeyIdx) el.scrollIntoView({ block: 'nearest' });
        }
      });
    }

    function searchGoTo(type, region, id) {
      if (DB.currentRegion !== region) {
        DB.currentRegion = region;
        save();
        populateRegions();
      }
      
      const dd = document.getElementById('searchDropdown');
      dd.style.display = 'none';
      
      const inp = document.getElementById('globalSearch');
      inp.value = '';
      searchKeyIdx = -1;
      searchItems = [];

      if (type === 'order') {
        openOrderDetailModal(id, region);
      } else if (type === 'tech') {
        openTechHistory(id);
      } else if (type === 'log') {
        renderPageWithTransition('daily');
        setTimeout(() => {
          const dateEl = document.getElementById('dailyDate');
          if (dateEl) { 
            dateEl.value = id; 
            loadDailyLog(); 
          }
        }, 150);
      }
    }

    function openOrderDetailModal(orderNo, regionName) {
      const rName = regionName || DB.currentRegion;
      const region = DB.regions[rName];
      if (!region) return;
      const order = region.orders[orderNo];
      if (!order) return;

      const balance = order.totalLiters - order.suppliedTotal;
      const progress = Math.min(100, (order.suppliedTotal / order.totalLiters) * 100);
      const hasAllocations = Object.keys(order.allocations || {}).length > 0;
      let statusText, statusBadge;
      
      if (!hasAllocations) {
        statusText = 'Unassigned';
        statusBadge = 'badge-neutral';
      } else if (balance <= 0) {
        statusText = 'Closed';
        statusBadge = 'badge-warning';
      } else {
        statusText = 'Open';
        statusBadge = 'badge-success';
      }

      let techRows = '';
      const allocEntries = Object.entries(order.allocations || {});
      
      if (hasAllocations) {
        allocEntries.forEach(([tech, alloc]) => {
          const supplied = Object.values(region.dailyLog).flat()
            .filter(e => e.orderNo === orderNo && e.technician === tech)
            .reduce((s, e) => s + e.supplied, 0);
          const remaining = alloc - supplied;
          const isOver = supplied > alloc;
          const techProgress = Math.min(100, (supplied / alloc) * 100);
          const plate = region.technicianPlates[tech] || '';
          
          techRows += `<div class="tech-alloc-row mb-2">
            ${techAvatarHtml(tech)}
            <div class="tech-details flex-1">
              <div class="tech-name">${tech} ${plate ? '<span class="text-xs text-neutral-500 font-normal">' + plate + '</span>' : ''}</div>
              <div class="mt-1"><div class="progress-bar" style="height:6px;margin-bottom:4px;"><div class="progress-fill ${isOver ? 'danger' : 'success'}" style="width:${techProgress}%;"></div></div></div>
              <div class="tech-stats">
                <span class="stat-badge" style="background:var(--info-100);color:var(--info-700);">Alloc: ${alloc}L</span>
                <span class="stat-badge" style="background:var(--success-100);color:var(--success-700);">Supplied: ${supplied}L</span>
                <span class="stat-badge" style="background:${isOver ? 'var(--danger-100)' : 'var(--warning-100)'};color:${isOver ? 'var(--danger-700)' : 'var(--warning-700)'};">${isOver ? '+' + (supplied - alloc).toFixed(1) + 'L over' : remaining + 'L left'}</span>
              </div>
              ${order.overageComments && order.overageComments[tech] ? '<div class="text-xs text-danger-700 mt-1">💬 ' + order.overageComments[tech] + '</div>' : ''}
              <div class="flex gap-2 mt-2">
                <button class="btn btn-ghost btn-sm text-danger-700" onclick="unassignFuel('${orderNo}', '${tech}')">
                  <i class="fa-regular fa-user-slash"></i> Unassign
                </button>
                <div class="select-wrapper" style="width: 140px;">
                  <select class="select-field btn-sm" onchange="reassignFuel('${orderNo}', '${tech}', this.value); this.value='';">
                    <option value="">Reassign to...</option>
                    ${region.technicians.filter(t => t !== tech && !order.allocations[t]).map(t => `<option value="${t}">${t}</option>`).join('')}
                  </select>
                </div>
              </div>
            </div></div>`;
        });
      } else {
        const comment = region.unassignedComments?.[orderNo] || '';
        techRows = `
          <div class="unassign-comment-section">
            <div class="flex items-center justify-between mb-2">
              <span class="font-semibold">Unassigned Order Notes</span>
              <button class="btn btn-ghost btn-sm" onclick="openUnassignedCommentModal('${orderNo}')">
                <i class="fa-regular fa-pen"></i> ${comment ? 'Edit' : 'Add'} Comment
              </button>
            </div>
            ${comment ? `
            <div class="unassign-comment-display">
              <i class="fa-regular fa-message"></i>
              <span>${comment}</span>
            </div>` : `
            <div class="text-neutral-400 text-sm italic">No comment added yet.</div>`}
          </div>
        `;
      }

      const supplyHistory = [];
      Object.entries(region.dailyLog).forEach(([date, entries]) => {
        entries.forEach(e => { if (e.orderNo === orderNo) supplyHistory.push({ date, ...e }); });
      });
      supplyHistory.sort((a, b) => b.date.localeCompare(a.date));

      let historyRows = '';
      if (supplyHistory.length === 0) {
        historyRows = '<tr><td colspan="3" class="text-center text-neutral-500">No supply history yet</td></tr>';
      } else {
        supplyHistory.forEach(e => {
          const entryType = e.unallocated ? ' (Unallocated)' : '';
          historyRows += '<tr><td>' + new Date(e.date).toLocaleDateString('en-GB', {day:'2-digit',month:'short',year:'numeric'}) + '</td><td>' + e.technician + entryType + '</td><td>' + e.supplied + 'L</td></tr>';
        });
      }

      document.getElementById('orderDetailContent').innerHTML = `
        <div class="flex items-center justify-between mb-5">
          <div>
            <div class="text-2xl font-bold text-neutral-900">${orderNo}</div>
            <div class="text-sm text-neutral-500 mt-1">
              <i class="fa-regular fa-truck mr-1"></i>${order.vehiclePlate}
              &nbsp;·&nbsp; <i class="fa-regular fa-calendar mr-1"></i>${order.createdDate || '—'}
              &nbsp;·&nbsp;  ${rName}
            </div>
          </div>
          <span class="badge ${statusBadge} text-sm px-3 py-1.5">${statusText}</span>
        </div>

        <div class="grid grid-cols-3 gap-3 mb-5">
          <div class="stat-tile p-3"><div class="stat-label">Total Ordered</div><div class="stat-value text-2xl">${order.totalLiters}L</div></div>
          <div class="stat-tile p-3"><div class="stat-label">Supplied</div><div class="stat-value text-2xl text-success-700">${order.suppliedTotal}L</div></div>
          <div class="stat-tile p-3"><div class="stat-label">Remaining</div><div class="stat-value text-2xl ${balance > 0 && hasAllocations ? 'text-danger-700' : 'text-success-700'}">${hasAllocations ? balance + 'L' : 'N/A (Unassigned)'}</div></div>
        </div>

        <div class="mb-5">
          <div class="progress-bar" style="height:10px;">
            <div class="progress-fill ${!hasAllocations ? '' : (progress >= 100 ? 'warning' : progress >= 75 ? 'success' : 'info')}" style="width:${hasAllocations ? progress : 0}%;"></div>
          </div>
          <div class="text-center text-xs text-neutral-500 mt-1">${hasAllocations ? progress.toFixed(1) + '% complete' : 'Unassigned order - no allocation tracking'}</div>
        </div>

        <h4 class="text-lg font-semibold mb-3">${hasAllocations ? 'Technician Allocations' : 'Unassigned Order'}</h4>
        <div class="mb-5">${techRows}</div>

        <h4 class="text-lg font-semibold mb-3">Supply History</h4>
        <div class="table-container">
          <table class="table"><thead><tr><th>Date</th><th>Technician</th><th>Supplied</th></tr></thead>
          <tbody>${historyRows}</tbody></table>
        </div>
      `;

      document.getElementById('orderDetailTitle').textContent = 'Order: ' + orderNo;
      
      document.getElementById('orderDetailGoBtn').onclick = function() {
        closeModal('orderDetailModal');
        renderPageWithTransition('orders');
        setTimeout(function() {
          document.querySelectorAll('.order-card').forEach(function(card) {
            if (card.dataset.orderNo === orderNo) {
              card.scrollIntoView({ behavior: 'smooth', block: 'center' });
              card.style.outline = '3px solid var(--accent-500)';
              setTimeout(function() { card.style.outline = ''; }, 2500);
              
              const body = document.getElementById('body_' + orderNo);
              const chev = document.getElementById('chev_' + orderNo);
              if (body) body.style.display = 'block';
              if (chev) chev.style.transform = 'rotate(180deg)';
            }
          });
        }, 200);
      };

      openModal('orderDetailModal');
    }

    // ===== EXPORT FUNCTIONS =====
    function exportOrders() {
      const wb = XLSX.utils.book_new();
      
      const ordersData = [['Region', 'Order', 'Vehicle', 'Total', 'Supplied', 'Balance (Assigned)', 'Status', 'Date Created', 'Technicians', 'Unassigned Comment']];
      Object.entries(DB.regions).forEach(([rName, r]) => {
        Object.values(r.orders).forEach(o => {
          const techs = Object.keys(o.allocations || {}).join(', ');
          const unassignedComment = r.unassignedComments?.[o.orderNo] || '';
          const balance = Object.keys(o.allocations || {}).length > 0 ? o.totalLiters - o.suppliedTotal : 'N/A (Unassigned)';
          ordersData.push([rName, o.orderNo, o.vehiclePlate, o.totalLiters, o.suppliedTotal, balance, o.status, o.createdDate || '', techs, unassignedComment]);
        });
      });
      XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet(ordersData), 'Orders');
      
      // Extended daily log with all propagated fields
      const logData = [[
        'Region','Date','Technician','Order','Supplied (L)','Type','Site ID',
        'Fuel Found (L)','Supplier','CPH','Current RT','Previous RT',
        'DG Hours Used','Diesel Consumed (L)',
        'Prev Date','Prev Diesel','Fuel Left','Comment'
      ]];
      Object.entries(DB.regions).forEach(([rName, r]) => {
        Object.entries(r.dailyLog).forEach(([date, entries]) => {
          entries.forEach(e => {
            logData.push([
              rName, date, e.technician, e.orderNo || 'Unallocated', e.supplied,
              e.unallocated ? 'Unallocated' : 'Allocated',
              e.siteId || '', e.fuelFound || '', e.supplier || '', e.cph || '',
              e.currRt || '', e.prevRt || '',
              e.dgHoursUsed || '', e.dieselConsumed || '',
              e.prevDate || '', e.prevDiesel || '', e.fuelLeft || '',
              e.comment || ''
            ]);
          });
        });
      });
      const logSheet = XLSX.utils.aoa_to_sheet(logData);
      logSheet['!cols'] = [
        {wch:12},{wch:12},{wch:16},{wch:12},{wch:12},{wch:12},{wch:18},
        {wch:12},{wch:10},{wch:8},{wch:12},{wch:12},
        {wch:14},{wch:16},
        {wch:12},{wch:14},{wch:12},{wch:20}
      ];
      XLSX.utils.book_append_sheet(wb, logSheet, 'Daily Log');
      
      XLSX.writeFile(wb, `CCS_Report_${new Date().toISOString().slice(0, 10)}.xlsx`);
      showToast('Report exported successfully');
    }

    // ===== POPULATE REGIONS =====
    function populateRegions() {
      const sel = document.getElementById('regionSelect');
      if (!sel) return;
      sel.innerHTML = '';
      Object.keys(DB.regions).forEach(r => {
        const o = document.createElement('option');
        o.value = r; o.textContent = r; sel.appendChild(o);
      });
      sel.value = DB.currentRegion;
    }

    function changeRegion() {
      DB.currentRegion = document.getElementById('regionSelect').value;
      save();
      populateRegions();
      renderPageWithTransition(currentPage);
    }

    function _toggleSidebarLegacy() {
      document.getElementById('sidebar').classList.toggle('collapsed');
      document.getElementById('mainContent').classList.toggle('expanded');
    }

    // ===== CONTEXT MENU =====
    function setupContextMenu() {
      document.addEventListener('contextmenu', (e) => {
        const orderCard = e.target.closest('.order-card');
        const tableRow = e.target.closest('.table tbody tr');
        
        if (orderCard) {
          e.preventDefault();
          const orderNo = orderCard.dataset.orderNo;
          showContextMenu(e.clientX, e.clientY, [
            { icon: 'fa-eye', label: 'View Details', action: () => openOrderDetailModal(orderNo, DB.currentRegion) },
            { icon: 'fa-copy', label: 'Copy Order No.', action: () => { navigator.clipboard?.writeText(orderNo); showToast(`Copied: ${orderNo}`, 'info'); } },
            { separator: true },
            { icon: 'fa-pen', label: 'Edit Date', action: () => editOrderDate(orderNo) },
            { icon: 'fa-clone', label: 'Clone Order', action: () => cloneOrder(orderNo) },
            { icon: 'fa-pen-to-square', label: 'Edit Order', action: () => editOrder(orderNo) },
            { separator: true },
            { icon: 'fa-trash', label: 'Delete Order', danger: true, action: () => deleteOrder(orderNo) },
          ]);
        } else if (tableRow) {
          const cells = Array.from(tableRow.querySelectorAll('td'));
          if (cells.length) {
            e.preventDefault();
            const rowText = cells.map(c => c.textContent.trim()).join(' · ');
            showContextMenu(e.clientX, e.clientY, [
              { icon: 'fa-copy', label: 'Copy Row Data', action: () => { navigator.clipboard?.writeText(rowText); showToast('Row copied', 'info'); } },
            ]);
          }
        }
      });
      
      document.addEventListener('click', () => {
        const menu = document.getElementById('contextMenu');
        if (menu) menu.classList.remove('active');
      });
    }

    function showContextMenu(x, y, items) {
      const menu = document.getElementById('contextMenu');
      menu.innerHTML = items.map(item => {
        if (item.separator) return `<div class="context-menu-separator"></div>`;
        return `<button class="context-menu-item${item.danger ? ' danger' : ''}">
          <i class="fa-regular ${item.icon}"></i> ${item.label}
        </button>`;
      }).join('');

      let btnIdx = 0;
      menu.querySelectorAll('.context-menu-item').forEach(btn => {
        while (items[btnIdx] && items[btnIdx].separator) btnIdx++;
        const item = items[btnIdx++];
        if (item) btn.addEventListener('click', () => { menu.classList.remove('active'); item.action(); });
      });

      menu.classList.add('active');
      const vw = window.innerWidth, vh = window.innerHeight;
      const mw = menu.offsetWidth || 190, mh = menu.offsetHeight || 160;
      menu.style.left = (x + mw > vw ? x - mw : x) + 'px';
      menu.style.top = (y + mh > vh ? y - mh : y) + 'px';
    }

    // ===== KEYBOARD SHORTCUTS =====
    function setupKeyboardShortcuts() {
      document.addEventListener('keydown', (e) => {
        if ((e.metaKey || e.ctrlKey) && e.key === 's') {
          e.preventDefault();
          if (currentPage === 'daily') saveDaily();
        }
        
        // Ctrl+K → command palette (handled by the CMD listener above, but keep focus fallback)
        if ((e.metaKey || e.ctrlKey) && (e.key === 'f')) {
          e.preventDefault();
          openCommandPalette();
        }
        
        if ((e.metaKey || e.ctrlKey) && e.key === 'b') {
          e.preventDefault();
          toggleSidebar();
        }
        
        if ((e.metaKey || e.ctrlKey) && e.key === 'd') {
          e.preventDefault();
          setPage('dashboard', null);
        }
        
        if ((e.metaKey || e.ctrlKey) && e.key === 'o') {
          e.preventDefault();
          setPage('orders', null);
        }
        
        if ((e.metaKey || e.ctrlKey) && e.key === 'l') {
          e.preventDefault();
          setPage('leaderboard', null);
        }
        
        if (e.key === '/' && !['INPUT','TEXTAREA'].includes(document.activeElement?.tagName)) {
          e.preventDefault();
          openModal('shortcutsModal');
        }
        
        if (e.key === 'Escape') {
          // Close command palette first
          const cmdOverlay = document.getElementById('cmdOverlay');
          if (cmdOverlay?.classList.contains('active')) {
            closeCommandPalette();
            return;
          }
          // Close tour
          if (_tourActive) { endTour(); return; }

          const activeModals = document.querySelectorAll('.modal-overlay.active');
          if (activeModals.length) {
            const topModal = activeModals[activeModals.length - 1];
            closeModal(topModal.id);
          }
          
          const dd = document.getElementById('searchDropdown');
          const inp = document.getElementById('globalSearch');
          if (dd) dd.style.display = 'none';
          if (inp) inp.value = '';
          searchKeyIdx = -1;
          searchItems = [];
        }
      });
    }

    // ===== DASHBOARD PAGE =====
    function renderDashboardPage(container) {
      const now = new Date();
      const today = now.toISOString().slice(0,10);
      const weekAgo = new Date(now - 7*86400000).toISOString().slice(0,10);
      const monthAgo = new Date(now - 30*86400000).toISOString().slice(0,10);

      const region = DB.regions[DB.currentRegion];
      // Exclude carried-over orders from previous cycle in all KPI calculations
      const allOrders = Object.values(region.orders).filter(o => !o.carriedFromCycle);
      
      const assignedOrders = allOrders.filter(o => Object.keys(o.allocations || {}).length > 0);
      const unassignedOrders = allOrders.filter(o => Object.keys(o.allocations || {}).length === 0);
      
      const openOrders = assignedOrders.filter(o => (o.totalLiters - o.suppliedTotal) > 0);
      const totalOrderedAssigned = assignedOrders.reduce((s,o)=>s+o.totalLiters,0);
      const totalSuppliedAssigned = assignedOrders.reduce((s,o)=>s+o.suppliedTotal,0);
      const overallBalanceAssigned = totalOrderedAssigned - totalSuppliedAssigned;
      
      const totalOrderedUnassigned = unassignedOrders.reduce((s,o)=>s+o.totalLiters,0);

      let weekSupplied = 0;
      Object.entries(region.dailyLog).forEach(([date, entries]) => {
        if (date >= weekAgo) entries.forEach(e => { 
          if (!e.unallocated) weekSupplied += e.supplied; 
        });
      });

      const todayEntries = region.dailyLog[today] || [];
      const todaySupplied = todayEntries.reduce((s,e)=>s+e.supplied,0);

      const techTotals = {};
      Object.entries(region.dailyLog).forEach(([date, entries]) => {
        if (date >= monthAgo) entries.forEach(e => {
          if (!e.unallocated) techTotals[e.technician] = (techTotals[e.technician]||0)+e.supplied;
        });
      });
      const topTech = Object.entries(techTotals).sort((a,b)=>b[1]-a[1])[0];

      const nearlyClosing = assignedOrders.filter(o => { 
        const p = o.totalLiters>0?(o.suppliedTotal/o.totalLiters)*100:0; 
        return p>=90&&p<100; 
      }).length;

      let overageCount = 0;
      assignedOrders.forEach(o => {
        Object.entries(o.allocations||{}).forEach(([tech,alloc]) => {
          const s = Object.values(region.dailyLog).flat().filter(e=>e.orderNo===o.orderNo&&e.technician===tech).reduce((s,e)=>s+e.supplied,0);
          if(s>alloc) overageCount++;
        });
      });

      const monthlyTarget = region.monthlyTarget || 0;
      const monthSupplied = Object.entries(region.dailyLog).reduce((s,[date,entries]) => {
        const m = today.slice(0,7);
        if (date.startsWith(m)) return s + entries.reduce((ss,e)=> {
          if (!e.unallocated) return ss + e.supplied;
          return ss;
        }, 0);
        return s;
      }, 0);
      const targetPct = monthlyTarget > 0 ? Math.min(100,(monthSupplied/monthlyTarget)*100) : 0;

      const recentDates = Object.keys(region.dailyLog).sort().reverse().slice(0,5);

      const allDailyEntries = Object.values(region.dailyLog).flat();
      const dashDgHours = allDailyEntries.reduce((s,e) => s + (e.dgHoursUsed    || 0), 0);
      const dashDiesel  = allDailyEntries.reduce((s,e) => s + (e.dieselConsumed || 0), 0);

      container.innerHTML = `
        <div class="dashboard-hero">
          <div class="hero-content">
            <div class="text-xs opacity-70 mb-1 tracking-widest uppercase">Welcome back</div>
            <h1 class="text-2xl font-bold mb-1">${DB.currentRegion} Overview</h1>
            <div class="opacity-75 text-sm">${now.toLocaleDateString('en-GB',{weekday:'long',day:'2-digit',month:'long',year:'numeric'})}</div>
            <div class="mt-2 flex items-center gap-2">
              <span style="background:rgba(255,255,255,0.2);padding:3px 12px;border-radius:999px;font-size:0.78rem;font-weight:600;letter-spacing:0.05em;">🔄 ${DB.currentCycleName}</span>
              <span style="opacity:0.65;font-size:0.75rem;">Started ${new Date(DB.currentCycleStartDate).toLocaleDateString('en-GB',{day:'2-digit',month:'short',year:'numeric'})}</span>
            </div>
            <div class="mt-4 flex gap-5 flex-wrap">
              <div><div class="opacity-70 text-xs">Open Orders (Assigned)</div><div class="text-2xl font-bold" id="dash-openCount">0</div></div>
              <div><div class="opacity-70 text-xs">Balance (Assigned)</div><div class="text-2xl font-bold" id="dash-balance">0L</div></div>
              <div><div class="opacity-70 text-xs">Today Supplied</div><div class="text-2xl font-bold" id="dash-today">0L</div></div>
            </div>
          </div>
        </div>

        <div class="dashboard-kpi-grid">
          <div class="kpi-card">
            <div class="kpi-icon" style="background:var(--success-100);">🟢</div>
            <div class="kpi-value" style="color:var(--status-success);" id="kpi-open">0</div>
            <div class="kpi-label">Open Orders (Assigned)</div>
            <div class="kpi-trend" style="color:var(--status-success);"><i class="fa-solid fa-circle-dot"></i> Active</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-icon" style="background:var(--info-100);">⛽</div>
            <div class="kpi-value" style="color:var(--status-info);" id="kpi-week">0L</div>
            <div class="kpi-label">Allocated This Week</div>
            <div class="kpi-trend" style="color:var(--neutral-500);">Last 7 days</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-icon" style="background:var(--warning-100);">⚠️</div>
            <div class="kpi-value" style="color:var(--status-warning);" id="kpi-closing">0</div>
            <div class="kpi-label">Nearly Closing</div>
            <div class="kpi-trend" style="color:var(--status-warning);">&gt;90% used</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-icon" style="background:var(--danger-100);">🔴</div>
            <div class="kpi-value" style="color:var(--status-danger);" id="kpi-overage">0</div>
            <div class="kpi-label">Active Overages</div>
            <div class="kpi-trend" style="color:var(--neutral-500);">Needs attention</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-icon" style="background:var(--neutral-200);">📋</div>
            <div class="kpi-value" style="color:var(--status-unassigned);" id="kpi-unassigned">0</div>
            <div class="kpi-label">Unassigned Orders</div>
            <div class="kpi-trend" style="color:var(--neutral-500);">${unassignedOrders.length} orders · ${totalOrderedUnassigned}L total</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-icon" style="background:var(--accent-100);">🏆</div>
            <div class="kpi-value" style="color:var(--accent-700);font-size:1rem;" id="kpi-toptech">—</div>
            <div class="kpi-label">Top Tech This Month</div>
            <div class="kpi-trend" style="color:var(--neutral-500);" id="kpi-toptech-val"></div>
          </div>
          ${monthlyTarget > 0 ? `
          <div class="kpi-card">
            <div class="kpi-icon" style="background:var(--success-100);">🎯</div>
            <div class="kpi-value" style="color:var(--status-success);" id="kpi-target">${monthSupplied}L</div>
            <div class="kpi-label">Monthly Target Progress</div>
            <div class="target-bar-wrap">
              <div class="target-bar-label"><span>${targetPct.toFixed(0)}% of ${monthlyTarget}L</span></div>
              <div class="target-bar"><div class="target-bar-fill" id="kpi-target-bar" style="width:0%;"></div></div>
            </div>
          </div>` : `
          <div class="kpi-card" style="cursor:pointer;border:2px dashed var(--neutral-300);" onclick="openTargetModal()">
            <div class="kpi-icon" style="background:var(--neutral-100);">🎯</div>
            <div class="kpi-value" style="font-size:1rem;color:var(--neutral-500);">Set Target</div>
            <div class="kpi-label">Monthly Litre Target</div>
            <div class="kpi-trend" style="color:var(--accent-600);"><i class="fa-regular fa-plus"></i> Configure</div>
          </div>`}
          ${dashDgHours > 0 ? `
          <div class="kpi-card" style="cursor:pointer;" onclick="openPropagationModal()">
            <div class="kpi-icon" style="background:var(--status-info-bg);">⚡</div>
            <div class="kpi-value" style="color:var(--status-info);">${dashDgHours.toFixed(1)}h</div>
            <div class="kpi-label">Total DG Hours Used</div>
            <div class="kpi-trend" style="color:var(--neutral-500);">From propagation data</div>
          </div>` : ''}
          ${dashDiesel > 0 ? `
          <div class="kpi-card" style="cursor:pointer;" onclick="openPropagationModal()">
            <div class="kpi-icon" style="background:var(--status-warning-bg);">🔥</div>
            <div class="kpi-value" style="color:var(--status-warning);">${dashDiesel.toFixed(0)}L</div>
            <div class="kpi-label">Total Diesel Consumed</div>
            <div class="kpi-trend" style="color:var(--neutral-500);">CPH × DG hours</div>
          </div>` : ''}
        </div>

        <div class="grid grid-cols-2 gap-4 mb-4">
          <div class="card">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-semibold">Open Orders (Assigned)</h3>
              <button class="btn btn-secondary btn-sm" onclick="setPage('orders',null)">View All</button>
            </div>
            <div id="dash-orders-list"></div>
          </div>
          <div class="card">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-semibold">Recent Activity</h3>
              <button class="btn btn-secondary btn-sm" onclick="setPage('daily',null)">Daily Log</button>
            </div>
            <div id="dash-activity"></div>
          </div>
        </div>

        <div class="card">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold">Technician Performance (Allocated)</h3>
            <button class="btn btn-secondary btn-sm" onclick="setPage('leaderboard',null)">Full Leaderboard</button>
          </div>
          <div id="dash-tech-perf"></div>
        </div>
      `;

      setTimeout(() => {
        animateCounter(document.getElementById('dash-openCount'), openOrders.length, '');
        animateCounter(document.getElementById('dash-balance'), overallBalanceAssigned, 'L');
        animateCounter(document.getElementById('dash-today'), todaySupplied, 'L');
        animateCounter(document.getElementById('kpi-open'), openOrders.length, '');
        animateCounter(document.getElementById('kpi-week'), weekSupplied, 'L');
        animateCounter(document.getElementById('kpi-closing'), nearlyClosing, '');
        animateCounter(document.getElementById('kpi-overage'), overageCount, '');
        animateCounter(document.getElementById('kpi-unassigned'), unassignedOrders.length, '');
        
        const topEl = document.getElementById('kpi-toptech');
        const topValEl = document.getElementById('kpi-toptech-val');
        if (topTech) { 
          topEl.textContent = topTech[0]; 
          topValEl.textContent = topTech[1] + 'L supplied'; 
        }
        
        const targetBar = document.getElementById('kpi-target-bar');
        if (targetBar) setTimeout(() => { targetBar.style.width = targetPct + '%'; }, 100);
      }, 50);

      const openList = document.getElementById('dash-orders-list');
      if (openOrders.length === 0) {
        openList.innerHTML = renderEmptyState('orders', 'Create Order', 'setPage(\'orders\',null)');
      } else {
        openList.innerHTML = openOrders.sort((a,b)=>(a.createdDate||'').localeCompare(b.createdDate||'')).slice(0,5).map(o => {
          const p = Math.min(100,(o.suppliedTotal/o.totalLiters)*100);
          const bal = o.totalLiters - o.suppliedTotal;
          const isNearly = p >= 90;
          return `<div class="tech-alloc-row" style="cursor:pointer;${isNearly?'border-color:var(--status-warning);':''}" onclick="openOrderDetailModal('${o.orderNo}','${DB.currentRegion}')">
            <div class="tech-avatar" data-color="1">⛽</div>
            <div class="tech-details" style="flex:1;">
              <div class="tech-name flex items-center gap-1">${o.orderNo} ${isNearly?'<span class="text-xs text-warning-700">⚠️ Nearly full</span>':''}</div>
              <div class="mt-1"><div class="progress-bar" style="height:5px;"><div class="progress-fill ${isNearly ? 'warning' : 'success'}" style="width:${p}%;"></div></div></div>
              <div class="tech-plate">${o.vehiclePlate} · ${bal}L remaining</div>
            </div>
          </div>`;
        }).join('');
      }

      const actEl = document.getElementById('dash-activity');
      if (recentDates.length === 0) {
        actEl.innerHTML = renderEmptyState('daily', 'Add Entry', 'setPage(\'daily\',null)');
      } else {
        actEl.innerHTML = recentDates.map(date => {
          const entries = region.dailyLog[date];
          const total = entries.reduce((s,e)=>s+e.supplied,0);
          const techSet = [...new Set(entries.map(e=>e.technician))];
          return `<div class="tech-alloc-row" style="cursor:pointer;" onclick="setPage('daily',null);setTimeout(()=>{document.getElementById('dailyDate').value='${date}';loadDailyLog();},150)">
            <div class="tech-avatar" data-color="5"><i class="fa-regular fa-calendar"></i></div>
            <div class="tech-details">
              <div class="tech-name">${new Date(date).toLocaleDateString('en-GB',{weekday:'short',day:'2-digit',month:'short'})}</div>
              <div class="tech-plate">${entries.length} entries · ${total}L · ${techSet.slice(0,2).join(', ')}${techSet.length>2?' +'+( techSet.length-2)+' more':''}</div>
            </div>
            <span class="stat-badge" style="background:var(--info-100);color:var(--info-700);">${total}L</span>
          </div>`;
        }).join('');
      }

      const perfEl = document.getElementById('dash-tech-perf');
      const sortedTechs = Object.entries(techTotals).sort((a,b)=>b[1]-a[1]).slice(0,6);
      if (sortedTechs.length === 0) {
        perfEl.innerHTML = renderEmptyState('leaderboard', 'View Leaderboard', 'setPage(\'leaderboard\',null)');
      } else {
        const maxVal = sortedTechs[0][1];
        perfEl.innerHTML = sortedTechs.map(([tech,litres],i) => {
          const pct = (litres/maxVal)*100;
          const c = techColor(tech);
          const colorMap = ['#3D8662','#4F86B0','#C23B4C','#D47A3E','#6b3a9b','#3a809b','#9b3a7a','#5a9b3a'];
          return `<div class="flex items-center gap-3 mb-3 cursor-pointer" onclick="openTechHistory('${tech}')">
            ${techAvatarHtml(tech)}
            <div style="flex:1;">
              <div class="flex justify-between mb-1">
                <span class="font-semibold text-sm">${tech}</span>
                <span class="font-mono text-sm font-bold" style="color:${colorMap[c]};">${litres}L</span>
              </div>
              <div class="progress-bar" style="height:8px;"><div style="height:100%;border-radius:999px;background:${colorMap[c]};width:${pct}%;transition:width 0.8s;"></div></div>
            </div>
          </div>`;
        }).join('');
      }

      renderNotifications();
    }

    // ===== CYCLE MANAGEMENT =====
    function _openEndCycleModalCore() {
      const region = DB.regions[DB.currentRegion];
      // Only count assigned orders in the summary
      const allOrders = Object.values(region.orders).filter(o => Object.keys(o.allocations || {}).length > 0);
      const totalOrders = allOrders.length;
      const openOrders = allOrders.filter(o => (o.totalLiters - o.suppliedTotal) > 0).length;
      const totalSupplied = allOrders.reduce((s,o) => s + o.suppliedTotal, 0);
      const totalLiters = allOrders.reduce((s,o) => s + o.totalLiters, 0);
      const allRegionCount = Object.keys(DB.regions).length;
      const cycleDays = Math.round((Date.now() - new Date(DB.currentCycleStartDate).getTime()) / 86400000);

      const techTotals = {};
      Object.values(DB.regions).forEach(r => {
        Object.values(r.dailyLog).forEach(entries => {
          entries.forEach(e => {
            if (!e.unallocated) techTotals[e.technician] = (techTotals[e.technician]||0) + e.supplied;
          });
        });
      });
      const topTech = Object.entries(techTotals).sort((a,b)=>b[1]-a[1])[0];

      document.getElementById('endCycleSummaryCard').innerHTML = `
        <div class="text-sm font-semibold mb-3" style="color:var(--neutral-700);">
          <i class="fa-regular fa-clock-rotate-left"></i> Current Cycle: <span style="color:var(--accent-600);">${DB.currentCycleName}</span>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div style="background:white;border-radius:var(--radius-md);padding:10px;border:1px solid var(--neutral-200);">
            <div class="text-xs text-neutral-500">Started</div>
            <div class="font-semibold">${new Date(DB.currentCycleStartDate).toLocaleDateString('en-GB',{day:'2-digit',month:'short',year:'numeric'})}</div>
            <div class="text-xs text-neutral-400">${cycleDays} days ago</div>
          </div>
          <div style="background:white;border-radius:var(--radius-md);padding:10px;border:1px solid var(--neutral-200);">
            <div class="text-xs text-neutral-500">Regions</div>
            <div class="font-semibold">${allRegionCount}</div>
          </div>
          <div style="background:white;border-radius:var(--radius-md);padding:10px;border:1px solid var(--neutral-200);">
            <div class="text-xs text-neutral-500">Total Orders</div>
            <div class="font-semibold">${totalOrders}</div>
            ${openOrders > 0 ? `<div class="text-xs mt-1" style="color:var(--status-warning);">⏳ ${openOrders} assigned open order${openOrders!==1?'s':''} will carry over</div>` : ''}
          </div>
          <div style="background:white;border-radius:var(--radius-md);padding:10px;border:1px solid var(--neutral-200);">
            <div class="text-xs text-neutral-500">Total Supplied</div>
            <div class="font-semibold font-mono">${totalSupplied.toLocaleString()}L / ${totalLiters.toLocaleString()}L</div>
          </div>
          ${topTech ? `<div style="background:white;border-radius:var(--radius-md);padding:10px;border:1px solid var(--neutral-200);grid-column:span 2;">
            <div class="text-xs text-neutral-500">Top Technician</div>
            <div class="font-semibold">🏆 ${topTech[0]} · ${topTech[1].toLocaleString()}L</div>
          </div>` : ''}
        </div>
      `;

      // Suggest a name for the new cycle
      const months = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER'];
      const now = new Date();
      const suggested = `${months[now.getMonth()]} CYCLE`;
      document.getElementById('newCycleName').value = suggested;

      openModal('endCycleModal');
    }

    function confirmEndCycle() {
      const newName = document.getElementById('newCycleName').value.trim().toUpperCase();
      if (!newName) return showToast('Please enter a name for the new cycle', 'warning');

      // Archive current cycle snapshot
      const snapshot = {
        name: DB.currentCycleName,
        startDate: DB.currentCycleStartDate,
        endDate: new Date().toISOString().slice(0,10),
        endedAt: new Date().toISOString(),
        regions: JSON.parse(JSON.stringify(DB.regions)) // deep clone
      };
      DB.cycles.push(snapshot);

      // Reset all region data — but carry open orders forward with a cycle tag
      Object.keys(DB.regions).forEach(rName => {
        const r = DB.regions[rName];

        // Only carry ASSIGNED open orders (balance > 0 AND has at least one allocation).
        // Unassigned orders were never delivered — they are dropped on cycle end.
        const carryOrders = {};
        Object.entries(r.orders).forEach(([orderNo, order]) => {
          const balance = order.totalLiters - order.suppliedTotal;
          const isAssigned = Object.keys(order.allocations || {}).length > 0;
          if (balance > 0 && isAssigned) {
            carryOrders[orderNo] = {
              ...order,
              carriedFromCycle: DB.currentCycleName,
              carriedFromCycleStartDate: DB.currentCycleStartDate
            };
          }
        });

        // Build a carried daily log — only entries relevant to carried orders
        const carryLog = {};
        Object.entries(r.dailyLog).forEach(([date, entries]) => {
          const relevant = entries.filter(e => e.orderNo && carryOrders[e.orderNo]);
          if (relevant.length > 0) carryLog[date] = relevant;
        });

        r.orders = carryOrders;
        r.dailyLog = carryLog;
        r.monthlyTarget = null;
        r.unassignedComments = {};
        // Keep: technicians, technicianPlates, techMonthlyTargets
      });

      // Start new cycle
      DB.currentCycleName = newName;
      DB.currentCycleStartDate = new Date().toISOString().slice(0,10);

      save();
      closeModal('endCycleModal');
      showToast(`🏁 Cycle ended! Starting: ${newName}`, 'success', 5000);
      renderPageWithTransition('dashboard');
    }

    // ===== CYCLES PAGE =====
    function renderCyclesPage(container) {
      const cycles = DB.cycles || [];
      
      // Compute summary for the current live cycle — assigned orders only
      let currentSummary = { orders: 0, supplied: 0, techs: new Set() };
      Object.values(DB.regions).forEach(r => {
        // Count only assigned orders
        currentSummary.orders += Object.values(r.orders).filter(o => Object.keys(o.allocations || {}).length > 0).length;
        Object.values(r.dailyLog).forEach(entries => entries.forEach(e => {
          if (!e.unallocated) { currentSummary.supplied += e.supplied; currentSummary.techs.add(e.technician); }
        }));
      });

      container.innerHTML = `
        <div class="card mb-4" style="background:linear-gradient(135deg,var(--primary-800),var(--primary-700));color:white;">
          <div class="flex items-center justify-between flex-wrap gap-3">
            <div>
              <div class="text-xs opacity-70 mb-1 tracking-widest uppercase">Active Cycle</div>
              <h2 class="text-2xl font-bold">${DB.currentCycleName}</h2>
              <div class="opacity-75 text-sm mt-1">Started: ${new Date(DB.currentCycleStartDate).toLocaleDateString('en-GB',{weekday:'long',day:'2-digit',month:'long',year:'numeric'})}</div>
            </div>
            <button class="btn" onclick="openEndCycleModal()" style="background:rgba(255,255,255,0.15);color:white;border:1px solid rgba(255,255,255,0.3);">
              <i class="fa-regular fa-flag-checkered"></i> End This Cycle
            </button>
          </div>
          <div class="flex gap-6 mt-4 flex-wrap">
            <div><div class="text-xs opacity-70">Orders</div><div class="text-xl font-bold">${currentSummary.orders}</div></div>
            <div><div class="text-xs opacity-70">Total Supplied</div><div class="text-xl font-bold">${currentSummary.supplied.toLocaleString()}L</div></div>
            <div><div class="text-xs opacity-70">Active Technicians</div><div class="text-xl font-bold">${currentSummary.techs.size}</div></div>
            <div><div class="text-xs opacity-70">Regions</div><div class="text-xl font-bold">${Object.keys(DB.regions).length}</div></div>
          </div>
        </div>

        <div class="flex items-center justify-between mb-4">
          <h3 class="text-xl font-semibold">📚 Past Cycles (${cycles.length})</h3>
        </div>

        ${cycles.length === 0 ? `
          <div class="card text-center py-10">
            <div style="font-size:3rem;margin-bottom:1rem;">🔄</div>
            <h3 class="text-lg font-semibold mb-2">No Past Cycles Yet</h3>
            <p class="text-sm text-neutral-500">When you end a cycle, it will appear here with all its data preserved for review.</p>
          </div>
        ` : cycles.slice().reverse().map((cycle, revIdx) => {
          const idx = cycles.length - 1 - revIdx;
          // Only count assigned orders (ignore unassigned fuel) in all summaries
          const allOrders = Object.values(cycle.regions).flatMap(r =>
            Object.values(r.orders).filter(o => Object.keys(o.allocations || {}).length > 0)
          );
          const totalOrders = allOrders.length;
          const totalSupplied = allOrders.reduce((s,o) => s + o.suppliedTotal, 0);
          const totalLiters = allOrders.reduce((s,o) => s + o.totalLiters, 0);
          const techTotals = {};
          Object.values(cycle.regions).forEach(r => {
            Object.values(r.dailyLog).forEach(entries => entries.forEach(e => {
              if (!e.unallocated) techTotals[e.technician] = (techTotals[e.technician]||0) + e.supplied;
            }));
          });
          const topTech = Object.entries(techTotals).sort((a,b)=>b[1]-a[1])[0];
          const cycleDays = Math.round((new Date(cycle.endDate) - new Date(cycle.startDate)) / 86400000) + 1;
          const completionPct = totalLiters > 0 ? Math.min(100, (totalSupplied / totalLiters * 100)) : 0;

          return `
            <div class="card mb-3" style="border-left:4px solid var(--accent-600);">
              <div class="flex items-center justify-between flex-wrap gap-3 mb-3">
                <div>
                  <div class="flex items-center gap-2">
                    <span style="background:var(--accent-100);color:var(--accent-700);font-weight:700;padding:2px 10px;border-radius:999px;font-size:0.8rem;">#${idx+1}</span>
                    <h4 class="text-lg font-bold">${cycle.name}</h4>
                  </div>
                  <div class="text-sm mt-1" style="color:var(--neutral-500);">
                    ${new Date(cycle.startDate).toLocaleDateString('en-GB',{day:'2-digit',month:'short',year:'numeric'})} → ${new Date(cycle.endDate).toLocaleDateString('en-GB',{day:'2-digit',month:'short',year:'numeric'})}
                    <span class="ml-2 badge badge-neutral">${cycleDays} days</span>
                  </div>
                </div>
                <div class="flex gap-2">
                  <button class="btn btn-secondary btn-sm" onclick="viewCycleDetails(${idx})">
                    <i class="fa-regular fa-eye"></i> Full Details
                  </button>
                  <button class="btn btn-secondary btn-sm" onclick="exportCycleData(${idx})">
                    <i class="fa-regular fa-download"></i> Excel
                  </button>
                </div>
              </div>

              <div class="grid grid-cols-4 gap-3 mb-3">
                <div class="text-center" style="background:var(--neutral-50);border-radius:var(--radius-md);padding:10px;">
                  <div class="text-xs text-neutral-500">Orders</div>
                  <div class="font-bold text-lg font-mono">${totalOrders}</div>
                </div>
                <div class="text-center" style="background:var(--neutral-50);border-radius:var(--radius-md);padding:10px;">
                  <div class="text-xs text-neutral-500">Supplied</div>
                  <div class="font-bold text-lg font-mono">${totalSupplied.toLocaleString()}L</div>
                </div>
                <div class="text-center" style="background:var(--neutral-50);border-radius:var(--radius-md);padding:10px;">
                  <div class="text-xs text-neutral-500">Total Ordered</div>
                  <div class="font-bold text-lg font-mono">${totalLiters.toLocaleString()}L</div>
                </div>
                <div class="text-center" style="background:var(--neutral-50);border-radius:var(--radius-md);padding:10px;">
                  <div class="text-xs text-neutral-500">Regions</div>
                  <div class="font-bold text-lg font-mono">${Object.keys(cycle.regions).length}</div>
                </div>
              </div>

              <div class="mb-2">
                <div class="flex justify-between text-xs mb-1">
                  <span class="text-neutral-500">Completion</span>
                  <span class="font-semibold">${completionPct.toFixed(1)}%</span>
                </div>
                <div class="progress-bar" style="height:8px;">
                  <div class="progress-fill success" style="width:${completionPct}%;"></div>
                </div>
              </div>

              ${topTech ? `<div class="text-xs mt-2" style="color:var(--neutral-500);">🏆 Top Technician: <strong>${topTech[0]}</strong> · ${topTech[1].toLocaleString()}L supplied</div>` : ''}
            </div>
          `;
        }).join('')}
      `;
    }

    function viewCycleDetails(cycleIdx) {
      window._viewingCycleIdx = cycleIdx;
      const cycle = DB.cycles[cycleIdx];
      if (!cycle) return;

      const cycleDays = Math.round((new Date(cycle.endDate) - new Date(cycle.startDate)) / 86400000) + 1;

      document.getElementById('viewCycleTitle').textContent = `📋 ${cycle.name}`;
      document.getElementById('viewCycleSubtitle').textContent =
        `${new Date(cycle.startDate).toLocaleDateString('en-GB',{day:'2-digit',month:'long',year:'numeric'})} → ${new Date(cycle.endDate).toLocaleDateString('en-GB',{day:'2-digit',month:'long',year:'numeric'})} · ${cycleDays} day${cycleDays!==1?'s':''}`;

      // ── Aggregate across ALL regions — ASSIGNED ORDERS ONLY ──────────────
      const allOrders     = Object.values(cycle.regions).flatMap(r => Object.values(r.orders));
      // Only count orders that have at least one tech allocated (ignore unassigned fuel)
      const assignedOrders= allOrders.filter(o => Object.keys(o.allocations || {}).length > 0);
      const totalOrders   = assignedOrders.length;
      const totalOrdered  = assignedOrders.reduce((s,o) => s + o.totalLiters,  0);
      const totalSupplied = assignedOrders.reduce((s,o) => s + o.suppliedTotal, 0);
      const closedOrders  = assignedOrders.filter(o => (o.totalLiters - o.suppliedTotal) <= 0).length;
      const openOrders    = assignedOrders.filter(o => (o.totalLiters - o.suppliedTotal) >  0).length;
      const completionPct = totalOrdered > 0 ? Math.min(100, (totalSupplied / totalOrdered) * 100) : 0;

      // Carry-overs: assigned orders still open at cycle end
      const carryOvers = assignedOrders.filter(o => (o.totalLiters - o.suppliedTotal) > 0);
      const carryBalance = carryOvers.reduce((s,o) => s + (o.totalLiters - o.suppliedTotal), 0);

      // Per-tech totals (allocated only, across all regions)
      const techTotals = {};   // tech -> { supplied, orders: Set, days: Set }
      const techTargets = {};  // tech -> allocated litres
      Object.entries(cycle.regions).forEach(([, r]) => {
        Object.values(r.orders).forEach(o => {
          Object.entries(o.allocations || {}).forEach(([tech, alloc]) => {
            if (!techTargets[tech]) techTargets[tech] = 0;
            techTargets[tech] += alloc;
          });
        });
        Object.entries(r.dailyLog).forEach(([date, entries]) => {
          entries.forEach(e => {
            if (e.unallocated || !e.technician) return;
            if (!techTotals[e.technician]) techTotals[e.technician] = { supplied: 0, orders: new Set(), days: new Set() };
            techTotals[e.technician].supplied += e.supplied;
            if (e.orderNo) techTotals[e.technician].orders.add(e.orderNo);
            techTotals[e.technician].days.add(date);
          });
        });
      });
      const sortedTechs = Object.entries(techTotals).sort((a,b) => b[1].supplied - a[1].supplied);
      const maxTechSupply = sortedTechs.length > 0 ? sortedTechs[0][1].supplied : 1;

      // Color palette for tech bars
      const barColors = ['#2B6CB0','#276749','#C53030','#744210','#553C9A','#0987A0','#97266D','#2C7A7B'];

      // ── BUILD HTML ────────────────────────────────────────────────────────
      let html = '';

      // ══════════════════════════════════════════════════════════════════════
      // SECTION 1 — HEADER BANNER
      // ══════════════════════════════════════════════════════════════════════
      html += `
        <div style="background:linear-gradient(135deg,#0f2240,#1a3a5c);border-radius:16px;padding:28px 32px;margin-bottom:24px;color:white;">
          <div style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:16px;">
            <div>
              <div style="font-size:0.65rem;letter-spacing:0.18em;text-transform:uppercase;opacity:0.55;margin-bottom:6px;">CCS FUEL SYSTEM · CYCLE REPORT</div>
              <div style="font-size:1.9rem;font-weight:900;letter-spacing:-0.01em;line-height:1.1;">${cycle.name}</div>
              <div style="font-size:0.88rem;opacity:0.7;margin-top:8px;">
                ${new Date(cycle.startDate).toLocaleDateString('en-GB',{weekday:'long',day:'2-digit',month:'long',year:'numeric'})}
                &nbsp;→&nbsp;
                ${new Date(cycle.endDate).toLocaleDateString('en-GB',{weekday:'long',day:'2-digit',month:'long',year:'numeric'})}
                &nbsp;·&nbsp; ${cycleDays} days
              </div>
            </div>
            <div style="text-align:right;flex-shrink:0;">
              <div style="font-size:0.65rem;letter-spacing:0.12em;text-transform:uppercase;opacity:0.5;margin-bottom:4px;">Overall Completion</div>
              <div style="font-size:3rem;font-weight:900;font-family:var(--font-mono);line-height:1;color:${completionPct>=100?'#68d391':completionPct>=75?'#f6e05e':'#fc8181'};">${completionPct.toFixed(1)}%</div>
              <div style="font-size:0.75rem;opacity:0.65;margin-top:4px;">${totalSupplied.toLocaleString()}L supplied of ${totalOrdered.toLocaleString()}L ordered</div>
            </div>
          </div>

          <!-- Big progress bar -->
          <div style="margin-top:20px;">
            <div style="height:16px;background:rgba(255,255,255,0.1);border-radius:999px;overflow:hidden;position:relative;">
              <div style="position:absolute;top:0;left:0;height:100%;width:${completionPct}%;background:linear-gradient(90deg,#48bb78,#68d391);border-radius:999px;transition:width 1.4s;"></div>
            </div>
          </div>
        </div>`;

      // ══════════════════════════════════════════════════════════════════════
      // SECTION 2 — KEY NUMBERS (large, clear, labelled boxes)
      // ══════════════════════════════════════════════════════════════════════
      const kpiItems = [
        { label: 'Total Orders',    value: totalOrders,                           unit: '',  color: '#1a3a5c', bg: '#eef4fb', border: '#c3d9f0' },
        { label: 'Total Ordered',   value: totalOrdered.toLocaleString(),         unit: 'L', color: '#1a3a5c', bg: '#eef4fb', border: '#c3d9f0' },
        { label: 'Total Supplied',  value: totalSupplied.toLocaleString(),         unit: 'L', color: '#276749', bg: '#f0fff4', border: '#9ae6b4' },
        { label: 'Not Supplied',    value: (totalOrdered-totalSupplied).toLocaleString(), unit:'L', color:(totalOrdered-totalSupplied)>0?'#c53030':'#276749', bg:(totalOrdered-totalSupplied)>0?'#fff5f5':'#f0fff4', border:(totalOrdered-totalSupplied)>0?'#feb2b2':'#9ae6b4' },
        { label: 'Closed Orders',   value: closedOrders,                          unit: '',  color: '#276749', bg: '#f0fff4', border: '#9ae6b4' },
        { label: 'Carried Forward', value: openOrders,                            unit: '',  color: openOrders>0?'#744210':'#276749', bg: openOrders>0?'#fffbeb':'#f0fff4', border: openOrders>0?'#f6ad55':'#9ae6b4' },
        { label: 'Technicians',     value: sortedTechs.length,                    unit: '',  color: '#553c9a', bg: '#faf5ff', border: '#d6bcfa' },
        { label: 'Duration',        value: cycleDays,                             unit: ' days', color: '#0987a0', bg: '#e6fffa', border: '#81e6d9' },
      ];
      html += `
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:24px;">
          ${kpiItems.map(k => `
            <div style="background:${k.bg};border:1.5px solid ${k.border};border-radius:12px;padding:16px 14px;text-align:center;">
              <div style="font-size:0.62rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#667085;margin-bottom:8px;">${k.label}</div>
              <div style="font-size:1.65rem;font-weight:900;font-family:var(--font-mono);color:${k.color};line-height:1;">${k.value}<span style="font-size:1rem;font-weight:600;">${k.unit}</span></div>
            </div>`).join('')}
        </div>`;

      // ══════════════════════════════════════════════════════════════════════
      // SECTION 3 — TECHNICIAN PERFORMANCE TABLE (clear, readable, printable)
      // ══════════════════════════════════════════════════════════════════════
      html += `
        <div style="background:white;border:1.5px solid #e2e8f0;border-radius:14px;margin-bottom:24px;overflow:hidden;">
          <div style="background:#f8fafc;padding:16px 20px;border-bottom:1.5px solid #e2e8f0;display:flex;align-items:center;justify-content:space-between;">
            <div>
              <div style="font-size:1rem;font-weight:800;color:#1a202c;">🏆 Technician Performance</div>
              <div style="font-size:0.72rem;color:#718096;margin-top:2px;">Allocated supply entries only · sorted by litres supplied</div>
            </div>
            <span style="background:#1a3a5c;color:white;padding:3px 12px;border-radius:999px;font-size:0.72rem;font-weight:600;">${sortedTechs.length} technician${sortedTechs.length!==1?'s':''}</span>
          </div>`;

      if (sortedTechs.length === 0) {
        html += `<div style="padding:40px;text-align:center;color:#a0aec0;font-style:italic;">No supply data recorded for this cycle.</div>`;
      } else {
        html += `
          <table style="width:100%;border-collapse:collapse;font-size:0.85rem;">
            <thead>
              <tr style="background:#f1f5f9;">
                <th style="padding:11px 16px;text-align:left;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">#</th>
                <th style="padding:11px 16px;text-align:left;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Technician</th>
                <th style="padding:11px 16px;text-align:right;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Allocated (L)</th>
                <th style="padding:11px 16px;text-align:right;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Supplied (L)</th>
                <th style="padding:11px 16px;text-align:right;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">% of Alloc</th>
                <th style="padding:11px 16px;text-align:center;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Orders</th>
                <th style="padding:11px 16px;text-align:center;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Days Active</th>
                <th style="padding:11px 16px;text-align:left;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Progress</th>
              </tr>
            </thead>
            <tbody>`;

        sortedTechs.forEach(([tech, data], i) => {
          const allocated = techTargets[tech] || 0;
          const allocPct  = allocated > 0 ? Math.min(100, (data.supplied / allocated) * 100) : null;
          const barColor  = barColors[i % barColors.length];
          const isTop     = i === 0;
          const rowBg     = isTop ? '#fffbeb' : i % 2 === 0 ? 'white' : '#fafafa';
          html += `
              <tr style="background:${rowBg};border-bottom:1px solid #e2e8f0;">
                <td style="padding:12px 16px;font-weight:700;font-size:0.8rem;color:#94a3b8;">
                  ${i===0?'🥇':i===1?'🥈':i===2?'🥉':'#'+(i+1)}
                </td>
                <td style="padding:12px 16px;">
                  <div style="display:flex;align-items:center;gap:10px;">
                    <div style="width:36px;height:36px;border-radius:50%;background:${barColor}22;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.9rem;color:${barColor};flex-shrink:0;">${tech.charAt(0).toUpperCase()}</div>
                    <span style="font-weight:700;font-size:0.9rem;color:#1a202c;">${tech}</span>
                    ${isTop?'<span style="font-size:0.65rem;background:#fef3c7;color:#92400e;border-radius:999px;padding:1px 8px;font-weight:700;">TOP</span>':''}
                  </div>
                </td>
                <td style="padding:12px 16px;text-align:right;font-family:var(--font-mono);font-size:0.88rem;color:#475569;font-weight:600;">${allocated>0?allocated.toLocaleString()+'L':'—'}</td>
                <td style="padding:12px 16px;text-align:right;font-family:var(--font-mono);font-size:0.95rem;font-weight:800;color:${barColor};">${data.supplied.toLocaleString()}L</td>
                <td style="padding:12px 16px;text-align:right;">
                  ${allocPct !== null
                    ? `<span style="font-size:0.85rem;font-weight:700;color:${allocPct>=100?'#276749':allocPct>=75?'#744210':'#c53030'};">${allocPct.toFixed(1)}%</span>`
                    : '<span style="color:#a0aec0;">—</span>'}
                </td>
                <td style="padding:12px 16px;text-align:center;font-weight:700;color:#1a202c;">${data.orders.size}</td>
                <td style="padding:12px 16px;text-align:center;font-weight:700;color:#1a202c;">${data.days.size}</td>
                <td style="padding:12px 16px;min-width:120px;">
                  <div style="height:8px;background:#e2e8f0;border-radius:999px;overflow:hidden;">
                    <div style="height:100%;width:${(data.supplied/maxTechSupply)*100}%;background:${barColor};border-radius:999px;"></div>
                  </div>
                </td>
              </tr>`;
        });

        // Totals row
        const totalAllocated = Object.values(techTargets).reduce((s,v)=>s+v,0);
        html += `
              <tr style="background:#f1f5f9;border-top:2px solid #e2e8f0;">
                <td style="padding:12px 16px;" colspan="2"><span style="font-weight:800;font-size:0.85rem;color:#1a202c;">TOTAL</span></td>
                <td style="padding:12px 16px;text-align:right;font-family:var(--font-mono);font-weight:800;font-size:0.9rem;color:#1a202c;">${totalAllocated>0?totalAllocated.toLocaleString()+'L':'—'}</td>
                <td style="padding:12px 16px;text-align:right;font-family:var(--font-mono);font-weight:800;font-size:0.9rem;color:#276749;">${totalSupplied.toLocaleString()}L</td>
                <td style="padding:12px 16px;text-align:right;font-weight:800;color:#276749;">${completionPct.toFixed(1)}%</td>
                <td colspan="3"></td>
              </tr>`;

        html += `</tbody></table>`;
      }
      html += `</div>`;

      // ══════════════════════════════════════════════════════════════════════
      // SECTION 4 — CARRY-OVER ORDERS (if any)
      // ══════════════════════════════════════════════════════════════════════
      if (carryOvers.length > 0) {
        html += `
          <div style="background:white;border:2px solid #f6ad55;border-radius:14px;margin-bottom:24px;overflow:hidden;">
            <div style="background:#fffbeb;padding:16px 20px;border-bottom:1.5px solid #f6ad55;display:flex;align-items:center;justify-content:space-between;">
              <div>
                <div style="font-size:1rem;font-weight:800;color:#744210;">⏳ Orders Carried to Next Cycle</div>
                <div style="font-size:0.72rem;color:#92400e;margin-top:2px;">These orders were still open when this cycle ended · ${carryBalance.toLocaleString()}L total outstanding</div>
              </div>
              <span style="background:#92400e;color:white;padding:3px 12px;border-radius:999px;font-size:0.72rem;font-weight:600;">${carryOvers.length} order${carryOvers.length!==1?'s':''}</span>
            </div>
            <table style="width:100%;border-collapse:collapse;font-size:0.85rem;">
              <thead>
                <tr style="background:#fef3c7;">
                  <th style="padding:10px 16px;text-align:left;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#92400e;border-bottom:1.5px solid #f6ad55;">Order No</th>
                  <th style="padding:10px 16px;text-align:left;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#92400e;border-bottom:1.5px solid #f6ad55;">Vehicle</th>
                  <th style="padding:10px 16px;text-align:left;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#92400e;border-bottom:1.5px solid #f6ad55;">Date</th>
                  <th style="padding:10px 16px;text-align:right;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#92400e;border-bottom:1.5px solid #f6ad55;">Ordered (L)</th>
                  <th style="padding:10px 16px;text-align:right;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#92400e;border-bottom:1.5px solid #f6ad55;">Supplied (L)</th>
                  <th style="padding:10px 16px;text-align:right;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#92400e;border-bottom:1.5px solid #f6ad55;">Outstanding (L)</th>
                  <th style="padding:10px 16px;text-align:left;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#92400e;border-bottom:1.5px solid #f6ad55;">Progress</th>
                  <th style="padding:10px 16px;text-align:left;font-weight:700;font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#92400e;border-bottom:1.5px solid #f6ad55;">Technician(s)</th>
                </tr>
              </thead>
              <tbody>
                ${carryOvers.map((o, i) => {
                  const bal = o.totalLiters - o.suppliedTotal;
                  const pct = o.totalLiters > 0 ? Math.min(100,(o.suppliedTotal/o.totalLiters)*100) : 0;
                  const techs = Object.keys(o.allocations||{}).join(', ') || '—';
                  return `<tr style="border-bottom:1px solid #fde68a;background:${i%2===0?'white':'#fffbeb'};">
                    <td style="padding:11px 16px;font-family:var(--font-mono);font-weight:700;color:#744210;">${o.orderNo}</td>
                    <td style="padding:11px 16px;font-family:var(--font-mono);font-size:0.82rem;">${o.vehiclePlate||'—'}</td>
                    <td style="padding:11px 16px;font-size:0.82rem;color:#718096;">${o.createdDate||'—'}</td>
                    <td style="padding:11px 16px;text-align:right;font-family:var(--font-mono);font-weight:600;">${o.totalLiters.toLocaleString()}</td>
                    <td style="padding:11px 16px;text-align:right;font-family:var(--font-mono);font-weight:600;color:#276749;">${o.suppliedTotal.toLocaleString()}</td>
                    <td style="padding:11px 16px;text-align:right;font-family:var(--font-mono);font-weight:800;color:#c53030;">${bal.toLocaleString()}</td>
                    <td style="padding:11px 16px;min-width:110px;">
                      <div style="height:8px;background:#fde68a;border-radius:999px;overflow:hidden;margin-bottom:3px;">
                        <div style="height:100%;width:${pct}%;background:#d97706;border-radius:999px;"></div>
                      </div>
                      <span style="font-size:0.65rem;color:#92400e;">${pct.toFixed(0)}% done</span>
                    </td>
                    <td style="padding:11px 16px;font-size:0.78rem;">${techs}</td>
                  </tr>`;
                }).join('')}
              </tbody>
              <tfoot>
                <tr style="background:#fef3c7;border-top:2px solid #f6ad55;">
                  <td colspan="3" style="padding:10px 16px;font-weight:800;font-size:0.82rem;color:#744210;">TOTAL OUTSTANDING</td>
                  <td style="padding:10px 16px;text-align:right;font-family:var(--font-mono);font-weight:800;color:#744210;">${carryOvers.reduce((s,o)=>s+o.totalLiters,0).toLocaleString()}</td>
                  <td style="padding:10px 16px;text-align:right;font-family:var(--font-mono);font-weight:800;color:#276749;">${carryOvers.reduce((s,o)=>s+o.suppliedTotal,0).toLocaleString()}</td>
                  <td style="padding:10px 16px;text-align:right;font-family:var(--font-mono);font-weight:800;color:#c53030;">${carryBalance.toLocaleString()}</td>
                  <td colspan="2"></td>
                </tr>
              </tfoot>
            </table>
          </div>`;
      }

      // ══════════════════════════════════════════════════════════════════════
      // SECTION 5 — ALL ORDERS TABLE (per region, full detail)
      // ══════════════════════════════════════════════════════════════════════
      Object.entries(cycle.regions).forEach(([rName, r]) => {
        const rOrders = Object.values(r.orders)
          .filter(o => Object.keys(o.allocations || {}).length > 0)
          .sort((a,b) => (a.createdDate||'').localeCompare(b.createdDate||''));
        if (rOrders.length === 0) return;

        const rOrdered  = rOrders.reduce((s,o)=>s+o.totalLiters,0);
        const rSupplied = rOrders.reduce((s,o)=>s+o.suppliedTotal,0);
        const rClosed   = rOrders.filter(o=>(o.totalLiters-o.suppliedTotal)<=0).length;
        const rCarried  = rOrders.filter(o=>(o.totalLiters-o.suppliedTotal)>0).length;

        html += `
          <div style="background:white;border:1.5px solid #e2e8f0;border-radius:14px;margin-bottom:20px;overflow:hidden;">
            <div style="background:#f8fafc;padding:16px 20px;border-bottom:1.5px solid #e2e8f0;display:flex;align-items:center;flex-wrap:wrap;gap:10px;">
              <div style="background:#1a3a5c;color:white;padding:5px 16px;border-radius:999px;font-weight:800;font-size:0.85rem;">${rName}</div>
              <span style="background:#f0fff4;color:#276749;border:1px solid #9ae6b4;padding:3px 10px;border-radius:999px;font-size:0.75rem;font-weight:600;">✅ ${rClosed} Closed</span>
              ${rCarried>0?`<span style="background:#fffbeb;color:#744210;border:1px solid #f6ad55;padding:3px 10px;border-radius:999px;font-size:0.75rem;font-weight:600;">⏳ ${rCarried} Carried</span>`:''}
              <div style="margin-left:auto;text-align:right;">
                <span style="font-size:0.8rem;font-weight:700;color:#276749;">${rSupplied.toLocaleString()}L supplied</span>
                <span style="font-size:0.8rem;color:#94a3b8;"> / </span>
                <span style="font-size:0.8rem;font-weight:700;color:#1a202c;">${rOrdered.toLocaleString()}L ordered</span>
              </div>
            </div>
            <table style="width:100%;border-collapse:collapse;font-size:0.84rem;">
              <thead>
                <tr style="background:#f1f5f9;">
                  <th style="padding:10px 14px;text-align:left;font-weight:700;font-size:0.68rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Order No</th>
                  <th style="padding:10px 14px;text-align:left;font-weight:700;font-size:0.68rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Vehicle</th>
                  <th style="padding:10px 14px;text-align:left;font-weight:700;font-size:0.68rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Date</th>
                  <th style="padding:10px 14px;text-align:right;font-weight:700;font-size:0.68rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Ordered (L)</th>
                  <th style="padding:10px 14px;text-align:right;font-weight:700;font-size:0.68rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Supplied (L)</th>
                  <th style="padding:10px 14px;text-align:right;font-weight:700;font-size:0.68rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Balance (L)</th>
                  <th style="padding:10px 14px;text-align:center;font-weight:700;font-size:0.68rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Status</th>
                  <th style="padding:10px 14px;text-align:left;font-weight:700;font-size:0.68rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Progress</th>
                  <th style="padding:10px 14px;text-align:left;font-weight:700;font-size:0.68rem;letter-spacing:0.06em;text-transform:uppercase;color:#64748b;border-bottom:2px solid #e2e8f0;">Technician(s)</th>
                </tr>
              </thead>
              <tbody>
                ${rOrders.map((o, i) => {
                  const bal = o.totalLiters - o.suppliedTotal;
                  const pct = o.totalLiters > 0 ? Math.min(100,(o.suppliedTotal/o.totalLiters)*100) : 0;
                  const isClosed = bal <= 0;
                  const techs = Object.keys(o.allocations||{}).join(', ') || '—';
                  return `<tr style="border-bottom:1px solid #e2e8f0;background:${!isClosed?'#fffbeb':i%2===0?'white':'#fafafa'};">
                    <td style="padding:11px 14px;">
                      <span style="font-family:var(--font-mono);font-weight:700;font-size:0.88rem;color:#1a3a5c;">${o.orderNo}</span>
                      ${!isClosed?`<span style="display:inline-block;font-size:0.58rem;background:#fef3c7;color:#92400e;border-radius:999px;padding:1px 6px;margin-left:5px;font-weight:700;">CARRIED</span>`:''}
                    </td>
                    <td style="padding:11px 14px;font-family:var(--font-mono);font-size:0.82rem;color:#475569;">${o.vehiclePlate||'—'}</td>
                    <td style="padding:11px 14px;font-size:0.82rem;color:#718096;">${o.createdDate||'—'}</td>
                    <td style="padding:11px 14px;text-align:right;font-family:var(--font-mono);font-weight:600;color:#475569;">${o.totalLiters.toLocaleString()}</td>
                    <td style="padding:11px 14px;text-align:right;font-family:var(--font-mono);font-weight:700;color:#276749;">${o.suppliedTotal.toLocaleString()}</td>
                    <td style="padding:11px 14px;text-align:right;font-family:var(--font-mono);font-weight:800;color:${isClosed?'#276749':'#c53030'};">${isClosed?'—':bal.toLocaleString()}</td>
                    <td style="padding:11px 14px;text-align:center;">
                      <span style="display:inline-block;padding:3px 10px;border-radius:999px;font-size:0.68rem;font-weight:700;
                        background:${isClosed?'#f0fff4':'#fffbeb'};
                        color:${isClosed?'#276749':'#744210'};
                        border:1px solid ${isClosed?'#9ae6b4':'#f6ad55'};">
                        ${isClosed?'✅ CLOSED':'⏳ OPEN'}
                      </span>
                    </td>
                    <td style="padding:11px 14px;min-width:100px;">
                      <div style="height:6px;background:#e2e8f0;border-radius:999px;overflow:hidden;margin-bottom:2px;">
                        <div style="height:100%;width:${pct}%;background:${isClosed?'#48bb78':'#ed8936'};border-radius:999px;"></div>
                      </div>
                      <span style="font-size:0.62rem;color:#94a3b8;">${pct.toFixed(0)}%</span>
                    </td>
                    <td style="padding:11px 14px;font-size:0.78rem;color:#1a202c;">${techs}</td>
                  </tr>`;
                }).join('')}
              </tbody>
              <tfoot>
                <tr style="background:#f1f5f9;border-top:2px solid #e2e8f0;">
                  <td colspan="3" style="padding:10px 14px;font-weight:800;font-size:0.82rem;color:#1a202c;">REGION TOTAL</td>
                  <td style="padding:10px 14px;text-align:right;font-family:var(--font-mono);font-weight:800;color:#1a202c;">${rOrdered.toLocaleString()}</td>
                  <td style="padding:10px 14px;text-align:right;font-family:var(--font-mono);font-weight:800;color:#276749;">${rSupplied.toLocaleString()}</td>
                  <td style="padding:10px 14px;text-align:right;font-family:var(--font-mono);font-weight:800;color:${(rOrdered-rSupplied)>0?'#c53030':'#276749'};">${(rOrdered-rSupplied)>0?(rOrdered-rSupplied).toLocaleString():'—'}</td>
                  <td colspan="3"></td>
                </tr>
              </tfoot>
            </table>
          </div>`;
      });

      document.getElementById('viewCycleContent').innerHTML = html;
      openModal('viewCycleModal');
    }

    // ===== CYCLE EDITOR =====
    function toggleCycleEditorFullscreen() {
      const container = document.getElementById('cycleEditorContainer');
      const icon      = document.getElementById('cycleEditorExpandIcon');
      const overlay   = document.getElementById('cycleEditorModal');
      if (!container) return;
      const isFS = container.dataset.fullscreen === '1';
      if (isFS) {
        container.dataset.fullscreen = '0';
        container.style.cssText = 'max-width:980px;width:96vw;max-height:94vh;overflow-y:auto;transition:all 0.3s ease;';
        overlay.style.alignItems = '';
        icon.className = 'fa-regular fa-expand';
      } else {
        container.dataset.fullscreen = '1';
        container.style.cssText = 'max-width:100vw;width:100vw;max-height:100vh;height:100vh;border-radius:0;overflow-y:auto;transition:all 0.3s ease;';
        overlay.style.alignItems = 'flex-start';
        icon.className = 'fa-regular fa-compress';
      }
    }

    function openCycleEditor(cycleIdx) {
      const cycle = DB.cycles[cycleIdx];
      if (!cycle) return showToast('Cycle not found', 'error');
      window._editingCycleIdx = cycleIdx;

      document.getElementById('cycleEditorTitle').textContent = `✏️ Editing: ${cycle.name}`;
      document.getElementById('cycleEditorSubtitle').textContent = '⚠️ Changes here are permanent and affect archived data. Edit carefully.';

      let html = '';

      // ── CYCLE META ────────────────────────────────────────────────────────
      html += `
        <div style="background:white;border:1px solid var(--neutral-200);border-radius:var(--radius-xl);padding:var(--space-5);margin-bottom:var(--space-4);">
          <div style="font-weight:700;font-size:0.95rem;margin-bottom:var(--space-4);display:flex;align-items:center;gap:8px;">
            <i class="fa-regular fa-circle-info" style="color:var(--accent-600);"></i> Cycle Information
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:var(--space-4);">
            <div>
              <label style="font-size:0.75rem;font-weight:600;color:var(--neutral-600);display:block;margin-bottom:4px;">Cycle Name</label>
              <input type="text" id="cycleEdit_name" value="${cycle.name}" class="input-field" style="font-weight:700;font-size:0.95rem;text-transform:uppercase;">
            </div>
            <div>
              <label style="font-size:0.75rem;font-weight:600;color:var(--neutral-600);display:block;margin-bottom:4px;">Start Date</label>
              <input type="date" id="cycleEdit_startDate" value="${cycle.startDate}" class="input-field">
            </div>
            <div>
              <label style="font-size:0.75rem;font-weight:600;color:var(--neutral-600);display:block;margin-bottom:4px;">End Date</label>
              <input type="date" id="cycleEdit_endDate" value="${cycle.endDate}" class="input-field">
            </div>
          </div>
        </div>`;

      // ── PER-REGION ORDER EDITOR ───────────────────────────────────────────
      Object.entries(cycle.regions).forEach(([rName, r]) => {
        const assignedOrders = Object.values(r.orders).filter(o => Object.keys(o.allocations || {}).length > 0);
        if (assignedOrders.length === 0) return;
        assignedOrders.sort((a,b) => (a.createdDate||'').localeCompare(b.createdDate||''));

        const regionTechs = [...new Set(assignedOrders.flatMap(o => Object.keys(o.allocations||{})))].sort();

        html += `
          <div style="background:white;border:1px solid var(--neutral-200);border-radius:var(--radius-xl);padding:var(--space-5);margin-bottom:var(--space-4);">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--space-4);">
              <div style="background:var(--primary-800);color:white;padding:4px 14px;border-radius:999px;font-weight:700;font-size:0.85rem;">${rName}</div>
              <span style="font-size:0.78rem;color:var(--neutral-500);">${assignedOrders.length} assigned orders</span>
              <button onclick="cycleEditorAddOrder('${rName}')" class="btn btn-secondary btn-sm" style="margin-left:auto;">
                <i class="fa-regular fa-plus"></i> Add Order
              </button>
            </div>
            <div style="overflow-x:auto;">
              <table style="width:100%;border-collapse:collapse;font-size:0.8rem;" id="cycleOrderTable_${rName.replace(/\s/g,'_')}">
                <thead>
                  <tr style="background:var(--neutral-50);border-bottom:2px solid var(--neutral-200);">
                    <th style="padding:8px 10px;text-align:left;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;letter-spacing:0.04em;white-space:nowrap;">Order No</th>
                    <th style="padding:8px 10px;text-align:left;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;letter-spacing:0.04em;white-space:nowrap;">Vehicle</th>
                    <th style="padding:8px 10px;text-align:left;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;letter-spacing:0.04em;white-space:nowrap;">Date</th>
                    <th style="padding:8px 10px;text-align:right;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;letter-spacing:0.04em;white-space:nowrap;">Ordered (L)</th>
                    <th style="padding:8px 10px;text-align:right;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;letter-spacing:0.04em;white-space:nowrap;">Supplied (L)</th>
                    <th style="padding:8px 10px;text-align:right;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;letter-spacing:0.04em;white-space:nowrap;">Balance</th>
                    <th style="padding:8px 10px;text-align:left;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;letter-spacing:0.04em;">Technicians</th>
                    <th style="padding:8px 10px;text-align:center;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;letter-spacing:0.04em;">Actions</th>
                  </tr>
                </thead>
                <tbody>`;

        assignedOrders.forEach((o, rowIdx) => {
          const bal  = o.totalLiters - o.suppliedTotal;
          const isClosed = bal <= 0;
          const techList = Object.keys(o.allocations||{}).join(', ');
          const safeRegion = rName.replace(/\s/g,'_');
          const rowId = `cerow_${safeRegion}_${rowIdx}`;

          html += `
                  <tr id="${rowId}" style="border-bottom:1px solid var(--neutral-100);" data-orderkey="${o.orderNo}" data-region="${rName}">
                    <td style="padding:6px 8px;">
                      <input type="text" class="ce-input" value="${o.orderNo}" data-field="orderNo" data-row="${rowId}"
                        style="width:110px;padding:4px 7px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-family:var(--font-mono);font-size:0.8rem;font-weight:600;">
                    </td>
                    <td style="padding:6px 8px;">
                      <input type="text" class="ce-input" value="${o.vehiclePlate||''}" data-field="vehiclePlate" data-row="${rowId}"
                        style="width:100px;padding:4px 7px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-family:var(--font-mono);font-size:0.8rem;text-transform:uppercase;">
                    </td>
                    <td style="padding:6px 8px;">
                      <input type="date" class="ce-input" value="${o.createdDate||''}" data-field="createdDate" data-row="${rowId}"
                        style="width:130px;padding:4px 7px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-size:0.78rem;">
                    </td>
                    <td style="padding:6px 8px;text-align:right;">
                      <input type="number" class="ce-input" value="${o.totalLiters}" data-field="totalLiters" data-row="${rowId}" min="0" step="0.1"
                        style="width:90px;padding:4px 7px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-family:var(--font-mono);font-size:0.8rem;text-align:right;"
                        oninput="cycleEditorUpdateBalance('${rowId}')">
                    </td>
                    <td style="padding:6px 8px;text-align:right;">
                      <input type="number" class="ce-input" value="${o.suppliedTotal}" data-field="suppliedTotal" data-row="${rowId}" min="0" step="0.1"
                        style="width:90px;padding:4px 7px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-family:var(--font-mono);font-size:0.8rem;text-align:right;"
                        oninput="cycleEditorUpdateBalance('${rowId}')">
                    </td>
                    <td style="padding:6px 8px;text-align:right;">
                      <span id="${rowId}_balance" style="font-family:var(--font-mono);font-size:0.8rem;font-weight:700;color:${isClosed?'var(--status-success)':'var(--status-warning)'};">
                        ${isClosed?'✓':bal.toFixed(1)+'L'}
                      </span>
                    </td>
                    <td style="padding:6px 8px;">
                      <input type="text" class="ce-input" value="${techList}" data-field="allocations" data-row="${rowId}"
                        placeholder="Tech1, Tech2"
                        style="width:160px;padding:4px 7px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-size:0.78rem;"
                        title="Comma-separated technician names">
                    </td>
                    <td style="padding:6px 8px;text-align:center;">
                      <button onclick="cycleEditorDeleteRow('${rowId}')" title="Delete order"
                        style="width:28px;height:28px;border-radius:var(--radius-sm);border:1px solid var(--status-danger);background:var(--status-danger-bg);color:var(--status-danger);cursor:pointer;font-size:0.75rem;">
                        <i class="fa-regular fa-trash"></i>
                      </button>
                    </td>
                  </tr>`;
        });

        html += `
                </tbody>
              </table>
            </div>
          </div>`;
      });

      // ── DAILY LOG EDITOR ─────────────────────────────────────────────────
      let allEntries = [];
      Object.entries(cycle.regions).forEach(([rName, r]) => {
        Object.entries(r.dailyLog).forEach(([date, entries]) => {
          entries.forEach((e, eIdx) => {
            if (!e.unallocated) allEntries.push({ ...e, date, region: rName, _eIdx: eIdx });
          });
        });
      });
      allEntries.sort((a,b) => b.date.localeCompare(a.date));

      if (allEntries.length > 0) {
        html += `
          <div style="background:white;border:1px solid var(--neutral-200);border-radius:var(--radius-xl);padding:var(--space-5);margin-bottom:var(--space-4);">
            <div style="font-weight:700;font-size:0.95rem;margin-bottom:var(--space-4);display:flex;align-items:center;gap:8px;">
              <i class="fa-regular fa-calendar-days" style="color:var(--status-info);"></i>
              Daily Log Entries
              <span style="background:var(--neutral-200);padding:2px 8px;border-radius:999px;font-size:0.72rem;font-weight:600;margin-left:4px;">${allEntries.length} entries</span>
              <span style="font-size:0.72rem;color:var(--neutral-500);font-weight:400;margin-left:4px;">Allocated only · edit supplied amounts and dates</span>
            </div>
            <div style="overflow-x:auto;max-height:380px;overflow-y:auto;">
              <table style="width:100%;border-collapse:collapse;font-size:0.8rem;" id="cycleDailyLogTable">
                <thead style="position:sticky;top:0;z-index:2;">
                  <tr style="background:var(--neutral-50);border-bottom:2px solid var(--neutral-200);">
                    <th style="padding:8px 10px;text-align:left;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;">Date</th>
                    <th style="padding:8px 10px;text-align:left;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;">Technician</th>
                    <th style="padding:8px 10px;text-align:left;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;">Order No</th>
                    <th style="padding:8px 10px;text-align:right;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;">Supplied (L)</th>
                    <th style="padding:8px 10px;text-align:left;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;">Region</th>
                    <th style="padding:8px 10px;text-align:center;font-weight:600;color:var(--neutral-600);font-size:0.72rem;text-transform:uppercase;">Del</th>
                  </tr>
                </thead>
                <tbody>`;

        allEntries.forEach((e, i) => {
          const logRowId = `celog_${i}`;
          html += `
                  <tr id="${logRowId}" style="border-bottom:1px solid var(--neutral-100);"
                      data-region="${e.region}" data-date="${e.date}" data-eidx="${e._eIdx}">
                    <td style="padding:5px 8px;">
                      <input type="date" class="ce-log-input" value="${e.date}" data-field="date" data-logrow="${logRowId}"
                        style="width:130px;padding:3px 6px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-size:0.77rem;">
                    </td>
                    <td style="padding:5px 8px;">
                      <input type="text" class="ce-log-input" value="${e.technician||''}" data-field="technician" data-logrow="${logRowId}"
                        style="width:130px;padding:3px 6px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-size:0.77rem;">
                    </td>
                    <td style="padding:5px 8px;">
                      <input type="text" class="ce-log-input" value="${e.orderNo||''}" data-field="orderNo" data-logrow="${logRowId}"
                        style="width:110px;padding:3px 6px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-family:var(--font-mono);font-size:0.77rem;">
                    </td>
                    <td style="padding:5px 8px;text-align:right;">
                      <input type="number" class="ce-log-input" value="${e.supplied}" data-field="supplied" data-logrow="${logRowId}" min="0" step="0.1"
                        style="width:80px;padding:3px 6px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-family:var(--font-mono);font-size:0.77rem;text-align:right;">
                    </td>
                    <td style="padding:5px 8px;font-size:0.75rem;color:var(--neutral-500);">${e.region}</td>
                    <td style="padding:5px 8px;text-align:center;">
                      <button onclick="cycleEditorDeleteLogRow('${logRowId}')" title="Delete entry"
                        style="width:26px;height:26px;border-radius:var(--radius-sm);border:1px solid var(--status-danger);background:var(--status-danger-bg);color:var(--status-danger);cursor:pointer;font-size:0.7rem;">
                        <i class="fa-regular fa-trash"></i>
                      </button>
                    </td>
                  </tr>`;
        });

        html += `</tbody></table></div></div>`;
      }

      document.getElementById('cycleEditorContent').innerHTML = html;
      openModal('cycleEditorModal');
    }

    function cycleEditorUpdateBalance(rowId) {
      const ordered  = parseFloat(document.querySelector(`[data-row="${rowId}"][data-field="totalLiters"]`)?.value) || 0;
      const supplied = parseFloat(document.querySelector(`[data-row="${rowId}"][data-field="suppliedTotal"]`)?.value) || 0;
      const bal = ordered - supplied;
      const el = document.getElementById(`${rowId}_balance`);
      if (el) {
        el.textContent    = bal <= 0 ? '✓' : bal.toFixed(1) + 'L';
        el.style.color    = bal <= 0 ? 'var(--status-success)' : 'var(--status-warning)';
      }
    }

    function cycleEditorDeleteRow(rowId) {
      const row = document.getElementById(rowId);
      if (!row) return;
      if (!confirm(`Delete order "${row.dataset.orderkey}" from this cycle archive?`)) return;
      row.style.transition = 'opacity 0.25s';
      row.style.opacity = '0';
      setTimeout(() => row.remove(), 260);
    }

    function cycleEditorDeleteLogRow(logRowId) {
      const row = document.getElementById(logRowId);
      if (!row) return;
      if (!confirm('Delete this log entry from the cycle archive?')) return;
      row.style.transition = 'opacity 0.25s';
      row.style.opacity = '0';
      setTimeout(() => row.remove(), 260);
    }

    function cycleEditorAddOrder(regionName) {
      const safeRegion = regionName.replace(/\s/g,'_');
      const tbody = document.querySelector(`#cycleOrderTable_${safeRegion} tbody`);
      if (!tbody) return;
      const rowIdx = tbody.querySelectorAll('tr').length;
      const rowId = `cerow_${safeRegion}_new_${rowIdx}`;
      const tr = document.createElement('tr');
      tr.id = rowId;
      tr.dataset.region = regionName;
      tr.dataset.orderkey = '';
      tr.style.borderBottom = '1px solid var(--neutral-100)';
      tr.style.background = 'rgba(37,99,235,0.04)';
      tr.innerHTML = `
        <td style="padding:6px 8px;"><input type="text" class="ce-input" value="" data-field="orderNo" data-row="${rowId}" placeholder="Order No" style="width:110px;padding:4px 7px;border:1px solid var(--status-info);border-radius:var(--radius-sm);font-family:var(--font-mono);font-size:0.8rem;font-weight:600;"></td>
        <td style="padding:6px 8px;"><input type="text" class="ce-input" value="" data-field="vehiclePlate" data-row="${rowId}" placeholder="Plate" style="width:100px;padding:4px 7px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-family:var(--font-mono);font-size:0.8rem;text-transform:uppercase;"></td>
        <td style="padding:6px 8px;"><input type="date" class="ce-input" value="" data-field="createdDate" data-row="${rowId}" style="width:130px;padding:4px 7px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-size:0.78rem;"></td>
        <td style="padding:6px 8px;text-align:right;"><input type="number" class="ce-input" value="0" data-field="totalLiters" data-row="${rowId}" min="0" step="0.1" style="width:90px;padding:4px 7px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-family:var(--font-mono);font-size:0.8rem;text-align:right;" oninput="cycleEditorUpdateBalance('${rowId}')"></td>
        <td style="padding:6px 8px;text-align:right;"><input type="number" class="ce-input" value="0" data-field="suppliedTotal" data-row="${rowId}" min="0" step="0.1" style="width:90px;padding:4px 7px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-family:var(--font-mono);font-size:0.8rem;text-align:right;" oninput="cycleEditorUpdateBalance('${rowId}')"></td>
        <td style="padding:6px 8px;text-align:right;"><span id="${rowId}_balance" style="font-family:var(--font-mono);font-size:0.8rem;font-weight:700;color:var(--status-warning);">0L</span></td>
        <td style="padding:6px 8px;"><input type="text" class="ce-input" value="" data-field="allocations" data-row="${rowId}" placeholder="Tech1, Tech2" style="width:160px;padding:4px 7px;border:1px solid var(--neutral-200);border-radius:var(--radius-sm);font-size:0.78rem;" title="Comma-separated technician names"></td>
        <td style="padding:6px 8px;text-align:center;">
          <button onclick="cycleEditorDeleteRow('${rowId}')" style="width:28px;height:28px;border-radius:var(--radius-sm);border:1px solid var(--status-danger);background:var(--status-danger-bg);color:var(--status-danger);cursor:pointer;font-size:0.75rem;"><i class="fa-regular fa-trash"></i></button>
        </td>`;
      tbody.appendChild(tr);
      tr.querySelector('input').focus();
    }

    function saveCycleEdits() {
      const cycleIdx = window._editingCycleIdx;
      if (cycleIdx === undefined || cycleIdx === null) return;
      const cycle = DB.cycles[cycleIdx];
      if (!cycle) return showToast('Cycle not found', 'error');

      // ── 1. Save cycle meta ──────────────────────────────────────────────
      const newName      = document.getElementById('cycleEdit_name')?.value.trim().toUpperCase();
      const newStartDate = document.getElementById('cycleEdit_startDate')?.value;
      const newEndDate   = document.getElementById('cycleEdit_endDate')?.value;
      if (newName)      cycle.name      = newName;
      if (newStartDate) cycle.startDate = newStartDate;
      if (newEndDate)   cycle.endDate   = newEndDate;

      // ── 2. Save order rows ───────────────────────────────────────────────
      // Rebuild each region's orders from the table rows still present in DOM
      Object.keys(cycle.regions).forEach(rName => {
        cycle.regions[rName].orders = {};
      });

      document.querySelectorAll('[id^="cerow_"]').forEach(row => {
        const rName = row.dataset.region;
        if (!rName || !cycle.regions[rName]) return;

        const get = (field) => row.querySelector(`[data-field="${field}"]`)?.value?.trim() || '';
        const orderNo      = get('orderNo');
        const vehiclePlate = get('vehiclePlate').toUpperCase();
        const createdDate  = get('createdDate');
        const totalLiters  = parseFloat(get('totalLiters')) || 0;
        const suppliedTotal= parseFloat(get('suppliedTotal')) || 0;
        const techStr      = get('allocations');

        if (!orderNo) return; // skip blank rows

        const allocations = {};
        techStr.split(',').map(t => t.trim()).filter(Boolean).forEach(t => {
          allocations[t] = totalLiters; // store alloc = total ordered
        });

        cycle.regions[rName].orders[orderNo] = {
          orderNo, vehiclePlate, totalLiters, suppliedTotal,
          allocations,
          status: (totalLiters - suppliedTotal) <= 0 ? 'CLOSED' : 'OPEN',
          createdDate
        };
      });

      // ── 3. Save daily log rows ──────────────────────────────────────────
      // Rebuild each region's dailyLog from table rows still present
      Object.keys(cycle.regions).forEach(rName => {
        cycle.regions[rName].dailyLog = {};
      });

      document.querySelectorAll('[id^="celog_"]').forEach(row => {
        const rName = row.dataset.region;
        if (!rName || !cycle.regions[rName]) return;

        const get = (field) => row.querySelector(`[data-field="${field}"]`)?.value?.trim() || '';
        const date       = get('date');
        const technician = get('technician');
        const orderNo    = get('orderNo');
        const supplied   = parseFloat(get('supplied')) || 0;

        if (!date || !technician || supplied <= 0) return;

        if (!cycle.regions[rName].dailyLog[date]) cycle.regions[rName].dailyLog[date] = [];
        cycle.regions[rName].dailyLog[date].push({ technician, orderNo, supplied, unallocated: false });
      });

      save();
      closeModal('cycleEditorModal');
      showToast(`✅ Cycle "${cycle.name}" saved`, 'success');
      // Refresh the view summary if still open
      if (document.getElementById('viewCycleModal')?.classList.contains('active')) {
        viewCycleDetails(cycleIdx);
      }
      // Refresh cycles page
      if (currentPage === 'cycles') renderPageWithTransition('cycles');
    }

    function exportCycleData(cycleIdx) {
      const cycle = DB.cycles[cycleIdx];
      if (!cycle) return showToast('Cycle not found', 'error');

      const wb = XLSX.utils.book_new();

      // Summary sheet
      const summaryData = [['Cycle Name', cycle.name], ['Start Date', cycle.startDate], ['End Date', cycle.endDate], ['Regions', Object.keys(cycle.regions).join(', ')]];
      XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet(summaryData), 'Cycle Summary');

      // Orders sheet
      const ordersData = [['Region','Order No','Vehicle','Total Litres','Supplied','Balance','Status','Date','Technicians']];
      Object.entries(cycle.regions).forEach(([rName, r]) => {
        Object.values(r.orders).forEach(o => {
          const techs = Object.keys(o.allocations||{}).join(', ');
          ordersData.push([rName, o.orderNo, o.vehiclePlate||'', o.totalLiters, o.suppliedTotal, o.totalLiters-o.suppliedTotal, o.status||'OPEN', o.createdDate||'', techs]);
        });
      });
      XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet(ordersData), 'Orders');

      // Daily Log sheet
      const logData = [['Region','Date','Technician','Order No','Supplied','Type','Comment']];
      Object.entries(cycle.regions).forEach(([rName, r]) => {
        Object.entries(r.dailyLog).forEach(([date, entries]) => {
          entries.forEach(e => {
            logData.push([rName, date, e.technician, e.orderNo||'Unallocated', e.supplied, e.unallocated?'Unallocated':'Allocated', e.comment||'']);
          });
        });
      });
      XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet(logData), 'Daily Log');

      // Technician summary sheet
      const techMap = {};
      Object.entries(cycle.regions).forEach(([rName, r]) => {
        Object.values(r.dailyLog).forEach(entries => entries.forEach(e => {
          if (!e.unallocated) {
            const key = `${e.technician}|${rName}`;
            techMap[key] = (techMap[key]||0) + e.supplied;
          }
        }));
      });
      const techData = [['Technician','Region','Total Supplied (L)']];
      Object.entries(techMap).sort((a,b)=>b[1]-a[1]).forEach(([key, litres]) => {
        const [tech, region] = key.split('|');
        techData.push([tech, region, litres]);
      });
      XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet(techData), 'Technician Summary');

      XLSX.writeFile(wb, `CCS_${cycle.name.replace(/\s+/g,'_')}_${cycle.startDate}_to_${cycle.endDate}.xlsx`);
      showToast(`Exported: ${cycle.name}`, 'success');
    }

    // ===== INITIALIZATION =====
    function init() {
      // Restore dark mode
      if (localStorage.getItem('ccs_dark_mode') === '1') {
        document.body.classList.add('dark-mode');
        const btn = document.getElementById('darkModeBtn');
        if (btn) btn.innerHTML = '<i class="fa-regular fa-sun"></i><span>Light Mode</span>';
      }

      // Restore sidebar collapsed state
      if (localStorage.getItem('ccs_sidebar_collapsed') === '1') {
        document.getElementById('sidebar')?.classList.add('collapsed');
        document.getElementById('mainContent')?.classList.add('expanded');
        const icon = document.getElementById('sidebarToggleIcon');
        const btn = document.getElementById('sidebarToggleBtn');
        if (icon) icon.className = 'fa-regular fa-chevron-right';
        if (btn) { const sp = btn.querySelector('span'); if(sp) sp.textContent = 'Expand'; }
      }

      // Apply saved table density
      setTableDensity(localStorage.getItem('ccs_table_density') || 'default');

      populateRegions();
      renderPageWithTransition('dashboard');
      updateBreadcrumb('dashboard');
      setupKeyboardShortcuts();
      renderBackupStatus();
      setupContextMenu();
      setTimeout(renderNotifications, 500);
      
      startAutoBackup();

      // First-run: show What's New modal after 1.5s
      if (!localStorage.getItem('ccs_seen_v2')) {
        setTimeout(() => {
          openWhatsNewModal();
          localStorage.setItem('ccs_seen_v2', '1');
        }, 1500);
      }

      const searchInput = document.getElementById('globalSearch');
      if (searchInput) {
        searchInput.addEventListener('keydown', handleSearchKeydown);
      }

      document.addEventListener('click', (e) => {
        const dd = document.getElementById('searchDropdown');
        const inp = document.getElementById('globalSearch');
        if (dd && !dd.contains(e.target) && e.target !== inp) {
          dd.style.display = 'none';
          searchKeyIdx = -1;
          searchItems = [];
        }
        
        const notifDd = document.getElementById('notifDropdown');
        const notifBtn = document.getElementById('notifBellBtn');
        if (notifDd && !notifDd.contains(e.target) && notifBtn && !notifBtn.contains(e.target)) {
          notifDd.classList.remove('open');
        }

        const fabMenu = document.getElementById('fabMenu');
        const fabMain = document.getElementById('fabMain');
        if (fabMenu && fabMenu.classList.contains('open') && 
            !fabMenu.contains(e.target) && !fabMain.contains(e.target)) {
          fabMenu.classList.remove('open');
        }
      });
      
      setupSwipeNavigation();
      updateNetworkStatus();
      updateSystemClock();
      setInterval(updateSystemClock, 1000);
      setInterval(updateRegionFooter, 3000);

      // Schedule daily alert refresh at midnight
      function scheduleMidnightAlertReset() {
        const now = new Date();
        const midnight = new Date(now);
        midnight.setHours(24, 0, 0, 0);
        const msUntilMidnight = midnight - now;
        setTimeout(() => {
          _alertsShown.clear();
          renderNotifications();
          scheduleMidnightAlertReset(); // reschedule for next midnight
        }, msUntilMidnight);
      }
      scheduleMidnightAlertReset();
    }

    // ===== SWIPE NAVIGATION =====
    function setupSwipeNavigation() {
      let touchStartX = 0;
      let touchEndX = 0;
      
      document.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });
      
      document.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
      }, { passive: true });
      
      function handleSwipe() {
        const swipeThreshold = 100;
        const swipeDistance = touchEndX - touchStartX;
        
        if (Math.abs(swipeDistance) < swipeThreshold) return;
        
        const pages = ['dashboard', 'daily', 'orders', 'reports', 'leaderboard'];
        const currentIndex = pages.indexOf(currentPage);
        
        if (swipeDistance > 0 && currentIndex > 0) {
          setPage(pages[currentIndex - 1], null);
        } else if (swipeDistance < 0 && currentIndex < pages.length - 1) {
          setPage(pages[currentIndex + 1], null);
        }
      }
    }

    // ===== FOOTER FUNCTIONS =====
    function updateSystemClock() {
      const el = document.getElementById('footerSystemTime');
      if (!el) return;
      const now = new Date();
      el.textContent = now.toLocaleDateString() + ' ' + now.toLocaleTimeString();
    }

    function updateNetworkStatus() {
      const dot = document.getElementById('systemStatusDot');
      const text = document.getElementById('systemStatusText');
      if (!dot || !text) return;
      if (navigator.onLine) {
        dot.classList.remove('offline');
        dot.classList.add('online');
        text.textContent = 'System Online';
      } else {
        dot.classList.remove('online');
        dot.classList.add('offline');
        text.textContent = 'Offline Mode';
      }
    }

    window.addEventListener('online', updateNetworkStatus);
    window.addEventListener('offline', updateNetworkStatus);

    function updateRegionFooter() {
      const el = document.getElementById('footerActiveRegion');
      if (!el) return;
      el.textContent = 'Region: ' + (DB.currentRegion || 'Unknown');
    }

    function setAutosaveStatus(state) {
      const el = document.getElementById('footerAutosave');
      if (!el) return;
      if (state === 'saving') {
        el.textContent = 'Saving...';
      } else if (state === 'saved') {
        el.textContent = 'Autosave Complete';
      }
    }

    // ===== AUTOMATION MODULE =====
    // Persisted automation config in DB
    if (!DB.automation) DB.automation = { watchedPersons: ['John IHS', 'Muta IHS', 'Trina IHS'] };

    // Global file handle for the automation page
    window._autoFile = null;

    // ---- VEHICLE → TECHNICIAN + REGION MAP ----
    // The system derives this from technicianPlates across all regions.
    // Additionally we store a global plate→tech map for WhatsApp parsing
    function buildPlateTechMap() {
      const map = {}; // plate -> { techName, regionName }
      Object.entries(DB.regions).forEach(([regionName, r]) => {
        Object.entries(r.technicianPlates || {}).forEach(([tech, plate]) => {
          if (plate) map[plate.trim().toUpperCase()] = { techName: tech, regionName };
        });
      });
      return map;
    }

    // ---- SITE ID LOOKUP via TECH_MANAGER (used by automation parser) ----
    function lookupSiteIdTech(siteId) {
      const result = TECH_MANAGER.lookup(siteId);
      if (!result) return null;
      return { techName: result.techName, region: result.region };
    }

    // ---- WHATSAPP IMPORT ----
    let waParsedOrders = []; // holds parsed order objects ready to review

    function openWhatsAppImport() {
      waParsedOrders = [];
      document.getElementById('waTextInput').value = '';
      document.getElementById('waStep1').style.display = 'block';
      document.getElementById('waStep2').style.display = 'none';
      document.getElementById('waStep3').style.display = 'none';
      document.getElementById('waStep1Badge').className = 'badge badge-info';
      document.getElementById('waStep2Badge').className = 'badge badge-neutral';
      document.getElementById('waStep3Badge').className = 'badge badge-neutral';
      openModal('whatsappImportModal');
    }

    function waHandleFileUpload(event) {
      const file = event.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = e => { document.getElementById('waTextInput').value = e.target.result; };
      reader.readAsText(file, 'UTF-8');
    }

    function waParseTxt() {
      const raw = document.getElementById('waTextInput').value;
      if (!raw.trim()) return showToast('Please paste or upload WhatsApp text first', 'warning');

      const plateTechMap = buildPlateTechMap();

      // CRITICAL FIX: Normalize ALL line endings (\r\n Windows, \r old Mac, \n Unix)
      // then split cleanly so no stray \r chars break the regex
      const normalised = raw.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
      const lines = normalised.split('\n');

      // WhatsApp export format (handles both Android & iOS exports):
      // DD/MM/YYYY, HH:MM - Sender: message body
      // Note: body can be empty for media-only messages, hence (.*)$ not (.+)$
      const lineRe = /^(\d{2}\/\d{2}\/\d{4}),\s*(\d{2}:\d{2})\s*-\s*(.+?):\s*(.*)$/;

      // OTP message pattern — tolerant of extra spaces and comma-formatted numbers
      const otpRe = /Dear Customer,\s*(\d+)\s+is the OTP.*?for\s+([\d,.]+)\s*Ltrs?\s+to vehicle\s+([A-Z]{2,3}\s*\d{4})/i;

      // Parse all standard WhatsApp lines
      const messages = [];
      for (const rawLine of lines) {
        const line = rawLine.trim(); // strip any leftover \r or spaces
        if (!line) continue;
        const m = line.match(lineRe);
        if (m) {
          messages.push({
            date: m[1].trim(),
            time: m[2].trim(),
            sender: m[3].trim(),
            body: m[4].trim()
          });
        }
      }

      if (messages.length === 0) {
        showToast('Could not read any WhatsApp messages. Make sure the file is a valid WhatsApp export.', 'error');
        return;
      }

      const parsedMap = {};   // orderNo → order object
      const watchedHits = {}; // watchedName → [messages]

      // Watched persons scan — search ALL messages by sender name (partial match)
      // Only include messages posted within the last 3 days (< 3 days from today)
      const watched = (DB.automation.watchedPersons || []).map(p => p.trim().toLowerCase()).filter(Boolean);
      const nowMs = Date.now();
      const threeDaysMs = 3 * 24 * 60 * 60 * 1000;
      messages.forEach(msg => {
        // Convert msg.date (DD/MM/YYYY) to a comparable date
        const parts = msg.date.split('/');
        if (parts.length === 3) {
          const msgDate = new Date(`${parts[2]}-${parts[1].padStart(2,'0')}-${parts[0].padStart(2,'0')}T${msg.time}:00`);
          const msgAge = nowMs - msgDate.getTime();
          if (msgAge > threeDaysMs) return; // skip — older than 3 days
        }
        const senderLower = msg.sender.toLowerCase();
        watched.forEach(w => {
          if (senderLower.includes(w)) {
            if (!watchedHits[w]) watchedHits[w] = [];
            watchedHits[w].push(msg);
          }
        });
      });

      // OTP order extraction
      messages.forEach(msg => {
        const match = msg.body.match(otpRe);
        if (!match) return;

        const orderNo   = match[1].trim();
        const liters    = parseFloat(match[2].replace(/[,\s]/g, ''));
        const rawPlate  = match[3].replace(/\s+/g, ' ').trim().toUpperCase();

        // Convert DD/MM/YYYY → YYYY-MM-DD
        const parts = msg.date.split('/');
        const dd = parts[0], mm = parts[1], yyyy = parts[2];
        const createdDate = `${yyyy}-${mm.padStart(2,'0')}-${dd.padStart(2,'0')}`;

        // ── DATE RANGE FILTER ──────────────────────────────────────
        const fromDate = document.getElementById('waDateFrom')?.value;
        const toDate   = document.getElementById('waDateTo')?.value;
        if (fromDate && createdDate < fromDate) return; // too old
        if (toDate   && createdDate > toDate)   return; // too new
        // ───────────────────────────────────────────────────────────

        const plateInfo  = plateTechMap[rawPlate] || null;
        const regionName = plateInfo ? plateInfo.regionName : DB.currentRegion;
        const techName   = plateInfo ? plateInfo.techName  : null;

        const region     = DB.regions[regionName];
        const isDuplicate = !!(region && region.orders[orderNo]);

        // Keep earliest occurrence if the same OTP appears multiple times
        if (!parsedMap[orderNo]) {
          parsedMap[orderNo] = {
            orderNo, vehiclePlate: rawPlate,
            totalLiters: liters, suppliedTotal: 0,
            allocations: {}, status: 'OPEN',
            createdDate, regionName, techName,
            timestamp: new Date(`${yyyy}-${mm.padStart(2,'0')}-${dd.padStart(2,'0')}T${msg.time}:00`).getTime(),
            isDuplicate,
            selected: !isDuplicate
          };
        }
      });

      waParsedOrders = Object.values(parsedMap).sort((a, b) => a.timestamp - b.timestamp);

      if (waParsedOrders.length === 0) {
        showToast(`Parsed ${messages.length} messages but found 0 MERU OTP orders. Check the file content.`, 'warning');
        // Still proceed to review so user can see the watched-persons alerts
      }

      waShowReview(watchedHits, messages.length);
    }

    function waShowReview(watchedHits, totalMessages) {
      const total     = waParsedOrders.length;
      const dupes     = waParsedOrders.filter(o => o.isDuplicate).length;
      const newOrders = total - dupes;

      let summaryHtml = `<div class="flex gap-4 flex-wrap items-center">
        <span class="badge badge-neutral">📨 ${totalMessages} messages scanned</span>
        <span class="badge badge-success">🆕 ${newOrders} New Order${newOrders!==1?'s':''}</span>
        ${dupes > 0 ? `<span class="badge badge-warning">⚠️ ${dupes} Duplicate${dupes!==1?'s':''} (skipped)</span>` : ''}
        <span class="badge badge-info">📋 ${total} OTP${total!==1?'s':''} Found</span>
      </div>`;

      // Watched person alerts
      const watchKeys = Object.keys(watchedHits);
      if (watchKeys.length > 0) {
        summaryHtml += `<div class="card mt-3" style="background:var(--status-warning-bg);border:1px solid var(--status-warning);">
          <div class="font-semibold text-sm mb-2" style="color:var(--status-warning);">⚠️ Watched Persons Activity Detected</div>`;
        watchKeys.forEach(w => {
          const label = w.split(' ').map(s => s.charAt(0).toUpperCase()+s.slice(1)).join(' ');
          summaryHtml += `<div class="font-semibold text-sm mb-1" style="color:var(--status-warning);">${label} — ${watchedHits[w].length} message(s)</div>`;
          watchedHits[w].slice(0, 6).forEach(msg => {
            summaryHtml += `<div class="text-xs font-mono p-2 mb-1 rounded" style="background:rgba(0,0,0,0.06);">[${msg.date} ${msg.time}] <strong>${msg.sender}:</strong> ${msg.body.substring(0,150)}${msg.body.length>150?'…':''}</div>`;
          });
          if (watchedHits[w].length > 6) summaryHtml += `<div class="text-xs mb-2" style="color:var(--neutral-500);">…and ${watchedHits[w].length-6} more messages</div>`;
        });
        summaryHtml += `</div>`;
        watchKeys.forEach(w => {
          addSystemNotification(`👁️ ${w.toUpperCase()} posted ${watchedHits[w].length} time(s)`, 'Check Import Orders results for details', '#f59e0b20', '⚠️');
        });
      }

      document.getElementById('waParseSummary').innerHTML = summaryHtml;

      // Orders review table
      let tableHtml = '';
      if (waParsedOrders.length === 0) {
        tableHtml = `<div class="card" style="text-align:center;padding:2rem;color:var(--neutral-500);">
          No MERU OTP orders found. The file was parsed successfully (${totalMessages} messages read) but none matched the "Dear Customer, [OTP] is the OTP..." pattern.
        </div>`;
      } else {
        tableHtml = `<div class="table-container" style="max-height:340px;overflow-y:auto;">
          <table class="table">
            <thead><tr>
              <th><input type="checkbox" id="waSelectAll" onchange="waToggleAll(this.checked)" ${newOrders===0?'disabled':''} checked></th>
              <th>Order No (OTP)</th><th>Vehicle</th><th>Litres</th><th>Date</th><th>Technician</th><th>Region</th><th>Status</th>
            </tr></thead><tbody>`;
        waParsedOrders.forEach((o, idx) => {
          tableHtml += `<tr style="${o.isDuplicate?'opacity:0.5;':''}">
            <td><input type="checkbox" class="waOrderCheck" data-idx="${idx}" ${o.selected?'checked':''} ${o.isDuplicate?'disabled':''}></td>
            <td class="font-mono font-semibold">${o.orderNo}</td>
            <td class="font-mono">${o.vehiclePlate}</td>
            <td>${o.totalLiters}L</td>
            <td>${o.createdDate}</td>
            <td>${o.techName || '<span style="color:var(--status-warning);">⚠️ Unknown plate</span>'}</td>
            <td>${o.regionName}</td>
            <td>${o.isDuplicate ? '<span class="badge badge-warning">Duplicate</span>' : '<span class="badge badge-success">New</span>'}</td>
          </tr>`;
        });
        tableHtml += `</tbody></table></div>`;
      }

      document.getElementById('waOrdersPreview').innerHTML = tableHtml;
      document.getElementById('waStep1').style.display = 'none';
      document.getElementById('waStep2').style.display = 'block';
      document.getElementById('waStep1Badge').className = 'badge badge-success';
      document.getElementById('waStep2Badge').className = 'badge badge-info';
    }

    function waToggleAll(checked) {
      document.querySelectorAll('.waOrderCheck:not([disabled])').forEach(cb => {
        const idx = parseInt(cb.dataset.idx);
        cb.checked = checked;
        waParsedOrders[idx].selected = checked;
      });
    }

    function waBackToStep1() {
      document.getElementById('waStep1').style.display = 'block';
      document.getElementById('waStep2').style.display = 'none';
      document.getElementById('waStep1Badge').className = 'badge badge-info';
      document.getElementById('waStep2Badge').className = 'badge badge-neutral';
    }

    function waConfirmImport() {
      document.querySelectorAll('.waOrderCheck').forEach(cb => {
        waParsedOrders[parseInt(cb.dataset.idx)].selected = cb.checked;
      });

      const toImport = waParsedOrders.filter(o => o.selected && !o.isDuplicate);
      if (toImport.length === 0) return showToast('No orders selected for import', 'warning');

      let imported = 0, unknownTech = 0;
      const importedOrderNos = [];

      toImport.forEach(o => {
        const regionData = DB.regions[o.regionName];
        if (!regionData) return;
        let allocations = {};
        if (o.techName && regionData.technicians.includes(o.techName)) {
          allocations[o.techName] = o.totalLiters;
        } else {
          unknownTech++;
        }
        regionData.orders[o.orderNo] = {
          orderNo: o.orderNo, vehiclePlate: o.vehiclePlate,
          totalLiters: o.totalLiters, suppliedTotal: 0,
          allocations, status: 'OPEN', createdDate: o.createdDate,
          autoImported: true  // ← tag so supply log can show badge
        };
        importedOrderNos.push(o.orderNo);
        imported++;
      });

      save();

      // Build result with full CRUD table
      let resultHtml = `<div class="card mb-4" style="background:var(--status-success-bg);border:1px solid var(--status-success);">
        <div class="font-semibold" style="color:var(--status-success);">✅ ${imported} Order${imported!==1?'s':''} Imported Successfully</div>
        ${unknownTech > 0 ? `<div class="text-sm mt-1" style="color:var(--status-warning);">⚠️ ${unknownTech} order(s) have no technician — vehicle plate not mapped. Use the edit buttons below or go to Orders page to allocate.</div>` : ''}
        <div class="text-sm mt-2" style="color:var(--neutral-600);">You can edit or delete any imported order directly below before closing.</div>
      </div>`;

      resultHtml += `<div class="table-container" style="max-height:400px;overflow-y:auto;">
        <table class="table">
          <thead><tr><th>Order No</th><th>Vehicle</th><th>Litres</th><th>Date</th><th>Allocated To</th><th>Region</th><th>Actions</th></tr></thead>
          <tbody id="waImportedOrdersBody">`;

      toImport.forEach(o => {
        const allocated = (o.techName && DB.regions[o.regionName]?.technicians?.includes(o.techName)) ? o.techName : '—';
        resultHtml += waImportedRowHtml(o.orderNo, o.vehiclePlate, o.totalLiters, o.createdDate, allocated, o.regionName);
      });

      resultHtml += `</tbody></table></div>`;
      document.getElementById('waStep2').style.display = 'none';
      document.getElementById('waStep3').style.display = 'block';
      document.getElementById('waStep2Badge').className = 'badge badge-success';
      document.getElementById('waStep3Badge').className = 'badge badge-info';
      document.getElementById('waImportResult').innerHTML = resultHtml;
      showToast(`${imported} orders imported!`, 'success');
    }

    function waImportedRowHtml(orderNo, vehiclePlate, totalLiters, createdDate, allocated, regionName) {
      return `<tr id="warow_${orderNo}">
        <td class="font-mono font-semibold">${orderNo}</td>
        <td class="font-mono">${vehiclePlate}</td>
        <td>${totalLiters}L</td>
        <td>${createdDate}</td>
        <td>${allocated !== '—' ? allocated : '<span style="color:var(--status-warning);">⚠️ Unallocated</span>'}</td>
        <td class="text-xs">${regionName}</td>
        <td>
          <div class="flex gap-1">
            <button class="btn btn-secondary btn-sm" onclick="waEditImportedOrder('${orderNo}','${regionName}')"><i class="fa-regular fa-pen"></i> Edit</button>
            <button class="btn btn-sm" style="background:var(--status-danger-bg);color:var(--status-danger);border:1px solid var(--status-danger);" onclick="waDeleteImportedOrder('${orderNo}','${regionName}')"><i class="fa-regular fa-trash"></i></button>
          </div>
        </td>
      </tr>`;
    }

    function waEditImportedOrder(orderNo, regionName) {
      const region = DB.regions[regionName];
      if (!region || !region.orders[orderNo]) return showToast('Order not found', 'error');
      const order = region.orders[orderNo];
      const techOptions = region.technicians.map(t => `<option value="${t}" ${Object.keys(order.allocations)[0]===t?'selected':''}>${t}</option>`).join('');
      const newOrderNo = prompt('Order Number:', order.orderNo);
      if (newOrderNo === null) return;
      const newPlate = prompt('Vehicle Plate:', order.vehiclePlate);
      if (newPlate === null) return;
      const newLiters = prompt('Total Litres:', order.totalLiters);
      if (newLiters === null) return;
      const newDate = prompt('Date (YYYY-MM-DD):', order.createdDate);
      if (newDate === null) return;

      const parsedLiters = parseFloat(newLiters);
      if (isNaN(parsedLiters) || parsedLiters <= 0) return showToast('Invalid litres value', 'error');

      // Handle order number change
      if (newOrderNo.trim() !== orderNo) {
        if (region.orders[newOrderNo.trim()]) return showToast('Order number already exists', 'error');
        region.orders[newOrderNo.trim()] = { ...order, orderNo: newOrderNo.trim() };
        delete region.orders[orderNo];
      } else {
        region.orders[orderNo].vehiclePlate = newPlate.trim().toUpperCase();
        region.orders[orderNo].totalLiters = parsedLiters;
        region.orders[orderNo].createdDate = newDate.trim();
      }
      save();
      // Refresh that row
      const finalOrderNo = newOrderNo.trim();
      const finalOrder = region.orders[finalOrderNo];
      const allocated = Object.keys(finalOrder.allocations)[0] || '—';
      const row = document.getElementById(`warow_${orderNo}`);
      if (row) row.outerHTML = waImportedRowHtml(finalOrderNo, finalOrder.vehiclePlate, finalOrder.totalLiters, finalOrder.createdDate, allocated, regionName);
      showToast('Order updated', 'success');
    }

    function waDeleteImportedOrder(orderNo, regionName) {
      if (!confirm(`Delete imported order ${orderNo}?`)) return;
      const region = DB.regions[regionName];
      if (region && region.orders[orderNo]) {
        delete region.orders[orderNo];
        save();
      }
      const row = document.getElementById(`warow_${orderNo}`);
      if (row) {
        row.style.transition = 'opacity 0.3s';
        row.style.opacity = '0';
        setTimeout(() => row.remove(), 300);
      }
      showToast(`Order ${orderNo} deleted`, 'info');
    }

    // ---- AUTO DAILY ENTRY IMPORT ----
    let dailyAutoRows = []; // parsed rows from excel

    function openDailyAutoImport() {
      dailyAutoRows = [];
      document.getElementById('dailyAutoPreview').style.display = 'none';
      document.getElementById('dailyAutoResult').style.display = 'none';
      openModal('dailyAutoImportModal');
    }

    function downloadDailyImportTemplate() {
      if (typeof XLSX === 'undefined') return showToast('XLSX library not loaded', 'error');
      const wb = XLSX.utils.book_new();
      const ws = XLSX.utils.aoa_to_sheet([
        ['Technician', 'Date', 'Total Supplied'],
        ['Royd', '2026-03-12', 1800],
        ['ISAAC CCS', '2026-03-12', 500],
        ['LUNGILE JAULA', '2026-03-12', 950],
        ['Fackson', '2026-03-12', 750]
      ]);
      XLSX.utils.book_append_sheet(wb, ws, 'Daily Supply');
      XLSX.writeFile(wb, 'CCS_Daily_Import_Template.xlsx');
    }

    function dailyAutoHandleFile(event) {
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = e => {
        try {
          const wb = XLSX.read(new Uint8Array(e.target.result), { type: 'array', cellDates: true });
          const ws = wb.Sheets[wb.SheetNames[0]];
          const rows = XLSX.utils.sheet_to_json(ws, { defval: '' });
          dailyAutoProcessRows(rows);
        } catch (err) {
          showToast('Error reading file: ' + err.message, 'error');
        }
      };
      reader.readAsArrayBuffer(file);
    }

    function parseFlexDate(val) {
      if (!val) return null;
      // If already a Date object (from XLSX with cellDates)
      if (val instanceof Date) return val.toISOString().slice(0, 10);
      const str = String(val).trim();
      // YYYY-MM-DD
      if (/^\d{4}-\d{2}-\d{2}$/.test(str)) return str;
      // DD/MM/YYYY
      const m = str.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})$/);
      if (m) return `${m[3]}-${m[2].padStart(2,'0')}-${m[1].padStart(2,'0')}`;
      // Excel serial number
      const serial = parseFloat(str);
      if (!isNaN(serial) && serial > 40000) {
        const d = new Date((serial - 25569) * 86400 * 1000);
        return d.toISOString().slice(0, 10);
      }
      return null;
    }

    function normalizeTechName(name, regionTechs) {
      // Try exact match first
      const exactMatch = regionTechs.find(t => t.toLowerCase() === String(name).toLowerCase().trim());
      if (exactMatch) return exactMatch;
      // Partial match
      const nameLower = String(name).toLowerCase().trim();
      const partial = regionTechs.find(t => t.toLowerCase().includes(nameLower) || nameLower.includes(t.toLowerCase()));
      return partial || null;
    }

    function dailyAutoProcessRows(rows) {
      const region = DB.regions[DB.currentRegion];
      const techNames = region.technicians;
      const results = [];

      // Normalize column names (case insensitive)
      rows.forEach((row, rowIdx) => {
        const keys = Object.keys(row);
        const techKey = keys.find(k => /tech/i.test(k) || /name/i.test(k));
        const dateKey = keys.find(k => /date/i.test(k));
        const supplyKey = keys.find(k => /supply|supplied|total|litre|liter/i.test(k));

        if (!techKey || !dateKey || !supplyKey) return;

        const rawTech = String(row[techKey]).trim();
        const rawDate = row[dateKey];
        const rawSupply = row[supplyKey];

        const techName = normalizeTechName(rawTech, techNames);
        const date = parseFlexDate(rawDate);
        const totalSupplied = parseFloat(String(rawSupply).replace(/[^0-9.]/g, ''));

        if (!rawTech || !date || isNaN(totalSupplied) || totalSupplied <= 0) return;

        // Calculate how to distribute this supply across oldest open orders
        const openOrders = Object.values(region.orders)
          .filter(o => {
            const balance = o.totalLiters - o.suppliedTotal;
            return balance > 0 && o.allocations && o.allocations[techName];
          })
          .sort((a, b) => (a.createdDate || '').localeCompare(b.createdDate || ''));

        let remaining = totalSupplied;
        const entries = [];

        for (const order of openOrders) {
          if (remaining <= 0) break;
          const orderBalance = order.totalLiters - order.suppliedTotal;
          const toFill = Math.min(remaining, orderBalance);
          entries.push({ orderNo: order.orderNo, techName, supplied: toFill, date, vehiclePlate: order.vehiclePlate, orderBalance });
          remaining -= toFill;
        }

        const overage = remaining > 0 ? remaining : 0;

        results.push({
          rawTech,
          techName,
          date,
          totalSupplied,
          entries,
          overage,
          noMatch: !techName,
          rowIdx
        });
      });

      dailyAutoRows = results;
      dailyAutoShowPreview();
    }

    function dailyAutoShowPreview() {
      const previewDiv = document.getElementById('dailyAutoPreview');
      const summaryDiv = document.getElementById('dailyAutoSummary');
      const entriesDiv = document.getElementById('dailyAutoEntriesPreview');

      const matched = dailyAutoRows.filter(r => !r.noMatch);
      const unmatched = dailyAutoRows.filter(r => r.noMatch);
      const totalEntries = matched.reduce((s, r) => s + r.entries.length, 0);
      const totalOverage = matched.reduce((s, r) => s + r.overage, 0);

      summaryDiv.innerHTML = `<div class="flex gap-4 flex-wrap">
        <div><span class="badge badge-success">${matched.length} Technician(s) Matched</span></div>
        <div><span class="badge badge-info">${totalEntries} Daily Entries to Create</span></div>
        ${unmatched.length > 0 ? `<div><span class="badge badge-danger">${unmatched.length} Unmatched</span></div>` : ''}
        ${totalOverage > 0 ? `<div><span class="badge badge-warning">${totalOverage}L Overage (no orders left)</span></div>` : ''}
      </div>`;

      let html = '';

      if (unmatched.length > 0) {
        html += `<div class="card mb-3" style="background:var(--status-danger-bg);border:1px solid var(--status-danger);">
          <div class="font-semibold text-sm mb-1" style="color:var(--status-danger);">❌ Unmatched Technicians (will be skipped):</div>
          ${unmatched.map(r => `<div class="text-sm font-mono">"${r.rawTech}" — not found in region "${DB.currentRegion}"</div>`).join('')}
        </div>`;
      }

      matched.forEach(r => {
        html += `<div class="card mb-3" style="background:var(--neutral-50);">
          <div class="flex items-center justify-between mb-2">
            <div class="font-semibold">${r.techName} <span class="text-sm font-normal" style="color:var(--neutral-500);">${r.date}</span></div>
            <div class="badge badge-info">${r.totalSupplied}L total</div>
          </div>
          <div class="table-container"><table class="table">
            <thead><tr><th>Order</th><th>Vehicle</th><th>To Enter</th><th>Order Balance</th></tr></thead>
            <tbody>
              ${r.entries.map(e => `<tr>
                <td class="font-mono">${e.orderNo}</td>
                <td class="font-mono">${e.vehiclePlate}</td>
                <td class="font-semibold">${e.supplied}L</td>
                <td>${e.orderBalance}L</td>
              </tr>`).join('')}
              ${r.overage > 0 ? `<tr style="background:var(--status-warning-bg);">
                <td colspan="2" style="color:var(--status-warning);font-weight:600;">⚠️ Overage (no orders left)</td>
                <td style="color:var(--status-warning);font-weight:600;">${r.overage}L</td>
                <td>—</td>
              </tr>` : ''}
            </tbody>
          </table></div>
        </div>`;
      });

      if (matched.length === 0) {
        html = `<div class="card" style="text-align:center;color:var(--neutral-500);padding:2rem;">No matching technicians found. Check that technician names in your Excel match this region's technician list.</div>`;
      }

      entriesDiv.innerHTML = html;
      previewDiv.style.display = 'block';
    }

    function dailyAutoConfirmImport() {
      const region = DB.regions[DB.currentRegion];
      const matched = dailyAutoRows.filter(r => !r.noMatch);
      let totalSaved = 0;
      const importedEntries = []; // for the result log

      matched.forEach(r => {
        const date = r.date;
        if (!region.dailyLog[date]) region.dailyLog[date] = [];

        r.entries.forEach(e => {
          const order = region.orders[e.orderNo];
          if (!order || order.status === 'CLOSED') return;
          const entryIdx = region.dailyLog[date].length;
          region.dailyLog[date].push({ orderNo: e.orderNo, technician: r.techName, supplied: e.supplied, autoImported: true });
          order.suppliedTotal += e.supplied;
          importedEntries.push({ date, techName: r.techName, orderNo: e.orderNo, supplied: e.supplied, vehiclePlate: e.vehiclePlate, entryIdx: region.dailyLog[date].length - 1 });
          totalSaved++;
        });

        if (r.overage > 0) {
          region.dailyLog[date].push({
            technician: r.techName, supplied: r.overage,
            comment: `Auto-import overage: ${r.overage}L — no remaining open orders`,
            unallocated: true
          });
          importedEntries.push({ date, techName: r.techName, orderNo: '—', supplied: r.overage, vehiclePlate: '—', isOverage: true, entryIdx: region.dailyLog[date].length - 1 });
        }
      });

      // Close orders that are now full
      Object.values(region.orders).forEach(o => {
        if (o.suppliedTotal >= o.totalLiters) o.status = 'CLOSED';
      });

      save();

      // Build CRUD result table
      let resultHtml = `<div class="card mb-3" style="background:var(--status-success-bg);border:1px solid var(--status-success);">
        <div class="font-semibold" style="color:var(--status-success);">✅ ${totalSaved} Daily Entries Applied</div>
        <div class="text-sm mt-1" style="color:var(--neutral-600);">Review the entries below. You can edit or delete any entry if the automation made a mistake.</div>
      </div>
      <div class="table-container" style="max-height:420px;overflow-y:auto;">
        <table class="table">
          <thead><tr><th>Date</th><th>Technician</th><th>Order</th><th>Vehicle</th><th>Supplied</th><th>Type</th><th>Actions</th></tr></thead>
          <tbody id="dailyAutoResultBody">`;

      importedEntries.forEach((e, i) => {
        resultHtml += dailyAutoEntryRowHtml(e, i);
      });

      resultHtml += `</tbody></table></div>`;

      document.getElementById('dailyAutoPreview').style.display = 'none';
      document.getElementById('dailyAutoResult').innerHTML = resultHtml;
      document.getElementById('dailyAutoResult').style.display = 'block';

      // Store imported entries for CRUD reference
      window._dailyAutoImported = importedEntries;
      showToast(`${totalSaved} daily entries applied!`, 'success');
    }

    function dailyAutoEntryRowHtml(e, i) {
      const typeBadge = e.isOverage
        ? `<span class="badge badge-warning">Overage</span>`
        : `<span class="badge badge-success">Allocated</span>`;
      return `<tr id="darow_${i}">
        <td>${e.date}</td>
        <td>${e.techName}</td>
        <td class="font-mono">${e.orderNo}</td>
        <td class="font-mono text-xs">${e.vehiclePlate}</td>
        <td class="font-semibold">${e.supplied}L</td>
        <td>${typeBadge}</td>
        <td>
          <div class="flex gap-1">
            <button class="btn btn-secondary btn-sm" onclick="dailyAutoEditEntry(${i})"><i class="fa-regular fa-pen"></i></button>
            <button class="btn btn-sm" style="background:var(--status-danger-bg);color:var(--status-danger);border:1px solid var(--status-danger);" onclick="dailyAutoDeleteEntry(${i})"><i class="fa-regular fa-trash"></i></button>
          </div>
        </td>
      </tr>`;
    }

    function dailyAutoEditEntry(i) {
      const e = window._dailyAutoImported[i];
      if (!e) return;
      const region = DB.regions[DB.currentRegion];
      const entries = region.dailyLog[e.date];
      if (!entries || !entries[e.entryIdx]) return showToast('Entry no longer found', 'error');
      const entry = entries[e.entryIdx];

      const newSupplied = prompt(`Edit supplied litres for ${e.techName} on ${e.date} (Order: ${e.orderNo}):`, entry.supplied);
      if (newSupplied === null) return;
      const parsed = parseFloat(newSupplied);
      if (isNaN(parsed) || parsed < 0) return showToast('Invalid value', 'error');

      // Adjust order total
      if (!entry.unallocated && entry.orderNo) {
        const order = region.orders[entry.orderNo];
        if (order) order.suppliedTotal = order.suppliedTotal - entry.supplied + parsed;
        // Re-evaluate order status
        if (order && order.suppliedTotal >= order.totalLiters) order.status = 'CLOSED';
        else if (order) order.status = 'OPEN';
      }

      entry.supplied = parsed;
      window._dailyAutoImported[i].supplied = parsed;
      save();

      // Refresh row
      const row = document.getElementById(`darow_${i}`);
      if (row) row.outerHTML = dailyAutoEntryRowHtml(window._dailyAutoImported[i], i);
      showToast('Entry updated', 'success');
    }

    function dailyAutoDeleteEntry(i) {
      const e = window._dailyAutoImported[i];
      if (!e) return;
      if (!confirm(`Delete entry: ${e.techName} — ${e.supplied}L on ${e.date}?`)) return;

      const region = DB.regions[DB.currentRegion];
      const entries = region.dailyLog[e.date];
      if (entries && entries[e.entryIdx]) {
        const entry = entries[e.entryIdx];
        if (!entry.unallocated && entry.orderNo) {
          const order = region.orders[entry.orderNo];
          if (order) {
            order.suppliedTotal -= entry.supplied;
            if (order.suppliedTotal < order.totalLiters) order.status = 'OPEN';
          }
        }
        entries.splice(e.entryIdx, 1);
        if (entries.length === 0) delete region.dailyLog[e.date];
        // Update entryIdx for subsequent entries on the same date
        window._dailyAutoImported.forEach((other, j) => {
          if (j > i && other.date === e.date && other.entryIdx > e.entryIdx) other.entryIdx--;
        });
      }
      save();
      const row = document.getElementById(`darow_${i}`);
      if (row) {
        row.style.transition = 'opacity 0.3s';
        row.style.opacity = '0';
        setTimeout(() => row.remove(), 300);
      }
      showToast('Entry deleted', 'info');
    }

    // ---- WATCHED PERSONS ----
    function openWatchedPersonsModal() {
      renderWatchedPersonsList();
      openModal('watchedPersonsModal');
    }

    function renderWatchedPersonsList() {
      const list = DB.automation.watchedPersons || [];
      const container = document.getElementById('watchedPersonsList');
      if (!list.length) {
        container.innerHTML = `<div class="text-sm" style="color:var(--neutral-400);">No one on the watch list yet.</div>`;
        return;
      }
      container.innerHTML = list.map((p, i) => `
        <div class="tech-alloc-row mb-2">
          <div class="tech-avatar" style="background:var(--status-warning-bg);color:var(--status-warning);">
            <i class="fa-regular fa-eye"></i>
          </div>
          <div class="tech-details"><div class="tech-name">${p}</div></div>
          <div class="tech-stats">
            <button class="btn btn-icon btn-ghost btn-sm" onclick="removeWatchedPerson(${i})"><i class="fa-regular fa-trash"></i></button>
          </div>
        </div>`).join('');
    }

    function addWatchedPerson() {
      const name = document.getElementById('watchPersonInput').value.trim();
      if (!name) return showToast('Enter a name first', 'warning');
      if (!DB.automation.watchedPersons) DB.automation.watchedPersons = [];
      if (DB.automation.watchedPersons.some(p => p.toLowerCase() === name.toLowerCase())) {
        return showToast('Already on watch list', 'warning');
      }
      DB.automation.watchedPersons.push(name);
      document.getElementById('watchPersonInput').value = '';
      renderWatchedPersonsList();
    }

    function removeWatchedPerson(idx) {
      DB.automation.watchedPersons.splice(idx, 1);
      renderWatchedPersonsList();
    }

    function saveWatchedPersons() {
      save();
      closeModal('watchedPersonsModal');
      showToast('Watch list saved!', 'success');
    }

    // ---- SMART ALERTS ----
    // Tracks which alert keys have already been shown in this session
    const _alertsShown = new Set();

    function runSmartAlerts() {
      if (typeof _notifData === 'undefined') return;
      const today = new Date().toISOString().slice(0, 10);
      const twoDaysAgo = new Date(Date.now() - 2 * 86400000).toISOString().slice(0, 10);

      Object.entries(DB.regions).forEach(([rName, region]) => {

        // ── ALERT 1: Open orders inactive for more than 2 days ──────────
        Object.values(region.orders).forEach(order => {
          if (order.status === 'CLOSED') return;
          const balance = order.totalLiters - order.suppliedTotal;
          if (balance <= 0) return; // effectively closed

          // Find the most recent supply date for this order
          let lastSupplyDate = order.createdDate || null;
          Object.entries(region.dailyLog).forEach(([date, entries]) => {
            entries.forEach(e => {
              if (e.orderNo === order.orderNo && date > lastSupplyDate) {
                lastSupplyDate = date;
              }
            });
          });

          if (lastSupplyDate && lastSupplyDate < twoDaysAgo) {
            const alertKey = `inactive_order_${rName}_${order.orderNo}_${today}`;
            if (!_alertsShown.has(alertKey)) {
              _alertsShown.add(alertKey);
              const daysSince = Math.round((Date.now() - new Date(lastSupplyDate).getTime()) / 86400000);
              addSystemNotification(
                `⚠️ Inactive Order: ${order.orderNo}`,
                `No supply activity for ${daysSince} day${daysSince !== 1 ? 's' : ''} · ${rName} · Balance: ${balance}L`,
                'var(--status-warning-bg)',
                '⏰'
              );
            }
          }
        });

        // ── ALERT 2: Technicians with no supply today ─────────────────────
        if (region.technicians.length === 0) return;
        const todayEntries = region.dailyLog[today] || [];
        const techsActiveToday = new Set(todayEntries.map(e => e.technician));

        // Only fire if there IS some activity today in this region (so we don't spam on days before anyone starts)
        // OR if there are open orders assigned to technicians
        const hasOpenOrders = Object.values(region.orders).some(o =>
          o.status !== 'CLOSED' && (o.totalLiters - o.suppliedTotal) > 0 && Object.keys(o.allocations || {}).length > 0
        );

        if (hasOpenOrders) {
          region.technicians.forEach(tech => {
            // Only flag techs who have an open order allocated to them
            const hasOpenAllocation = Object.values(region.orders).some(o =>
              o.status !== 'CLOSED' && (o.totalLiters - o.suppliedTotal) > 0 && (o.allocations || {})[tech]
            );
            if (!hasOpenAllocation) return;

            if (!techsActiveToday.has(tech)) {
              const alertKey = `idle_tech_${rName}_${tech}_${today}`;
              if (!_alertsShown.has(alertKey)) {
                _alertsShown.add(alertKey);
                addSystemNotification(
                  `🔔 No Supply Today: ${tech}`,
                  `${tech} has not recorded any supply for today (${today}) · ${rName}`,
                  'var(--status-info-bg)',
                  '📋'
                );
              }
            }
          });
        }
      });
    }


    function addSystemNotification(title, desc, bg, icon) {
      if (typeof _notifData === 'undefined') return;
      _notifData.unshift({ title, desc, bg: bg || 'var(--status-info-bg)', icon: icon || 'ℹ️', action: null });
      renderNotifications();
    }

    // ============================================================
    // ===== PHASE 1: TECHNICIAN DATA (all regions merged) ========
    // ============================================================
    const TECHNICIAN_DATA = {
      nrw: {
        "IHS_NRW_001M":"KENNY","IHS_NRW_002M":"LOMBE","IHS_NRW_003M":"KENNY",
        "IHS_NRW_004M":"KENNY","IHS_NRW_005M":"KENNY","IHS_NRW_006M":"LEN",
        "IHS_NRW_007M":"LOMBE","IHS_NRW_008M":"LOMBE","IHS_NRW_009M":"LOMBE",
        "IHS_NRW_011M":"KENNY","IHS_NRW_013M":"KENNY","IHS_NRW_014M":"LEN",
        "IHS_NRW_015M":"KENNY","IHS_NRW_016M":"LEN","IHS_NRW_017M":"LOMBE",
        "IHS_NRW_018M":"KENNY","IHS_NRW_020M":"LEN","IHS_NRW_021M":"KENNY",
        "IHS_NRW_023M":"KENNY","IHS_NRW_024M":"LOMBE","IHS_NRW_026M":"LEN",
        "IHS_NRW_028M":"LEN","IHS_NRW_029M":"LEN","IHS_NRW_032M":"ABISHY",
        "IHS_NRW_035M":"LEN","IHS_NRW_036M":"ABISHY","IHS_NRW_037M":"ABISHY",
        "IHS_NRW_038M":"ABISHY","IHS_NRW_039M":"ABISHY","IHS_NRW_040M":"MCGLEN",
        "IHS_NRW_042M":"ABISHY","IHS_NRW_043M":"ABISHY","IHS_NRW_044M":"ABISHY",
        "IHS_NRW_046M":"JOHNATHAN","IHS_NRW_047M":"JOHNATHAN","IHS_NRW_050M":"KENNY",
        "IHS_NRW_051M":"KENNY","IHS_NRW_052M":"KENNY","IHS_NRW_054M":"LEN",
        "IHS_NRW_056M":"LEN","IHS_NRW_059M":"KENNY",
        "IHS_NRW_201A":"ABISHY","IHS_NRW_202A":"JOHNATHAN","IHS_NRW_203A":"ABISHY",
        "IHS_NRW_204A":"MCGLEN","IHS_NRW_206A":"ABISHY","IHS_NRW_207A":"MCGLEN",
        "IHS_NRW_208A":"ABISHY","IHS_NRW_209A":"JOHNATHAN","IHS_NRW_212A":"KENNY",
        "IHS_NRW_213A":"ABISHY","IHS_NRW_214A":"JOHNATHAN","IHS_NRW_215A":"MCGLEN",
        "IHS_NRW_216A":"MCGLEN","IHS_NRW_217A":"LOMBE","IHS_NRW_219A":"KENNY",
        "IHS_NRW_220A":"LEN","IHS_NRW_222A":"KENNY","IHS_NRW_223A":"JOHNATHAN",
        "IHS_NRW_224A":"ABISHY","IHS_NRW_225A":"ABISHY","IHS_NRW_226A":"JOHNATHAN",
        "IHS_NRW_227A":"JOHNATHAN","IHS_NRW_229A":"ABISHY","IHS_NRW_230A":"ABISHY",
        "IHS_NRW_231A":"LOMBE","IHS_NRW_232A":"ABISHY","IHS_NRW_233A":"LOMBE",
        "IHS_NRW_235A":"LOMBE","IHS_NRW_236A":"KENNY","IHS_NRW_239A":"JOHNATHAN",
        "IHS_NRW_240A":"MCGLEN","IHS_NRW_241A":"MCGLEN","IHS_NRW_243A":"ABISHY",
        "IHS_NRW_245A":"MCGLEN","IHS_NRW_247A":"LEN","IHS_NRW_249A":"MCGLEN",
        "IHS_NRW_250A":"MCGLEN","IHS_NRW_251A":"MCGLEN","IHS_NRW_253A":"MCGLEN",
        "IHS_NRW_255A":"MCGLEN","IHS_NRW_257A":"LEN","IHS_NRW_258A":"LEN",
        "IHS_NRW_260A":"LOMBE","IHS_NRW_263A":"KENNY","IHS_NRW_264A":"KENNY",
        "IHS_NRW_266A":"KENNY","IHS_NRW_267A":"KENNY","IHS_NRW_268A":"KENNY",
        "IHS_NRW_269A":"LOMBE"
      },
      eastern: {
        "IHS_EST_001M":"HOWARD","IHS_EST_002M":"HOWARD","IHS_EST_006M":"PATRICK",
        "IHS_EST_007M":"HOWARD","IHS_EST_008M":"HOWARD","IHS_EST_009M":"HOWARD",
        "IHS_EST_010M":"HOWARD","IHS_EST_011M":"HOWARD","IHS_EST_012M":"PATRICK",
        "IHS_EST_013M":"HOWARD","IHS_EST_014M":"HOWARD","IHS_EST_015M":"PATRICK",
        "IHS_EST_016M":"ZKE/GEORGE","IHS_EST_017M":"PATRICK","IHS_EST_018M":"HOWARD",
        "IHS_EST_020M":"HOWARD","IHS_EST_021M":"HOWARD","IHS_EST_022M":"HOWARD",
        "IHS_EST_023M":"HOWARD","IHS_EST_024M":"PATRICK","IHS_EST_025M":"PATRICK",
        "IHS_EST_026M":"HOWARD","IHS_EST_028M":"HOWARD","IHS_EST_029M":"ZKE/GEORGE",
        "IHS_EST_030M":"ZKE/GEORGE","IHS_EST_032M":"CHARLES","IHS_EST_033M":"HOWARD",
        "IHS_EST_035M":"CHARLES","IHS_EST_037M":"HOWARD","IHS_EST_039M":"ZKE/GEORGE",
        "IHS_EST_040M":"ZKE/GEORGE","IHS_EST_044M":"HOWARD","IHS_EST_045M":"ZKE/GEORGE",
        "IHS_EST_046M":"HOWARD","IHS_EST_047M":"PATRICK",
        "IHS_EST_201A":"HOWARD","IHS_EST_202A":"PATRICK","IHS_EST_203A":"PATRICK",
        "IHS_EST_206A":"CHARLES","IHS_EST_207A":"ZKE/GEORGE","IHS_EST_208A":"CHARLES",
        "IHS_EST_209A":"PATRICK","IHS_EST_210A":"CHARLES","IHS_EST_211A":"HOWARD",
        "IHS_EST_214A":"CHARLES","IHS_EST_216A":"CHARLES","IHS_EST_218A":"HOWARD",
        "IHS_EST_221A":"HOWARD","IHS_EST_222A":"HOWARD","IHS_EST_224A":"CHARLES",
        "IHS_EST_225A":"CHARLES","IHS_EST_226A":"CHARLES","IHS_EST_227A":"HOWARD",
        "IHS_EST_228A":"PATRICK","IHS_EST_229A":"CHARLES","IHS_EST_230A":"HOWARD",
        "IHS_EST_231A":"HOWARD","IHS_EST_232A":"HOWARD","IHS_EST_233A":"HOWARD",
        "IHS_EST_234A":"CHARLES","IHS_EST_235A":"CHARLES","IHS_EST_236A":"PATRICK",
        "IHS_EST_237A":"HOWARD","IHS_EST_238A":"HOWARD","IHS_EST_240A":"CHARLES",
        "IHS_EST_241A":"CHARLES","IHS_EST_244A":"ZKE/GEORGE","IHS_EST_245A":"ZKE/GEORGE",
        "IHS_EST_246A":"HOWARD","IHS_EST_247A":"PATRICK","IHS_EST_249A":"CHARLES",
        "IHS_EST_250A":"ZKE/GEORGE","IHS_EST_251A":"ZKE/GEORGE","IHS_EST_252A":"HOWARD",
        "IHS_EST_253A":"ZKE/GEORGE","IHS_EST_254A":"HOWARD","IHS_EST_257A":"ZKE/GEORGE",
        "IHS_EST_258A":"HOWARD","IHS_EST_259A":"ZKE/GEORGE","IHS_EST_260A":"ZKE/GEORGE",
        "IHS_EST_261A":"HOWARD","IHS_EST_262A":"HOWARD","IHS_EST_263A":"ZKE/GEORGE",
        "IHS_EST_265A":"HOWARD","IHS_EST_266A":"CHARLES","IHS_EST_267A":"CHARLES",
        "IHS_EST_269A":"HOWARD","IHS_EST_270A":"CHARLES","IHS_EST_271A":"HOWARD",
        "IHS_EST_272A":"CHARLES","IHS_EST_273A":"HOWARD","IHS_EST_274A":"HOWARD",
        "IHS_EST_275A":"HOWARD","IHS_EST_276A":"HOWARD","IHS_EST_277A":"HOWARD",
        "IHS_EST_278A":"HOWARD","IHS_EST_279A":"HOWARD","IHS_EST_280A":"ZKE/GEORGE",
        "IHS_EST_281A":"PATRICK","IHS_EST_282A":"HOWARD","IHS_EST_284A":"HOWARD",
        "IHS_EST_285A":"PATRICK","IHS_EST_286A":"HOWARD","IHS_EST_288A":"HOWARD",
        "IHS_EST_289A":"HOWARD","IHS_EST_290A":"HOWARD","IHS_EST_291A":"ZKE/GEORGE",
        "IHS_EST_292A":"PATRICK","IHS_EST_293A":"PATRICK","IHS_EST_294A":"PATRICK",
        "IHS_EST_295A":"ZKE/GEORGE","IHS_EST_296A":"ZKE/GEORGE","IHS_EST_297A":"ZKE/GEORGE",
        "IHS_EST_298A":"ZKE/GEORGE","IHS_EST_299A":"ZKE/GEORGE","IHS_EST_300A":"HOWARD",
        "IHS_EST_302A":"HOWARD","IHS_EST_303A":"ZKE/GEORGE","IHS_EST_304A":"ZKE/GEORGE",
        "IHS_EST_307A":"ZKE/GEORGE","IHS_EST_308A":"PATRICK","IHS_EST_309A":"ZKE/GEORGE",
        "IHS_EST_310A":"HOWARD","IHS_EST_311A":"ZKE/GEORGE","IHS_EST_312A":"HOWARD",
        "IHS_EST_313A":"HOWARD","IHS_EST_314A":"HOWARD","IHS_EST_315A":"ZKE/GEORGE",
        "IHS_EST_316A":"HOWARD","IHS_EST_317A":"ZKE/GEORGE","IHS_NTH_061M":"HOWARD"
      },
      old_cbt: {
        "IHS_CBT_110M":"LAWRANCE","IHS_CBT_124M":"LAWRANCE","IHS_CBT_125M":"LAWRANCE",
        "IHS_CBT_128M":"LAWRANCE","IHS_CBT_130M":"LAWRANCE","IHS_CBT_131M":"LAWRANCE",
        "IHS_CBT_135M":"LAWRANCE","IHS_CBT_136M":"LAWRANCE","IHS_CBT_138M":"LAWRANCE",
        "IHS_CBT_141M":"LAWRANCE","IHS_CBT_143M":"LAWRANCE","IHS_CBT_144M":"LAWRANCE",
        "IHS_CBT_147M":"LAWRANCE","IHS_CBT_149M":"LAWRANCE","IHS_CBT_152M":"LAWRANCE",
        "IHS_CBT_153M":"LAWRANCE","IHS_CBT_173M":"LAWRANCE","IHS_CBT_208M":"LAWRANCE",
        "IHS_CBT_234M":"LAWRANCE","IHS_CBT_205A":"LAWRANCE","IHS_CBT_208A":"LAWRANCE",
        "IHS_CBT_213A":"LAWRANCE","IHS_CBT_240A":"LAWRANCE","IHS_CBT_248A":"LAWRANCE",
        "IHS_CBT_270A":"LAWRANCE","IHS_CBT_304A":"LAWRANCE","IHS_CBT_322A":"LAWRANCE",
        "IHS_CBT_358A":"LAWRANCE",
        "IHS_CBT_142M":"CASCIOUS","IHS_CBT_145M":"CASCIOUS","IHS_CBT_158M":"CASCIOUS",
        "IHS_CBT_169M":"CASCIOUS","IHS_CBT_174M":"CASCIOUS","IHS_CBT_176M":"CASCIOUS",
        "IHS_CBT_177M":"CASCIOUS","IHS_CBT_178M":"CASCIOUS","IHS_CBT_180M":"CASCIOUS",
        "IHS_CBT_182M":"CASCIOUS","IHS_CBT_183M":"CASCIOUS","IHS_CBT_184M":"CASCIOUS",
        "IHS_CBT_185M":"CASCIOUS","IHS_CBT_186M":"CASCIOUS","IHS_CBT_187M":"CASCIOUS",
        "IHS_CBT_188M":"CASCIOUS","IHS_CBT_189M":"CASCIOUS","IHS_CBT_190M":"CASCIOUS",
        "IHS_CBT_196M":"CASCIOUS","IHS_CBT_206M":"CASCIOUS","IHS_CBT_207M":"CASCIOUS",
        "IHS_CBT_212M":"CASCIOUS","IHS_CBT_214M":"CASCIOUS","IHS_CBT_221M":"CASCIOUS",
        "IHS_CBT_229M":"CASCIOUS","IHS_CBT_231M":"CASCIOUS","IHS_CBT_232M":"CASCIOUS",
        "IHS_CBT_238A":"CASCIOUS","IHS_CBT_247A":"CASCIOUS","IHS_CBT_255A":"CASCIOUS",
        "IHS_CBT_258A":"CASCIOUS","IHS_CBT_271A":"CASCIOUS","IHS_CBT_273A":"CASCIOUS",
        "IHS_CBT_275A":"CASCIOUS","IHS_CBT_281A":"CASCIOUS","IHS_CBT_294A":"CASCIOUS",
        "IHS_CBT_295A":"CASCIOUS","IHS_CBT_303A":"CASCIOUS","IHS_CBT_324A":"CASCIOUS",
        "IHS_CBT_340A":"CASCIOUS","IHS_CBT_374A":"CASCIOUS","IHS_CBT_382A":"CASCIOUS",
        "IHS_CBT_204A":"CASCIOUS",
        "IHS_CBT_171M":"ELIJAH","IHS_CBT_228M":"ELIJAH","IHS_CBT_230M":"ELIJAH",
        "IHS_CBT_219A":"ELIJAH",
        "IHS_CBT_194M":"MWILA","IHS_CBT_197M":"MWILA","IHS_CBT_198M":"MWILA",
        "IHS_CBT_199M":"MWILA","IHS_CBT_202M":"MWILA","IHS_CBT_203A":"MWILA",
        "IHS_CBT_287A":"MWILA","IHS_CBT_366A":"MWILA","IHS_CBT_389A":"MWILA",
        "IHS_CBT_313A":"LOMBE"
      },
      new_cbt: {
        "IHS_CBT_002M":"KAMBOLE","IHS_CBT_005M":"KAMBOLE","IHS_CBT_011M":"KAMBOLE",
        "IHS_CBT_013M":"KAMBOLE","IHS_CBT_015M":"KAMBOLE","IHS_CBT_017M":"KAMBOLE",
        "IHS_CBT_023M":"KAMBOLE","IHS_CBT_025M":"KAMBOLE","IHS_CBT_029M":"KAMBOLE",
        "IHS_CBT_031M":"KAMBOLE","IHS_CBT_037M":"KAMBOLE","IHS_CBT_041M":"KAMBOLE",
        "IHS_CBT_072M":"KAMBOLE","IHS_CBT_216M":"KAMBOLE","IHS_CBT_219M":"KAMBOLE",
        "IHS_CBT_220M":"KAMBOLE","IHS_CBT_222M":"KAMBOLE","IHS_CBT_218A":"KAMBOLE",
        "IHS_CBT_226A":"KAMBOLE","IHS_CBT_226M":"KAMBOLE","IHS_CBT_233A":"KAMBOLE",
        "IHS_CBT_245A":"KAMBOLE","IHS_CBT_257A":"KAMBOLE","IHS_CBT_264A":"KAMBOLE",
        "IHS_CBT_291A":"KAMBOLE","IHS_CBT_335A":"KAMBOLE","IHS_CBT_344A":"KAMBOLE",
        "IHS_CBT_347A":"KAMBOLE","IHS_CBT_359A":"KAMBOLE","IHS_CBT_360A":"KAMBOLE",
        "IHS_CBT_361A":"KAMBOLE","IHS_CBT_364A":"KAMBOLE","IHS_CBT_378A":"KAMBOLE",
        "IHS_CBT_390A":"KAMBOLE",
        "IHS_CBT_001M":"ROYD","IHS_CBT_003M":"ROYD","IHS_CBT_004M":"ROYD",
        "IHS_CBT_006M":"ROYD","IHS_CBT_007M":"ROYD","IHS_CBT_008M":"ROYD",
        "IHS_CBT_009M":"ROYD","IHS_CBT_010M":"ROYD","IHS_CBT_012M":"ROYD",
        "IHS_CBT_014M":"ROYD","IHS_CBT_016M":"ROYD","IHS_CBT_020M":"ROYD",
        "IHS_CBT_021M":"ROYD","IHS_CBT_022M":"ROYD","IHS_CBT_024M":"ROYD",
        "IHS_CBT_027M":"ROYD","IHS_CBT_032M":"ROYD","IHS_CBT_033M":"ROYD",
        "IHS_CBT_034M":"ROYD","IHS_CBT_035M":"ROYD","IHS_CBT_036M":"ROYD",
        "IHS_CBT_156M":"ROYD","IHS_CBT_164M":"ROYD","IHS_CBT_207A":"ROYD",
        "IHS_CBT_214A":"ROYD","IHS_CBT_224M":"ROYD","IHS_CBT_232A":"ROYD",
        "IHS_CBT_246A":"ROYD","IHS_CBT_252A":"ROYD","IHS_CBT_253A":"ROYD",
        "IHS_CBT_283A":"ROYD","IHS_CBT_288A":"ROYD","IHS_CBT_293A":"ROYD",
        "IHS_CBT_325A":"ROYD","IHS_CBT_331A":"ROYD","IHS_CBT_332A":"ROYD",
        "IHS_CBT_338A":"ROYD","IHS_CBT_349A":"ROYD","IHS_CBT_362A":"ROYD",
        "IHS_CBT_363A":"ROYD","IHS_CBT_385A":"ROYD",
        "IHS_CBT_061M":"FACKSON","IHS_CBT_073M":"FACKSON","IHS_CBT_074M":"FACKSON",
        "IHS_CBT_075M":"FACKSON","IHS_CBT_081M":"FACKSON","IHS_CBT_082M":"FACKSON",
        "IHS_CBT_083M":"FACKSON","IHS_CBT_088M":"FACKSON","IHS_CBT_092M":"FACKSON",
        "IHS_CBT_094M":"FACKSON","IHS_CBT_096M":"FACKSON","IHS_CBT_102M":"FACKSON",
        "IHS_CBT_104M":"FACKSON","IHS_CBT_105M":"FACKSON","IHS_CBT_108M":"FACKSON",
        "IHS_CBT_217A":"FACKSON","IHS_CBT_218M":"FACKSON","IHS_CBT_222A":"FACKSON",
        "IHS_CBT_223M":"FACKSON","IHS_CBT_237A":"FACKSON","IHS_CBT_244A":"FACKSON",
        "IHS_CBT_251A":"FACKSON","IHS_CBT_260A":"FACKSON","IHS_CBT_274A":"FACKSON",
        "IHS_CBT_289A":"FACKSON","IHS_CBT_297A":"FACKSON","IHS_CBT_299A":"FACKSON",
        "IHS_CBT_300A":"FACKSON","IHS_CBT_305A":"FACKSON","IHS_CBT_334A":"FACKSON",
        "IHS_CBT_345A":"FACKSON","IHS_CBT_353A":"FACKSON","IHS_CBT_355A":"FACKSON",
        "IHS_CBT_356A":"FACKSON","IHS_CBT_373A":"FACKSON",
        "IHS_CBT_080M":"JAULA","IHS_CBT_087M":"JAULA","IHS_CBT_089M":"JAULA",
        "IHS_CBT_090M":"JAULA","IHS_CBT_093M":"JAULA","IHS_CBT_098M":"JAULA",
        "IHS_CBT_099M":"JAULA","IHS_CBT_103M":"JAULA","IHS_CBT_111M":"JAULA",
        "IHS_CBT_112M":"JAULA","IHS_CBT_113M":"JAULA","IHS_CBT_114M":"JAULA",
        "IHS_CBT_115M":"JAULA","IHS_CBT_116M":"JAULA","IHS_CBT_120M":"JAULA",
        "IHS_CBT_217M":"JAULA","IHS_CBT_235M":"JAULA","IHS_CBT_220A":"JAULA",
        "IHS_CBT_228A":"JAULA","IHS_CBT_229A":"JAULA","IHS_CBT_241A":"JAULA",
        "IHS_CBT_249A":"JAULA","IHS_CBT_263A":"JAULA","IHS_CBT_266A":"JAULA",
        "IHS_CBT_269A":"JAULA","IHS_CBT_276A":"JAULA","IHS_CBT_285A":"JAULA",
        "IHS_CBT_296A":"JAULA","IHS_CBT_333A":"JAULA","IHS_CBT_351A":"JAULA",
        "IHS_CBT_354A":"JAULA","IHS_CBT_381A":"JAULA","IHS_CBT_383A":"JAULA",
        "IHS_CBT_384A":"JAULA","IHS_CBT_386A":"JAULA","IHS_CBT_393A":"JAULA",
        "IHS_CBT_042M":"ISAAC","IHS_CBT_043M":"ISAAC","IHS_CBT_044M":"ISAAC",
        "IHS_CBT_047M":"ISAAC","IHS_CBT_048M":"ISAAC","IHS_CBT_049M":"ISAAC",
        "IHS_CBT_050M":"ISAAC","IHS_CBT_052M":"ISAAC","IHS_CBT_054M":"ISAAC",
        "IHS_CBT_057M":"ISAAC","IHS_CBT_058M":"ISAAC","IHS_CBT_062M":"ISAAC",
        "IHS_CBT_064M":"ISAAC","IHS_CBT_065M":"ISAAC","IHS_CBT_068M":"ISAAC",
        "IHS_CBT_069M":"ISAAC","IHS_CBT_076M":"ISAAC","IHS_CBT_137M":"ISAAC",
        "IHS_CBT_161M":"ISAAC","IHS_CBT_172M":"ISAAC","IHS_CBT_179M":"ISAAC",
        "IHS_CBT_193M":"ISAAC","IHS_CBT_210M":"ISAAC","IHS_CBT_227M":"ISAAC",
        "IHS_CBT_233M":"ISAAC","IHS_CBT_201A":"ISAAC","IHS_CBT_210A":"ISAAC",
        "IHS_CBT_211A":"ISAAC","IHS_CBT_230A":"ISAAC","IHS_CBT_254A":"ISAAC",
        "IHS_CBT_265A":"ISAAC","IHS_CBT_277A":"ISAAC","IHS_CBT_278A":"ISAAC",
        "IHS_CBT_307A":"ISAAC","IHS_CBT_312A":"ISAAC","IHS_CBT_314A":"ISAAC",
        "IHS_CBT_339A":"ISAAC","IHS_CBT_343A":"ISAAC","IHS_CBT_367A":"ISAAC",
        "IHS_CBT_369A":"ISAAC","IHS_CBT_377A":"ISAAC",
        "IHS_CBT_040M":"JUSTIN","IHS_CBT_045M":"JUSTIN","IHS_CBT_056M":"JUSTIN",
        "IHS_CBT_060M":"JUSTIN","IHS_CBT_070M":"JUSTIN","IHS_CBT_085M":"JUSTIN",
        "IHS_CBT_091M":"JUSTIN","IHS_CBT_148M":"JUSTIN","IHS_CBT_227A":"JUSTIN",
        "IHS_CBT_234A":"JUSTIN","IHS_CBT_235A":"JUSTIN","IHS_CBT_236A":"JUSTIN",
        "IHS_CBT_306A":"JUSTIN","IHS_CBT_309A":"JUSTIN","IHS_CBT_320A":"JUSTIN",
        "IHS_CBT_326A":"JUSTIN","IHS_CBT_346A":"JUSTIN",
        "IHS_CBT_078M":"SAMUEL","IHS_CBT_079M":"SAMUEL","IHS_CBT_084M":"SAMUEL",
        "IHS_CBT_107M":"SAMUEL","IHS_CBT_117M":"SAMUEL","IHS_CBT_118M":"SAMUEL",
        "IHS_CBT_119M":"SAMUEL","IHS_CBT_121M":"SAMUEL","IHS_CBT_126M":"SAMUEL",
        "IHS_CBT_127M":"SAMUEL","IHS_CBT_129M":"SAMUEL","IHS_CBT_132M":"SAMUEL",
        "IHS_CBT_133M":"SAMUEL","IHS_CBT_134M":"SAMUEL","IHS_CBT_146M":"SAMUEL",
        "IHS_CBT_167M":"SAMUEL"
      }
    };

    // ============================================================
    // ===== TECHNICIAN MANAGER CLASS =============================
    // ============================================================
    class TechnicianManager {
      constructor(data) {
        this.data = data;
        this._exactIndex = {};
        this._suffixIndex = {};
        this._techToSites = {};
        this.allTechs = new Set();
        this._build();
      }
      _build() {
        for (const [region, map] of Object.entries(this.data)) {
          for (const [siteId, techName] of Object.entries(map)) {
            const sid = siteId.toUpperCase();
            const tech = techName.toUpperCase();
            this._exactIndex[sid] = { techName: tech, region };
            const suffix = this._extractSuffix(sid);
            if (suffix) {
              if (!this._suffixIndex[suffix]) this._suffixIndex[suffix] = [];
              this._suffixIndex[suffix].push({ siteId: sid, techName: tech, region });
            }
            if (!this._techToSites[tech]) this._techToSites[tech] = [];
            this._techToSites[tech].push({ siteId: sid, region });
            this.allTechs.add(tech);
          }
        }
      }
      _extractSuffix(siteId) {
        const m = siteId.match(/(\d+[A-Z]?)$/);
        return m ? m[1] : null;
      }
      lookup(siteId, contextRegion) {
        if (!siteId) return null;
        const sid = siteId.trim().toUpperCase();
        if (this._exactIndex[sid]) return this._exactIndex[sid];
        for (const prefix of ['IHS_CBT_','IHS_NRW_','IHS_EST_']) {
          const full = prefix + sid;
          if (this._exactIndex[full]) return this._exactIndex[full];
        }
        const suffix = this._extractSuffix(sid);
        if (suffix && this._suffixIndex[suffix]) {
          const matches = this._suffixIndex[suffix];
          if (contextRegion) {
            const hit = matches.find(m => m.region === contextRegion);
            if (hit) return hit;
          }
          return matches[0];
        }
        return null;
      }
      getTechName(siteId, contextRegion) {
        const r = this.lookup(siteId, contextRegion);
        return r ? r.techName : '';
      }
      getSitesForTech(techName) {
        return this._techToSites[techName.toUpperCase()] || [];
      }
      getRegionStats() {
        const stats = {};
        for (const [region, map] of Object.entries(this.data)) {
          const techs = new Set(Object.values(map).map(t => t.toUpperCase()));
          stats[region] = { sites: Object.keys(map).length, techs: techs.size, techList: [...techs] };
        }
        return stats;
      }
      getAllAssignments() {
        const rows = [];
        for (const [region, map] of Object.entries(this.data)) {
          for (const [siteId, techName] of Object.entries(map)) {
            rows.push({ siteId, techName: techName.toUpperCase(), region });
          }
        }
        return rows;
      }
    }
    const TECH_MANAGER = new TechnicianManager(TECHNICIAN_DATA);

    // ============================================================
    // ===== TECHNICIAN MANAGER PAGE ==============================
    // ============================================================
    let _tmState = { search: '', filterRegion: 'all', filterTech: '' };

    function renderTechniciansPage(container) {
      const stats = TECH_MANAGER.getRegionStats();
      const totalSites = Object.values(stats).reduce((s,r)=>s+r.sites,0);
      const totalTechs = TECH_MANAGER.allTechs.size;

      const regionLabels = { nrw:'NRW', eastern:'Eastern', old_cbt:'Old CBT', new_cbt:'New CBT' };
      const regionColors = { nrw:'var(--accent-600)', eastern:'var(--status-info)', old_cbt:'var(--status-success)', new_cbt:'var(--status-warning)' };
      const regionPrefixes = { nrw:'IHS_NRW', eastern:'IHS_EST', old_cbt:'IHS_CBT', new_cbt:'IHS_CBT' };

      // Collect known tech names across all regions for datalist
      const allKnownTechs = [...TECH_MANAGER.allTechs].sort();

      container.innerHTML = `
      <div class="page-header mb-5">
        <div>
          <h2 class="font-bold tracking-tight">Technician Manager</h2>
          <p class="text-sm mt-1" style="color:var(--neutral-500)">Site-to-technician assignments across all regions</p>
        </div>
        <div class="flex gap-3 flex-wrap">
          <button class="btn btn-ghost btn-sm" id="tmBulkDeleteBtn" style="display:none;color:var(--status-danger);" onclick="tmBulkDelete()">
            <i class="fa-regular fa-trash"></i> Delete Selected (<span id="tmBulkCount">0</span>)
          </button>
          <label class="btn btn-secondary btn-sm" style="cursor:pointer;" title="Import CSV or JSON">
            <i class="fa-regular fa-file-import"></i> Import CSV/JSON
            <input type="file" accept=".csv,.json" style="display:none;" onchange="tmHandleImport(event)">
          </label>
          <button class="btn btn-secondary btn-sm" onclick="tmExportCSV()"><i class="fa-regular fa-download"></i> Export CSV</button>
        </div>
      </div>

      <!-- KPI tiles -->
      <div class="grid grid-cols-4 gap-4 mb-5">
        <div class="card" style="text-align:center;">
          <div class="text-3xl font-bold" style="color:var(--accent-600);">${totalSites}</div>
          <div class="text-sm mt-1" style="color:var(--neutral-500)">Total Sites</div>
        </div>
        <div class="card" style="text-align:center;">
          <div class="text-3xl font-bold" style="color:var(--status-info);">${totalTechs}</div>
          <div class="text-sm mt-1" style="color:var(--neutral-500)">Technicians</div>
        </div>
        ${Object.entries(stats).map(([r,s])=>`
        <div class="card" style="text-align:center;border-left:3px solid ${regionColors[r]||'var(--neutral-300)'};">
          <div class="text-2xl font-bold" style="color:${regionColors[r]||'var(--neutral-700)'};">${s.sites}</div>
          <div class="text-sm mt-1" style="color:var(--neutral-500)">${regionLabels[r]||r} · ${s.techs} techs</div>
        </div>`).join('')}
      </div>

      <!-- ═══ ACTION PANELS ═══ -->
      <div class="grid grid-cols-3 gap-4 mb-5" id="tmActionPanels">

        <!-- Panel 1: Add New Site Assignment -->
        <div class="card" style="border-top:3px solid var(--accent-600);">
          <div class="flex items-center gap-2 mb-4">
            <div style="width:32px;height:32px;border-radius:var(--radius-md);background:var(--accent-100);display:flex;align-items:center;justify-content:center;color:var(--accent-600);flex-shrink:0;">
              <i class="fa-regular fa-plus"></i>
            </div>
            <div>
              <div class="font-semibold text-sm">Add New Site</div>
              <div style="font-size:0.7rem;color:var(--neutral-500);">Assign a site ID to a technician</div>
            </div>
          </div>
          <div class="flex flex-col gap-3">
            <div>
              <label style="font-size:0.72rem;font-weight:600;color:var(--neutral-600);display:block;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.04em;">Region</label>
              <div class="select-wrapper">
                <select class="select-field" id="tmAddRegion" onchange="tmUpdateSitePrefix()">
                  <option value="">— select region —</option>
                  ${Object.entries(regionLabels).map(([k,v])=>`<option value="${k}">${v} (${regionPrefixes[k]})</option>`).join('')}
                </select>
              </div>
            </div>
            <div>
              <label style="font-size:0.72rem;font-weight:600;color:var(--neutral-600);display:block;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.04em;">Site ID</label>
              <div style="display:flex;gap:6px;align-items:center;">
                <span id="tmSitePrefix" style="font-family:var(--font-mono);font-size:0.75rem;font-weight:700;color:var(--neutral-500);white-space:nowrap;padding:0 4px;">IHS_???_</span>
                <input type="text" class="input-field" id="tmAddSiteNum" placeholder="e.g. 035M or 210A"
                  style="font-family:var(--font-mono);font-size:0.85rem;text-transform:uppercase;flex:1;"
                  oninput="this.value=this.value.toUpperCase();tmPreviewSiteId()"
                  maxlength="8">
              </div>
              <div id="tmSiteIdPreview" style="font-size:0.72rem;margin-top:4px;min-height:16px;"></div>
            </div>
            <div>
              <label style="font-size:0.72rem;font-weight:600;color:var(--neutral-600);display:block;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.04em;">Technician</label>
              <input type="text" class="input-field" id="tmAddTechName" placeholder="e.g. KENNY"
                style="text-transform:uppercase;"
                oninput="this.value=this.value.toUpperCase()"
                list="tmKnownTechsList" autocomplete="off">
              <datalist id="tmKnownTechsList">
                ${allKnownTechs.map(t=>`<option value="${t}">`).join('')}
              </datalist>
            </div>
            <div id="tmAddSiteHint" style="font-size:0.72rem;min-height:16px;"></div>
            <button class="btn btn-primary w-full" onclick="tmAddSite()">
              <i class="fa-regular fa-check"></i> Add Site Assignment
            </button>
          </div>
        </div>

        <!-- Panel 2: Add / Rename Technician -->
        <div class="card" style="border-top:3px solid var(--status-info);">
          <div class="flex items-center gap-2 mb-4">
            <div style="width:32px;height:32px;border-radius:var(--radius-md);background:var(--status-info-bg);display:flex;align-items:center;justify-content:center;color:var(--status-info);flex-shrink:0;">
              <i class="fa-regular fa-user-plus"></i>
            </div>
            <div>
              <div class="font-semibold text-sm">Add / Rename Technician</div>
              <div style="font-size:0.7rem;color:var(--neutral-500);">Bulk-rename or add a new tech name</div>
            </div>
          </div>
          <div class="flex flex-col gap-3">
            <div>
              <label style="font-size:0.72rem;font-weight:600;color:var(--neutral-600);display:block;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.04em;">Region</label>
              <div class="select-wrapper">
                <select class="select-field" id="tmRenameRegion">
                  <option value="">— all regions —</option>
                  ${Object.entries(regionLabels).map(([k,v])=>`<option value="${k}">${v}</option>`).join('')}
                </select>
              </div>
            </div>
            <div>
              <label style="font-size:0.72rem;font-weight:600;color:var(--neutral-600);display:block;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.04em;">Old / Existing Name</label>
              <input type="text" class="input-field" id="tmOldTechName" placeholder="e.g. KENNY"
                style="text-transform:uppercase;"
                oninput="this.value=this.value.toUpperCase();tmPreviewRename()"
                list="tmKnownTechsList2" autocomplete="off">
              <datalist id="tmKnownTechsList2">
                ${allKnownTechs.map(t=>`<option value="${t}">`).join('')}
              </datalist>
            </div>
            <div>
              <label style="font-size:0.72rem;font-weight:600;color:var(--neutral-600);display:block;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.04em;">New Name</label>
              <input type="text" class="input-field" id="tmNewTechName" placeholder="e.g. KENNETH"
                style="text-transform:uppercase;"
                oninput="this.value=this.value.toUpperCase();tmPreviewRename()">
            </div>
            <div id="tmRenameHint" style="font-size:0.72rem;min-height:16px;"></div>
            <button class="btn w-full" style="background:var(--status-info-bg);color:var(--status-info);border:1px solid var(--status-info)44;" onclick="tmRenameTech()">
              <i class="fa-regular fa-pen"></i> Apply Rename
            </button>
          </div>
        </div>

        <!-- Panel 3: Reassign Site -->
        <div class="card" style="border-top:3px solid var(--status-success);">
          <div class="flex items-center gap-2 mb-4">
            <div style="width:32px;height:32px;border-radius:var(--radius-md);background:var(--status-success-bg);display:flex;align-items:center;justify-content:center;color:var(--status-success);flex-shrink:0;">
              <i class="fa-regular fa-arrows-rotate"></i>
            </div>
            <div>
              <div class="font-semibold text-sm">Reassign Site</div>
              <div style="font-size:0.7rem;color:var(--neutral-500);">Move a site from one tech to another</div>
            </div>
          </div>
          <div class="flex flex-col gap-3">
            <div>
              <label style="font-size:0.72rem;font-weight:600;color:var(--neutral-600);display:block;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.04em;">Site ID to Reassign</label>
              <input type="text" class="input-field" id="tmReassignSiteId" placeholder="e.g. IHS_NRW_035M"
                style="font-family:var(--font-mono);font-size:0.85rem;text-transform:uppercase;"
                oninput="this.value=this.value.toUpperCase();tmPreviewReassign()"
                list="tmAllSitesList" autocomplete="off">
              <datalist id="tmAllSitesList">
                ${TECH_MANAGER.getAllAssignments().map(r=>`<option value="${r.siteId}">`).join('')}
              </datalist>
            </div>
            <div id="tmReassignCurrentInfo" style="font-size:0.72rem;min-height:36px;padding:6px 10px;border-radius:var(--radius-md);background:var(--neutral-50);border:1px solid var(--neutral-200);display:none;"></div>
            <div>
              <label style="font-size:0.72rem;font-weight:600;color:var(--neutral-600);display:block;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.04em;">Reassign To</label>
              <input type="text" class="input-field" id="tmReassignToTech" placeholder="e.g. LOMBE"
                style="text-transform:uppercase;"
                oninput="this.value=this.value.toUpperCase()"
                list="tmKnownTechsList3" autocomplete="off">
              <datalist id="tmKnownTechsList3">
                ${allKnownTechs.map(t=>`<option value="${t}">`).join('')}
              </datalist>
            </div>
            <div id="tmReassignHint" style="font-size:0.72rem;min-height:16px;"></div>
            <button class="btn w-full" style="background:var(--status-success-bg);color:var(--status-success);border:1px solid var(--status-success)44;" onclick="tmReassignSite()">
              <i class="fa-regular fa-arrows-rotate"></i> Reassign Site
            </button>
          </div>
        </div>
      </div>

      <!-- ═══ SEARCH + TABLE ═══ -->
      <div class="card mb-4">
        <div class="flex gap-3 flex-wrap items-center">
          <div class="flex-1" style="min-width:200px;">
            <input type="text" class="input-field" placeholder="Search site ID or technician..." id="tmSearchInput"
              oninput="_tmState.search=this.value;tmRenderTable()" value="${_tmState.search}" style="padding:10px 14px;">
          </div>
          <div class="select-wrapper" style="min-width:150px;">
            <select class="select-field" id="tmRegionFilter" onchange="_tmState.filterRegion=this.value;tmRenderTable()">
              <option value="all">All Regions</option>
              ${Object.entries(regionLabels).map(([k,v])=>`<option value="${k}" ${_tmState.filterRegion===k?'selected':''}>${v}</option>`).join('')}
            </select>
          </div>
          <button class="btn btn-ghost btn-sm" onclick="_tmState.search='';_tmState.filterRegion='all';document.getElementById('tmSearchInput').value='';document.getElementById('tmRegionFilter').value='all';tmRenderTable()">
            <i class="fa-regular fa-xmark"></i> Clear
          </button>
        </div>
        <div id="tmQuickResult" style="display:none;margin-top:14px;padding:12px 16px;border-radius:var(--radius-lg);border:1px solid var(--neutral-200);background:var(--neutral-50);"></div>
      </div>

      <div class="card" style="padding:0;overflow:hidden;">
        <div style="display:flex;align-items:center;justify-content:space-between;padding:10px 16px;border-bottom:1px solid var(--neutral-200);background:var(--neutral-50);">
          <span class="text-xs font-semibold" style="color:var(--neutral-500);">SITE ASSIGNMENTS</span>
          <div style="display:flex;align-items:center;gap:10px;">
            ${renderDensityToggle()}
          </div>
        </div>
        <div id="tmTableWrap" style="max-height:520px;overflow-y:auto;">
          <table class="table" style="table-layout:fixed;width:100%;" role="table" aria-label="Site assignments">
            <thead><tr>
              <th style="width:36px;padding:10px 8px;"><input type="checkbox" id="tmSelectAll" title="Select all" onchange="tmToggleSelectAll(this.checked)" style="cursor:pointer;accent-color:var(--accent-600);"></th>
              <th style="width:34%" scope="col">Site ID</th>
              <th style="width:28%" scope="col">Technician</th>
              <th style="width:24%" scope="col">Region</th>
              <th style="width:80px;text-align:center;" scope="col">Actions</th>
            </tr></thead>
            <tbody id="tmTableBody"></tbody>
          </table>
        </div>
        <div id="tmFooter" class="p-4 text-sm" style="color:var(--neutral-500);border-top:1px solid var(--neutral-200);display:flex;align-items:center;justify-content:space-between;">
          <span id="tmRowCount"></span>
        </div>
      </div>`;

      tmRenderTable();
    }

    // ── helpers for the action panels ──────────────────────────────────────────

    const _tmRegionPrefixes = { nrw:'IHS_NRW', eastern:'IHS_EST', old_cbt:'IHS_CBT', new_cbt:'IHS_CBT' };
    const _tmRegionLabels   = { nrw:'NRW', eastern:'Eastern', old_cbt:'Old CBT', new_cbt:'New CBT' };

    function tmUpdateSitePrefix() {
      const region = document.getElementById('tmAddRegion')?.value;
      const pfxEl  = document.getElementById('tmSitePrefix');
      if (pfxEl) pfxEl.textContent = region ? (_tmRegionPrefixes[region] + '_') : 'IHS_???_';
      tmPreviewSiteId();
    }

    function _tmNormaliseSuffix(raw) {
      // Zero-pad numeric part to 3 digits
      const s = raw.trim().toUpperCase();
      const m = s.match(/^(\d+)([A-Z]*)$/);
      if (!m) return s;
      const padded = m[1].length < 3 ? m[1].padStart(3, '0') : m[1];
      return padded + m[2];
    }

    function tmPreviewSiteId() {
      const region  = document.getElementById('tmAddRegion')?.value;
      const numRaw  = (document.getElementById('tmAddSiteNum')?.value || '').trim();
      const preview = document.getElementById('tmSiteIdPreview');
      const hint    = document.getElementById('tmAddSiteHint');
      if (!preview) return;

      if (!region || !numRaw) {
        preview.textContent = '';
        if (hint) { hint.textContent = ''; hint.style.color = ''; }
        return;
      }

      const suffix = _tmNormaliseSuffix(numRaw);
      const fullId = `${_tmRegionPrefixes[region]}_${suffix}`;
      preview.innerHTML = `<span style="font-family:var(--font-mono);font-weight:700;color:var(--accent-700);">→ ${fullId}</span>`;

      // Check for duplicate
      const exists = TECH_MANAGER.data[region]?.[fullId] !== undefined;
      if (hint) {
        if (exists) {
          hint.textContent = `⚠ Already assigned to: ${TECH_MANAGER.data[region][fullId]}`;
          hint.style.color = 'var(--status-warning)';
        } else if (numRaw.length >= 2) {
          hint.textContent = '✓ Site ID available';
          hint.style.color = 'var(--status-success)';
        } else {
          hint.textContent = '';
        }
      }
    }

    function tmAddSite() {
      const region   = document.getElementById('tmAddRegion')?.value;
      const numRaw   = (document.getElementById('tmAddSiteNum')?.value || '').trim();
      const techRaw  = (document.getElementById('tmAddTechName')?.value || '').trim().toUpperCase();
      const hint     = document.getElementById('tmAddSiteHint');

      const setHint = (msg, color) => { if (hint) { hint.textContent = msg; hint.style.color = color; } };

      if (!region)  return setHint('Please select a region.', 'var(--status-danger)');
      if (!numRaw)  return setHint('Please enter a site number (e.g. 035M).', 'var(--status-danger)');
      if (!techRaw) return setHint('Please enter a technician name.', 'var(--status-danger)');

      const suffix = _tmNormaliseSuffix(numRaw);
      const fullId = `${_tmRegionPrefixes[region]}_${suffix}`;

      if (TECH_MANAGER.data[region]?.[fullId] !== undefined) {
        return setHint(`⚠ ${fullId} already exists (assigned to ${TECH_MANAGER.data[region][fullId]}).`, 'var(--status-warning)');
      }

      if (!TECHNICIAN_DATA[region]) TECHNICIAN_DATA[region] = {};
      TECHNICIAN_DATA[region][fullId] = techRaw;
      TECH_MANAGER._build();

      // Clear fields
      document.getElementById('tmAddSiteNum').value   = '';
      document.getElementById('tmAddTechName').value  = '';
      document.getElementById('tmSiteIdPreview').textContent = '';
      setHint(`✅ Added: ${fullId} → ${techRaw}`, 'var(--status-success)');

      showToast(`✅ Added ${fullId} → ${techRaw}`, 'success');
      tmRenderTable();
      // Highlight the new row
      setTimeout(() => {
        const row = document.querySelector(`tr[data-siteid="${fullId}"]`);
        if (row) {
          row.style.background = 'var(--accent-50)';
          row.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          setTimeout(() => { row.style.background = ''; }, 2000);
        }
      }, 100);
    }

    function tmPreviewRename() {
      const oldName = (document.getElementById('tmOldTechName')?.value || '').trim().toUpperCase();
      const newName = (document.getElementById('tmNewTechName')?.value || '').trim().toUpperCase();
      const hint    = document.getElementById('tmRenameHint');
      if (!hint) return;

      if (!oldName || !newName) { hint.textContent = ''; return; }

      const region = document.getElementById('tmRenameRegion')?.value;
      let count = 0;
      Object.entries(TECHNICIAN_DATA).forEach(([r, map]) => {
        if (region && r !== region) return;
        Object.values(map).forEach(t => { if (t === oldName) count++; });
      });

      if (count === 0) {
        hint.textContent = `⚠ "${oldName}" not found${region ? ' in ' + _tmRegionLabels[region] : ''}.`;
        hint.style.color = 'var(--status-warning)';
      } else {
        hint.textContent = `→ Will rename ${count} site${count!==1?'s':''} from "${oldName}" to "${newName}"`;
        hint.style.color = 'var(--status-info)';
      }
    }

    function tmRenameTech() {
      const oldName = (document.getElementById('tmOldTechName')?.value || '').trim().toUpperCase();
      const newName = (document.getElementById('tmNewTechName')?.value || '').trim().toUpperCase();
      const region  = document.getElementById('tmRenameRegion')?.value;
      const hint    = document.getElementById('tmRenameHint');

      const setHint = (msg, color) => { if (hint) { hint.textContent = msg; hint.style.color = color; } };

      if (!oldName) return setHint('Enter the existing technician name.', 'var(--status-danger)');
      if (!newName) return setHint('Enter the new technician name.', 'var(--status-danger)');
      if (oldName === newName) return setHint('Old and new names are the same.', 'var(--status-warning)');

      let count = 0;
      Object.entries(TECHNICIAN_DATA).forEach(([r, map]) => {
        if (region && r !== region) return;
        Object.keys(map).forEach(sid => {
          if (map[sid] === oldName) { map[sid] = newName; count++; }
        });
      });

      TECH_MANAGER._build();

      if (count === 0) {
        return setHint(`"${oldName}" not found — no changes made.`, 'var(--status-warning)');
      }

      document.getElementById('tmOldTechName').value = '';
      document.getElementById('tmNewTechName').value = '';
      setHint(`✅ Renamed ${count} site${count!==1?'s':''} from "${oldName}" to "${newName}"`, 'var(--status-success)');
      showToast(`✅ Renamed "${oldName}" → "${newName}" (${count} site${count!==1?'s':''})`, 'success');
      tmRenderTable();
    }

    function tmPreviewReassign() {
      const siteId  = (document.getElementById('tmReassignSiteId')?.value || '').trim().toUpperCase();
      const infoEl  = document.getElementById('tmReassignCurrentInfo');
      const hint    = document.getElementById('tmReassignHint');
      if (!infoEl) return;

      if (!siteId || siteId.length < 6) {
        infoEl.style.display = 'none';
        if (hint) hint.textContent = '';
        return;
      }

      const hit = TECH_MANAGER.lookup(siteId);
      if (hit) {
        infoEl.style.display = 'block';
        infoEl.innerHTML = `<span style="color:var(--neutral-500);">Currently assigned to:</span> <strong style="color:var(--accent-700);">${hit.techName}</strong> <span style="color:var(--neutral-400);">(${_tmRegionLabels[hit.region]||hit.region})</span>`;
        if (hint) { hint.textContent = ''; }
      } else {
        infoEl.style.display = 'block';
        infoEl.innerHTML = `<span style="color:var(--status-danger);">Site ID not found in any region.</span>`;
        if (hint) { hint.textContent = ''; }
      }
    }

    function tmReassignSite() {
      const siteId  = (document.getElementById('tmReassignSiteId')?.value || '').trim().toUpperCase();
      const toTech  = (document.getElementById('tmReassignToTech')?.value || '').trim().toUpperCase();
      const hint    = document.getElementById('tmReassignHint');

      const setHint = (msg, color) => { if (hint) { hint.textContent = msg; hint.style.color = color; } };

      if (!siteId)  return setHint('Enter the site ID to reassign.', 'var(--status-danger)');
      if (!toTech)  return setHint('Enter the technician to assign to.', 'var(--status-danger)');

      const hit = TECH_MANAGER.lookup(siteId);
      if (!hit) return setHint(`Site ID "${siteId}" not found.`, 'var(--status-danger)');

      const fromTech = hit.techName;
      if (fromTech === toTech) return setHint(`Site is already assigned to ${toTech}.`, 'var(--status-warning)');

      TECHNICIAN_DATA[hit.region][siteId] = toTech;
      TECH_MANAGER._build();

      // Clear fields
      document.getElementById('tmReassignSiteId').value = '';
      document.getElementById('tmReassignToTech').value = '';
      document.getElementById('tmReassignCurrentInfo').style.display = 'none';
      setHint(`✅ ${siteId} reassigned from ${fromTech} to ${toTech}`, 'var(--status-success)');

      showToast(`✅ Reassigned ${siteId}: ${fromTech} → ${toTech}`, 'success');
      tmRenderTable();
      // Highlight the updated row
      setTimeout(() => {
        const row = document.querySelector(`tr[data-siteid="${siteId}"]`);
        if (row) {
          row.style.background = 'var(--status-success-bg)';
          row.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          setTimeout(() => { row.style.background = ''; }, 2000);
        }
      }, 100);
    }

    function tmRenderTable() {
      const search = (_tmState.search||'').toLowerCase().trim();
      const region = _tmState.filterRegion;
      const regionLabels = { nrw:'NRW', eastern:'Eastern', old_cbt:'Old CBT', new_cbt:'New CBT' };
      const regionColors = { nrw:'var(--accent-600)', eastern:'var(--status-info)', old_cbt:'var(--status-success)', new_cbt:'var(--status-warning)' };

      // Quick-lookup: if search looks like a site ID, show instant result
      const quickEl = document.getElementById('tmQuickResult');
      if (quickEl && search.length >= 3) {
        const hit = TECH_MANAGER.lookup(search.toUpperCase());
        if (hit) {
          const sitesForTech = TECH_MANAGER.getSitesForTech(hit.techName);
          const sameRegionCount = sitesForTech.filter(s => s.region === hit.region).length;
          quickEl.style.display = 'block';
          quickEl.innerHTML = `
            <div class="flex items-center gap-4 flex-wrap">
              <div style="font-size:1.5rem;">🔍</div>
              <div>
                <div class="text-xs font-medium mb-1" style="color:var(--neutral-500);text-transform:uppercase;letter-spacing:0.05em;">Quick Lookup</div>
                <div class="font-bold text-lg" style="color:var(--accent-600);">${hit.techName}</div>
                <div class="text-sm" style="color:var(--neutral-600);">${regionLabels[hit.region]||hit.region} · ${sameRegionCount} site${sameRegionCount!==1?'s':''} assigned</div>
              </div>
              <button class="btn btn-secondary btn-sm tm-see-all-btn">
                <span class="tm-tech-target" style="display:none">${hit.techName}</span>
                <i class="fa-regular fa-list"></i> See all sites
              </button>
            </div>`;
        } else {
          quickEl.style.display = 'none';
        }
      } else if (quickEl) {
        quickEl.style.display = 'none';
      }

      let rows = TECH_MANAGER.getAllAssignments();
      if (region !== 'all') rows = rows.filter(r => r.region === region);
      if (search) rows = rows.filter(r => r.siteId.toLowerCase().includes(search) || r.techName.toLowerCase().includes(search));

      rows.sort((a,b) => a.siteId.localeCompare(b.siteId));

      const tbody = document.getElementById('tmTableBody');
      const footer = document.getElementById('tmFooter');
      if (!tbody) return;

      if (rows.length === 0) {
        tbody.innerHTML = `<tr><td colspan="3" style="text-align:center;padding:2rem;color:var(--neutral-400);">No assignments match your search.</td></tr>`;
        if (footer) footer.textContent = '0 results';
        return;
      }

      tbody.innerHTML = rows.map(r => `
        <tr data-siteid="${r.siteId}" data-region="${r.region}">
          <td style="padding:8px;text-align:center;"><input type="checkbox" class="tmRowCheck" data-siteid="${r.siteId}" data-region="${r.region}" onchange="tmUpdateBulkBar()" style="cursor:pointer;accent-color:var(--accent-600);"></td>
          <td class="font-mono text-sm" id="tm-siteid-${r.siteId}" ondblclick="tmInlineEdit(this,'siteId','${r.siteId}','${r.region}')" title="Double-click to edit">${r.siteId}</td>
          <td id="tm-tech-${r.siteId}" ondblclick="tmInlineEdit(this,'techName','${r.siteId}','${r.region}')" title="Double-click to edit"><span class="badge" style="background:var(--neutral-100);color:var(--neutral-800);font-weight:600;cursor:pointer;">${r.techName}</span></td>
          <td><span class="badge" style="background:${(regionColors[r.region]||'var(--neutral-300)')}22;color:${regionColors[r.region]||'var(--neutral-600)'};border:1px solid ${(regionColors[r.region]||'var(--neutral-300)')}55;">${regionLabels[r.region]||r.region}</span></td>
          <td style="text-align:center;">
            <button class="btn btn-icon btn-ghost btn-sm" title="Delete" onclick="tmDeleteRow('${r.siteId}','${r.region}')" style="color:var(--status-danger);"><i class="fa-regular fa-trash"></i></button>
          </td>
        </tr>`).join('');

      if (footer) footer.textContent = `Showing ${rows.length.toLocaleString()} of ${TECH_MANAGER.getAllAssignments().length.toLocaleString()} assignments`;
    }

    function tmExportCSV() {
      const rows = TECH_MANAGER.getAllAssignments();
      const csv = ['Site ID,Technician,Region', ...rows.map(r=>`${r.siteId},${r.techName},${r.region}`)].join('\n');
      const blob = new Blob([csv], { type: 'text/csv' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `technician_assignments_${new Date().toISOString().slice(0,10)}.csv`;
      a.click();
      showToast('Exported ' + rows.length + ' assignments to CSV', 'success');
    }

    // ============================================================
    // ===== TECHNICIAN MANAGER CRUD OPERATIONS (Issue #2) ========
    // ============================================================

    // --- Checkbox / bulk selection bar ---
    function tmToggleSelectAll(checked) {
      document.querySelectorAll('.tmRowCheck').forEach(cb => { cb.checked = checked; });
      tmUpdateBulkBar();
    }

    function tmUpdateBulkBar() {
      const checked = document.querySelectorAll('.tmRowCheck:checked');
      const btn = document.getElementById('tmBulkDeleteBtn');
      const cnt = document.getElementById('tmBulkCount');
      const selAll = document.getElementById('tmSelectAll');
      const total  = document.querySelectorAll('.tmRowCheck');
      if (btn)  btn.style.display = checked.length > 0 ? '' : 'none';
      if (cnt)  cnt.textContent   = checked.length;
      if (selAll) selAll.indeterminate = checked.length > 0 && checked.length < total.length;
      if (selAll && checked.length === total.length && total.length > 0) selAll.checked = true;
      if (selAll && checked.length === 0) selAll.checked = false;
    }

    // --- Delete a single row ---
    function tmDeleteRow(siteId, region) {
      if (!confirm(`Remove assignment:\n${siteId} → ${TECH_MANAGER.data[region]?.[siteId] || '?'}\nfrom ${region}?`)) return;
      if (TECH_MANAGER.data[region] && TECH_MANAGER.data[region][siteId] !== undefined) {
        delete TECH_MANAGER.data[region][siteId];
        TECH_MANAGER._build();  // rebuild indexes
        showToast(`Removed ${siteId} from ${region}`, 'success');
        tmRenderTable();
      } else {
        showToast('Assignment not found', 'error');
      }
    }

    // --- Bulk delete selected rows ---
    function tmBulkDelete() {
      const checked = document.querySelectorAll('.tmRowCheck:checked');
      if (!checked.length) return;
      if (!confirm(`Delete ${checked.length} selected assignment${checked.length!==1?'s':''}? This cannot be undone.`)) return;
      let removed = 0;
      checked.forEach(cb => {
        const sid    = cb.dataset.siteid;
        const region = cb.dataset.region;
        if (TECH_MANAGER.data[region] && TECH_MANAGER.data[region][sid] !== undefined) {
          delete TECH_MANAGER.data[region][sid];
          removed++;
        }
      });
      TECH_MANAGER._build();
      showToast(`✅ Removed ${removed} assignment${removed!==1?'s':''}`, 'success');
      tmRenderTable();
    }

    // --- Inline editing (double-click a cell) ---
    function tmInlineEdit(cellEl, field, siteId, region) {
      if (cellEl.querySelector('input')) return; // already editing
      const currentVal = field === 'siteId' ? siteId : (TECH_MANAGER.data[region]?.[siteId] || '');
      const origHTML = cellEl.innerHTML;

      cellEl.innerHTML = '';
      const input = document.createElement('input');
      input.value = currentVal;
      input.style.cssText = 'width:100%;padding:4px 8px;border:2px solid var(--accent-500);border-radius:var(--radius-sm);font:inherit;background:var(--surface);color:var(--text-primary);outline:none;';
      cellEl.appendChild(input);
      input.focus();
      input.select();

      const commit = () => {
        const newVal = input.value.trim().toUpperCase();
        if (!newVal || newVal === currentVal.toUpperCase()) {
          cellEl.innerHTML = origHTML;
          return;
        }
        if (field === 'techName') {
          // Update technician name for this site
          if (TECH_MANAGER.data[region] && TECH_MANAGER.data[region][siteId] !== undefined) {
            TECH_MANAGER.data[region][siteId] = newVal;
            TECH_MANAGER._build();
            showToast(`✅ Updated: ${siteId} → ${newVal}`, 'success');
          }
        } else if (field === 'siteId') {
          // Rename a site ID — move the entry to new key
          if (TECH_MANAGER.data[region] && TECH_MANAGER.data[region][siteId] !== undefined) {
            if (TECH_MANAGER.data[region][newVal] !== undefined) {
              showToast(`Site ID "${newVal}" already exists in ${region}`, 'warning');
              cellEl.innerHTML = origHTML;
              return;
            }
            const techVal = TECH_MANAGER.data[region][siteId];
            TECH_MANAGER.data[region][newVal] = techVal;
            delete TECH_MANAGER.data[region][siteId];
            TECH_MANAGER._build();
            showToast(`✅ Site ID renamed: ${siteId} → ${newVal}`, 'success');
          }
        }
        tmRenderTable();
      };

      const cancel = () => { cellEl.innerHTML = origHTML; };

      input.addEventListener('keydown', e => {
        if (e.key === 'Enter')  { e.preventDefault(); commit(); }
        if (e.key === 'Escape') { e.preventDefault(); cancel(); }
      });
      input.addEventListener('blur', commit);
    }

    // --- Import CSV or JSON of new technicians ---
    // Expected CSV columns: Site ID, Technician, Region   (header row required)
    // Expected JSON: [{ "siteId": "IHS_NRW_001", "techName": "KENNY", "region": "nrw" }, ...]
    // Skips duplicates (existing Site IDs are never overwritten per user spec)
    function tmHandleImport(event) {
      const file = event.target.files[0];
      if (!file) return;
      event.target.value = ''; // reset so same file can be re-imported

      const ext = file.name.split('.').pop().toLowerCase();
      const reader = new FileReader();

      reader.onload = e => {
        try {
          let rows = [];

          if (ext === 'json') {
            const parsed = JSON.parse(e.target.result);
            if (!Array.isArray(parsed)) throw new Error('JSON must be an array of objects');
            parsed.forEach((obj, i) => {
              const sid    = String(obj.siteId || obj.site_id || obj['Site ID'] || '').trim().toUpperCase();
              const tech   = String(obj.techName || obj.tech_name || obj.technician || obj['Technician'] || '').trim().toUpperCase();
              const region = String(obj.region || obj.Region || '').trim().toLowerCase();
              if (sid && tech && region) rows.push({ sid, tech, region });
              else console.warn(`Import row ${i+1} skipped — missing siteId, techName or region`);
            });

          } else {
            // CSV parsing — handle comma or semicolon delimiters
            const lines = e.target.result.replace(/\r\n/g,'\n').replace(/\r/g,'\n').split('\n').filter(l => l.trim());
            if (!lines.length) throw new Error('CSV file is empty');
            const delim  = lines[0].includes(';') ? ';' : ',';
            const hdr    = lines[0].split(delim).map(h => h.trim().toLowerCase().replace(/[^a-z0-9]/g,''));
            const sidIdx = hdr.findIndex(h => h.includes('siteid') || h.includes('site'));
            const techIdx= hdr.findIndex(h => h.includes('tech') || h.includes('name'));
            const regIdx = hdr.findIndex(h => h.includes('region') || h.includes('reg'));

            if (sidIdx === -1 || techIdx === -1 || regIdx === -1) {
              throw new Error(`CSV must have columns: Site ID, Technician, Region. Found: ${lines[0]}`);
            }

            for (let i = 1; i < lines.length; i++) {
              const cols = lines[i].split(delim).map(c => c.trim().replace(/^"|"$/g,''));
              const sid    = (cols[sidIdx]  || '').toUpperCase();
              const tech   = (cols[techIdx] || '').toUpperCase();
              const region = (cols[regIdx]  || '').toLowerCase();
              if (sid && tech && region) rows.push({ sid, tech, region });
            }
          }

          if (!rows.length) { showToast('No valid rows found in file', 'warning'); return; }

          // Validate regions — must match an existing key in TECHNICIAN_DATA
          const validRegions = new Set(Object.keys(TECHNICIAN_DATA));
          // Also allow friendly labels → map them
          const regionAliases = {
            'nrw':'nrw','new ccs':'new_cbt','new_ccs':'new_cbt','old ccs':'old_cbt',
            'old_ccs':'old_cbt','eastern':'eastern','cbt':'new_cbt','new_cbt':'new_cbt',
            'old_cbt':'old_cbt'
          };
          let added = 0, skipped = 0, badRegion = 0;
          const importLog = [];

          rows.forEach(({ sid, tech, region }) => {
            const mappedRegion = regionAliases[region] || region;
            if (!validRegions.has(mappedRegion)) {
              badRegion++;
              importLog.push(`⚠️ Unknown region "${region}" for ${sid} — skipped`);
              return;
            }
            if (!TECHNICIAN_DATA[mappedRegion]) TECHNICIAN_DATA[mappedRegion] = {};
            if (TECHNICIAN_DATA[mappedRegion][sid] !== undefined) {
              skipped++;
              importLog.push(`⏭️ ${sid} already exists in ${mappedRegion} — skipped`);
              return;
            }
            TECHNICIAN_DATA[mappedRegion][sid] = tech;
            added++;
            importLog.push(`✅ Added: ${sid} → ${tech} (${mappedRegion})`);
          });

          TECH_MANAGER._build();  // rebuild all indexes

          // Show result toast + detailed modal
          showToast(`Import done — ${added} added · ${skipped} skipped · ${badRegion} bad region`, added > 0 ? 'success' : 'warning');

          // Show a brief result modal
          const modal = document.createElement('div');
          modal.className = 'modal-overlay';
          modal.style.display = 'flex';
          modal.innerHTML = `
            <div class="modal-container" style="max-width:520px;width:100%;max-height:80vh;overflow-y:auto;">
              <div class="modal-header">
                <h3 class="text-xl font-semibold"><i class="fa-regular fa-file-import" style="color:var(--accent-600);"></i> Import Results</h3>
                <button class="btn btn-icon btn-ghost" onclick="this.closest('.modal-overlay').remove()"><i class="fa-regular fa-xmark"></i></button>
              </div>
              <div class="modal-body">
                <div class="grid grid-cols-3 gap-3 mb-4 text-center">
                  <div class="card" style="background:var(--status-success-bg);">
                    <div class="text-2xl font-bold" style="color:var(--status-success);">${added}</div>
                    <div class="text-xs mt-1" style="color:var(--neutral-500);">Added</div>
                  </div>
                  <div class="card" style="background:var(--neutral-100);">
                    <div class="text-2xl font-bold" style="color:var(--neutral-500);">${skipped}</div>
                    <div class="text-xs mt-1" style="color:var(--neutral-500);">Skipped (duplicate)</div>
                  </div>
                  <div class="card" style="background:${badRegion?'var(--status-danger-bg)':'var(--neutral-100)'};">
                    <div class="text-2xl font-bold" style="color:${badRegion?'var(--status-danger)':'var(--neutral-400)'};">${badRegion}</div>
                    <div class="text-xs mt-1" style="color:var(--neutral-500);">Bad region</div>
                  </div>
                </div>
                <div style="font-family:var(--font-mono);font-size:0.72rem;max-height:280px;overflow-y:auto;padding:10px 12px;background:var(--neutral-100);border-radius:var(--radius-md);line-height:1.8;">
                  ${importLog.map(l => `<div>${escHtml(l)}</div>`).join('')}
                </div>
                ${badRegion > 0 ? `<div class="mt-3 p-3 rounded text-sm" style="background:var(--status-warning-bg);color:var(--neutral-700);"><strong>Valid region values:</strong> ${[...validRegions].join(', ')}<br>Also accepted: nrw, eastern, new ccs, old ccs, cbt</div>` : ''}
              </div>
              <div class="modal-footer">
                <button class="btn btn-primary" onclick="this.closest('.modal-overlay').remove();tmRenderTable()">Done</button>
              </div>
            </div>`;
          document.body.appendChild(modal);

        } catch(err) {
          showToast('Import failed: ' + err.message, 'error');
          console.error(err);
        }
      };
      reader.onerror = () => showToast('Could not read file', 'error');
      reader.readAsText(file, 'UTF-8');
    }

    // ============================================================
    // ===== PHASE 2+3: FUEL CHAT PARSER + AUTOMATION PAGE ========
    // ============================================================

    // Variation maps for fuzzy column matching (ported from FUEL_AUTO.py)
    const FIELD_VARIATIONS = {
      'CURRENT_RT':   ['rt','dg current run time','gd run time','runtime','run time','run','dg rt','dg run time'],
      'PREVIOUS_RT':  ['pre rt','previous run time','previous runtime','previous rt','previous gd rt'],
      'FUEL_FOUND':   ['fuel found','initial fuel level','initial','found','intial dp','initial dp','intial level'],
      'FUEL_ADDED':   ['fuel added','added','fuel add','added fuel','uplifted'],
      'SITE_ID':      ['site id','site i\'d','site id :','site i\'d:','cbt','nrw','est','code','site id:'],
      'SITE_NAME':    ['site name','site name','name'],
      'SUPPLIER':     ['fuel source','source','puma fuel','meru fuel'],
      'DATE':         ['date'],
      'CPH':          ['cph'],
      'TECHNICIAN':   ['name of technician','technician','tech','technician name']
    };

    const ALLOWED_SOURCES = ['SAHARA','MERU','PUMA','CCS','TOTAL','CCS FUEL'];

    // Region config for the parser
    const REGION_CONFIGS = {
      'New CCS':  { prefix:'IHS_CBT', techData: TECHNICIAN_DATA.new_cbt },
      'Old CCS':  { prefix:'IHS_CBT', techData: TECHNICIAN_DATA.old_cbt },
      'NRW':      { prefix:'IHS_NRW', techData: TECHNICIAN_DATA.nrw },
      'Eastern':  { prefix:'IHS_EST', techData: TECHNICIAN_DATA.eastern }
    };

    let _autoParseResults = [];  // holds preview rows
    let _autoLogLines = [];
    let _autoPageState = { dateFrom: '', dateTo: '', region: '' }; // persists across nav

    function renderAutomationPage(container) {
      container.innerHTML = `
      <div class="page-header mb-5">
        <div>
          <h2 class="font-bold tracking-tight">Fuel Chat Automation</h2>
          <p class="text-sm mt-1" style="color:var(--neutral-500)">Parse WhatsApp fuel supply messages and import into daily log</p>
        </div>
        <div class="flex gap-2">
          <button class="btn btn-secondary btn-sm" onclick="openPropagationModal()">
            <i class="fa-regular fa-rotate" style="color:var(--status-info);"></i> Run Propagation
          </button>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-4 mb-4">

        <!-- Left: Upload & Config -->
        <div class="card">
          <h4 class="font-semibold mb-3"><i class="fa-regular fa-gear" style="color:var(--accent-600);"></i> Configuration</h4>
          <div class="input-group mb-3">
            <label class="text-sm font-medium mb-1 block" style="color:var(--neutral-700)">Region / Report Type</label>
            <div class="select-wrapper">
              <select class="select-field" id="autoRegionSelect">
                <option value="New CCS" ${DB.currentRegion==='New CCS'?'selected':''}>New CCS (IHS_CBT — Kambole, Royd, Fackson…)</option>
                <option value="Old CCS" ${DB.currentRegion==='Old CCS'?'selected':''}>Old CCS (IHS_CBT — Lawrance, Cascious, Elijah…)</option>
                <option value="NRW" ${DB.currentRegion==='NRW'?'selected':''}>NRW (IHS_NRW — Kenny, Lombe, Abishy…)</option>
                <option value="Eastern" ${DB.currentRegion==='Eastern'?'selected':''}>Eastern (IHS_EST — Howard, Patrick, Charles…)</option>
              </select>
            </div>
          </div>
          <div class="input-group mb-3">
            <label class="text-sm font-medium mb-2 block" style="color:var(--neutral-700)">Upload WhatsApp Chat (.txt)</label>
            <label style="display:flex;align-items:center;gap:10px;cursor:pointer;padding:14px;border:2px dashed var(--neutral-300);border-radius:var(--radius-lg);transition:all 0.2s;" id="autoDropZone">
              <i class="fa-regular fa-file-arrow-up fa-lg" style="color:var(--accent-600);"></i>
              <span class="text-sm" style="color:var(--neutral-600);" id="autoFileName">Click to select a .txt file…</span>
              <input type="file" accept=".txt" style="display:none;" id="autoFileInput" onchange="autoHandleFile(event)">
            </label>
          </div>
          <div class="input-group mb-3">
            <label class="text-sm font-medium mb-2 block" style="color:var(--neutral-700)">
              Upload Target Excel Report (.xlsx)
              <span class="text-xs font-normal ml-1" style="color:var(--neutral-400);">— parsed data will be written into this file</span>
            </label>
            <label style="display:flex;align-items:center;gap:10px;cursor:pointer;padding:14px;border:2px dashed var(--neutral-300);border-radius:var(--radius-lg);transition:all 0.2s;" id="autoXlsxDropZone">
              <i class="fa-regular fa-file-excel fa-lg" style="color:var(--status-success);"></i>
              <span class="text-sm" style="color:var(--neutral-600);" id="autoXlsxFileName">Click to select an .xlsx file…</span>
              <input type="file" accept=".xlsx" style="display:none;" id="autoXlsxInput" onchange="autoHandleXlsx(event)">
            </label>
            <div id="autoXlsxInfo" style="display:none;margin-top:8px;padding:8px 12px;background:var(--status-success-bg);border-radius:var(--radius-md);border:1px solid var(--status-success);font-size:0.75rem;color:var(--neutral-700);"></div>
          </div>
          <div class="input-group mb-3">
            <label class="text-sm font-medium mb-1 block" style="color:var(--neutral-700)">Date Range Filter (optional)</label>
            <div class="flex gap-2">
              <input type="date" class="input-field flex-1" id="autoDateFrom" style="padding:10px 12px;" title="From date">
              <input type="date" class="input-field flex-1" id="autoDateTo" style="padding:10px 12px;" title="To date">
            </div>
          </div>
          <div class="flex gap-3 mt-4">
            <button class="btn btn-primary flex-1" onclick="autoRunParser()" id="autoRunBtn" disabled>
              <i class="fa-regular fa-play"></i> Parse & Preview
            </button>
            <button class="btn btn-ghost btn-sm" onclick="autoClearAll()"><i class="fa-regular fa-trash"></i></button>
          </div>
        </div>

        <!-- Right: Processing Log -->
        <div class="card" style="padding:0;overflow:hidden;">
          <div class="p-4 pb-2" style="border-bottom:1px solid var(--neutral-200);">
            <h4 class="font-semibold"><i class="fa-regular fa-terminal" style="color:var(--status-success);"></i> Processing Log</h4>
          </div>
          <div id="autoLog" style="font-family:var(--font-mono);font-size:0.75rem;padding:12px 14px;height:220px;overflow-y:auto;color:var(--neutral-700);line-height:1.6;background:var(--neutral-100);border-radius:0 0 var(--radius-lg) var(--radius-lg);"></div>
        </div>
      </div>

      <!-- Preview Results -->
      <div id="autoPreviewSection" style="display:none;">
        <div class="card mb-4" id="autoSummaryCard"></div>
        <div class="card" style="padding:0;overflow:hidden;">
          <div class="p-4 pb-2 flex items-center justify-between" style="border-bottom:1px solid var(--neutral-200);">
            <h4 class="font-semibold">Parsed Entries — Review Before Import</h4>
            <div class="flex gap-2">
              <button class="btn btn-ghost btn-sm" onclick="autoSelectAll(true)">Select All</button>
              <button class="btn btn-ghost btn-sm" onclick="autoSelectAll(false)">Deselect All</button>
            </div>
          </div>
          <div style="overflow-x:auto;max-height:420px;overflow-y:auto;">
            <table class="table" id="autoPreviewTable">
              <thead><tr>
                <th style="width:40px;"></th>
                <th>Date</th><th>Site ID</th><th>Technician</th>
                <th>Fuel Found</th><th>Fuel Added</th><th>Supplier</th><th>CPH</th><th>Bowser</th><th>Status</th>
              </tr></thead>
              <tbody id="autoPreviewBody"></tbody>
            </table>
          </div>
          <div class="p-4 flex gap-3 justify-between items-center" style="border-top:1px solid var(--neutral-200);">
            <div id="autoPreviewCount" class="text-sm" style="color:var(--neutral-500);"></div>
            <div class="flex gap-2">
              <button class="btn btn-secondary btn-sm" onclick="autoExportCSV()" id="autoExportBtn">
                <i class="fa-regular fa-file-csv"></i> CSV
              </button>
              <button class="btn btn-secondary btn-sm" onclick="autoExportXLSX()">
                <i class="fa-regular fa-file-excel"></i> New Excel
              </button>
              <button class="btn btn-secondary btn-sm" onclick="autoWriteToUploadedXlsx()" id="autoWriteXlsxBtn" style="display:none;">
                <i class="fa-regular fa-file-arrow-down" style="color:var(--status-success);"></i> Write to Excel &amp; Download
              </button>
              <button class="btn btn-primary" onclick="autoConfirmImport()" id="autoConfirmBtn">
                <i class="fa-regular fa-file-import"></i> Import into Daily Log
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Import Result Summary (shown after confirm) -->
      <div id="autoResultSection" style="display:none;" class="mt-4">
        <div class="card" id="autoResultCard" style="border-left:4px solid var(--status-success);"></div>
      </div>`;

      // Restore log if any
      autoRefreshLog();

      // Restore date filter and region from state
      const df = document.getElementById('autoDateFrom');
      const dt = document.getElementById('autoDateTo');
      const rs = document.getElementById('autoRegionSelect');
      if (df && _autoPageState.dateFrom) df.value = _autoPageState.dateFrom;
      if (dt && _autoPageState.dateTo)   dt.value = _autoPageState.dateTo;
      if (rs && _autoPageState.region)   rs.value = _autoPageState.region;

      // Wire up state persistence for date/region changes
      if (df) df.addEventListener('change', () => { _autoPageState.dateFrom = df.value; });
      if (dt) dt.addEventListener('change', () => { _autoPageState.dateTo   = dt.value; });
      if (rs) rs.addEventListener('change', () => { _autoPageState.region   = rs.value; });

      // Restore parse preview if results still in memory
      if (_autoParseResults.length > 0) {
        setTimeout(() => autoRenderPreview(_autoParseResults), 50);
      }

      // Restore file label if file still loaded
      if (window._autoFile) {
        const fn = document.getElementById('autoFileName');
        const btn = document.getElementById('autoRunBtn');
        if (fn) fn.textContent = window._autoFile.name;
        if (btn) btn.removeAttribute('disabled');
      }
      // Restore xlsx file label if still loaded
      if (window._autoXlsxFile) {
        const xn = document.getElementById('autoXlsxFileName');
        if (xn) xn.textContent = window._autoXlsxFile.name;
        // Re-peek sheet names
        const reader = new FileReader();
        reader.onload = e => {
          try {
            const wb2 = XLSX.read(new Uint8Array(e.target.result), { type: 'array' });
            const infoEl = document.getElementById('autoXlsxInfo');
            if (infoEl) {
              infoEl.style.display = 'block';
              infoEl.innerHTML = `<i class="fa-regular fa-circle-check" style="color:var(--status-success);"></i> <strong>${window._autoXlsxFile.name}</strong> — ${wb2.SheetNames.length} sheet(s): ${wb2.SheetNames.map(s=>`<em>${s}</em>`).join(', ')}`;
            }
          } catch(_) {}
        };
        reader.readAsArrayBuffer(window._autoXlsxFile);
      }
    }

    function autoHandleFile(event) {
      const file = event.target.files[0];
      if (!file) return;
      document.getElementById('autoFileName').textContent = file.name;
      document.getElementById('autoRunBtn').removeAttribute('disabled');
      window._autoFile = file;
      autoLog(`📂 File loaded: ${file.name} (${(file.size/1024).toFixed(1)} KB)`);
    }

    // ---- XLSX upload handler ----
    function autoHandleXlsx(event) {
      const file = event.target.files[0];
      if (!file) return;
      window._autoXlsxFile = file;
      document.getElementById('autoXlsxFileName').textContent = file.name;
      autoLog(`📊 Excel template loaded: ${file.name} (${(file.size/1024).toFixed(1)} KB)`);

      // Peek at sheet names using SheetJS
      const reader = new FileReader();
      reader.onload = e => {
        try {
          const wb = XLSX.read(new Uint8Array(e.target.result), { type: 'array' });
          const sheets = wb.SheetNames;
          const infoEl = document.getElementById('autoXlsxInfo');
          if (infoEl) {
            infoEl.style.display = 'block';
            infoEl.innerHTML = `<i class="fa-regular fa-circle-check" style="color:var(--status-success);"></i> <strong>${file.name}</strong> — ${sheets.length} sheet${sheets.length!==1?'s':''}: ${sheets.map(s=>`<em>${s}</em>`).join(', ')}`;
          }
          // Show write button if preview has results
          const writeBtn = document.getElementById('autoWriteXlsxBtn');
          if (writeBtn && _autoParseResults.length > 0) writeBtn.style.display = '';
        } catch(err) {
          autoLog('⚠️ Could not read Excel file: ' + err.message, 'warn');
        }
      };
      reader.readAsArrayBuffer(file);
    }

    function autoLog(msg, type) {
      const color = type === 'error' ? '#dc2626' : type === 'warn' ? '#d97706' : type === 'ok' ? '#16a34a' : 'inherit';
      _autoLogLines.push(`<span style="color:${color};">${escHtml(msg)}</span>`);
      // Throttle DOM updates — only refresh if no pending frame
      if (!autoLog._pending) {
        autoLog._pending = true;
        requestAnimationFrame(() => { autoLog._pending = false; autoRefreshLog(); });
      }
    }

    function autoRefreshLog() {
      const el = document.getElementById('autoLog');
      if (!el) return;
      // Only render last 300 lines to avoid huge innerHTML
      const lines = _autoLogLines.length > 300 ? _autoLogLines.slice(-300) : _autoLogLines;
      el.innerHTML = lines.length ? lines.join('<br>') : '<span style="color:var(--neutral-400);">Ready. Load a .txt file and press Parse.</span>';
      el.scrollTop = el.scrollHeight;
    }

    function escHtml(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

    function autoClearAll() {
      _autoLogLines = [];
      _autoParseResults = [];
      window._autoFile = null;
      window._autoXlsxFile = null;
      const fi = document.getElementById('autoFileInput');
      if (fi) fi.value = '';
      const fn = document.getElementById('autoFileName');
      if (fn) fn.textContent = 'Click to select a .txt file…';
      const xi = document.getElementById('autoXlsxInput');
      if (xi) xi.value = '';
      const xn = document.getElementById('autoXlsxFileName');
      if (xn) xn.textContent = 'Click to select an .xlsx file…';
      const xinfo = document.getElementById('autoXlsxInfo');
      if (xinfo) { xinfo.style.display = 'none'; xinfo.innerHTML = ''; }
      const writeBtn = document.getElementById('autoWriteXlsxBtn');
      if (writeBtn) writeBtn.style.display = 'none';
      const btn = document.getElementById('autoRunBtn');
      if (btn) btn.setAttribute('disabled','');
      const sec = document.getElementById('autoPreviewSection');
      if (sec) sec.style.display = 'none';
      const res = document.getElementById('autoResultSection');
      if (res) res.style.display = 'none';
      const df = document.getElementById('autoDateFrom');
      const dt = document.getElementById('autoDateTo');
      if (df) df.value = '';
      if (dt) dt.value = '';
      autoRefreshLog();
    }

    function autoRunParser() {
      if (!window._autoFile) return showToast('No file loaded', 'warning');
      const btn = document.getElementById('autoRunBtn');
      if (btn) { btn.setAttribute('disabled',''); btn.innerHTML = '<i class="fa-regular fa-spinner fa-spin"></i> Parsing…'; }
      const reader = new FileReader();
      reader.onload = e => {
        try {
          _autoLogLines = [];
          autoLog('⚙️  Starting parser…');
      const region = document.getElementById('autoRegionSelect').value;
      _autoPageState.region = region;
      const results = fuelChatParse(e.target.result, region);
          _autoParseResults = results;
          autoRenderPreview(results);
        } catch(err) {
          autoLog('❌ Fatal error: ' + err.message, 'error');
          showToast('Parser error: ' + err.message, 'error');
        } finally {
          if (btn) { btn.removeAttribute('disabled'); btn.innerHTML = '<i class="fa-regular fa-play"></i> Parse & Preview'; }
        }
      };
      reader.onerror = () => {
        autoLog('❌ Could not read file', 'error');
        if (btn) { btn.removeAttribute('disabled'); btn.innerHTML = '<i class="fa-regular fa-play"></i> Parse & Preview'; }
      };
      reader.readAsText(window._autoFile, 'UTF-8');
    }

    // ---- THE CORE PARSER (ported from FUEL_AUTO.py) ----
    // ============================================================
    // PER-REGION VARIATION MAPS — exact port of Python MultiSourceConfig
    // ============================================================
    const REGION_VARIATION_MAPS = {
      'New CCS': {
        'CURRENT DG RUN HOURS':  ['dg current run time','gd run time','dg run time','dg run','dg rt','runtime','run time','run'],
        'PREVIOUS DG RUN HOURS': ['previous run time','previous runtime','previous time','pre rt','previous rt','previous'],
        'FUEL FOUND':  ['initial fuel level','initial fuel','fuel found','initial dp','intial dp','intial level','initial'],
        'FUEL ADDED':  ['fuel added','added fuel','uplifted','added'],
        'QTY FUEL':    ['qty fuel','qty'],
        'FUEL LEFT':   ['fuel quantity left','fuel quantity left:','quantity left'],
        'BOWSER PLATE':['bowser number plate','bowser plate','number plate'],
        'OIL LEVEL':   ['dg oil level','oil level'],
        'FAN BELT':    ['fan belt status','fan belt'],
        'COOLANT':     ['dg coolant level','coolant level','coolant'],
        'FUEL LEAKS':  ['fuel lines leakages','fuel leakage','leakages'],
        'SITE ID':     ['site id','site i\'d','cbt'],
        'SITE NAME':   ['site name','name'],
        'SUPPLIER':    ['fuel source','source'],
        'DATE':        ['date'],
        'CPH':         ['cph'],
        'NAME OF TECHNICIAN': ['name of technician','technician','tech']
      },
      'Old CCS': {
        'CURRENT DG RUN HOURS':  ['dg current run time','gd run time','dg run time','runtime','run time','run'],
        'PREVIOUS DG RUN HOURS': ['previous run time','previous runtime','previous time','previous rt','previous'],
        'FUEL FOUND':  ['initial fuel level','initial fuel','fuel found','initial dp','intial dp','initial'],
        'FUEL ADDED':  ['fuel added','added fuel','uplifted','added'],
        'QTY FUEL':    ['qty fuel','qty'],
        'FUEL LEFT':   ['fuel quantity left','quantity left'],
        'BOWSER PLATE':['bowser number plate','bowser plate','number plate'],
        'OIL LEVEL':   ['dg oil level','oil level'],
        'FAN BELT':    ['fan belt status','fan belt'],
        'COOLANT':     ['dg coolant level','coolant level'],
        'FUEL LEAKS':  ['fuel lines leakages','fuel leakage'],
        'SITE ID':     ['site id','site i\'d','cbt'],
        'SITE NAME':   ['site name'],
        'SUPPLIER':    ['fuel source','source'],
        'DATE':        ['date'],
        'CPH':         ['cph'],
        'NAME OF TECHNICIAN': ['name of technician','technician']
      },
      'NRW': {
        'CURRENT DG RUN HOURS':  ['gd run time','dg run time','dg rt','run time','runtime','runTime','rt'],
        'PREVIOUS DG RUN HOURS': ['previous gd run time','previous gd rt','previous run time','previous rt','pre rt'],
        'FUEL FOUND':  ['initial fuel level','initial dp','intial dp','fuel found','found','initial'],
        'FUEL ADDED':  ['added fuel','fuel added','added','uplifted'],
        'SITE ID':     ['site id','site i\'d','site i\'d:','nrw','code'],
        'SITE NAME':   ['site name','site :'],
        'SUPPLIER':    ['fuel source','source','puma(ccs fuel)','puma fuel','meru fuel'],
        'DATE':        ['date'],
        'CPH':         ['cph'],
        'NAME OF TECHNICIAN': ['name of technician','technician name','technician']
      },
      'Eastern': {
        'CURRENT DG RUN HOURS':  ['run time','runtime','runt','run _time','runtime','rt','run'],
        'PREVIOUS DG RUN HOURS': ['previous runtime','previous run time','previous rt'],
        'FUEL FOUND':  ['intial dp','initial dp','intial level','initial level','initial'],
        'FUEL ADDED':  ['fuel added','fuel aded','fuel add','fuel axdded','added fuel','added'],
        'SITE ID':     ['est','nth','site id','site i\'d','site i\'d:','site id :'],
        'SITE NAME':   ['site name','name'],
        'SUPPLIER':    ['source','fuel source'],
        'DATE':        ['date'],
        'CPH':         ['cph'],
        'NAME OF TECHNICIAN': ['name of technician','technician name','technician','tech']
      }
    };

    // ============================================================
    // CORE PARSER — faithful JS port of UniversalParser._split_blocks
    //               + UniversalParser._parse_block
    // ============================================================
    // Global skipped-entries log — reset on each parse run
    let _skippedLog = []; // [{reason, block, date, siteId}]

    function fuelChatParse(rawText, regionName) {
      _skippedLog = []; // reset
      const cfg    = REGION_CONFIGS[regionName] || REGION_CONFIGS['New CCS'];
      const prefix = cfg.prefix;
      const varMap = REGION_VARIATION_MAPS[regionName] || REGION_VARIATION_MAPS['New CCS'];

      autoLog(`📄 Loaded ${rawText.length} chars for region: ${regionName}`);

      // ── Stage 1: Split the raw text on every WA message header ──
      // Mirrors Python: re.split(r'(?=\d{1,2}/\d{1,2}/\d{4},\s*\d{1,2}:\d{2}\s*-)', content)
      // Also handles iOS format: [DD/MM/YYYY, HH:MM:SS AM] Sender:
      const waHeaderRe = /(\d{1,2}\/\d{1,2}\/\d{2,4}),\s*\d{1,2}:\d{2}/;

      // Split so that each segment STARTS with a WA timestamp line
      // CRITICAL: require the timestamp to start at a line boundary (^) so the
      // lookahead never fires mid-number. E.g. "22/03/2026" must NOT be split
      // at the second "2" leaving "2/03/2026". The 'm' flag makes ^ match \n.
      const rawSegments = rawText
        .replace(/\r\n/g,'\n').replace(/\r/g,'\n')
        .split(/(?=(?:^|\n)(?:\[)?\d{1,2}\/\d{1,2}\/\d{2,4},\s*\d{1,2}:\d{2})/m);

      autoLog(`📨 ${rawSegments.length} raw WA segments`);

      // Extract the WA post date from the WA header line of a segment.
      // We require the full timestamp format: DD/MM/YYYY, HH:MM - Sender:
      // This prevents accidentally picking up a technician's written date
      // (e.g. "21/03/26") as the WA timestamp.
      const waDateFromSeg = seg => {
        // Match a complete WA header: digits/digits/4-digit-year, HH:MM
        const m = seg.match(/(\d{1,2})\/(\d{1,2})\/(\d{4}),\s*\d{1,2}:\d{2}/);
        if (!m) return null;
        return `${m[3]}-${m[2].padStart(2,'0')}-${m[1].padStart(2,'0')}`;
      };

      // Extract the WA sender name from the first line of a segment
      // Format: "DD/MM/YYYY, HH:MM - Sender Name: message"
      const waSenderFromSeg = seg => {
        const m = seg.match(/\d{1,2}\/\d{1,2}\/\d{2,4},\s*\d{1,2}:\d{2}\s*-\s*([^:]+):/);
        if (!m) return '';
        // Clean up tildes (~) and emoji used in WA group display names
        return m[1].trim().replace(/^[~\s]+/, '').replace(/\s+$/, '');
      };

      // ── Stage 2: Within each WA segment, sub-split on site-ID lines ──
      // Mirrors Python site_split_pat
      // Prefixes per region
      const shortPfx = prefix.split('_').pop(); // CBT / NRW / EST
      // Build a pattern that matches the START of a site-ID line
      // (IHS_ optional, then CBT/NRW/EST then digits, or emoji 🆔, or Code:)
      const siteSplitRe = new RegExp(
        `(?=(?:^|\\n)\\s*(?:[✅👉🏾👉✍️]\\s*)*`+
        `(?:(?:IHS[_\\s]*)?(?:${shortPfx}|NTH)[\\s_:,\\-\\.]*\\d|🆔\\s*\\d|Code\\s*[:\\-]?\\s*\\d))`,
        'im'
      );

      const blocks = []; // [{text, waDate, waSender}]

      for (const seg of rawSegments) {
        const trimmed = seg.trim();
        if (!trimmed) continue;
        const waDate   = waDateFromSeg(trimmed);   // YYYY-MM-DD or null
        const waSender = waSenderFromSeg(trimmed); // e.g. "Lombe", "Mr Kenny CCS"

        // Sub-split on site-ID boundary lines within this WA message
        const subBlocks = trimmed.split(siteSplitRe);

        // ── CCS extra split: also split on "REFUELING TEMPLATE" headers ──
        // CCS technicians often paste multiple reports in one WA message without
        // a site-ID line at the start. Split those apart here.
        const ccsSubBlocks = [];
        for (const sb of subBlocks) {
          // Check if this sub-block contains multiple REFUELING TEMPLATE headers
          if (/REFUELING\s+TEMPLATE/i.test(sb)) {
            const refuelParts = sb.split(/(?=REFUELING\s+TEMPLATE)/i);
            for (const part of refuelParts) {
              const t = part.trim();
              if (t) ccsSubBlocks.push(t);
            }
          } else {
            ccsSubBlocks.push(sb);
          }
        }

        for (const sb of ccsSubBlocks) {
          const t = sb.trim();
          if (!t || t.length < 5) continue;

          // Gate: must look like a fuel report (same as Python _split_blocks filter)
          const hasSite      = new RegExp(`(?:IHS[_\\s]*)?(?:${shortPfx}|NTH)[\\s_:,\\-\\.]*\\d`,'i').test(t);
          const hasEmojiId   = /🆔\s*\d/.test(t);
          const hasCodeId    = /\bCode\s*[:\-]?\s*\d/i.test(t);
          // "Site id 050m" / "Site ID: 050m" style — no region prefix, just a numeric ID
          const hasSiteLabel = /Site\s*I[Dd]\s*[:\s]\s*\d/i.test(t);
          const hasFuel      = /(fuel|found|added|runtime|RT\b|Run\s*Time|Uplifted)/i.test(t);
          const hasStructure = /(Site|Date|Found|Added|RT|Run|CPH|Initial|Fuel)\s*[:\-]/i.test(t);
          // Skip fuel-request / planning messages — have site IDs but zero fuel data
          const isFuelRequest = /fuel\s*request\s*for/i.test(t);
          // CCS: also admit blocks that start with REFUELING TEMPLATE and have fuel structure
          const isRefuelingTemplate = /REFUELING\s+TEMPLATE/i.test(t);

          if (isFuelRequest) { continue; } // silently skip fuel-request messages
          if (!(hasSite || hasEmojiId || hasCodeId || hasSiteLabel || isRefuelingTemplate || (hasFuel && hasStructure))) continue;
          blocks.push({ text: t, waDate, waSender });
        }
      }

      autoLog(`📦 ${blocks.length} fuel blocks identified`);

      // Date range filter
      const dateFrom = document.getElementById('autoDateFrom')?.value || '';
      const dateTo   = document.getElementById('autoDateTo')?.value   || '';
      if (dateFrom || dateTo) autoLog(`📅 Date filter: ${dateFrom||'any'} → ${dateTo||'any'}`);

      const results = [];
      let matched=0, skipped=0, faulty=0, filtered=0;

      for (let bi=0; bi<blocks.length; bi++) {
        const {text, waDate, waSender} = blocks[bi];
        const entry = parseBlock(text, bi, waDate, prefix, varMap, waSender);
        if (!entry) { skipped++; continue; } // null = no fuel data — not worth logging
        if (entry._faulty) {
          faulty++;
          autoLog(`⚠️  Block ${bi+1}: ${entry._reason}`, 'warn');
          if (_skippedLog.length < 200) _skippedLog.push({ reason: entry._reason || 'Faulty entry', date: entry.date || '', siteId: entry.siteId || '', block: text.substring(0,120) });
          results.push(entry);
          continue;
        }
        // Date-range filter (entry.date is YYYY-MM-DD)
        if (dateFrom && entry.date < dateFrom) { filtered++; _skippedLog.push({reason:`Date ${entry.date} before filter start ${dateFrom}`, date:entry.date, siteId:entry.siteId||'', block:text.substring(0,120)}); continue; }
        if (dateTo   && entry.date > dateTo)   { filtered++; _skippedLog.push({reason:`Date ${entry.date} after filter end ${dateTo}`, date:entry.date, siteId:entry.siteId||'', block:text.substring(0,120)}); continue; }
        matched++;
        results.push(entry);
      }

      autoLog(`✅ Done — Valid: ${matched} | Faulty: ${faulty} | Skipped: ${skipped}${filtered?` | Filtered: ${filtered}`:''}`, 'ok');
      return results;
    }

    // ── parseBlock — faithful port of UniversalParser._parse_block ──
    function parseBlock(blockText, blockIdx, waDate, prefix, varMap, waSender) {
      waSender = waSender || '';
      // Strip WA header cruft from lines for clean processing
      const waHeaderStrip = /\d{1,2}\/\d{1,2}\/\d{4},\s*\d{1,2}:\d{2}\s*-[^:]+:/g;
      // ── CCS PRE-CLEAN ── Applied before any parsing so all downstream logic is clean
      // 1. Superscript "⁵Previous" → "Previous" (Faxon's copy-paste artifact)
      let blockPreClean = blockText.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹]+\s*(Previous)/gi, '$1');
      // 2. Dot-separated date "04.04.26" → "04/04/26"
      blockPreClean = blockPreClean.replace(/(\d{1,2})\.(\d{1,2})\.(\d{2,4})/g, '$1/$2/$3');
      // 3. Spaces inside numbers e.g. "10 0" → "100" and "2 .5" → "2.5"
      //    Only on value sides (after colon/separator) to avoid matching site IDs
      blockPreClean = blockPreClean.replace(/:\s*(\d+)\s+0(?=\s*$|\s*\n)/gm, ': $10');
      blockPreClean = blockPreClean.replace(/(\d)\s+\.\s*(\d)/g, '$1.$2');
      // 4. "stollen"/"Stollen" → "stolen" (typo normalisation for stolen fuel)
      blockPreClean = blockPreClean.replace(/stollen/gi, 'stolen');
      // 5. "Qty" lines that have both label and value on same line → keep as-is (handled by varMap)
      const cleanText = blockPreClean.replace(waHeaderStrip, '').trim();
      const lines = cleanText.split('\n').map(l=>l.trim()).filter(Boolean);
      if (!lines.length) return null;

      const data = {};

      // ── 1. DATE — mirrors normalize_date() with WA drift correction ──
      // Pre-clean: remove spaces inside date like "14 /12/2025"
      // Note: dot-dates already converted to slash in pre-clean above
      let dateClean = cleanText.replace(/(\d+)\s*\/\s*/g,'$1/');
      // Fix letter-digit typos like "3p/09" → "30/09"
      dateClean = dateClean.replace(/(\d)([A-Za-z])\//g, (_, d) => d+'0/');

      let writtenDate = null;
      // Pattern 1: "Date: DD/MM/YY", "Date:DD/MM/YY", "Date28/03/26" (no separator)
      // Strip the WA header line first so we don't match its timestamp as the written date.
      const dateSearchText = dateClean.replace(/\d{1,2}\/\d{1,2}\/\d{4},\s*\d{1,2}:\d{2}\s*-[^\n]*/g, '');
      const dateM1 = dateSearchText.match(/(?:Date\s*[:\-=*.]?\s*)(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})/i);
      if (dateM1) {
        const s = dateM1[1].replace(/-/g,'/');
        const p = s.split('/');
        if (p.length===3) {
          let yr = p[2]; if (yr.length===2) yr='20'+yr;
          writtenDate = `${yr}-${p[1].padStart(2,'0')}-${p[0].padStart(2,'0')}`;
        }
      }
      // Pattern 1b: bare date with no "Date" label at all (e.g. "22/03/26" alone on a line)
      // Only use if no labelled date was found above.
      if (!writtenDate) {
        const bareM = dateSearchText.match(/(?:^|\n)\s*(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})\s*(?:\n|$)/);
        if (bareM) {
          const s = bareM[1].replace(/-/g,'/');
          const p = s.split('/');
          if (p.length===3) {
            let yr = p[2]; if (yr.length===2) yr='20'+yr;
            writtenDate = `${yr}-${p[1].padStart(2,'0')}-${p[0].padStart(2,'0')}`;
          }
        }
      }
      // Pattern 2: spaced date "14 - 12 - 2025"
      if (!writtenDate) {
        const dateM2 = dateClean.match(/(\d{1,2})\s*[-_]\s*(\d{1,2})\s*[-_]\s*(\d{2,4})/);
        if (dateM2) {
          let yr=dateM2[3]; if(yr.length===2) yr='20'+yr;
          writtenDate = `${yr}-${dateM2[2].padStart(2,'0')}-${dateM2[1].padStart(2,'0')}`;
        }
      }

      // Pattern 3: "DATE 25 - 03 - 26" at bottom of Lombe blocks (BEFORE drift check)
      if (!writtenDate) {
        const dateM3 = dateSearchText.match(/\bDATE\s+(\d{1,2})\s*[-_]\s*(\d{1,2})\s*[-_]\s*(\d{2,4})/i);
        if (dateM3) {
          let yr = dateM3[3]; if (yr.length===2) yr='20'+yr;
          writtenDate = `${yr}-${dateM3[2].padStart(2,'0')}-${dateM3[1].padStart(2,'0')}`;
        }
      }

      // WA drift correction — applied AFTER all written-date patterns are tried.
      // Mirrors Python _MAX_DATE_DRIFT_DAYS = 30.
      // Raised to 60 to accommodate remote-area technicians who post many days late.
      const MAX_DRIFT_DAYS = 60;
      if (writtenDate && waDate) {
        const drift = Math.abs((new Date(writtenDate) - new Date(waDate)) / 86400000);
        if (drift > MAX_DRIFT_DAYS) {
          if (drift >= 330 && drift <= 400) {
            // Year typo (e.g. "23/03/25" when it should be "23/03/26") — keep written date
            autoLog(`⚠️  Block ${blockIdx+1}: year-typo drift ${drift.toFixed(0)}d — keeping written date`, 'warn');
          } else {
            autoLog(`⚠️  Block ${blockIdx+1}: drift ${drift.toFixed(0)}d — using WA date ${waDate}`, 'warn');
            writtenDate = waDate;
          }
        }
      }

      if (writtenDate)      data['CURRENT VISIT DATE'] = writtenDate;
      else if (waDate)      { data['CURRENT VISIT DATE'] = waDate; autoLog(`⚠️  Block ${blockIdx+1}: no written date — using WA date`,'warn'); }

      // ── 2. SITE ID — mirrors normalize_site_id() ──
      const shortPfx = prefix.split('_').pop();

      // ── normaliseSiteId ──────────────────────────────────────────────────────
      // Enforces the canonical format: IHS_<REGION>_<3-digit-zero-padded><M|A>
      //   e.g.  "IHS_NRW_35M"  → "IHS_NRW_035M"
      //         "IHS_EST_4A"   → "IHS_EST_004A"
      //         "ihs_nrw_035m" → "IHS_NRW_035M"
      //         "IHS_EST_304M" → "IHS_EST_304M"  (already correct, unchanged)
      //         "IHS_NRW_1234M"→ "IHS_NRW_1234M" (4-digit — left as-is, no prefix data uses 4 digits)
      // rawSuffix is the captured part after the region prefix, e.g. "35M", "004A", "210"
      function normaliseSiteId(rawSuffix) {
        // Uppercase the whole thing first
        const s = rawSuffix.trim().toUpperCase();
        // Separate the numeric part from the trailing letter(s)
        const m = s.match(/^(\d+)([A-Z]*)$/);
        if (!m) return `${prefix}_${s}`; // unrecognised format — pass through uppercase
        const digits = m[1];
        const letter = m[2]; // 'M', 'A', or '' if missing
        // Zero-pad to 3 digits only when the number is < 3 digits
        // Numbers already 3+ digits are left exactly as-is
        const padded = digits.length < 3 ? digits.padStart(3, '0') : digits;
        // If no suffix letter present, leave without adding one (parser will match
        // later via TECH_MANAGER even without letter when the TECHNICIAN_DATA key has one)
        return `${prefix}_${padded}${letter}`;
      }

      // Build site regex matching Python's site_pattern
      const siteRe = new RegExp(
        `(?:IHS[_\\s]*)?(?:${shortPfx}|NTH)[\\s_:,\\-\\.]*([0-9]{1,4}[A-Za-z]{0,2})`,
        'i'
      );
      let siteId = '';
      const siteM = cleanText.match(siteRe);
      if (siteM) {
        siteId = normaliseSiteId(siteM[1]);
      }
      // Emoji fallback: 🆔 35M  or  🆔 001M
      if (!siteId) {
        const em = cleanText.match(/🆔\s*(\d{1,4}[A-Za-z]{0,2})/);
        if (em) siteId = normaliseSiteId(em[1]);
      }
      // Code: fallback  e.g. "Code: 35M"
      if (!siteId) {
        const cm = cleanText.match(/\bCode\s*[:\-]?\s*(\d{1,4}[A-Za-z]{0,2})/i);
        if (cm) siteId = normaliseSiteId(cm[1]);
      }
      // Bare "Site I'd: 286A" fallback (no region prefix in message)
      if (!siteId) {
        const bm = cleanText.match(/Site\s*I'?d\s*[:\-]?\s*(\d{2,4}[A-Za-z]{0,2})/i);
        if (bm) siteId = normaliseSiteId(bm[1]);
      }
      // "Site id 050m" / "Site ID 050m" — no prefix, just numeric id after label
      if (!siteId) {
        const sm = cleanText.match(/Site\s*[Ii][Dd]\s*[:\s]\s*(\d{2,4}[A-Za-z]{0,2})/i);
        if (sm) siteId = normaliseSiteId(sm[1]);
      }

      if (siteId) {
        data['SITE ID']       = siteId;
        data['I.H.S SITE ID'] = siteId;
      }

      // ── 3. KEY-VALUE EXTRACTION — mirrors _parse_block line loop ──
      // Supports separators: : - = ;  AND no-separator Kenny-style ("RT 5093")
      for (const line of lines) {
        const lowerLine = line.toLowerCase();
        for (const [col, variants] of Object.entries(varMap)) {
          if (data[col] && col !== 'NAME OF TECHNICIAN') continue;
          for (const variant of variants) {
            if (!lowerLine.includes(variant.toLowerCase())) continue;
            // Try separator split first
            const sepMatch = line.match(/^(.+?)\s*[:\-=;]\s*(.+)$/);
            if (sepMatch) {
              data[col] = sepMatch[2].trim();
            } else {
              // No separator — strip keyword from start (Kenny-style)
              const stripped = line.replace(new RegExp('^\\s*'+variant.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\s*','i'),'').trim();
              if (stripped) data[col] = stripped;
            }
            break;
          }
          if (data[col]) break;
        }
      }

      // ── 4. SITE NAME extraction ──
      // "Site Name: ..." label
      if (!data['SITE NAME']) {
        const snM = cleanText.match(/Site\s*Name\s*[:\-]?\s*(.+)/i);
        if (snM) {
          let sn = snM[1].split('\n')[0].trim();
          sn = sn.replace(/Site\s*I'?d|Site\s*ID|Run Time/i,'').trim();
          if (sn) data['SITE NAME'] = sn;
        }
      }
      // Short "Site: name" label
      if (!data['SITE NAME']) {
        const snM2 = cleanText.match(/(?<!\w)Site\s*[:\-]\s*(.+)/i);
        if (snM2) {
          const sn = snM2[1].split('\n')[0].trim();
          if (sn && !/^(ID|I'd|name)/i.test(sn)) data['SITE NAME'] = sn;
        }
      }
      // Site name on same line as site ID
      if (!data['SITE NAME'] && siteId) {
        for (const line of lines) {
          if (line.toUpperCase().includes(siteId.split('_').pop())) {
            let sn = line.replace(siteRe,'').replace(/IHS[_\s]*(NRW|EST|CBT)[_\s:,\-]*[0-9]{0,4}[A-Za-z]{0,2}/ig,'').trim();
            sn = sn.replace(/\d{1,2}\/\d{1,2}\/\d{4},\s*\d{1,2}:\d{2}\s*-[^:]+:/,'').trim().replace(/^[:\-,\s]+/,'');
            // Strip vehicle plate patterns (3 letters + space + 4 digits)
            sn = sn.replace(/\b[A-Z]{2,3}\s*\d{4}\b/g,'').trim();
            // Strip trailing "refueled" suffix (Jonathan-style: "NRW_209A Chavuma Rpt refueled")
            sn = sn.replace(/\s*refueled\s*$/i,'').trim();
            if (sn && sn.length > 2) { data['SITE NAME'] = sn; break; }
          }
        }
      }

      // ── 4b. NRW emoji-block site name extraction ──
      // Lombe/Castro style: lines prefixed with ✅ where the site name appears
      // either BEFORE the site-ID line, or as the first non-ID ✅ line.
      // Pattern examples:
      //   ✅ Maheba refugee camp / ✅Nrw : 260A  → site name = "Maheba refugee camp"
      //   ✅Messenger A / ✅NRW 002m             → site name = "Messenger A"
      //   ✅ KAMBAZHIA / ✅NRW 017m              → site name = "KAMBAZHIA"
      if (!data['SITE NAME']) {
        const emojiLines = lines
          .map(l => l.replace(/^[✅👉🏾👉✍️\s]+/, '').trim())
          .filter(l => l.length > 1);
        // Find which line contains the site ID
        const siteIdLineIdx = emojiLines.findIndex(l =>
          /(?:IHS[_\s]*)?(?:NRW|CBT|EST|NTH)[\s_:,\-]*\d/i.test(l) ||
          /🆔\s*\d/.test(l)
        );
        if (siteIdLineIdx > 0) {
          // Site name is the line immediately before the site-ID line
          let candidate = emojiLines[siteIdLineIdx - 1];
          // Skip if it looks like a date or a WA header
          if (candidate && !/^\d{1,2}[\-\/]\d{1,2}[\-\/]\d{2,4}/.test(candidate) &&
              !/\d{1,2}\/\d{1,2}\/\d{4},\s*\d/.test(candidate)) {
            // Strip any remaining emoji/punctuation from start
            candidate = candidate.replace(/^[:\-,\s]+/, '').trim();
            if (candidate.length > 1) data['SITE NAME'] = candidate;
          }
        }
      }

      // ── 4c. Site name from TECH_MANAGER lookup (last resort) ──
      // If we still have no site name but have a site ID, use the TECH_MANAGER
      // to find the technician — the site name itself is not stored there, but
      // this guards against future extension. For now just ensure it's truly empty.
      // (Site names are not in TECH_MANAGER, so this is a no-op placeholder.)

      // ── 5. NUMERIC CONVERSION — mirrors convert_numeric(allow_faulty=True for RT) ──
      const convertNum = (val, allowFaulty=false) => {
        if (val===undefined||val===null) return null;
        let v = String(val).trim().replace(/,/g,'')
                     .replace(/\s*liters?\s*$/i,'')  // "100liters" → "100"
                     .replace(/[Ll]$/,'');            // "100L" → "100" 
        if (!v || /^(h|hr|hrs|hour|hours)$/i.test(v)) return null;
        if (/^(fault|faulty|fault controller|faulty controller)$/i.test(v))
          return allowFaulty ? 'FAULTY' : null;
        // "stolen", "..", "(stolen)", "..L" → treat as 0 (fuel was stolen/empty)
        if (/^[\.\s\(\)]*$/.test(v) || /stolen/i.test(v) || /^\.*$/.test(v)) return 0;
        // Strip parenthetical notes like "0L( Tank decanted)" → "0"
        v = v.replace(/\s*\(.*\)\s*$/, '').trim().replace(/[Ll]$/, '');
        // ── KEY RULE: if no digit present at all → FAULTY for RT fields ──
        // Catches "Faulty Controller", "N/A", "broken", "--", etc.
        if (allowFaulty && !/\d/.test(v)) return 'FAULTY';
        // Mixed alpha-numeric → strip letters
        if (/[a-zA-Z]/.test(v) && /\d/.test(v)) v = v.replace(/[^0-9.]/g,'');
        const n = parseFloat(v);
        if (isNaN(n)) return allowFaulty ? 'FAULTY' : null;
        return v.includes('.') ? n : Math.round(n);
      };

      for (const f of ['CURRENT DG RUN HOURS','PREVIOUS DG RUN HOURS']) {
        if (data[f]!==undefined) data[f] = convertNum(data[f], true);
      }
      for (const f of ['FUEL ADDED','FUEL FOUND','CPH']) {
        if (data[f]!==undefined) data[f] = convertNum(data[f], false);
      }

      // ── 6. SUPPLIER normalisation ──
      // Check kv field first, then full block text (Python fallback)
      const normaliseSupplier = (text) => {
        for (const src of ALLOWED_SOURCES) {
          if (new RegExp('\\b'+src+'\\b','i').test(text)) return src;
        }
        return '';
      };
      if (data['SUPPLIER']) data['SUPPLIER'] = normaliseSupplier(data['SUPPLIER']) || normaliseSupplier(cleanText);
      else                  data['SUPPLIER'] = normaliseSupplier(cleanText);

      // ── 7. TECHNICIAN — site-map lookup → kv field → WA sender name → N/A ──
      let tech = '';
      if (siteId) tech = TECH_MANAGER.getTechName(siteId) || '';
      if (!tech && data['NAME OF TECHNICIAN']) tech = String(data['NAME OF TECHNICIAN']).trim().toUpperCase();
      // Fallback: use the WhatsApp sender name when no other source resolves.
      // Strip role suffixes like "CCS", "~" etc. so we get a clean name.
      if (!tech && waSender) {
        // Only use if sender is not a bare phone number (+260...)
        if (!/^\+?\d[\d\s\-]+$/.test(waSender.trim())) {
          tech = waSender.replace(/\s*CCS\s*$/i, '').replace(/\s*IHS\s*$/i, '').trim().toUpperCase();
        }
      }
      data['NAME OF TECHNICIAN'] = tech || 'N/A';

      // ── 8. ULTRA-PERMISSIVE VALIDATION (Python: accept if ANY piece exists) ──
      const hasDate    = !!data['CURRENT VISIT DATE'];
      const hasSiteId  = !!data['SITE ID'];
      const hasSiteName= !!data['SITE NAME'];
      const hasRT      = data['CURRENT DG RUN HOURS']!=null && data['CURRENT DG RUN HOURS']!=='' && data['CURRENT DG RUN HOURS']!=='FAULTY';
      const hasFound   = data['FUEL FOUND']!=null && data['FUEL FOUND']!=='' && data['FUEL FOUND']!=='FAULTY';
      const hasAdded   = data['FUEL ADDED']!=null && data['FUEL ADDED']!=='' && data['FUEL ADDED']!=='FAULTY';

      if (!(hasDate || hasSiteId || hasSiteName || hasRT || hasFound || hasAdded)) return null;

      // Convert date to YYYY-MM-DD string for preview table / filter
      const entryDate = data['CURRENT VISIT DATE'] || '';

      // Fuel left = found + added
      // Also try to extract "Final level" / "Final dp" as a cross-check
      let finalLevelRaw = '';
      const finalM = cleanText.match(/(?:final(?:\s*fuel)?\s*(?:level|dp)|final\s*level)\s*[:\-]?\s*([\d]+)/i);
      if (finalM) finalLevelRaw = finalM[1];

      const fuelFoundN = Number(data['FUEL FOUND'])||0;
      const fuelAddedN = Number(data['FUEL ADDED'])||0;
      let   fuelLeft   = fuelFoundN + fuelAddedN;
      // If fuelLeft computed to 0 but we have a final level reading, use it
      const finalLevelN = Number(finalLevelRaw) || 0;
      if (fuelLeft === 0 && finalLevelN > 0) fuelLeft = finalLevelN;

      // CCS OVERRIDE: use explicit "Fuel quantity Left" if present (more accurate than computed)
      // This field is: remaining bowser fuel, not on-site — but it IS the site remaining figure
      // as stated in the template ("Final fuel level" is site, "Fuel quantity Left" is bowser remaining)
      // We keep the computed fuelLeft (Initial + Added = Final level on site) as the site fuel.
      // The bowser remaining (Fuel quantity Left / data['FUEL LEFT']) is stored separately.
      const bowserRemaining = data['FUEL LEFT'] ? convertNum(data['FUEL LEFT']) : null;
      const bowserQty       = data['QTY FUEL']  ? convertNum(data['QTY FUEL'])  : null;
      const bowserPlate     = data['BOWSER PLATE'] ? String(data['BOWSER PLATE']).trim().toUpperCase() : '';

      // CPH: handle "Stollen" as a flag rather than a number
      const cphRaw = data['CPH'];
      let cphVal = 0;
      if (cphRaw !== undefined && cphRaw !== null) {
        const cphStr = String(cphRaw).trim();
        if (/stolen/i.test(cphStr)) {
          data['_STOLEN'] = true;
          cphVal = 0;
        } else {
          cphVal = Number(convertNum(cphRaw, false)) || 0;
        }
      }

      // Mark faulty if truly missing both siteId and fuelAdded
      const issues = [];
      if (!siteId && !data['SITE NAME']) issues.push('no site ID or name');

      return {
        // Fields written to Excel (use Python column names as keys)
        'CURRENT VISIT DATE':    entryDate,
        'SITE ID':               data['SITE ID']               || '',
        'I.H.S SITE ID':         data['I.H.S SITE ID']         || '',
        'SITE NAME':             data['SITE NAME']             || '',
        'NAME OF TECHNICIAN':    data['NAME OF TECHNICIAN']    || 'N/A',
        'FUEL FOUND':            data['FUEL FOUND']            ?? '',
        'FUEL ADDED':            data['FUEL ADDED']            ?? '',
        'FUEL LEFT ON SITE':     fuelLeft > 0 ? fuelLeft : '',
        'SUPPLIER':              data['SUPPLIER']              || '',
        'CPH':                   data['CPH']                   ?? '',
        'CURRENT DG RUN HOURS':  data['CURRENT DG RUN HOURS']  ?? '',
        'PREVIOUS DG RUN HOURS': data['PREVIOUS DG RUN HOURS'] ?? '',
        // CCS-specific extra fields
        'QTY FUEL (BOWSER)':     bowserQty  !== null ? bowserQty  : '',
        'BOWSER REMAINING':      bowserRemaining !== null ? bowserRemaining : '',
        'BOWSER PLATE':          bowserPlate || '',
        'OIL LEVEL':             data['OIL LEVEL']  || '',
        'FAN BELT':              data['FAN BELT']   || '',
        'COOLANT':               data['COOLANT']    || '',
        'FUEL LEAKS':            data['FUEL LEAKS'] || '',
        // Convenience aliases used by preview table & daily-log import
        siteId:   data['SITE ID'] || '',
        techName: data['NAME OF TECHNICIAN'] || 'N/A',
        date:     entryDate,
        fuelFound: fuelFoundN,
        fuelAdded: fuelAddedN,
        fuelLeft:  fuelLeft > 0 ? fuelLeft : 0,
        supplier:  data['SUPPLIER'] || '',
        cph:       cphVal,
        currRt:    Number(data['CURRENT DG RUN HOURS'])||0,
        prevRt:    Number(data['PREVIOUS DG RUN HOURS'])||0,
        siteName:  data['SITE NAME'] || '',
        sender:    waSender || '',
        bowserPlate: bowserPlate || '',
        bowserQty:   bowserQty || 0,
        bowserRemaining: bowserRemaining || 0,
        stolen:    !!data['_STOLEN'],
        // Raw CCS check fields for Excel output
        _rawOilLevel:  data['OIL LEVEL']  || '',
        _rawFanBelt:   data['FAN BELT']   || '',
        _rawCoolant:   data['COOLANT']    || '',
        _rawFuelLeaks: data['FUEL LEAKS'] || '',
        _faulty:   issues.length > 0,
        _reason:   issues.join('; '),
        _selected: issues.length === 0,
        _resolved: issues.length === 0
      };
    }

    function autoRenderPreview(results) {
      const section = document.getElementById('autoPreviewSection');
      if (!section) return;
      if (results.length === 0) {
        section.style.display = 'none';
        showToast('No fuel entries found in that file.', 'warning');
        return;
      }

      const good = results.filter(r => !r._faulty);
      const bad  = results.filter(r => r._faulty);

      document.getElementById('autoSummaryCard').innerHTML = `
        <div class="flex gap-4 flex-wrap items-center">
          <span class="badge badge-success">✅ ${good.length} Valid entries</span>
          ${bad.length ? `<span class="badge badge-warning">⚠️ ${bad.length} Faulty (shown for review)</span>` : ''}
          <span class="badge badge-neutral">📋 ${results.length} Total blocks matched</span>
        </div>`;

      const tbody = document.getElementById('autoPreviewBody');
      tbody.innerHTML = results.map((r, i) => `
        <tr style="${r._faulty ? 'opacity:0.6;background:var(--status-danger-bg);' : ''}">
          <td><input type="checkbox" class="autoEntryCheck" data-idx="${i}" ${r._selected && !r._faulty ? 'checked' : ''} ${r._faulty ? 'disabled title="'+escHtml(r._reason)+'"' : ''}></td>
          <td class="text-sm">${r.date}</td>
          <td class="font-mono text-sm">${r.siteId||'<span style="color:var(--status-danger)">—</span>'}</td>
          <td><span class="badge" style="background:var(--neutral-100);color:var(--neutral-800);">${r.techName||'?'}</span></td>
          <td class="text-sm">${r.fuelFound||'—'}L</td>
          <td class="text-sm font-semibold">${r.fuelAdded||'—'}L</td>
          <td class="text-sm">${r.supplier||'—'}</td>
          <td class="text-sm">${r.stolen ? '<span class="badge badge-danger" title="Fuel stolen">🔴 Stolen</span>' : (r.cph||'—')}</td>
          <td class="text-sm font-mono" style="font-size:0.72rem;color:var(--neutral-600);">${r.bowserPlate||'—'}</td>
          <td>${r._faulty
            ? `<span class="badge badge-danger" title="${escHtml(r._reason)}">Faulty</span>`
            : '<span class="badge badge-success">OK</span>'}</td>
        </tr>`).join('');

      document.getElementById('autoPreviewCount').textContent =
        `${good.length} valid entries ready to import`;
      section.style.display = 'block';
      // Show "Write to Excel" button if an xlsx template is already loaded
      const writeBtn = document.getElementById('autoWriteXlsxBtn');
      if (writeBtn) writeBtn.style.display = window._autoXlsxFile ? '' : 'none';

      // ── Skipped entries log panel ──
      renderSkippedLog();
    }

    function renderSkippedLog() {
      // Remove existing panel
      const existing = document.getElementById('skippedLogPanel');
      if (existing) existing.remove();
      if (!_skippedLog || _skippedLog.length === 0) return;

      const section = document.getElementById('autoPreviewSection');
      if (!section) return;

      // Only show entries that have meaningful data (have a siteId or recognisable reason)
      const meaningful = _skippedLog.filter(s => s.siteId || (s.reason && s.reason !== 'No recognisable data in block'));
      if (meaningful.length === 0) return;

      // Cap display at 100 rows — full data still available via download
      const displayRows = meaningful.slice(0, 100);
      const rowsHtml = displayRows.map((s,i) =>
        `<tr><td>${i+1}</td><td class="font-mono" style="white-space:nowrap;">${s.date||'—'}</td>` +
        `<td class="font-mono" style="white-space:nowrap;">${escHtml(s.siteId||'—')}</td>` +
        `<td style="color:var(--status-danger);max-width:200px;">${escHtml(s.reason||'')}</td>` +
        `<td style="max-width:250px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;" title="${escHtml(s.block||'')}">${escHtml((s.block||'').substring(0,80))}</td></tr>`
      ).join('');

      const panel = document.createElement('div');
      panel.id = 'skippedLogPanel';
      panel.className = 'card mt-4';
      panel.style.cssText = 'border:1px solid var(--status-warning);background:var(--status-warning-bg);';
      panel.innerHTML =
        `<div class="flex items-center justify-between mb-3">` +
          `<h4 class="font-semibold" style="color:#92400e;">⚠️ ${meaningful.length} Faulty Entries` +
          `${meaningful.length > 100 ? ' <span style="font-weight:normal;font-size:0.8em;">(showing first 100)</span>' : ''}</h4>` +
          `<div class="flex gap-2">` +
            `<button class="btn btn-secondary btn-sm" onclick="downloadSkippedLog('xlsx')">⬇ Excel</button>` +
            `<button class="btn btn-secondary btn-sm" onclick="downloadSkippedLog('csv')">⬇ CSV</button>` +
          `</div>` +
        `</div>` +
        `<p class="text-sm mb-2" style="color:var(--neutral-600);">Entries with site/fuel data that could not be fully parsed. Download for full list.</p>` +
        `<div style="max-height:260px;overflow-y:auto;">` +
          `<table class="table" style="font-size:0.76rem;"><thead><tr>` +
          `<th>#</th><th>Date</th><th>Site ID</th><th>Reason</th><th>Preview</th>` +
          `</tr></thead><tbody>${rowsHtml}</tbody></table>` +
        `</div>`;
      section.appendChild(panel);
    }

    function downloadSkippedLog(fmt) {
      if (!_skippedLog || _skippedLog.length === 0) {
        showToast('No skipped entries to export', 'warning'); return;
      }
      const headers = ['#','Date','Site ID','Reason Skipped','Block Preview'];
      const rows = _skippedLog.map((s,i) => [
        i+1, s.date||'', s.siteId||'', s.reason||'', (s.block||'').replace(/[\r\n]+/g,' ').substring(0,200)
      ]);

      if (fmt === 'csv') {
        const csv = [headers, ...rows].map(r =>
          r.map(c => `"${String(c).replace(/"/g,'""')}"`).join(',')
        ).join('\n');
        const blob = new Blob([csv], {type:'text/csv'});
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = `NRW_Skipped_Entries_${new Date().toISOString().slice(0,10)}.csv`;
        a.click();
        showToast('CSV downloaded', 'ok');
        return;
      }

      // XLSX — use SheetJS if available, otherwise fall back to CSV
      if (typeof XLSX !== 'undefined') {
        const ws = XLSX.utils.aoa_to_sheet([headers, ...rows]);
        ws['!cols'] = [{wch:4},{wch:12},{wch:14},{wch:40},{wch:60}];
        const wb = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(wb, ws, 'Skipped Entries');
        XLSX.writeFile(wb, `NRW_Skipped_Entries_${new Date().toISOString().slice(0,10)}.xlsx`);
        showToast('Excel downloaded', 'ok');
      } else {
        // SheetJS not loaded — fall back to CSV with .xlsx extension note
        showToast('SheetJS not available — downloading as CSV instead', 'warning');
        downloadSkippedLog('csv');
      }
    }

    function autoSelectAll(val) {
      document.querySelectorAll('.autoEntryCheck:not([disabled])').forEach(cb => {
        const idx = parseInt(cb.dataset.idx);
        cb.checked = val;
        if (_autoParseResults[idx]) _autoParseResults[idx]._selected = val;
      });
    }

    function autoConfirmImport() {
      document.querySelectorAll('.autoEntryCheck').forEach(cb => {
        const idx = parseInt(cb.dataset.idx);
        if (_autoParseResults[idx]) _autoParseResults[idx]._selected = cb.checked;
      });

      const regionName = document.getElementById('autoRegionSelect').value;
      const toImport = _autoParseResults.filter(r => r._selected && !r._faulty);
      if (toImport.length === 0) return showToast('No valid entries selected', 'warning');

      // Get or create region in DB
      if (!DB.regions[regionName]) {
        DB.regions[regionName] = { technicians: [], technicianPlates: {}, orders: {}, dailyLog: {}, monthlyTarget: null, techMonthlyTargets: {}, unassignedComments: {} };
        showToast(`Created new region: ${regionName}`, 'info');
      }
      const region = DB.regions[regionName];

      let added = 0, skipped = 0;
      for (const entry of toImport) {
        const date = entry.date;
        if (!region.dailyLog[date]) region.dailyLog[date] = [];

        // Auto-add technician to region if not present
        const techUpper = entry.techName.toUpperCase();
        const techInRegion = region.technicians.find(t => t.toUpperCase() === techUpper);
        const techName = techInRegion || entry.techName;
        if (!techInRegion && entry.techName) {
          region.technicians.push(entry.techName);
        }

        // Try to find an open order allocated to this tech
        const openOrders = Object.values(region.orders)
          .filter(o => {
            const bal = o.totalLiters - o.suppliedTotal;
            return bal > 0 && o.allocations && o.allocations[techName];
          })
          .sort((a,b) => (a.createdDate||'').localeCompare(b.createdDate||''));

        if (openOrders.length > 0) {
          let remaining = entry.fuelAdded;
          for (const order of openOrders) {
            if (remaining <= 0) break;
            const bal = order.totalLiters - order.suppliedTotal;
            const toFill = Math.min(remaining, bal);
            region.dailyLog[date].push({
              orderNo: order.orderNo,
              technician: techName,
              supplied: toFill,
              fuelFound: entry.fuelFound,
              supplier: entry.supplier,
              cph: entry.cph,
              siteId: entry.siteId,
              autoImported: true
            });
            order.suppliedTotal += toFill;
            if (order.suppliedTotal >= order.totalLiters) order.status = 'CLOSED';
            remaining -= toFill;
            added++;
          }
          if (remaining > 0) {
            // Unallocated remainder
            region.dailyLog[date].push({
              orderNo: null, unallocated: true,
              technician: techName, supplied: remaining,
              fuelFound: entry.fuelFound, supplier: entry.supplier,
              cph: entry.cph, siteId: entry.siteId, autoImported: true
            });
            added++;
          }
        } else {
          // No orders — add as unallocated
          region.dailyLog[date].push({
            orderNo: null, unallocated: true,
            technician: techName, supplied: entry.fuelAdded,
            fuelFound: entry.fuelFound, supplier: entry.supplier,
            cph: entry.cph, siteId: entry.siteId, autoImported: true
          });
          added++;
        }
      }

      save();
      showToast(`✅ Imported ${added} entries into ${regionName} daily log`, 'success');
      autoLog(`✅ Imported ${added} entries into region "${regionName}"`, 'ok');
      document.getElementById('autoPreviewSection').style.display = 'none';
      _autoParseResults = [];

      // Show result summary card
      const resultSection = document.getElementById('autoResultSection');
      const resultCard = document.getElementById('autoResultCard');
      if (resultSection && resultCard) {
        const unallocatedCount = toImport.filter(e => !Object.values(DB.regions[regionName]?.orders||{}).some(o=>o.allocations&&o.allocations[e.techName])).length;
        resultCard.innerHTML = `
          <div class="flex items-center gap-4 flex-wrap">
            <div style="font-size:2rem;">✅</div>
            <div class="flex-1">
              <div class="font-bold text-lg">Import Complete</div>
              <div class="text-sm mt-1" style="color:var(--neutral-600);">
                ${added} daily log entries added to <strong>${regionName}</strong>
                ${skipped > 0 ? ` · ${skipped} skipped (no matching orders)` : ''}
              </div>
            </div>
            <div class="flex gap-3">
              <button class="btn btn-secondary btn-sm" onclick="setPage('daily',null)">
                <i class="fa-regular fa-calendar"></i> View Daily Log
              </button>
              <button class="btn btn-ghost btn-sm" onclick="document.getElementById('autoResultSection').style.display='none'">
                <i class="fa-regular fa-xmark"></i>
              </button>
            </div>
          </div>`;
        resultSection.style.display = 'block';
      }

      // Switch to the region
      if (DB.currentRegion !== regionName) {
        DB.currentRegion = regionName;
        save();
      }
    }

    // ============================================================
    // ===== WRITE PARSED ENTRIES INTO UPLOADED XLSX (Issue #1) ===
    // ============================================================
    // Mirrors FUEL_AUTO.py: UniversalDataUpdater.update_excel()
    // + UniversalDataPropagator.propagate_data()
    // Steps:
    //  1. Read uploaded .xlsx into SheetJS workbook
    //  2. Detect header row (must contain SITE ID + CURRENT VISIT DATE)
    //  3. Build a dup-check set from existing data rows
    //  4. Append new rows from selected parse results (skip true duplicates)
    //  5. Run in-workbook propagation (prev date, prev diesel, DG hours)
    //  6. Trigger download of modified workbook
    // ================================================================
    // autoWriteToUploadedXlsx
    // ================================================================
    // Strategy: treat the .xlsx as a ZIP archive (which it is).
    // We read the raw bytes with JSZip, parse ONLY the target worksheet
    // XML to find the header row and last data row, then inject new <row>
    // elements as raw XML strings.  Every other file inside the ZIP
    // (styles.xml, sharedStrings.xml, calcChain.xml, drawings, charts,
    // relationships, etc.) is left completely byte-for-byte identical.
    // This guarantees 100% formula / style / layout preservation because
    // we never re-serialize anything we didn't write ourselves.
    // ================================================================
    async function autoWriteToUploadedXlsx() {
      if (!window._autoXlsxFile) return showToast('Please upload an .xlsx file first', 'warning');

      document.querySelectorAll('.autoEntryCheck').forEach(cb => {
        const idx = parseInt(cb.dataset.idx);
        if (_autoParseResults[idx]) _autoParseResults[idx]._selected = cb.checked;
      });

      const toWrite = _autoParseResults.filter(r => r._selected && !r._faulty);
      if (!toWrite.length) return showToast('No valid entries selected to write', 'warning');

      const btn = document.getElementById('autoWriteXlsxBtn');
      if (btn) { btn.setAttribute('disabled',''); btn.innerHTML = '<i class="fa-regular fa-spinner fa-spin"></i> Writing…'; }

      try {
        // ── 0. Read the xlsx as raw ArrayBuffer ──────────────────────
        const arrayBuf = await window._autoXlsxFile.arrayBuffer();
        const zip      = await JSZip.loadAsync(arrayBuf);

        // ── 1. Find the target worksheet path ────────────────────────
        // workbook.xml lists all sheets; we want "fuel capture" or first
        const wbXml   = await zip.file('xl/workbook.xml').async('string');
        const sheetsM = [...wbXml.matchAll(/<sheet\s[^>]*name="([^"]*)"[^>]*r:id="([^"]*)"[^>]*/gi)];
        const relXml  = await zip.file('xl/_rels/workbook.xml.rels').async('string');

        let targetSheetName = '', targetRId = '';
        // prefer "fuel capture" sheet, else first
        for (const m of sheetsM) {
          const name = m[1].toLowerCase().replace(/\s/g,'');
          if (name === 'fuelcapture' || name.includes('fuelcapture') || name.includes('fuel')) {
            targetSheetName = m[1]; targetRId = m[2]; break;
          }
        }
        if (!targetRId) { targetSheetName = sheetsM[0][1]; targetRId = sheetsM[0][2]; }

        // resolve rId → actual path
        const relMatch = relXml.match(new RegExp(`Id="${targetRId}"[^>]*Target="([^"]+)"`));
        const wsRelPath = relMatch ? relMatch[1] : null;
        if (!wsRelPath) throw new Error(`Cannot resolve sheet path for rId ${targetRId}`);
        const wsPath = wsRelPath.startsWith('/') ? wsRelPath.slice(1) : `xl/${wsRelPath}`;

        autoLog(`📂 Target sheet: "${targetSheetName}" → ${wsPath}`);

        // ── 2. Load sharedStrings — we will append new string entries ──
        const sstFile = zip.file('xl/sharedStrings.xml');
        let   sstXml  = sstFile ? await sstFile.async('string') : null;
        let   sstCreatedFresh = false;

        // If there is no sharedStrings.xml at all, create an empty one.
        // We also need to register it in the workbook relationships file.
        if (!sstXml) {
          sstXml = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="0" uniqueCount="0"></sst>`;
          sstCreatedFresh = true;
          autoLog('📝 sharedStrings.xml not found — creating fresh one');
        }

        // Parse existing SST entry count from the ROOT <sst> element only.
        // Use a targeted regex that matches the opening tag to avoid hitting
        // count= attributes that may appear inside individual <si> elements.
        let sstCount = 0, sstUnique = 0;
        {
          const rootTagM = sstXml.match(/<sst\s[^>]*>/);
          if (rootTagM) {
            const cntM = rootTagM[0].match(/\bcount="(\d+)"/);
            const unqM = rootTagM[0].match(/\buniqueCount="(\d+)"/);
            if (cntM) sstCount  = parseInt(cntM[1]);
            if (unqM) sstUnique = parseInt(unqM[1]);
          }
        }

        // Build bidirectional string ↔ index maps.
        // Handles plain <si><t>text</t></si> AND rich-text <si> blocks with <rPr> runs.
        const sstIndex = {};   // string → 0-based index
        const sstByIdx = {};   // 0-based index → string
        {
          let idx = 0;
          for (const siM of sstXml.matchAll(/<si>([\s\S]*?)<\/si>/g)) {
            const texts = [...siM[1].matchAll(/<t(?:[^>]*)>([\s\S]*?)<\/t>/g)].map(m => m[1]);
            const s = texts.join('');
            sstIndex[s] = idx;
            sstByIdx[idx] = s;
            idx++;
          }
        }

        // getSstIdx: return existing index or append a new <si> entry.
        // New indices start from sstUnique (the count of pre-existing unique strings).
        const newSstEntries = [];
        const getSstIdx = (str) => {
          const s = String(str);
          if (sstIndex[s] !== undefined) return sstIndex[s];
          const newIdx = sstUnique + newSstEntries.length;
          sstIndex[s]  = newIdx;
          sstByIdx[newIdx] = s;
          const esc = s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
          newSstEntries.push(`<si><t xml:space="preserve">${esc}</t></si>`);
          return newIdx;
        };

        // ── 3. Read and parse the worksheet XML ──────────────────────
        let wsXml = await zip.file(wsPath).async('string');

        // Helper: col letter(s) → 0-based index  (A=0, B=1, … Z=25, AA=26 …)
        const colLetterToIdx = s => {
          s = s.toUpperCase();
          let n = 0;
          for (const ch of s) n = n * 26 + (ch.charCodeAt(0) - 64);
          return n - 1;
        };
        // Helper: 0-based col index → column letter(s)
        const colIdxToLetter = n => {
          let s = '';
          n++;
          while (n > 0) { n--; s = String.fromCharCode(65 + (n % 26)) + s; n = Math.floor(n / 26); }
          return s;
        };
        // Helper: cell address → {r:0-based, c:0-based}
        const decodeCell = addr => {
          const m = addr.match(/^([A-Z]+)(\d+)$/i);
          if (!m) return null;
          return { c: colLetterToIdx(m[1]), r: parseInt(m[2]) - 1 };
        };

        // ── 4. Find header row by scanning <row> elements ─────────────
        // We look for the row that contains cells with values matching
        // "SITE ID" and "DATE" — same logic as Python get_sheet_info().
        // We parse row XML with regex (no DOM available in this context).

        // Extract all <row ...>...</row> blocks
        const rowBlocks = [...wsXml.matchAll(/<row\s[^>]*r="(\d+)"[^>]*>([\s\S]*?)<\/row>/gi)];

        // Read a cell's value (handles SST strings, inline strings, numbers, dates)
        // Returns the value as a human-readable string.
        // Date cells (t omitted, value is an Excel serial number) are converted
        // to DD/MM/YYYY so dup-check and last-date detection work correctly.
        const cellVal = (cellXml) => {
          const tM  = cellXml.match(/\st="([^"]+)"/);
          const vM  = cellXml.match(/<v>([\s\S]*?)<\/v>/i);
          const iM  = cellXml.match(/<is><t>([\s\S]*?)<\/t><\/is>/i);
          if (!vM && !iM) return '';
          const raw = iM ? iM[1] : vM[1];
          const t   = tM ? tM[1] : '';

          if (t === 's') {
            // Shared-string reference → direct O(1) reverse lookup
            return sstByIdx[parseInt(raw)] ?? '';
          }
          if (t === 'inlineStr' || t === 'str') return raw; // inline / formula-result string

          // No type attribute → could be a number OR an Excel date serial.
          // Detect date by checking if the cell has a date number format (s attribute
          // maps to a style that contains numFmt like "DD/MM/YYYY").
          // Simpler heuristic: if the cell has an s="" attribute we check if the
          // raw numeric value looks like a plausible date serial (> 40000 = after ~2009).
          const numVal = parseFloat(raw);
          if (!isNaN(numVal) && numVal > 40000 && numVal < 60000) {
            // Likely an Excel date serial — convert to DD/MM/YYYY
            const epoch = new Date(Date.UTC(1899, 11, 30));
            const d = new Date(epoch.getTime() + numVal * 86400000);
            if (!isNaN(d.getTime())) {
              const dd = String(d.getUTCDate()).padStart(2,'0');
              const mm = String(d.getUTCMonth()+1).padStart(2,'0');
              const yyyy = d.getUTCFullYear();
              return `${dd}/${mm}/${yyyy}`;
            }
          }
          return raw;  // plain number or formula cached value
        };

        // getCellsInRow: parse all <c> elements from a row block
        const getCellsInRow = (rowContent) => {
          const cells = {};
          for (const m of rowContent.matchAll(/<c\s[^>]*r="([A-Z]+\d+)"[^>]*>([\s\S]*?)<\/c>/gi)) {
            const pos = decodeCell(m[1]);
            if (pos) cells[pos.c] = { addr: m[1], xml: m[0], val: cellVal(m[0]) };
          }
          return cells;
        };

        let headerRowNum = -1;  // 1-based Excel row number
        let headerCells  = {};  // col index → value string
        let colOf        = {};  // alias → col index (0-based)

        for (const [, rowNum, rowContent] of rowBlocks) {
          const rn = parseInt(rowNum);
          const cells = getCellsInRow(rowContent);
          const vals = Object.entries(cells).map(([,c]) => c.val.toUpperCase());
          if (vals.some(v => v === 'SITE ID' || v.includes('SITE ID')) &&
              vals.some(v => v.includes('DATE'))) {
            headerRowNum = rn;
            for (const [ci, cell] of Object.entries(cells)) {
              const norm = cell.val.toUpperCase().trim();
              headerCells[ci] = norm;
              colOf[norm] = parseInt(ci);
              if (norm === 'CURRENT VISIT DATE' || norm === 'DATE')                colOf['__DATE__']       = parseInt(ci);
              if (norm === 'SITE ID')                                               colOf['__SITEID__']     = parseInt(ci);
              if (norm === 'SITE NAME')                                             colOf['__SITENAME__']   = parseInt(ci);
              if (norm === 'FUEL FOUND')                                            colOf['__FUELFOUND__']  = parseInt(ci);
              if (norm === 'FUEL ADDED')                                            colOf['__FUELADDED__']  = parseInt(ci);
              if (norm === 'FUEL LEFT ON SITE' || norm === 'FUEL LEFT')            colOf['__FUELLEFT__']   = parseInt(ci);
              if (['NAME OF TECHNICIAN','TECHNICIAN NAME','TECHNICIAN'].includes(norm)) colOf['__TECH__'] = parseInt(ci);
              if (norm === 'SUPPLIER' || norm === 'SOURCE')                         colOf['__SUPPLIER__']   = parseInt(ci);
              if (norm === 'CPH')                                                   colOf['__CPH__']        = parseInt(ci);
              if (norm === 'CURRENT DG RUN HOURS' || norm === 'CURRENT RT')        colOf['__CURRRT__']     = parseInt(ci);
              if (norm === 'PREVIOUS DG RUN HOURS' || norm === 'PREVIOUS RT')      colOf['__PREVRT__']     = parseInt(ci);
              if (['I.H.S SITE ID','IHS SITE ID','I.H.S. SITE ID'].includes(norm)) colOf['__IHSID__']     = parseInt(ci);
              if (norm === 'LAST VISIT DATE' || norm === 'PREVIOUS VISIT DATE')     colOf['__LASTDATE__']   = parseInt(ci);
              if (norm === 'PREVIOUS DIESEL LEVEL')                                 colOf['__PREVDIESEL__'] = parseInt(ci);
            }
            break;
          }
        }

        if (headerRowNum === -1) throw new Error('No header row found (need SITE ID + DATE columns)');
        autoLog(`📋 Header at row ${headerRowNum}, ${Object.keys(headerCells).length} columns`);

        // Alias fallbacks (mirrors Python ensure_column_exists)
        const aliasFallbacks = {
          '__TECH__':       ['TECHNICIAN NAME','TECHNICIAN','TECH NAME'],
          '__IHSID__':      ['IHS SITE ID','I.H.S. SITE ID','IHS_SITE_ID'],
          '__FUELLEFT__':   ['FUEL LEFT'],
          '__LASTDATE__':   ['LAST VISIT DATE', 'PREVIOUS VISIT DATE'],
          '__PREVDIESEL__': ['PREVIOUS DIESEL LEVEL']
        };
        for (const [alias, alts] of Object.entries(aliasFallbacks)) {
          if (colOf[alias] !== undefined) continue;
          for (const alt of alts) {
            if (colOf[alt.toUpperCase()] !== undefined) {
              colOf[alias] = colOf[alt.toUpperCase()]; break;
            }
          }
        }

        // ── 5. Scan existing data rows for dup-check + last date ─────
        const existingKeys = new Set();
        let lastDate       = null;
        let lastDataRowNum = headerRowNum;  // 1-based

        for (const [, rowNum, rowContent] of rowBlocks) {
          const rn = parseInt(rowNum);
          if (rn <= headerRowNum) continue;
          const cells = getCellsInRow(rowContent);
          const get   = alias => (cells[colOf[alias]]?.val || '').trim();

          const dv = get('__DATE__');
          const sv = get('__SITEID__').toUpperCase();
          const rv = get('__CURRRT__');
          const fv = get('__FUELFOUND__');
          const av = get('__FUELADDED__');
          if (dv && sv && rv && fv && av) existingKeys.add(`${dv}|${sv}|${rv}|${fv}|${av}`);

          // Track last date (DD/MM/YYYY)
          if (dv) {
            const m = dv.match(/(\d{1,2})\/(\d{1,2})\/(\d{4})/);
            if (m) {
              const d = new Date(`${m[3]}-${m[2].padStart(2,'0')}-${m[1].padStart(2,'0')}`);
              if (!lastDate || d > lastDate) lastDate = d;
            }
          }
          // Track last data row: only advance when the row has a real value
          // in the SITE ID column OR the DATE column.
          // Using anyVal (any cell non-empty) was wrong — Excel places
          // formatting-only rows, print-area anchors, and named-range markers
          // far below the actual data, which pushed lastDataRowNum way down
          // and caused new entries to be written hundreds of rows too low.
          const hasSiteVal = sv !== '';
          const hasDateVal = dv !== '';
          if (hasSiteVal || hasDateVal) lastDataRowNum = rn;
        }

        if (lastDate) autoLog(`📅 Last date in Excel: ${lastDate.toLocaleDateString('en-GB')}`);
        autoLog(`📍 Last data row detected: row ${lastDataRowNum} — new entries will start at row ${lastDataRowNum + 1}`);

        // ── 6. Detect row style from last data row ───────────────────
        // We copy the s="" (style index) from existing data cells when
        // building new rows so the new rows inherit the same formatting.
        let rowStyleMap = {};  // col index → s attribute value (string)
        let lastRowXml  = '';
        for (const [, rowNum, rowContent] of rowBlocks) {
          if (parseInt(rowNum) === lastDataRowNum) { lastRowXml = rowContent; break; }
        }
        if (lastRowXml) {
          for (const m of lastRowXml.matchAll(/<c\s([^>]*)>/gi)) {
            const attrStr = m[1];
            const rM = attrStr.match(/r="([A-Z]+\d+)"/i);
            const sM = attrStr.match(/\bs="(\d+)"/);
            if (rM && sM) {
              const pos = decodeCell(rM[1]);
              if (pos) rowStyleMap[pos.c] = sM[1];
            }
          }
        }

        // ── 7. Build new <row> XML blocks ────────────────────────────
        // For each entry we build a complete <row r="N"> element.
        // String values go into the SST; numbers written as <v>.
        // Date values written as numeric serial (Excel date serial).
        // We NEVER touch formula cells from existing rows.

        // Excel date serial: days since 1899-12-30
        const dateToSerial = d => {
          const epoch = new Date(Date.UTC(1899,11,30));
          return Math.round((d - epoch) / 86400000);
        };

        // find the row attrs from last data row's opening tag to copy ht/spans etc
        const lastRowTagM = wsXml.match(new RegExp(`<row\\s[^>]*r="${lastDataRowNum}"[^>]*>`));
        const lastRowAttrs = lastRowTagM
          ? lastRowTagM[0].replace(/ r="\d+"/, '').replace('<row','').replace('>','').trim()
          : '';

        let added = 0, dupeSkipped = 0, dateSkipped = 0;
        const newRowXmls = [];

        // We also need to track propagation data as we build rows
        // so we can fill LAST VISIT DATE / PREVIOUS DIESEL for new rows immediately
        // (existing rows are propagated in step 8 separately)
        // Build a per-site list of {date, fuelLeft} from existing data
        const siteHistory = {}; // siteId → [{dateStr, fuelLeft}] sorted by date
        for (const [, rowNum, rowContent] of rowBlocks) {
          if (parseInt(rowNum) <= headerRowNum) continue;
          const cells = getCellsInRow(rowContent);
          const sid = (cells[colOf['__SITEID__']]?.val||'').toUpperCase();
          const dv  = cells[colOf['__DATE__']]?.val||'';
          const fl  = parseFloat(cells[colOf['__FUELLEFT__']]?.val||'') || 0;
          if (sid && dv) {
            if (!siteHistory[sid]) siteHistory[sid] = [];
            siteHistory[sid].push({dateStr: dv, fuelLeft: fl});
          }
        }

        for (const entry of toWrite) {
          // Normalise date
          let dateStr = entry['CURRENT VISIT DATE'] || entry.date || '';
          if (/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
            const [yr,mm,dd] = dateStr.split('-');
            dateStr = `${dd}/${mm}/${yr}`;
          }
          const siteIdUpper = (entry['SITE ID'] || entry.siteId || '').toUpperCase();

          // Skip entries strictly older than last date in Excel
          if (lastDate && dateStr) {
            const m = dateStr.match(/(\d{1,2})\/(\d{1,2})\/(\d{4})/);
            if (m) {
              const ed = new Date(`${m[3]}-${m[2].padStart(2,'0')}-${m[1].padStart(2,'0')}`);
              if (ed < lastDate) { dateSkipped++; continue; }
            }
          }

          // 5-field dup check
          const cRt  = String(entry['CURRENT DG RUN HOURS']  ?? entry.currRt   ?? '');
          const cFnd = String(entry['FUEL FOUND']             ?? entry.fuelFound ?? '');
          const cAdd = String(entry['FUEL ADDED']             ?? entry.fuelAdded ?? '');
          const dupKey = `${dateStr}|${siteIdUpper}|${cRt}|${cFnd}|${cAdd}`;
          if (existingKeys.has(dupKey)) { dupeSkipped++; continue; } // dup — silent skip

          // Compute derived values
          const fuelFound  = Number(entry['FUEL FOUND'] ?? entry.fuelFound ?? 0) || 0;
          const fuelAdded  = Number(entry['FUEL ADDED'] ?? entry.fuelAdded ?? 0) || 0;
          const fuelLeft   = fuelFound + fuelAdded;
          // FAULTY runtime: preserve the string 'FAULTY' exactly; otherwise numeric
          const rawCurrRt  = entry['CURRENT DG RUN HOURS'] ?? entry.currRt ?? '';
          const currRtIsFaulty = String(rawCurrRt).toUpperCase() === 'FAULTY';
          const currRt     = currRtIsFaulty ? 'FAULTY' : (Number(cRt) || 0);

          const rawPrevRt  = entry['PREVIOUS DG RUN HOURS'] ?? entry.prevRt ?? '';
          const prevRtIsFaulty = String(rawPrevRt).toUpperCase() === 'FAULTY';
          const prevRt     = prevRtIsFaulty ? 'FAULTY' : (Number(rawPrevRt) || 0);
          const cph        = Number(entry['CPH'] ?? entry.cph ?? 0) || 0;

          // Propagation values for new row
          // Clone the array before sorting so we never mutate the shared siteHistory
          // reference — otherwise multi-row imports for the same site in one batch
          // would see a corrupted prevVisit on the second and later entries.
          const toISODate = s => {
            // Handles both DD/MM/YYYY (from cellVal) and YYYY-MM-DD (from parseBlock)
            const p1 = s.match(/(\d{1,2})\/(\d{1,2})\/(\d{4})/);
            if (p1) return `${p1[3]}-${p1[2].padStart(2,'0')}-${p1[1].padStart(2,'0')}`;
            const p2 = s.match(/^(\d{4})-(\d{2})-(\d{2})$/);
            if (p2) return s; // already ISO
            return s;
          };
          const hist = (siteHistory[siteIdUpper] || []).slice(); // ← cloned copy
          hist.sort((a,b) => toISODate(a.dateStr).localeCompare(toISODate(b.dateStr)));
          const prevVisit  = hist.length ? hist[hist.length-1] : null;
          // Only fall back to own dateStr when there is genuinely no prior visit at all
          const prevDate   = prevVisit ? prevVisit.dateStr : dateStr;
          const prevDiesel = prevVisit ? prevVisit.fuelLeft : fuelLeft;

          // Row number for this new row: one after the current last data row.
          // lastDataRowNum is updated at the end of this iteration so this
          // is always exactly the next consecutive row — no gaps.
          const newRowNum = lastDataRowNum + 1;

          // Build cell map: colIndex → {type, value}
          // type: 's'=string(SST), 'n'=number, 'd'=date-as-serial
          const cellData = {};
          const setCell = (alias, type, val) => {
            if (colOf[alias] === undefined) return;
            // Only skip truly empty values — never skip 0 (valid fuel/RT reading)
            // and never skip by SST index (index 0 is a valid string)
            if (val === '' || val === null || val === undefined) return;
            cellData[colOf[alias]] = {type, val};
          };

          // Date cell — write as Excel date serial number with date format
          if (colOf['__DATE__'] !== undefined && dateStr) {
            const m = dateStr.match(/(\d{1,2})\/(\d{1,2})\/(\d{4})/);
            if (m) {
              const serial = dateToSerial(new Date(Date.UTC(parseInt(m[3]),parseInt(m[2])-1,parseInt(m[1]))));
              cellData[colOf['__DATE__']] = {type:'date', val: serial, s: rowStyleMap[colOf['__DATE__']]};
            }
          }
          // Log what we're about to write so missing values are visible in the log
          const siteName = entry['SITE NAME']  || entry.siteName  || '';
          const techName = entry['NAME OF TECHNICIAN'] || entry.techName || 'N/A';
          // Per-row detail suppressed to keep UI responsive (visible in final summary)
          setCell('__SITEID__',   's', siteIdUpper);
          setCell('__SITENAME__', 's', siteName);
          setCell('__TECH__',     's', techName);
          // Write numeric fields — only skip if genuinely absent (null/undefined/'')
          // A value of 0 is valid (e.g. empty tank, zero runtime) and must be written.
          if (fuelFound !== '' && fuelFound !== null && fuelFound !== undefined) setCell('__FUELFOUND__', 'n', fuelFound);
          if (fuelAdded !== '' && fuelAdded !== null && fuelAdded !== undefined) setCell('__FUELADDED__', 'n', fuelAdded);
          if (fuelLeft  > 0) setCell('__FUELLEFT__', 'n', fuelLeft);
          setCell('__SUPPLIER__', 's', entry['SUPPLIER'] || entry.supplier || '');
          if (cph    > 0) setCell('__CPH__',    'n', cph);
          // Write runtime — FAULTY written as string, valid number > 0 as numeric
          if (currRtIsFaulty) setCell('__CURRRT__', 's', 'FAULTY');
          else if (currRt > 0) setCell('__CURRRT__', 'n', currRt);
          if (prevRtIsFaulty) setCell('__PREVRT__', 's', 'FAULTY');
          else if (prevRt > 0) setCell('__PREVRT__', 'n', prevRt);
          setCell('__IHSID__', 's', siteIdUpper);

          // Propagation fields for new row
          if (colOf['__LASTDATE__'] !== undefined && prevDate) {
            // Handle both DD/MM/YYYY (from existing Excel rows via cellVal)
            // and YYYY-MM-DD (from parseBlock output stored in siteHistory within same batch)
            let ldSerial = null;
            const m1 = prevDate.match(/(\d{1,2})\/(\d{1,2})\/(\d{4})/);
            if (m1) ldSerial = dateToSerial(new Date(Date.UTC(parseInt(m1[3]),parseInt(m1[2])-1,parseInt(m1[1]))));
            if (!ldSerial) {
              const m2 = prevDate.match(/^(\d{4})-(\d{2})-(\d{2})$/);
              if (m2) ldSerial = dateToSerial(new Date(Date.UTC(parseInt(m2[1]),parseInt(m2[2])-1,parseInt(m2[3]))));
            }
            if (ldSerial !== null) {
              cellData[colOf['__LASTDATE__']] = {type:'date', val: ldSerial, s: rowStyleMap[colOf['__LASTDATE__']]};
            }
          }
          if (colOf['__PREVDIESEL__'] !== undefined && prevDiesel > 0) {
            cellData[colOf['__PREVDIESEL__']] = {type:'n', val: prevDiesel};
          }

          // Render cell XML
          const renderCell = (colIdx, data) => {
            const addr = colIdxToLetter(colIdx) + newRowNum;
            const sAttr = data.s ? ` s="${data.s}"` : (rowStyleMap[colIdx] ? ` s="${rowStyleMap[colIdx]}"` : '');
            if (data.type === 'n') {
              return `<c r="${addr}"${sAttr}><v>${data.val}</v></c>`;
            } else if (data.type === 'date') {
              return `<c r="${addr}"${sAttr}><v>${data.val}</v></c>`;
            } else {
              // string → SST
              const si = getSstIdx(String(data.val));
              return `<c r="${addr}" t="s"${sAttr}><v>${si}</v></c>`;
            }
          };

          // Sort cells by column order
          const sortedCols = Object.keys(cellData).map(Number).sort((a,b)=>a-b);
          const cellsXml = sortedCols.map(ci => renderCell(ci, cellData[ci])).join('');

          const rowAttrs = lastRowAttrs ? ` ${lastRowAttrs}` : '';
          newRowXmls.push(`<row r="${newRowNum}"${rowAttrs}>${cellsXml}</row>`);

          // Update history for subsequent new rows
          if (!siteHistory[siteIdUpper]) siteHistory[siteIdUpper] = [];
          siteHistory[siteIdUpper].push({dateStr, fuelLeft});

          existingKeys.add(dupKey);
          lastDataRowNum = newRowNum;
          added++;
        }

        autoLog(`✅ ${added} row${added!==1?'s':''} built`
          + (dupeSkipped?` · ${dupeSkipped} dup${dupeSkipped!==1?'s':''} skipped`:'')
          + (dateSkipped?` · ${dateSkipped} older-date skipped`:''), 'ok');

        // ── 8. INJECT new rows into worksheet XML ────────────────────
        // Find </sheetData> and insert before it
        if (newRowXmls.length > 0) {
          const injection = newRowXmls.join('');
          if (wsXml.includes('</sheetData>')) {
            wsXml = wsXml.replace('</sheetData>', injection + '</sheetData>');
          } else if (wsXml.includes('<sheetData/>')) {
            wsXml = wsXml.replace('<sheetData/>', `<sheetData>${injection}</sheetData>`);
          } else {
            throw new Error('Cannot locate <sheetData> in worksheet XML');
          }
        }

        // ── 9. PROPAGATION — mirrors Python UniversalDataPropagator exactly ──
        // After injecting new rows, re-parse sheetData, group by SITE ID,
        // sort each site's rows by date, then fill blank cells for:
        //   LAST VISIT DATE       ← previous row's CURRENT VISIT DATE
        //   PREVIOUS DIESEL LEVEL ← previous row's FUEL LEFT ON SITE
        //   PREVIOUS DG RUN HOURS ← previous row's CURRENT DG RUN HOURS
        //
        // Uses indexOf-based row location (not regex) to avoid lazy-match
        // truncation on rows that contain complex formula/string content.
        let propDates = 0, propDiesel = 0, propPrevRt = 0;
        {
          // Split wsXml on <row openings to get individual row chunks
          const rowChunks = wsXml.split(/(?=<row\s)/i).filter(s => s.trimStart().startsWith('<row'));

          const parsedRows = [];
          for (const chunk of rowChunks) {
            const rnM = chunk.match(/^<row\s[^>]*r="(\d+)"/i);
            if (!rnM) continue;
            const rn = parseInt(rnM[1]);
            if (rn <= headerRowNum) continue;
            const innerStart = chunk.indexOf('>') + 1;
            const innerEnd   = chunk.lastIndexOf('</row>');
            if (innerEnd <= innerStart) continue;
            const cells = getCellsInRow(chunk.substring(innerStart, innerEnd));
            parsedRows.push({rn, cells});
          }

          // Group by SITE ID
          const siteRowMap = {};
          for (const row of parsedRows) {
            const sid = (row.cells[colOf['__SITEID__']]?.val || '').trim().toUpperCase();
            if (!sid) continue;
            if (!siteRowMap[sid]) siteRowMap[sid] = [];
            siteRowMap[sid].push(row);
          }

          autoLog(`🔄 Propagation: ${Object.keys(siteRowMap).length} unique sites found`);

          // DD/MM/YYYY or YYYY-MM-DD string → Excel date serial
          const dateStrToSerial = (s) => {
            // Try DD/MM/YYYY first (output of cellVal for date serials)
            const m1 = s.match(/(\d{1,2})\/(\d{1,2})\/(\d{4})/);
            if (m1) return dateToSerial(new Date(Date.UTC(parseInt(m1[3]), parseInt(m1[2])-1, parseInt(m1[1]))));
            // Try YYYY-MM-DD (output of parseBlock / stored as text)
            const m2 = s.match(/^(\d{4})-(\d{2})-(\d{2})$/);
            if (m2) return dateToSerial(new Date(Date.UTC(parseInt(m2[1]), parseInt(m2[2])-1, parseInt(m2[3]))));
            return null;
          };

          // Collect patches: rowNum → [{addr, colIdx, cellXml}]
          const patches = {};
          const addPatch = (rn, colIdx, cellXml) => {
            if (colIdx === undefined) return;
            const addr = colIdxToLetter(colIdx) + rn;
            if (!patches[rn]) patches[rn] = [];
            if (!patches[rn].some(p => p.addr === addr)) {
              patches[rn].push({addr, colIdx, cellXml});
            }
          };
          const sOf = (ci) => rowStyleMap[ci] ? ` s="${rowStyleMap[ci]}"` : '';

          for (const rows of Object.values(siteRowMap)) {
            // Sort by date ascending — handles both DD/MM/YYYY and YYYY-MM-DD
            const toISO = s => {
              const p1 = s.match(/(\d{1,2})\/(\d{1,2})\/(\d{4})/);
              if (p1) return `${p1[3]}-${p1[2].padStart(2,'0')}-${p1[1].padStart(2,'0')}`;
              const p2 = s.match(/^(\d{4})-(\d{2})-(\d{2})$/);
              if (p2) return s; // already ISO
              return s;
            };
            rows.sort((a, b) => toISO(a.cells[colOf['__DATE__']]?.val||'')
                                .localeCompare(toISO(b.cells[colOf['__DATE__']]?.val||'')));

            let prevDate    = '';
            let prevFuelLeft = 0;
            let prevCurrRt  = 0;

            for (const {rn, cells} of rows) {
              const g = alias => (cells[colOf[alias]]?.val || '').trim();
              const currDate     = g('__DATE__');
              const currFuelLeft = parseFloat(g('__FUELLEFT__'))  || 0;
              const currRt       = parseFloat(g('__CURRRT__'))    || 0;

              // LAST VISIT DATE
              if (colOf['__LASTDATE__'] !== undefined && !g('__LASTDATE__')) {
                const fill = prevDate || currDate;
                if (fill) {
                  const serial = dateStrToSerial(fill);
                  if (serial !== null) {
                    const addr = colIdxToLetter(colOf['__LASTDATE__']) + rn;
                    addPatch(rn, colOf['__LASTDATE__'],
                      `<c r="${addr}"${sOf(colOf['__LASTDATE__'])}><v>${serial}</v></c>`);
                    propDates++;
                  }
                }
              }

              // PREVIOUS DIESEL LEVEL
              if (colOf['__PREVDIESEL__'] !== undefined && !g('__PREVDIESEL__')) {
                const fill = prevFuelLeft > 0 ? prevFuelLeft : currFuelLeft;
                if (fill > 0) {
                  const addr = colIdxToLetter(colOf['__PREVDIESEL__']) + rn;
                  addPatch(rn, colOf['__PREVDIESEL__'],
                    `<c r="${addr}"${sOf(colOf['__PREVDIESEL__'])}><v>${fill}</v></c>`);
                  propDiesel++;
                }
              }

              // PREVIOUS DG RUN HOURS
              if (colOf['__PREVRT__'] !== undefined && !g('__PREVRT__') && prevCurrRt > 0) {
                const addr = colIdxToLetter(colOf['__PREVRT__']) + rn;
                addPatch(rn, colOf['__PREVRT__'],
                  `<c r="${addr}"${sOf(colOf['__PREVRT__'])}><v>${prevCurrRt}</v></c>`);
                propPrevRt++;
              }

              // Advance trackers
              if (currDate)        prevDate     = currDate;
              if (currFuelLeft > 0) prevFuelLeft = currFuelLeft;
              if (currRt > 0)       prevCurrRt   = currRt;
            }
          }

          // Apply patches using indexOf — robust against complex row content
          for (const [rnStr, rowPatches] of Object.entries(patches)) {
            const rn = parseInt(rnStr);

            // Locate the row in wsXml by its opening tag
            const openTagSearch = `<row r="${rn}"`;
            let rowStart = wsXml.indexOf(openTagSearch);
            // Also handle rows where r= is not the first attribute
            if (rowStart === -1) {
              const alt = wsXml.indexOf(`r="${rn}" `);
              if (alt !== -1) {
                // walk back to find the < that opens this <row>
                let p = alt;
                while (p > 0 && wsXml[p] !== '<') p--;
                if (wsXml.substring(p, p+4) === '<row') rowStart = p;
              }
            }
            if (rowStart === -1) continue;

            const tagEnd  = wsXml.indexOf('>', rowStart) + 1;
            const rowEnd  = wsXml.indexOf('</row>', tagEnd);
            if (rowEnd === -1) continue;

            let inner = wsXml.substring(tagEnd, rowEnd);

            for (const patch of rowPatches) {
              // Search for existing cell with this address
              const cSearch = `r="${patch.addr}"`;
              const cStart  = inner.indexOf(cSearch);

              if (cStart !== -1) {
                // Walk back to find the < that opens this <c>
                let p = cStart;
                while (p > 0 && inner[p] !== '<') p--;
                const cEnd = inner.indexOf('</c>', p);
                if (cEnd !== -1) {
                  const existingCellXml = inner.substring(p, cEnd + 4);
                  // ── FORMULA GUARD: never overwrite a formula cell ──
                  // Formula cells have a <f> element; their cached value is in <v>
                  // with t="str" (string result) or no t attr (numeric result).
                  // We must NEVER replace a formula cell — doing so destroys it.
                  const hasFormula = /<f[\s>]/i.test(existingCellXml);
                  if (hasFormula) {
                    // Leave this cell completely untouched — formula is preserved.
                    continue;
                  }
                  inner = inner.substring(0, p) + patch.cellXml + inner.substring(cEnd + 4);
                }
              } else {
                // Cell not present — append inside row (safe: no formula to destroy)
                inner += patch.cellXml;
              }
            }

            wsXml = wsXml.substring(0, tagEnd) + inner + wsXml.substring(rowEnd);
          }

          const propTotal = propDates + propDiesel + propPrevRt;
          autoLog(propTotal > 0
            ? `🔄 Propagation done: ${propDates} dates · ${propDiesel} diesel levels · ${propPrevRt} prev RT filled`
            : 'ℹ️ Propagation: all fields already populated', 'ok');
        }

        // ── 10. Write updated SST back into the ZIP ─────────────────
        // Always write SST — even if no new entries were added (count may
        // need updating) and especially when it was created fresh.
        {
          const addedStrings = newSstEntries.length;
          const newCount     = sstCount  + addedStrings;
          const newUnique    = sstUnique + addedStrings;

          // Update the root <sst> element's count and uniqueCount attributes.
          // Replace only inside the opening <sst ...> tag — never inside <si> elements.
          sstXml = sstXml.replace(
            /(<sst\s[^>]*\bcount=")[^"]*(")/,
            `$1${newCount}$2`
          ).replace(
            /(<sst\s[^>]*\buniqueCount=")[^"]*(")/,
            `$1${newUnique}$2`
          );

          // Append new <si> entries before closing </sst>
          if (addedStrings > 0) {
            sstXml = sstXml.replace('</sst>', newSstEntries.join('') + '</sst>');
          }

          zip.file('xl/sharedStrings.xml', sstXml);
          autoLog(`📝 SharedStrings: ${newUnique} unique strings (${addedStrings > 0 ? '+' + addedStrings + ' new' : 'no new'})`);

          // If we created sharedStrings.xml from scratch, we must register it
          // in xl/_rels/workbook.xml.rels so Excel can find it.
          if (sstCreatedFresh) {
            const wbRelsPath = 'xl/_rels/workbook.xml.rels';
            let wbRelsXml = await zip.file(wbRelsPath).async('string');
            if (!wbRelsXml.includes('sharedStrings')) {
              const sstRel = `<Relationship Id="rIdSST" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings" Target="sharedStrings.xml"/>`;
              wbRelsXml = wbRelsXml.replace('</Relationships>', sstRel + '</Relationships>');
              zip.file(wbRelsPath, wbRelsXml);
              autoLog('📝 Registered sharedStrings.xml in workbook relationships');
            }
          }
        }

        // ── 11. Write modified worksheet back into ZIP ────────────────
        // Only this one file changes. Everything else (styles, formulas,
        // calcChain, drawings, charts, other sheets) is untouched.
        zip.file(wsPath, wsXml);

        // Remove calcChain.xml — Excel will rebuild it on open.
        // If we leave a stale calcChain pointing to old row ranges it can
        // cause Excel to show "repair" warnings.
        if (zip.file('xl/calcChain.xml')) {
          zip.remove('xl/calcChain.xml');
          autoLog('🗑️ calcChain.xml removed (Excel will rebuild on open)');
        }

        // ── 12. Generate ZIP and trigger download ─────────────────────
        const outBlob = await zip.generateAsync({
          type: 'blob',
          compression: 'DEFLATE',
          compressionOptions: { level: 6 }
        });

        const fname = window._autoXlsxFile.name.replace(/\.xlsx$/i,'') + '_updated.xlsx';
        const url   = URL.createObjectURL(outBlob);
        const a     = document.createElement('a');
        a.href = url; a.download = fname; a.click();
        setTimeout(() => URL.revokeObjectURL(url), 3000);

        autoLog(`📥 Downloaded: ${fname}`, 'ok');
        showToast(`✅ ${added} entries written · all formulas preserved · ${fname}`, 'success');

        // Result banner
        const resultSection = document.getElementById('autoResultSection');
        const resultCard    = document.getElementById('autoResultCard');
        if (resultSection && resultCard) {
          resultCard.innerHTML = `
            <div class="flex items-center gap-4 flex-wrap">
              <div style="font-size:2rem;">📊</div>
              <div class="flex-1">
                <div class="font-bold text-lg">Excel Updated &amp; Downloaded</div>
                <div class="text-sm mt-1" style="color:var(--neutral-600);">
                  <strong>${added}</strong> row${added!==1?'s':''} appended to <em>${targetSheetName}</em> · <strong>${fname}</strong>
                  ${dupeSkipped ? ` · ${dupeSkipped} dup${dupeSkipped!==1?'s':''} skipped` : ''}
                  ${dateSkipped ? ` · ${dateSkipped} older-date skipped` : ''}
                  <span style="color:var(--status-success);"> · ✓ formulas &amp; styles preserved</span>
                  ${propDates||propDiesel ? ` · propagation applied` : ''}
                </div>
              </div>
              <button class="btn btn-ghost btn-sm" onclick="document.getElementById('autoResultSection').style.display='none'">
                <i class="fa-regular fa-xmark"></i>
              </button>
            </div>`;
          resultSection.style.display = 'block';
        }

      } catch(err) {
        autoLog('❌ Excel write error: ' + err.message, 'error');
        showToast('Excel write failed: ' + err.message, 'error');
        console.error(err);
      } finally {
        if (btn) { btn.removeAttribute('disabled'); btn.innerHTML = '<i class="fa-regular fa-file-arrow-down" style="color:var(--status-success);"></i> Write to Excel &amp; Download'; }
      }
    }

    function autoExportCSV() {
      if (!_autoParseResults.length) return showToast('Nothing to export', 'warning');
      const rows = _autoParseResults.filter(r => !r._faulty);
      const headers = ['Date','Site ID','Site Name','Technician','Fuel Found (L)','Fuel Added (L)','Fuel Left (L)','Supplier','CPH','Curr RT','Prev RT','Bowser Plate','Bowser Remaining (L)','Stolen','Sender'];
      const csv = [
        headers.join(','),
        ...rows.map(r => [
          r.date, r.siteId, `"${r.siteName||''}"`, r.techName,
          r.fuelFound, r.fuelAdded, r.fuelLeft||'', r.supplier,
          r.stolen ? 'STOLEN' : (r.cph||''),
          r.currRt, r.prevRt,
          r.bowserPlate||'', r.bowserRemaining||'',
          r.stolen ? 'YES' : 'NO',
          `"${r.sender}"`
        ].join(','))
      ].join('\n');
      const blob = new Blob([csv], { type: 'text/csv' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `fuel_parsed_${new Date().toISOString().slice(0,10)}.csv`;
      a.click();
      showToast(`Exported ${rows.length} entries to CSV`, 'success');
    }

    // ============================================================
    // ===== XLSX EXPORT FROM AUTOMATION PAGE =====================
    // ============================================================
    function autoExportXLSX() {
      if (!_autoParseResults.length) return showToast('Nothing to export', 'warning');
      const rows = _autoParseResults.filter(r => !r._faulty);
      if (!rows.length) return showToast('No valid entries to export', 'warning');

      const regionName = document.getElementById('autoRegionSelect')?.value || 'Fuel Data';
      const isCCS = regionName.includes('CCS');
      const wb = XLSX.utils.book_new();

      // Sheet 1: Parsed fuel entries
      const headers = [
        'Date', 'Site ID', 'Site Name', 'Technician',
        'Fuel Found (L)', 'Fuel Added (L)', 'Fuel Left on Site (L)',
        'Supplier', 'CPH', 'Current RT (hrs)', 'Previous RT (hrs)',
        'DG Hours Used', 'Diesel Consumption (L)',
        ...(isCCS ? ['Bowser Plate','Bowser Remaining (L)','Qty Fuel (Bowser)','Oil Level','Fan Belt','Coolant','Fuel Leaks','Stolen','Sender'] : ['Sender'])
      ];
      const data = [headers, ...rows.map(r => {
        const fuelLeft = r.fuelLeft || ((r.fuelFound || 0) + (r.fuelAdded || 0));
        const dgHours  = (r.currRt  || 0) - (r.prevRt  || 0);
        const dieselUsed = dgHours > 0 && r.cph > 0 ? +(dgHours * r.cph).toFixed(2) : '';
        const base = [
          r.date, r.siteId, r.siteName || '', r.techName,
          r.fuelFound || '', r.fuelAdded || '', fuelLeft || '',
          r.supplier || '', r.stolen ? 'STOLEN' : (r.cph || ''),
          r.currRt || '', r.prevRt || '',
          dgHours > 0 ? +dgHours.toFixed(2) : '',
          dieselUsed,
        ];
        if (isCCS) {
          base.push(
            r.bowserPlate || '',
            r.bowserRemaining || '',
            r.bowserQty || '',
            r['OIL LEVEL'] || r._rawOilLevel || '',
            r['FAN BELT']  || r._rawFanBelt  || '',
            r['COOLANT']   || r._rawCoolant  || '',
            r['FUEL LEAKS']|| r._rawFuelLeaks|| '',
            r.stolen ? 'YES' : 'NO',
            r.sender
          );
        } else {
          base.push(r.sender);
        }
        return base;
      })];

      const ws1 = XLSX.utils.aoa_to_sheet(data);
      // Column widths
      ws1['!cols'] = [
        {wch:12},{wch:18},{wch:22},{wch:16},
        {wch:14},{wch:14},{wch:18},
        {wch:10},{wch:10},{wch:16},{wch:16},
        {wch:14},{wch:20},
        ...(isCCS ? [{wch:16},{wch:18},{wch:16},{wch:12},{wch:12},{wch:12},{wch:14},{wch:8},{wch:24}] : [{wch:24}])
      ];
      XLSX.utils.book_append_sheet(wb, ws1, 'Fuel Entries');

      // Sheet 2: Summary per technician
      const byTech = {};
      rows.forEach(r => {
        if (!byTech[r.techName]) byTech[r.techName] = { entries: 0, totalAdded: 0, sites: new Set(), stolen: 0 };
        byTech[r.techName].entries++;
        byTech[r.techName].totalAdded += r.fuelAdded || 0;
        if (r.siteId) byTech[r.techName].sites.add(r.siteId);
        if (r.stolen) byTech[r.techName].stolen++;
      });
      const summaryData = [
        ['Technician', 'Entries', 'Total Fuel Added (L)', 'Sites Visited', ...(isCCS ? ['Stolen Incidents'] : [])],
        ...Object.entries(byTech).sort((a,b) => b[1].totalAdded - a[1].totalAdded)
          .map(([tech, s]) => [tech, s.entries, s.totalAdded, s.sites.size, ...(isCCS ? [s.stolen||''] : [])])
      ];
      const ws2 = XLSX.utils.aoa_to_sheet(summaryData);
      ws2['!cols'] = [{wch:20},{wch:10},{wch:22},{wch:14},{wch:18}];
      XLSX.utils.book_append_sheet(wb, ws2, 'Summary');

      // CCS: Sheet 3 — Bowser tracking summary
      if (isCCS) {
        const bowserMap = {};
        rows.forEach(r => {
          const plate = r.bowserPlate || 'UNKNOWN';
          if (!bowserMap[plate]) bowserMap[plate] = { trips: 0, totalAdded: 0, sites: [] };
          bowserMap[plate].trips++;
          bowserMap[plate].totalAdded += r.fuelAdded || 0;
          if (r.siteId) bowserMap[plate].sites.push(r.siteId);
        });
        const bowserData = [
          ['Bowser Plate', 'Trips Made', 'Total Fuel Delivered (L)', 'Sites Visited'],
          ...Object.entries(bowserMap).sort((a,b) => b[1].totalAdded - a[1].totalAdded)
            .map(([plate, b]) => [plate, b.trips, b.totalAdded, [...new Set(b.sites)].length])
        ];
        const ws3 = XLSX.utils.aoa_to_sheet(bowserData);
        ws3['!cols'] = [{wch:16},{wch:12},{wch:26},{wch:16}];
        XLSX.utils.book_append_sheet(wb, ws3, 'Bowser Summary');
      }

      const fname = `fuel_${regionName.replace(/\s+/g,'_')}_${new Date().toISOString().slice(0,10)}.xlsx`;
      XLSX.writeFile(wb, fname);
      showToast(`Exported ${rows.length} entries to Excel${isCCS ? ' (+ Bowser Summary sheet)' : ''}`, 'success');
    }

    // ============================================================
    // ===== PROPAGATION ENGINE ===================================
    // ============================================================
    // Mirrors the Python UniversalDataPropagator + main_auto DataPropagator logic.
    // Operates on DB.regions[regionName].dailyLog entries that have
    // fuelFound, fuelAdded, currRt, prevRt, cph, siteId stored from automation import.
    //
    // For each site, sorted by date:
    //   - fuelLeft       = fuelFound + fuelAdded  (current visit)
    //   - prevDiesel     = previous visit's fuelLeft
    //   - dgHoursUsed    = currRt - prevRt
    //   - dieselConsumed = dgHoursUsed × cph  (if both present)
    //   - prevRt (if missing) ← previous visit's currRt

    function runPropagation(regionName) {
      regionName = regionName || DB.currentRegion;
      const region = DB.regions[regionName];
      if (!region) return { sites: 0, rows: 0, dates: 0, diesel: 0, dgHours: 0 };

      // Collect all entries across all dates that have siteId
      const siteMap = {}; // siteId → [{date, entryRef}]
      Object.entries(region.dailyLog).forEach(([date, entries]) => {
        entries.forEach((entry, idx) => {
          const sid = (entry.siteId || '').toUpperCase();
          if (!sid) return;
          if (!siteMap[sid]) siteMap[sid] = [];
          siteMap[sid].push({ date, idx, entry });
        });
      });

      let sitesProcessed = 0, rowsUpdated = 0, datesFixed = 0, dieselFilled = 0, dgFilled = 0;

      for (const [siteId, visits] of Object.entries(siteMap)) {
        // Sort visits chronologically
        visits.sort((a, b) => a.date.localeCompare(b.date));

        let prevDate     = null;
        let prevFuelLeft = null;
        let prevCurrRt   = null;

        for (const { date, entry } of visits) {
          let modified = false;

          // 1. Compute fuel left on site for this visit
          const fuelFound = entry.fuelFound || 0;
          const fuelAdded = entry.fuelAdded || entry.supplied || 0;
          const fuelLeft  = fuelFound + fuelAdded;
          if (!entry.fuelLeft && fuelLeft > 0) {
            entry.fuelLeft = fuelLeft;
            modified = true;
          }

          // 2. Previous diesel level ← previous visit's fuelLeft
          if (!entry.prevDiesel) {
            if (prevFuelLeft !== null) {
              entry.prevDiesel = prevFuelLeft;
              dieselFilled++;
              modified = true;
            } else if (fuelLeft > 0) {
              entry.prevDiesel = fuelLeft; // first visit: copy own fuelLeft
              dieselFilled++;
              modified = true;
            }
          }

          // 3. Previous date ← previous visit's date
          if (!entry.prevDate) {
            if (prevDate) {
              entry.prevDate = prevDate;
              datesFixed++;
              modified = true;
            } else {
              entry.prevDate = date; // first visit: copy own date
              datesFixed++;
              modified = true;
            }
          }

          // 4. Previous RT ← previous visit's currRt (if prevRt missing)
          const currRt = entry.currRt || 0;
          if (!entry.prevRt && prevCurrRt !== null && prevCurrRt > 0) {
            entry.prevRt = prevCurrRt;
            dgFilled++;
            modified = true;
          }

          // 5. DG hours used = currRt - prevRt
          if (currRt > 0 && entry.prevRt > 0 && !entry.dgHoursUsed) {
            const dg = +(currRt - entry.prevRt).toFixed(2);
            if (dg > 0) {
              entry.dgHoursUsed = dg;
              modified = true;
            }
          }

          // 6. Diesel consumed = dgHoursUsed × CPH
          if (entry.dgHoursUsed > 0 && entry.cph > 0 && !entry.dieselConsumed) {
            entry.dieselConsumed = +(entry.dgHoursUsed * entry.cph).toFixed(2);
            modified = true;
          }

          // Advance trackers
          if (fuelLeft > 0)  prevFuelLeft = fuelLeft;
          if (currRt > 0)    prevCurrRt   = currRt;
          prevDate = date;

          if (modified) rowsUpdated++;
        }
        sitesProcessed++;
      }

      save();
      return { sites: sitesProcessed, rows: rowsUpdated, dates: datesFixed, diesel: dieselFilled, dgHours: dgFilled };
    }

    function openPropagationModal() {
      // Build per-region stats before showing
      const regionName = DB.currentRegion;
      const region = DB.regions[regionName];
      if (!region) return showToast('No current region', 'warning');

      // Count how many entries have siteId (propagatable)
      let total = 0, withSite = 0;
      Object.values(region.dailyLog).forEach(entries => {
        entries.forEach(e => {
          total++;
          if (e.siteId) withSite++;
        });
      });

      // Count unique sites
      const sites = new Set();
      Object.values(region.dailyLog).forEach(entries =>
        entries.forEach(e => { if (e.siteId) sites.add(e.siteId.toUpperCase()); })
      );

      const modal = document.createElement('div');
      modal.className = 'modal-overlay';
      modal.id = 'propagationModal';
      modal.style.display = 'flex';
      modal.innerHTML = `
        <div class="modal-container" style="max-width:520px;width:100%;">
          <div class="modal-header">
            <div>
              <h3 class="text-xl font-semibold" style="color:var(--status-info);">
                <i class="fa-regular fa-rotate"></i> Data Propagation
              </h3>
              <p class="text-sm mt-1" style="color:var(--neutral-500);">
                Auto-fill previous dates, diesel levels and DG hours from prior visits
              </p>
            </div>
            <button class="btn btn-icon btn-ghost" onclick="document.getElementById('propagationModal').remove()">
              <i class="fa-regular fa-xmark"></i>
            </button>
          </div>
          <div class="modal-body">
            <div class="card mb-4" style="background:var(--neutral-50);">
              <div class="grid grid-cols-3 gap-4 text-center">
                <div>
                  <div class="text-2xl font-bold" style="color:var(--accent-600);">${total}</div>
                  <div class="text-xs mt-1" style="color:var(--neutral-500);">Total entries</div>
                </div>
                <div>
                  <div class="text-2xl font-bold" style="color:var(--status-info);">${sites.size}</div>
                  <div class="text-xs mt-1" style="color:var(--neutral-500);">Unique sites</div>
                </div>
                <div>
                  <div class="text-2xl font-bold" style="color:var(--status-success);">${withSite}</div>
                  <div class="text-xs mt-1" style="color:var(--neutral-500);">With site ID</div>
                </div>
              </div>
            </div>

            <div class="card mb-4" style="border-left:3px solid var(--status-info);">
              <p class="text-sm font-semibold mb-2">What propagation fills in:</p>
              <ul class="text-sm" style="color:var(--neutral-600);line-height:2;">
                <li><i class="fa-regular fa-calendar" style="width:18px;color:var(--status-info);"></i> <strong>Previous visit date</strong> — from prior visit to same site</li>
                <li><i class="fa-regular fa-droplet" style="width:18px;color:var(--status-info);"></i> <strong>Previous diesel level</strong> — from prior visit's fuel left on site</li>
                <li><i class="fa-regular fa-gauge-high" style="width:18px;color:var(--status-info);"></i> <strong>Previous DG hours</strong> — from prior visit's current runtime</li>
                <li><i class="fa-regular fa-clock" style="width:18px;color:var(--status-success);"></i> <strong>DG hours used</strong> — current RT minus previous RT</li>
                <li><i class="fa-regular fa-fire" style="width:18px;color:var(--status-warning);"></i> <strong>Diesel consumed</strong> — DG hours × CPH</li>
              </ul>
            </div>

            <div id="propagationResult" style="display:none;" class="card mb-4" style="background:var(--status-success-bg);border:1px solid var(--status-success);"></div>

            <div class="select-wrapper mb-4">
              <select class="select-field" id="propagationRegionSelect">
                ${Object.keys(DB.regions).map(r => `<option value="${r}" ${r===regionName?'selected':''}>${r}</option>`).join('')}
              </select>
            </div>
          </div>
          <div class="modal-footer">
            <button class="btn btn-ghost" onclick="document.getElementById('propagationModal').remove()">Cancel</button>
            <button class="btn btn-primary" onclick="confirmRunPropagation()">
              <i class="fa-regular fa-rotate"></i> Run Propagation
            </button>
          </div>
        </div>`;
      document.body.appendChild(modal);
    }

    function confirmRunPropagation() {
      const sel = document.getElementById('propagationRegionSelect');
      const regionName = sel ? sel.value : DB.currentRegion;
      const result = runPropagation(regionName);

      const resultDiv = document.getElementById('propagationResult');
      if (resultDiv) {
        resultDiv.style.display = 'block';
        resultDiv.style.background = 'var(--status-success-bg)';
        resultDiv.style.borderLeft = '3px solid var(--status-success)';
        resultDiv.innerHTML = `
          <div class="font-semibold mb-2" style="color:var(--status-success);">
            <i class="fa-regular fa-check-circle"></i> Propagation Complete
          </div>
          <div class="grid grid-cols-2 gap-3 text-sm">
            <div><span style="color:var(--neutral-500);">Sites processed:</span> <strong>${result.sites}</strong></div>
            <div><span style="color:var(--neutral-500);">Rows updated:</span> <strong>${result.rows}</strong></div>
            <div><span style="color:var(--neutral-500);">Dates filled:</span> <strong>${result.dates}</strong></div>
            <div><span style="color:var(--neutral-500);">Diesel levels:</span> <strong>${result.diesel}</strong></div>
            <div><span style="color:var(--neutral-500);">DG hours:</span> <strong>${result.dgHours}</strong></div>
          </div>`;
      }
      showToast(`Propagation done — ${result.rows} entries updated`, 'success');
      if (currentPage === 'automation') renderPageWithTransition('automation');
    }

    // ============================================================
    // ===== BULK IMPORT TECHNICIANS FROM TECH_MANAGER ============
    // ============================================================
    function openBulkTechImportModal() {
      const regionName = DB.currentRegion;
      const region = DB.regions[regionName];
      if (!region) return showToast('No current region set', 'warning');

      // Map region name → TECHNICIAN_DATA key
      const regionKeyMap = {
        'New CCS': 'new_cbt', 'Old CCS': 'old_cbt',
        'NRW': 'nrw', 'Eastern': 'eastern'
      };
      // Try exact match first, then fuzzy
      let dataKey = regionKeyMap[regionName];
      if (!dataKey) {
        const rLower = regionName.toLowerCase();
        if (rLower.includes('nrw'))     dataKey = 'nrw';
        else if (rLower.includes('east')) dataKey = 'eastern';
        else if (rLower.includes('old'))  dataKey = 'old_cbt';
        else if (rLower.includes('cbt') || rLower.includes('ccs')) dataKey = 'new_cbt';
      }

      const regionLabels = { nrw:'NRW', eastern:'Eastern', old_cbt:'Old CBT', new_cbt:'New CBT' };
      const stats = TECH_MANAGER.getRegionStats();
      const existing = new Set(region.technicians.map(t => t.toUpperCase()));

      // Build list of all techs from master, categorized by region
      const allRegionTechs = {};
      for (const [rKey, rStats] of Object.entries(stats)) {
        allRegionTechs[rKey] = rStats.techList.sort();
      }

      const modal = document.createElement('div');
      modal.className = 'modal-overlay';
      modal.id = 'bulkTechModal';
      modal.style.display = 'flex';

      const renderTechGroup = (rKey) => {
        const techs = allRegionTechs[rKey] || [];
        return techs.map(t => {
          const alreadyIn = existing.has(t.toUpperCase());
          return `
          <label class="flex items-center gap-2 p-2 rounded cursor-pointer"
            style="background:var(--neutral-50);margin-bottom:4px;${alreadyIn?'opacity:0.45;':''}">
            <input type="checkbox" class="bulkTechCheck" data-tech="${t}" data-region="${rKey}"
              ${alreadyIn ? 'disabled checked' : 'checked'}
              style="accent-color:var(--accent-600);">
            <span class="font-mono text-sm font-semibold">${t}</span>
            ${alreadyIn ? '<span class="badge badge-neutral" style="font-size:10px;margin-left:auto;">Already added</span>' : `<span class="text-xs" style="color:var(--neutral-400);margin-left:auto;">${stats[rKey].sites} sites</span>`}
          </label>`;
        }).join('');
      };

      modal.innerHTML = `
        <div class="modal-container" style="max-width:580px;width:100%;max-height:90vh;overflow-y:auto;">
          <div class="modal-header">
            <div>
              <h3 class="text-xl font-semibold">
                <i class="fa-regular fa-users-gear" style="color:var(--accent-600);"></i>
                Bulk Import Technicians
              </h3>
              <p class="text-sm mt-1" style="color:var(--neutral-500);">
                Adding to: <strong>${regionName}</strong>
              </p>
            </div>
            <button class="btn btn-icon btn-ghost" onclick="document.getElementById('bulkTechModal').remove()">
              <i class="fa-regular fa-xmark"></i>
            </button>
          </div>
          <div class="modal-body">
            <div class="card mb-3" style="background:var(--status-info-bg);border:1px solid var(--status-info);">
              <p class="text-sm" style="color:var(--neutral-700);">
                Select technicians from the master data to add to <strong>${regionName}</strong>.
                Technicians already in this region are shown greyed out.
              </p>
            </div>

            ${Object.entries(allRegionTechs).map(([rKey, techs]) => `
            <div class="mb-4">
              <div class="flex items-center justify-between mb-2">
                <div class="font-semibold text-sm">${regionLabels[rKey]||rKey} <span style="color:var(--neutral-400);font-weight:400;">(${techs.length} techs)</span></div>
                <button class="btn btn-ghost btn-sm" onclick="bulkTechSelectAll('${rKey}', true)" style="font-size:11px;">Select all</button>
              </div>
              <div>${renderTechGroup(rKey)}</div>
            </div>`).join('<hr style="border-color:var(--neutral-200);margin:12px 0;">')}
          </div>
          <div class="modal-footer">
            <button class="btn btn-ghost" onclick="document.getElementById('bulkTechModal').remove()">Cancel</button>
            <button class="btn btn-primary" onclick="confirmBulkTechImport()">
              <i class="fa-regular fa-download"></i> Import Selected
            </button>
          </div>
        </div>`;
      document.body.appendChild(modal);
    }

    function bulkTechSelectAll(regionKey, val) {
      document.querySelectorAll(`.bulkTechCheck[data-region="${regionKey}"]:not([disabled])`).forEach(cb => {
        cb.checked = val;
      });
    }

    function confirmBulkTechImport() {
      const region = DB.regions[DB.currentRegion];
      if (!region) return;
      const existing = new Set(region.technicians.map(t => t.toUpperCase()));
      let added = 0;

      document.querySelectorAll('.bulkTechCheck:not([disabled])').forEach(cb => {
        if (!cb.checked) return;
        const tech = cb.dataset.tech;
        if (!existing.has(tech.toUpperCase())) {
          region.technicians.push(tech);
          existing.add(tech.toUpperCase());
          added++;
        }
      });

      save();
      document.getElementById('bulkTechModal').remove();
      showToast(`✅ Added ${added} technician${added !== 1 ? 's' : ''} to ${DB.currentRegion}`, 'success');
      if (currentPage === 'regions') renderPageWithTransition('regions');
    }

    // ---- SEARCH HELPER: navigate to technicians page for a site ----
    function searchGoToSite(el) {
      var span = el.querySelector('.sr-site-id');
      if (!span) return;
      var sid = span.textContent.trim();
      setPage('technicians', null);
      setTimeout(function() {
        _tmState.search = sid;
        var inp = document.getElementById('tmSearchInput');
        if (inp) inp.value = sid;
        tmRenderTable();
      }, 400);
    }

    // ---- TM QUICK RESULT: "See all sites" via event delegation ----
    document.addEventListener('click', function(e) {
      var btn = e.target.closest('.tm-see-all-btn');
      if (!btn) return;
      var span = btn.querySelector('.tm-tech-target');
      if (!span) return;
      var tech = span.textContent.trim();
      _tmState.search = tech;
      var inp = document.getElementById('tmSearchInput');
      if (inp) inp.value = tech;
      tmRenderTable();
    });

    // ===== BREADCRUMB SYSTEM =====
    const PAGE_LABELS = {
      dashboard: 'Dashboard', daily: 'Daily Entries', orders: 'Orders',
      regions: 'Regions', reports: 'Reports', leaderboard: 'Leaderboard',
      cycles: 'Cycle History', technicians: 'Tech Manager', automation: 'Automation'
    };

    // Breadcrumb trail stack — each entry: { label, page (optional), action (optional) }
    let _breadcrumbTrail = [];

    function updateBreadcrumb(page, subLabel, subAction) {
      const bc = document.getElementById('pageBreadcrumb');
      const pill = document.getElementById('breadcrumbRegionPill');
      if (!bc) return;

      const pageLabel = PAGE_LABELS[page] || page;

      if (subLabel) {
        // Deep navigation: Home > Page > Sub
        _breadcrumbTrail = [
          { label: pageLabel, action: () => setPage(page, null) },
          { label: subLabel, action: subAction || null, current: true }
        ];
      } else {
        // Top-level page
        _breadcrumbTrail = [
          { label: pageLabel, action: null, current: true }
        ];
      }

      // Rebuild DOM
      let html = `
        <div class="breadcrumb-item">
          <span onclick="setPage('dashboard',null)" style="cursor:pointer;" title="Home" aria-label="Home">
            <i class="fa-regular fa-house" style="font-size:11px;"></i>
          </span>
        </div>`;

      _breadcrumbTrail.forEach((crumb, i) => {
        html += `<span class="breadcrumb-sep" aria-hidden="true"><i class="fa-regular fa-chevron-right" style="font-size:9px;"></i></span>`;
        if (crumb.current) {
          html += `<div class="breadcrumb-item current" id="breadcrumbCurrent" aria-current="page"><span>${crumb.label}</span></div>`;
        } else {
          html += `<div class="breadcrumb-item"><a onclick="${crumb.action ? '(' + crumb.action.toString() + ')()' : ''}" style="cursor:pointer;">${crumb.label}</a></div>`;
        }
      });

      // Inline region pill on right
      const region = DB.currentRegion || '-';
      html += `<span id="breadcrumbRegionPill" style="margin-left:auto;font-size:var(--text-xs);color:var(--neutral-400);">
        <span style="background:var(--accent-100);color:var(--accent-700);padding:2px 10px;border-radius:var(--radius-full);font-weight:500;">${region}</span>
      </span>`;

      bc.innerHTML = html;
      bc.setAttribute('aria-label', 'Breadcrumb navigation');
    }

    // Helper to push a sub-breadcrumb (e.g. when opening order detail inline)
    function pushBreadcrumb(subLabel, subAction) {
      updateBreadcrumb(currentPage, subLabel, subAction);
    }

    // ===== DESTRUCTIVE CYCLE CONFIRM =====
    function checkEndCycleConfirm() {
      const phrase = (document.getElementById('endCycleConfirmPhrase')?.textContent || '').trim();
      const input = (document.getElementById('endCycleConfirmInput')?.value || '').trim().toUpperCase();
      const btn = document.getElementById('endCycleConfirmBtn');
      const hint = document.getElementById('endCycleConfirmHint');
      const inp = document.getElementById('endCycleConfirmInput');
      const match = input === phrase.toUpperCase();
      if (btn) { btn.disabled = !match; btn.style.opacity = match ? '1' : '0.5'; btn.style.cursor = match ? 'pointer' : 'not-allowed'; }
      if (inp) inp.classList.toggle('matched', match);
      if (hint) {
        if (!input) { hint.textContent = ''; hint.className = 'field-hint'; }
        else if (match) { hint.textContent = '✓ Confirmed — you may proceed'; hint.className = 'field-hint success'; }
        else { hint.textContent = 'Text does not match — keep typing'; hint.className = 'field-hint error'; }
      }
    }

    function openEndCycleModal() {
      _openEndCycleModalCore();
      const phrase = document.getElementById('endCycleConfirmPhrase');
      const inp = document.getElementById('endCycleConfirmInput');
      if (phrase) phrase.textContent = DB.currentCycleName || 'INITIAL CYCLE';
      if (inp) { inp.value = ''; inp.classList.remove('matched'); }
      checkEndCycleConfirm();
    }

    // ===== COMMAND PALETTE =====
    const CMD_PAGES = [
      { label: 'Dashboard', icon: 'fa-gauge-high', sub: 'Overview & KPIs', page: 'dashboard' },
      { label: 'Daily Entries', icon: 'fa-calendar', sub: 'Log daily fuel supply', page: 'daily' },
      { label: 'Orders', icon: 'fa-file-lines', sub: 'Manage fuel orders', page: 'orders' },
      { label: 'Regions', icon: 'fa-building', sub: 'Region & tech management', page: 'regions' },
      { label: 'Reports', icon: 'fa-chart-bar', sub: 'Analytics & export', page: 'reports' },
      { label: 'Leaderboard', icon: 'fa-trophy', sub: 'Technician rankings', page: 'leaderboard' },
      { label: 'Cycle History', icon: 'fa-rotate', sub: 'Past cycles archive', page: 'cycles' },
      { label: 'Tech Manager', icon: 'fa-id-card', sub: 'Technician database', page: 'technicians' },
      { label: 'Automation', icon: 'fa-robot', sub: 'Import & propagate', page: 'automation' },
    ];
    const CMD_ACTIONS = [
      { label: 'Import Orders (WhatsApp)', icon: 'fa-whatsapp', sub: 'Parse WhatsApp message', fn: () => openWhatsAppImport() },
      { label: 'Auto Daily Entry', icon: 'fa-file-excel', sub: 'Import from Excel', fn: () => openDailyAutoImport() },
      { label: 'End Current Cycle', icon: 'fa-flag-checkered', sub: 'Archive & start fresh', fn: () => openEndCycleModal() },
      { label: 'Toggle Dark Mode', icon: 'fa-moon', sub: 'Switch light/dark theme', fn: () => toggleDarkMode() },
      { label: 'Keyboard Shortcuts', icon: 'fa-keyboard', sub: 'View all shortcuts', fn: () => openModal('shortcutsModal') },
      { label: 'Watch List', icon: 'fa-eye', sub: 'Tracked technicians', fn: () => openWatchedPersonsModal() },
      { label: 'What\'s New', icon: 'fa-sparkles', sub: 'See latest updates', fn: () => openWhatsNewModal() },
      { label: 'Help Tour', icon: 'fa-circle-question', sub: 'Take a guided tour', fn: () => startOnboardingTour() },
    ];
    let _cmdSelectedIndex = 0;
    let _cmdItems = [];

    function openCommandPalette() {
      const overlay = document.getElementById('cmdOverlay');
      if (!overlay) return;
      overlay.classList.add('active');
      const inp = document.getElementById('cmdInput');
      if (inp) { inp.value = ''; inp.focus(); }
      renderCmdResults('');
    }

    function closeCommandPalette() {
      const overlay = document.getElementById('cmdOverlay');
      if (overlay) overlay.classList.remove('active');
    }

    function renderCmdResults(query) {
      const body = document.getElementById('cmdBody');
      if (!body) return;
      query = query.toLowerCase().trim();
      _cmdItems = [];
      let html = '';

      // Technician search
      const region = DB.regions[DB.currentRegion];
      if (query.length >= 2 && region) {
        const techs = region.technicians.filter(t => t.toLowerCase().includes(query)).slice(0, 5);
        if (techs.length) {
          html += `<div class="cmd-section-label">Technicians</div>`;
          techs.forEach(t => {
            _cmdItems.push({ type: 'tech', label: t });
            html += `<button class="cmd-item" onclick="closeCmdAndGoTech('${t}')"><div class="cmd-item-icon"><i class="fa-regular fa-user"></i></div><div class="cmd-item-text"><div class="cmd-item-label">${t}</div><div class="cmd-item-sub">Technician · ${DB.currentRegion}</div></div></button>`;
          });
        }

        // Order search
        const orders = Object.keys(region.orders).filter(o => o.toLowerCase().includes(query)).slice(0, 5);
        if (orders.length) {
          html += `<div class="cmd-section-label">Orders</div>`;
          orders.forEach(o => {
            _cmdItems.push({ type: 'order', label: o });
            const ord = region.orders[o];
            const pct = ord.totalLiters > 0 ? Math.round((ord.suppliedTotal/ord.totalLiters)*100) : 0;
            html += `<button class="cmd-item" onclick="closeCommandPalette();setPage('orders',null)"><div class="cmd-item-icon"><i class="fa-regular fa-file-lines"></i></div><div class="cmd-item-text"><div class="cmd-item-label">${o}</div><div class="cmd-item-sub">${ord.totalLiters}L · ${pct}% used</div></div></button>`;
          });
        }
      }

      // Pages
      const pages = CMD_PAGES.filter(p => !query || p.label.toLowerCase().includes(query) || p.sub.toLowerCase().includes(query));
      if (pages.length) {
        html += `<div class="cmd-section-label">Pages</div>`;
        pages.forEach(p => {
          _cmdItems.push({ type: 'page', data: p });
          html += `<button class="cmd-item" onclick="closeCommandPalette();setPage('${p.page}',null)"><div class="cmd-item-icon"><i class="fa-regular ${p.icon}"></i></div><div class="cmd-item-text"><div class="cmd-item-label">${p.label}</div><div class="cmd-item-sub">${p.sub}</div></div><span class="cmd-item-tag">Page</span></button>`;
        });
      }

      // Actions
      const actions = CMD_ACTIONS.filter(a => !query || a.label.toLowerCase().includes(query) || a.sub.toLowerCase().includes(query));
      if (actions.length) {
        html += `<div class="cmd-section-label">Actions</div>`;
        actions.forEach(a => {
          _cmdItems.push({ type: 'action', data: a });
          html += `<button class="cmd-item action" onclick="closeCommandPalette();(${a.fn.toString()})()"><div class="cmd-item-icon"><i class="fa-regular ${a.icon}"></i></div><div class="cmd-item-text"><div class="cmd-item-label">${a.label}</div><div class="cmd-item-sub">${a.sub}</div></div><span class="cmd-item-tag">Action</span></button>`;
        });
      }

      body.innerHTML = html || `<div style="text-align:center;padding:var(--space-8);color:var(--neutral-400);font-size:var(--text-sm);">No results for "${query}"</div>`;
      _cmdSelectedIndex = 0;
      updateCmdSelection();
    }

    function closeCmdAndGoTech(techName) {
      closeCommandPalette();
      setPage('technicians', null);
      setTimeout(() => {
        _tmState.search = techName;
        const inp = document.getElementById('tmSearchInput');
        if (inp) inp.value = techName;
        if (typeof tmRenderTable === 'function') tmRenderTable();
      }, 400);
    }

    function updateCmdSelection() {
      document.querySelectorAll('#cmdBody .cmd-item').forEach((el, i) => {
        el.classList.toggle('selected', i === _cmdSelectedIndex);
        if (i === _cmdSelectedIndex) el.scrollIntoView({ block: 'nearest' });
      });
    }

    document.addEventListener('keydown', function(e) {
      const overlay = document.getElementById('cmdOverlay');
      if (!overlay) return;
      const isOpen = overlay.classList.contains('active');
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        isOpen ? closeCommandPalette() : openCommandPalette();
        return;
      }
      if (!isOpen) return;
      const items = document.querySelectorAll('#cmdBody .cmd-item');
      if (e.key === 'ArrowDown') { e.preventDefault(); _cmdSelectedIndex = Math.min(_cmdSelectedIndex + 1, items.length - 1); updateCmdSelection(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); _cmdSelectedIndex = Math.max(_cmdSelectedIndex - 1, 0); updateCmdSelection(); }
      else if (e.key === 'Enter') { e.preventDefault(); if (items[_cmdSelectedIndex]) items[_cmdSelectedIndex].click(); }
    });

    document.getElementById('cmdInput')?.addEventListener('input', function() {
      renderCmdResults(this.value);
    });

    document.getElementById('cmdOverlay')?.addEventListener('click', function(e) {
      if (e.target === this) closeCommandPalette();
    });

    // ===== ONBOARDING TOUR =====
    const TOUR_STEPS = [
      { selector: '#sidebar', title: 'Welcome to CCS Fuel System', desc: 'This sidebar is your main navigation. It\'s organised into Main pages and Quick Actions. Click any item to navigate, or collapse it for more screen space.', pos: 'right' },
      { selector: '.search-bar', title: 'Command Palette & Search', desc: 'Click the search bar or press Ctrl+K to open the command palette — your fastest way to navigate anywhere, run actions, or find technicians and orders.', pos: 'bottom' },
      { selector: '#regionSelect', title: 'Region Selector', desc: 'Your current region is always shown here. Change it to switch between New CCS, Old CCS, NRW, or Eastern data.', pos: 'bottom' },
      { selector: '#notifBellBtn', title: 'Smart Notifications', desc: 'The bell shows alerts for overages, near-full orders, unassigned orders needing comments, and inactive technicians.', pos: 'bottom' },
      { selector: '#pageBreadcrumb', title: 'Breadcrumb Navigation', desc: 'You always know where you are in the system. The breadcrumb shows your current page and region at a glance.', pos: 'bottom' },
      { selector: '[data-tooltip="End Cycle"]', title: 'End Cycle — Safe by Design', desc: 'This critical action now requires you to type the current cycle name before confirming — protecting you from accidental data archiving.', pos: 'right' },
    ];
    let _tourStep = 0;
    let _tourActive = false;

    function startOnboardingTour() {
      _tourActive = true;
      _tourStep = 0;
      document.getElementById('tourBackdrop').style.display = 'block';
      document.getElementById('tourTooltip').style.display = 'block';
      showTourStep(_tourStep);
    }

    function showTourStep(step) {
      const steps = TOUR_STEPS;
      if (step >= steps.length) { endTour(); return; }
      const s = steps[step];
      const el = document.querySelector(s.selector);
      const tooltip = document.getElementById('tourTooltip');
      const spotlight = document.getElementById('tourSpotlight');
      document.getElementById('tourStepIndicator').textContent = `Step ${step + 1} of ${steps.length}`;
      document.getElementById('tourTitle').textContent = s.title;
      document.getElementById('tourDesc').textContent = s.desc;
      document.getElementById('tourPrevBtn').style.display = step === 0 ? 'none' : '';
      document.getElementById('tourNextBtn').textContent = step === steps.length - 1 ? 'Finish ✓' : 'Next →';

      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        // Give scroll a moment to settle before measuring
        requestAnimationFrame(() => {
          const r = el.getBoundingClientRect();
          const pad = 8;
          spotlight.style.cssText = `left:${r.left - pad}px;top:${r.top - pad}px;width:${r.width + pad*2}px;height:${r.height + pad*2}px;display:block;`;
          const tW = 300, tH = 200;
          let tx, ty;
          if (s.pos === 'right') {
            tx = r.right + 16;
            ty = r.top;
          } else {
            tx = r.left;
            ty = r.bottom + 16;
          }
          // Clamp to viewport
          if (tx + tW > window.innerWidth - 20) tx = window.innerWidth - tW - 20;
          if (ty + tH > window.innerHeight - 20) ty = r.top - tH - 16;
          if (tx < 10) tx = 10;
          if (ty < 10) ty = 10;
          tooltip.style.cssText = `left:${tx}px;top:${ty}px;width:${tW}px;display:block;`;
        });
      } else {
        // Element not found — hide spotlight and center tooltip
        spotlight.style.cssText = 'display:none;';
        tooltip.style.cssText = `left:50%;top:50%;transform:translate(-50%,-50%);width:300px;display:block;`;
      }
    }

    function tourNext() {
      _tourStep++;
      if (_tourStep >= TOUR_STEPS.length) endTour();
      else showTourStep(_tourStep);
    }

    function tourPrev() {
      if (_tourStep > 0) { _tourStep--; showTourStep(_tourStep); }
    }

    function endTour() {
      _tourActive = false;
      document.getElementById('tourBackdrop').style.display = 'none';
      document.getElementById('tourTooltip').style.display = 'none';
    }

    // ===== WHAT'S NEW MODAL =====
    function openWhatsNewModal() {
      // Fix the date in the modal
      const dateEl = document.querySelector('#whatsNewModal .text-xs[style*="color:var(--neutral-400)"]');
      if (dateEl) dateEl.textContent = new Date().toLocaleDateString('en-GB', {day:'numeric',month:'short',year:'numeric'});
      openModal('whatsNewModal');
    }

    // ===== TABLE DENSITY TOGGLE =====
    let _tableDensity = localStorage.getItem('ccs_table_density') || 'default';

    function setTableDensity(density) {
      _tableDensity = density;
      localStorage.setItem('ccs_table_density', density);
      const mc = document.getElementById('mainContent');
      if (mc) {
        mc.classList.remove('table-density-compact', 'table-density-comfortable');
        if (density !== 'default') mc.classList.add('table-density-' + density);
      }
      document.querySelectorAll('.density-btn').forEach(b => {
        b.classList.toggle('active', b.dataset.density === density);
      });
    }

    function renderDensityToggle() {
      return `<div class="density-toggle" role="group" aria-label="Table density">
        <button class="density-btn ${_tableDensity==='compact'?'active':''}" data-density="compact" onclick="setTableDensity('compact')" title="Compact rows">Compact</button>
        <button class="density-btn ${_tableDensity==='default'?'active':''}" data-density="default" onclick="setTableDensity('default')" title="Default rows">Default</button>
        <button class="density-btn ${_tableDensity==='comfortable'?'active':''}" data-density="comfortable" onclick="setTableDensity('comfortable')" title="Comfortable rows">Comfortable</button>
      </div>`;
    }

    // ===== COLUMN CHOOSER =====
    // Per-table column visibility stored in localStorage
    const COL_CONFIGS = {
      orders: {
        key: 'ccs_col_orders',
        columns: [
          { id: 'status',    label: 'Status',       default: true },
          { id: 'vehicle',   label: 'Vehicle Plate', default: true },
          { id: 'date',      label: 'Date',          default: true },
          { id: 'total',     label: 'Total (L)',     default: true },
          { id: 'supplied',  label: 'Supplied (L)',  default: true },
          { id: 'balance',   label: 'Balance (L)',   default: true },
          { id: 'progress',  label: 'Progress',      default: true },
          { id: 'techs',     label: 'Technicians',   default: true },
        ]
      },
      daily: {
        key: 'ccs_col_daily',
        columns: [
          { id: 'technician', label: 'Technician',  default: true },
          { id: 'order',      label: 'Order No',    default: true },
          { id: 'supplied',   label: 'Supplied (L)',default: true },
          { id: 'type',       label: 'Type',         default: true },
          { id: 'comment',    label: 'Comment',      default: false },
          { id: 'site',       label: 'Site ID',      default: false },
        ]
      }
    };

    function getVisibleCols(tableId) {
      const config = COL_CONFIGS[tableId];
      if (!config) return {};
      try {
        const saved = JSON.parse(localStorage.getItem(config.key) || 'null');
        if (saved) return saved;
      } catch(e) {}
      // Build default
      const defaults = {};
      config.columns.forEach(c => { defaults[c.id] = c.default; });
      return defaults;
    }

    function setColVisible(tableId, colId, visible) {
      const vis = getVisibleCols(tableId);
      vis[colId] = visible;
      localStorage.setItem(COL_CONFIGS[tableId].key, JSON.stringify(vis));
      // Re-apply visibility to live table
      applyColVisibility(tableId);
    }

    function applyColVisibility(tableId) {
      const vis = getVisibleCols(tableId);
      Object.entries(vis).forEach(([colId, show]) => {
        document.querySelectorAll(`[data-col="${tableId}-${colId}"]`).forEach(el => {
          el.style.display = show ? '' : 'none';
        });
      });
    }

    function renderColChooser(tableId, extraClass) {
      const config = COL_CONFIGS[tableId];
      if (!config) return '';
      const vis = getVisibleCols(tableId);
      const id = `colChooser_${tableId}`;
      const items = config.columns.map(c => `
        <label class="col-chooser-item">
          <input type="checkbox" ${vis[c.id] ? 'checked' : ''}
            onchange="setColVisible('${tableId}','${c.id}',this.checked);updateColChooserBtn('${tableId}')">
          ${c.label}
        </label>`).join('');
      return `
        <div class="col-chooser-wrap" id="${id}_wrap">
          <button class="col-chooser-btn" onclick="toggleColChooser('${tableId}')" title="Show/hide columns" aria-haspopup="true" aria-expanded="false" id="${id}_btn">
            <i class="fa-regular fa-table-columns"></i> Columns
          </button>
          <div class="col-chooser-dropdown" id="${id}_dd" role="menu" aria-label="Column visibility">
            <div class="col-chooser-header">Show / Hide Columns</div>
            ${items}
          </div>
        </div>`;
    }

    function toggleColChooser(tableId) {
      const dd = document.getElementById(`colChooser_${tableId}_dd`);
      const btn = document.getElementById(`colChooser_${tableId}_btn`);
      if (!dd) return;
      const isOpen = dd.classList.toggle('open');
      if (btn) btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      if (isOpen) {
        // Close on outside click
        setTimeout(() => {
          document.addEventListener('click', function _close(e) {
            const wrap = document.getElementById(`colChooser_${tableId}_wrap`);
            if (wrap && !wrap.contains(e.target)) {
              dd.classList.remove('open');
              if (btn) btn.setAttribute('aria-expanded', 'false');
              document.removeEventListener('click', _close);
            }
          });
        }, 0);
      }
    }

    function updateColChooserBtn(tableId) {
      const vis = getVisibleCols(tableId);
      const config = COL_CONFIGS[tableId];
      if (!config) return;
      const hidden = config.columns.filter(c => !vis[c.id]).length;
      const btn = document.getElementById(`colChooser_${tableId}_btn`);
      if (btn) {
        btn.innerHTML = hidden > 0
          ? `<i class="fa-regular fa-table-columns"></i> Columns <span style="background:var(--accent-600);color:white;border-radius:999px;padding:0 5px;font-size:10px;">${hidden}</span>`
          : `<i class="fa-regular fa-table-columns"></i> Columns`;
      }
    }

    // ===== INLINE FORM MICRO-INTERACTIONS =====
    // Attach live validation feedback to any input with data-validate attribute.
    // data-validate values: "required", "number", "positive-number", "order-no", "plate"
    function liveValidate(input) {
      const rule = input.dataset.validate;
      const hintId = input.dataset.hint;
      const hint = hintId ? document.getElementById(hintId) : input.parentElement?.querySelector('.field-hint');
      if (!hint) return;

      const v = input.value.trim();

      const setHint = (msg, state) => {
        hint.textContent = msg;
        hint.className = 'field-hint' + (state ? ' ' + state : '');
      };

      if (!v) { setHint('', ''); input.style.borderColor = ''; return; }

      switch (rule) {
        case 'required':
          if (v.length >= 1) { setHint('✓ Looks good', 'success'); input.style.borderColor = 'var(--status-success)'; }
          break;
        case 'order-no': {
          const exists = DB.regions[DB.currentRegion]?.orders[v.toUpperCase()];
          if (exists) { setHint('⚠ Order number already exists', 'warning'); input.style.borderColor = 'var(--status-warning)'; }
          else if (v.length >= 2) { setHint('✓ Available', 'success'); input.style.borderColor = 'var(--status-success)'; }
          break;
        }
        case 'positive-number': {
          const n = parseFloat(v);
          if (isNaN(n) || n <= 0) { setHint('Enter a number greater than 0', 'error'); input.style.borderColor = 'var(--status-danger)'; }
          else { setHint(`✓ ${n.toLocaleString()} litres`, 'success'); input.style.borderColor = 'var(--status-success)'; }
          break;
        }
        case 'number': {
          const n = parseFloat(v);
          if (isNaN(n)) { setHint('Must be a valid number', 'error'); input.style.borderColor = 'var(--status-danger)'; }
          else { setHint(`✓ ${n.toLocaleString()}`, 'success'); input.style.borderColor = 'var(--status-success)'; }
          break;
        }
        case 'plate':
          if (v.length >= 3) { setHint('✓ Vehicle plate recorded', 'success'); input.style.borderColor = 'var(--status-success)'; }
          else { setHint('Enter at least 3 characters', 'warning'); input.style.borderColor = 'var(--status-warning)'; }
          break;
        case 'alloc-amount': {
          const orderNo = document.getElementById('allocOrder')?.value;
          const techName = document.getElementById('allocTech')?.value;
          const order = DB.regions[DB.currentRegion]?.orders[orderNo];
          const n = parseFloat(v);
          if (isNaN(n) || n <= 0) {
            setHint('Enter a positive amount', 'error');
            input.style.borderColor = 'var(--status-danger)';
          } else if (order) {
            const otherTotal = Object.entries(order.allocations || {})
              .filter(([t]) => t !== techName)
              .reduce((s, [, amt]) => s + amt, 0);
            const remaining = order.totalLiters - otherTotal;
            if (n > remaining) {
              setHint(`⚠ Exceeds available ${remaining}L`, 'warning');
              input.style.borderColor = 'var(--status-warning)';
            } else {
              setHint(`✓ ${n}L of ${remaining}L available`, 'success');
              input.style.borderColor = 'var(--status-success)';
            }
          } else {
            setHint(`✓ ${n} litres`, 'success');
            input.style.borderColor = 'var(--status-success)';
          }
          break;
        }
        default:
          break;
      }
    }

    // Clear all validation styling when a form resets
    function clearValidation(formSelector) {
      document.querySelectorAll(formSelector + ' .field-hint').forEach(h => { h.textContent = ''; h.className = 'field-hint'; });
      document.querySelectorAll(formSelector + ' input').forEach(i => { i.style.borderColor = ''; });
    }
    function toggleSidebar() {
      const sidebar = document.getElementById('sidebar');
      const main = document.getElementById('mainContent');
      const icon = document.getElementById('sidebarToggleIcon');
      const btn = document.getElementById('sidebarToggleBtn');
      if (!sidebar) return;
      sidebar.classList.toggle('collapsed');
      main?.classList.toggle('expanded');
      const isCollapsed = sidebar.classList.contains('collapsed');
      if (icon) icon.className = isCollapsed ? 'fa-regular fa-chevron-right' : 'fa-regular fa-chevron-left';
      if (btn) {
        const span = btn.querySelector('span');
        if (span) span.textContent = isCollapsed ? 'Expand' : 'Collapse';
      }
      localStorage.setItem('ccs_sidebar_collapsed', isCollapsed ? '1' : '0');
    }

    // Start the application
    init();
  </script>
</body>
</html>