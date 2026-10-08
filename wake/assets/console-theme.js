/* Console follows the device, including changes while the page stays open. */
(() => {
  const root = document.documentElement;
  const preference = window.matchMedia('(prefers-color-scheme: dark)');
  root.dataset.consoleTheme = 'system';
  const apply = () => {
    const dark = preference.matches;
    root.dataset.theme = dark ? 'dark' : 'light';
    root.style.colorScheme = root.dataset.theme;
    const chrome = document.querySelector('meta[name="theme-color"]');
    if (chrome) chrome.content = dark ? '#01040a' : '#f3f6fb';
    window.dispatchEvent(new CustomEvent('wake-theme-change', {detail: {theme: root.dataset.theme}}));
  };
  apply();
  if (preference.addEventListener) preference.addEventListener('change', apply);
  else preference.addListener(apply);
})();
