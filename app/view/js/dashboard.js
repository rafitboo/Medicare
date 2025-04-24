document.addEventListener('DOMContentLoaded', function() {
    // Search functionality
    const searchInput = document.getElementById('medicine-search');
    const medicineCards = document.querySelectorAll('.medicine-card');

    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        medicineCards.forEach(card => {
            const medicineName = card.querySelector('h3').textContent.toLowerCase();
            if (medicineName.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });

    // Sorting functionality
    const sortSelect = document.getElementById('sort-by');
    sortSelect.addEventListener('change', function() {
        const sortValue = this.value;
        const sortedCards = Array.from(medicineCards).sort((a, b) => {
            const aPrice = parseFloat(a.dataset.price);
            const bPrice = parseFloat(b.dataset.price);
            const aName = a.querySelector('h3').textContent;
            const bName = b.querySelector('h3').textContent;

            if (sortValue === 'name-asc') {
                return aName.localeCompare(bName);
            } else if (sortValue === 'name-desc') {
                return bName.localeCompare(aName);
            } else if (sortValue === 'price-asc') {
                return aPrice - bPrice;
            } else if (sortValue === 'price-desc') {
                return bPrice - aPrice;
            }
            return 0;
        });

        const container = document.getElementById('medicine-container');
        container.innerHTML = ''; // Clear existing cards
        sortedCards.forEach(card => container.appendChild(card)); // Append sorted cards
    });

    // Category filtering functionality
    const filterSelect = document.getElementById('filter-category');
    filterSelect.addEventListener('change', function() {
        const selectedCategory = this.value;
        medicineCards.forEach(card => {
            const cardCategory = card.dataset.category; // Assuming you have data-category attribute
            if (selectedCategory === 'all' || cardCategory === selectedCategory) {
                card.style.display = 'block'; // Show card
            } else {
                card.style.display = 'none'; // Hide card
            }
        });
    });

    // Add to Cart functionality
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const medicineId = this.dataset.id;
            const quantityInput = this.closest('.medicine-card').querySelector('.quantity-input');
            const quantity = quantityInput.value;

            fetch('/cart/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ medicine_id: medicineId, quantity: quantity })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.message); // Show error message
                } else {
                    alert('Item added to cart successfully!'); // Show success message
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});