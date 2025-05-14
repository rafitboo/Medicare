document.addEventListener('DOMContentLoaded', function() {
    const paymentForm = document.getElementById('payment-form');
    const paymentButtons = document.querySelectorAll('.payment-method-btn');
    const bkashFields = document.getElementById('bkash-fields');
    const codSubmitBtn = document.getElementById('cod-submit-btn');
    const bkashSubmitBtn = document.getElementById('bkash-submit-btn');
    const selectedPaymentMethod = document.getElementById('selected_payment_method');

    // Handle payment method selection
    paymentButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            paymentButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            
            const method = this.dataset.method;
            console.log('Selected payment method:', method); // Debug log

            // Set the hidden input value
            selectedPaymentMethod.value = method;

            if (method === 'cod') {
                bkashFields.style.display = 'none';
                codSubmitBtn.style.display = 'block';
                bkashSubmitBtn.style.display = 'none';
            } else {
                bkashFields.style.display = 'block';
                codSubmitBtn.style.display = 'none';
                bkashSubmitBtn.style.display = 'block';
            }
        });
    });

    // Handle form submission
    paymentForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        console.log('Form submitted'); // Debug log

        // Get the payment method directly from hidden input
        const paymentMethod = selectedPaymentMethod.value;
        console.log('Payment method at submission:', paymentMethod); // Debug log

        if (!paymentMethod) {
            alert('Please select a payment method');
            return;
        }

        try {
            const response = await fetch('/place_order', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    payment_method: paymentMethod,
                    bkash_number: document.getElementById('bkash_number')?.value || null,
                    transaction_id: document.getElementById('transaction_id')?.value || null
                })
            });

            const result = await response.json();

            if (result.success) {
                alert('Order placed successfully!');
                window.location.href = '/dashboard';
            } else {
                alert(result.error || 'Error placing order');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error processing order. Please try again.');
        }
    });
});