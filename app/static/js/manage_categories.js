document.addEventListener('DOMContentLoaded', function () {
    // Toggle form visibility
    const toggleFormBtn = document.getElementById('toggle-form-btn');
    const cancelFormBtn = document.querySelector('.btn-cancel');
    const categoryFormContainer = document.getElementById('category-form-container');

    toggleFormBtn.addEventListener('click', function () {
        categoryFormContainer.style.display = 'block';
    });

    cancelFormBtn.addEventListener('click', function () {
        categoryFormContainer.style.display = 'none';
    });

    // Search functionality
    const searchInput = document.getElementById('search-category');
    searchInput.addEventListener('input', function () {
        const searchTerm = this.value.toLowerCase();
        const categoryItems = document.querySelectorAll('.category-item');

        categoryItems.forEach(item => {
            const categoryName = item.getAttribute('data-name').toLowerCase();
            item.style.display = categoryName.includes(searchTerm) ? 'flex' : 'none';
        });
    });
});