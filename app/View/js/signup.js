document.addEventListener('DOMContentLoaded', function() {
    const signupForm = document.getElementById('signupForm');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const togglePasswordButtons = document.querySelectorAll('.toggle-password');
    const strengthMeter = document.querySelector('.strength-meter');
    const strengthText = document.querySelector('.strength-text');
    
    // Password visibility toggle
    togglePasswordButtons.forEach(button => {
        button.addEventListener('click', function() {
            const input = this.parentElement.querySelector('input');
            if (input.type === 'password') {
                input.type = 'text';
                this.textContent = '🙈';
            } else {
                input.type = 'password';
                this.textContent = '👁️';
            }
        });
    });
    
    // Password strength indicator
    passwordInput.addEventListener('input', function() {
        const password = this.value;
        const strength = calculatePasswordStrength(password);
        
        updateStrengthIndicator(strength);
    });
    
    function calculatePasswordStrength(password) {
        let strength = 0;
        
        // Length check
        if (password.length >= 8) strength += 1;
        if (password.length >= 12) strength += 1;
        
        // Character variety
        if (/[A-Z]/.test(password)) strength += 1; // Uppercase
        if (/[a-z]/.test(password)) strength += 1; // Lowercase
        if (/[0-9]/.test(password)) strength += 1; // Numbers
        if (/[^A-Za-z0-9]/.test(password)) strength += 1; // Special chars
        
        return Math.min(strength, 5); // Max strength is 5
    }
    
    function updateStrengthIndicator(strength) {
        const percentage = (strength / 5) * 100;
        strengthMeter.style.width = `${percentage}%`;
        
        // Update color and text based on strength
        if (strength <= 1) {
            strengthMeter.style.backgroundColor = 'var(--error-color)';
            strengthText.textContent = 'Very Weak';
            strengthText.style.color = 'var(--error-color)';
        } else if (strength <= 2) {
            strengthMeter.style.backgroundColor = "var(--warning-color)";
            strengthText.textContent = 'Weak';
            strengthText.style.color = 'var(--warning-color)';
        } else if (strength <= 3) {
            strengthMeter.style.backgroundColor = '#d69e2e';
            strengthText.textContent = 'Moderate';
            strengthText.style.color = '#d69e2e';
        } else if (strength <= 4) {
            strengthMeter.style.backgroundColor = '#38a169';
            strengthText.textContent = 'Strong';
            strengthText.style.color = '#38a169';
        } else {
            strengthMeter.style.backgroundColor = '#2f855a';
            strengthText.textContent = 'Very Strong';
            strengthText.style.color = '#2f855a';
        }
    }
    
    // Form validation
    signupForm.addEventListener('submit', function(e) {
        e.preventDefault();
        let isValid = true;
        
        // Reset error messages
        document.querySelectorAll('.error-message').forEach(el => {
            el.textContent = '';
        });
        
        // Name validation
        const nameInput = document.getElementById('fullName');
        if (nameInput.value.trim() === '') {
            document.getElementById('nameError').textContent = 'Full name is required';
            isValid = false;
        } else if (nameInput.value.trim().length < 3) {
            document.getElementById('nameError').textContent = 'Name must be at least 3 characters';
            isValid = false;
        }
        
        // Email validation
        const emailInput = document.getElementById('email');
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (emailInput.value.trim() === '') {
            document.getElementById('emailError').textContent = 'Email is required';
            isValid = false;
        } else if (!emailRegex.test(emailInput.value)) {
            document.getElementById('emailError').textContent = 'Please enter a valid email';
            isValid = false;
        }
        
        // Phone validation
        const phoneInput = document.getElementById('phone');
        const phoneRegex = /^[0-9]{10,15}$/;
        if (phoneInput.value.trim() === '') {
            document.getElementById('phoneError').textContent = 'Phone number is required';
            isValid = false;
        } else if (!phoneRegex.test(phoneInput.value)) {
            document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
            isValid = false;
        }
        
        // Password validation
        if (passwordInput.value === '') {
            document.getElementById('passwordError').textContent = 'Password is required';
            isValid = false;
        } else if (passwordInput.value.length < 8) {
            document.getElementById('passwordError').textContent = 'Password must be at least 8 characters';
            isValid = false;
        }
        
        // Confirm password validation
        if (confirmPasswordInput.value === '') {
            document.getElementById('confirmPasswordError').textContent = 'Please confirm your password';
            isValid = false;
        } else if (confirmPasswordInput.value !== passwordInput.value) {
            document.getElementById('confirmPasswordError').textContent = 'Passwords do not match';
            isValid = false;
        }
        
        // Terms checkbox validation
        const termsCheckbox = document.getElementById('terms');
        if (!termsCheckbox.checked) {
            document.getElementById('termsError').textContent = 'You must accept the terms and conditions';
            isValid = false;
        }
        
        // If form is valid, submit it
        if (isValid) {
            signupForm.submit(); // Actually submit the form to the server
        }
    });
    
    // Real-time password match validation
    confirmPasswordInput.addEventListener('input', function() {
        const errorElement = document.getElementById('confirmPasswordError');
        if (this.value !== passwordInput.value) {
            errorElement.textContent = 'Passwords do not match';
        } else {
            errorElement.textContent = '';
        }
    });
});