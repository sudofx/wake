/*
 * WAKE✳︎ MAINTAINER NOTE
 *
 * Optional zero-cycle/hidden-data presentation. This hides rendered data only; it never deletes or alters durable state.
 * The shared data loader in index.html applies the projection before browser views consume the record.
 */

(() => {
  'use strict';
  const storageKey = 'wake-hide-current-data';
  const toggle = document.getElementById('data-visibility-toggle');
  const note = document.getElementById('data-visibility-note');
  if (!toggle) return;

  let hidden = false;
  try { hidden = localStorage.getItem(storageKey) === '1'; } catch {}

  toggle.checked = hidden;
  toggle.setAttribute('aria-checked', String(hidden));
  if (note) note.textContent = hidden ? 'CURRENT DATA HIDDEN · ZERO-CYCLE VIEW' : 'CURRENT DATA VISIBLE';

  toggle.addEventListener('change', () => {
    try {
      if (toggle.checked) localStorage.setItem(storageKey, '1');
      else localStorage.removeItem(storageKey);
    } catch {}
    location.reload();
  });
})();
