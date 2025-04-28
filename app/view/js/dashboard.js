document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('medicine-search');
    const sortSelect = document.getElementById('sort-by');
    const filterSelect = document.getElementById('filter-category');
    const container = document.getElementById('medicine-container');
    const medicineCards = Array.from(document.querySelectorAll('.medicine-card'));

    let currentSearch = '';
    let currentCategory = 'all';
    let currentSort = sortSelect ? sortSelect.value : 'name-asc';

    function updateDisplay() {
        // Filter and search
        let visibleCards = medicineCards.filter(card => {
            const name = card.querySelector('h3').textContent.toLowerCase();
            const category = card.dataset.category;
            const matchesSearch = name.includes(currentSearch);
            const matchesCategory = (currentCategory === 'all' || category === currentCategory);
            return matchesSearch && matchesCategory;
        });

        // Sort
        visibleCards.sort((a, b) => {
            const aPrice = parseFloat(a.dataset.price);
            const bPrice = parseFloat(b.dataset.price);
            const aName = a.querySelector('h3').textContent;
            const bName = b.querySelector('h3').textContent;

            switch(currentSort) {
                case 'name-asc': return aName.localeCompare(bName);
                case 'name-desc': return bName.localeCompare(aName);
                case 'price-asc': return aPrice - bPrice;
                case 'price-desc': return bPrice - aPrice;
                default: return 0;
            }
        });

        // Hide all, then show only visibleCards in order
        medicineCards.forEach(card => card.style.display = 'none');
        visibleCards.forEach(card => {
            card.style.display = 'block';
            container.appendChild(card); // reorder in DOM
        });
    }

    if (searchInput) {
        searchInput.addEventListener('input', function() {
            currentSearch = this.value.toLowerCase();
            updateDisplay();
        });
    }

    if (filterSelect) {
        filterSelect.addEventListener('change', function() {
            currentCategory = this.value;
            updateDisplay();
        });
    }

    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            currentSort = this.value;
            updateDisplay();
        });
    }

    // Initial display
    updateDisplay();
});