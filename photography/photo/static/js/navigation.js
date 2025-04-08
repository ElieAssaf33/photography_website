document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle');
    const navContainer = document.querySelector('.nav-container');
    const portfolioDropdown = document.querySelector('.portfolio-dropdown');

    // Toggle mobile menu
    menuToggle.addEventListener('click', () => {
        menuToggle.classList.toggle('active');
        navContainer.classList.toggle('active');
    });

    // Handle portfolio dropdown on mobile
    if (window.innerWidth <= 768) {
        portfolioDropdown.addEventListener('click', (e) => {
            if (e.target.closest('.portfolio-dropdown')) {
                portfolioDropdown.classList.toggle('active');
            }
        });
    }

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.nav-container') && !e.target.closest('.menu-toggle')) {
            menuToggle.classList.remove('active');
            navContainer.classList.remove('active');
            portfolioDropdown.classList.remove('active');
        }
    });

    // Update dropdown behavior on window resize
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            portfolioDropdown.classList.remove('active');
            menuToggle.classList.remove('active');
            navContainer.classList.remove('active');
        }
    });
});
