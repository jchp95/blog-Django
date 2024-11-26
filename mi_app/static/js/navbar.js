const mobileMenu = document.getElementById('mobile-menu');
const navbarList = document.querySelector('.navbar-list');

mobileMenu.addEventListener('click', () => {
    navbarList.classList.toggle('active');
});