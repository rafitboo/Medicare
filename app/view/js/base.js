document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu functionality
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mainNav = document.querySelector('.main-nav');
    const authButtons = document.querySelector('.auth-buttons');
    
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function() {
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            
            // Toggle menu visibility
            if (mainNav) mainNav.style.display = isExpanded ? 'none' : 'flex';
            if (authButtons) authButtons.style.display = isExpanded ? 'none' : 'flex';
            
            // Update button state
            this.setAttribute('aria-expanded', !isExpanded);
            this.innerHTML = isExpanded ? '<i class="fas fa-bars"></i>' : '<i class="fas fa-times"></i>';
        });
    }
    
    // Add active class to current page nav item
    const navLinks = document.querySelectorAll('.nav-link');
    const currentUrl = window.location.pathname;
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentUrl) {
            link.classList.add('active');
            link.style.color = 'var(--primary-color)';
            link.style.fontWeight = '600';
        }
    });
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Footer year update
    const yearElement = document.querySelector('.footer-bottom p');
    if (yearElement) {
        const currentYear = new Date().getFullYear();
        yearElement.innerHTML = yearElement.innerHTML.replace('2023', currentYear);
    }
    
    // Flash message handling
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        // Show message with animation
        message.style.display = 'flex';
        message.style.animation = 'slideDown 0.3s ease-out';
        
        // Auto-hide after 5 seconds
        setTimeout(() => {
            message.style.animation = 'slideUp 0.3s ease-out';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
        
        // Handle close button
        const closeBtn = message.querySelector('.flash-close-btn');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                message.style.animation = 'slideUp 0.3s ease-out';
                setTimeout(() => {
                    message.remove();
                }, 300);
            });
        }
    });
});

// Add slideUp animation to CSS via JavaScript
const style = document.createElement('style');
style.textContent = `
    @keyframes slideUp {
        from {
            transform: translateY(0);
            opacity: 1;
        }
        to {
            transform: translateY(-20px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
document.head.appendChild(style);