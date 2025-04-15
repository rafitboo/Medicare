document.addEventListener('DOMContentLoaded', function() {
    // Update stock status badge dynamically
    const stockInput = document.getElementById('stock');
    const stockStatus = document.getElementById('stock-status');
    
    if (stockInput && stockStatus) {
        stockInput.addEventListener('input', function() {
            const stockValue = parseInt(this.value) || 0;
            let statusHtml = '';
            
            if (stockValue === 0) {
                statusHtml = '<span class="status-badge out-of-stock">Out of Stock</span>';
            } else if (stockValue < 10) {
                statusHtml = '<span class="status-badge low-stock">Low Stock</span>';
            } else {
                statusHtml = '<span class="status-badge in-stock">In Stock</span>';
            }
            
            stockStatus.innerHTML = statusHtml;
        });
    }
    
    // Price input formatting
    const priceInput = document.getElementById('price');
    if (priceInput) {
        priceInput.addEventListener('blur', function() {
            const value = parseFloat(this.value);
            if (!isNaN(value)) {
                this.value = value.toFixed(2);
            }
        });
    }
    
    // Form submission handling
    const medicineForm = document.querySelector('.edit-medicine-form');
    if (medicineForm) {
        medicineForm.addEventListener('submit', function(e) {
            // You can add form validation here if needed
            console.log('Form submitted');
            // In a real application, you would prevent default and use fetch API
            // to submit the form asynchronously
        });
    }
    
    // Initialize tooltips (if you're using a library like Bootstrap)
    // $('[data-toggle="tooltip"]').tooltip();
});