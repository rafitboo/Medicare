document.addEventListener('DOMContentLoaded', function() {
    // Quantity buttons
    document.querySelectorAll('.quantity-btn').forEach(button => {
        button.addEventListener('click', function() {
            const form = this.closest('form');
            const input = form.querySelector('.quantity-input');
            const maxStock = parseInt(input.getAttribute('data-max-stock'));
            const current = parseInt(input.value);
            
            if (this.classList.contains('minus')) {
                if (current > 1) {
                    input.value = current - 1;
                    form.submit();
                }
            } 
            else if (this.classList.contains('plus')) {
                if (current < maxStock) {
                    input.value = current + 1;
                    form.submit();
                } else {
                    alert(`Only ${maxStock} items available in stock!`);
                }
            }
        });
    });

    // Direct input changes
    document.querySelectorAll('.quantity-input').forEach(input => {
        input.addEventListener('change', function() {
            const maxStock = parseInt(this.getAttribute('data-max-stock'));
            if (parseInt(this.value) > maxStock) {
                alert(`Only ${maxStock} items available in stock!`);
                this.value = maxStock;
            }
            this.closest('form').submit();
        });
    });
});