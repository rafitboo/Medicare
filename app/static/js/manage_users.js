document.addEventListener('DOMContentLoaded', function () {
    // Toggle form visibility
    const toggleFormBtn = document.getElementById('toggle-form-btn');
    const cancelFormBtn = document.querySelector('.btn-cancel');
    const userFormContainer = document.getElementById('user-form-container');

    toggleFormBtn.addEventListener('click', function () {
        userFormContainer.style.display = 'block';
    });

    cancelFormBtn.addEventListener('click', function () {
        userFormContainer.style.display = 'none';
    });

    // Search functionality
    const searchInput = document.getElementById('search-user');
    searchInput.addEventListener('input', function () {
        const searchTerm = this.value.toLowerCase();
        const userItems = document.querySelectorAll('.user-item');

        userItems.forEach(item => {
            const userName = item.getAttribute('data-name').toLowerCase();
            item.style.display = userName.includes(searchTerm) ? 'flex' : 'none';
        });
    });

    // Role filter functionality (updated for customer/admin only)
    const roleFilter = document.getElementById('filter-role');
    roleFilter.addEventListener('change', function () {
        const filterValue = this.value;
        const userItems = document.querySelectorAll('.user-item');

        userItems.forEach(item => {
            const role = item.getAttribute('data-role');

            switch (filterValue) {
                case 'all':
                    item.style.display = 'flex';
                    break;
                case 'customer':
                    item.style.display = role === 'customer' ? 'flex' : 'none';
                    break;
                case 'admin':
                    item.style.display = role === 'admin' ? 'flex' : 'none';
                    break;
                case 'staff':
                    item.style.display = role === 'staff' ? 'flex' : 'none';
                    break;
            }
        });
    });
});