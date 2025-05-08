document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.profile-form');
    const newPassword = document.getElementById('new_password');
    const confirmPassword = document.getElementById('confirm_password');

    // Password matching validation
    function validatePasswords() {
        if (newPassword.value !== confirmPassword.value) {
            confirmPassword.setCustomValidity('Passwords do not match');
        } else {
            confirmPassword.setCustomValidity('');
        }
    }

    newPassword.addEventListener('change', validatePasswords);
    confirmPassword.addEventListener('keyup', validatePasswords);

    // Form submission validation
    form.addEventListener('submit', function(e) {
        if (!form.checkValidity()) {
            e.preventDefault();
            alert('Please fill in all required fields correctly');
        }
    });

    // Add focus effects to form inputs
    const inputs = form.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });

        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
        });
    });
}); 