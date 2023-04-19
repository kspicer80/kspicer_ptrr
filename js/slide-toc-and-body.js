const body = document.querySelector('body');
const nav = document.querySelector('nav');

nav.addEventListener('mouseenter', () => {
  body.classList.add('nav-open');
  nav.classList.add('open');
});

nav.addEventListener('mouseleave', () => {
  body.classList.remove('nav-open');
  nav.classList.remove('open');
});
