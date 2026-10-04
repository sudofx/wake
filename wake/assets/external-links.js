/* Every off-site destination opens separately; covers later rendered records. */
(() => {
  const apply = link => {
    try {
      const url = new URL(link.getAttribute('href'), location.href);
      if (['http:', 'https:'].includes(url.protocol) && url.origin !== location.origin) {
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
      }
    } catch { /* A missing or malformed destination remains inert. */ }
  };
  const scan = root => {
    if (root.matches?.('a[href]')) apply(root);
    root.querySelectorAll?.('a[href]').forEach(apply);
  };
  scan(document);
  new MutationObserver(records => {
    const roots = new Set();
    records.forEach(record => {
      if (record.type === 'attributes') roots.add(record.target);
      else record.addedNodes.forEach(node => { if (node.nodeType === 1) roots.add(node); });
    });
    roots.forEach(scan);
  }).observe(document.body, {subtree: true, childList: true, attributes: true, attributeFilter: ['href']});
})();
