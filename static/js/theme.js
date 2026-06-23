document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.getElementById('theme-toggle');
  const iconElement = themeToggle.querySelector('i');

  // Theme is already set in base.html <head>, just need to update icon
  const currentTheme = document.documentElement.getAttribute('data-theme');
  updateIcon(currentTheme);

  themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateIcon(newTheme);
  });

  function updateIcon(theme) {
    if (theme === 'dark') {
      iconElement.className = 'fas fa-sun'; // Show sun icon in dark mode to switch to light
    } else {
      iconElement.className = 'fas fa-moon'; // Show moon icon in light mode to switch to dark
    }
  }
});
