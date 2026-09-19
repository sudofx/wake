/*
 * WAKE✳︎ MAINTAINER NOTE
 *
 * Optional zero-cycle/hidden-data presentation. This hides rendered data only; it never deletes or alters durable state.
 *
 * Comments should preserve the boundary between presentation and the canonical durable record.
 */

(() => {
  'use strict';
  const storageKey = 'wake-hide-current-data';
  const dataNode = document.getElementById('wake-data');
  const toggle = document.getElementById('data-visibility-toggle');
  const note = document.getElementById('data-visibility-note');
  if (!dataNode || !toggle) return;

  let hidden = false;
  try { hidden = localStorage.getItem(storageKey) === '1'; } catch {}

  if (hidden) {
    const data = JSON.parse(dataNode.textContent);
    const state = data.state || {};
    Object.assign(state, {
      version: 0,
      beliefs: {},
      commitments: {},
      projects: {},
      notebooks: {},
      invocations: {},
      evidence: {},
      journal: [],
      research: {},
      posts: {}
    });
    data.events = [];
    data.wake_status = {};
    data.operation = null;
    dataNode.textContent = JSON.stringify(data).replace(/</g, '\\u003c');
  }

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