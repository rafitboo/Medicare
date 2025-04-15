document.addEventListener('DOMContentLoaded', function () {
    // Toggle form visibility
    const toggleFormBtn = document.getElementById('toggle-form-btn');
    const cancelFormBtn = document.querySelector('.btn-cancel');
    const medicineFormContainer = document.getElementById('medicine-form-container');

    toggleFormBtn.addEventListener('click', function () {
        medicineFormContainer.style.display = 'block';
    });

    cancelFormBtn.addEventListener('click', function () {
        medicineFormContainer.style.display = 'none';
    });

    // Search functionality
    const searchInput = document.getElementById('search-medicine');
    searchInput.addEventListener('input', function () {
        const searchTerm = this.value.toLowerCase();
        const medicineItems = document.querySelectorAll('.medicine-item');

        medicineItems.forEach(item => {
            const medicineName = item.getAttribute('data-name').toLowerCase();
            item.style.display = medicineName.includes(searchTerm) ? 'flex' : 'none';
        });
    });

    // Stock filter functionality
    const stockFilter = document.getElementById('filter-stock');
    stockFilter.addEventListener('change', function () {
        const filterValue = this.value;
        const medicineItems = document.querySelectorAll('.medicine-item');

        medicineItems.forEach(item => {
            const stock = parseInt(item.getAttribute('data-stock'));

            switch (filterValue) {
                case 'all':
                    item.style.display = 'flex';
                    break;
                case 'low':
                    item.style.display = stock < 10 && stock > 0 ? 'flex' : 'none';
                    break;
                case 'out':
                    item.style.display = stock === 0 ? 'flex' : 'none';
                    break;
            }
        });
    });
});