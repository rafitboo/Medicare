document.addEventListener('DOMContentLoaded', function() {
    // Search functionality
    const searchInput = document.getElementById('messageSearch');
    const conversationItems = document.querySelectorAll('.conversation-item');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            
            conversationItems.forEach(item => {
                const customerName = item.querySelector('h5').textContent.toLowerCase();
                const previewText = item.querySelector('.preview-text').textContent.toLowerCase();
                
                if (customerName.includes(searchTerm) || previewText.includes(searchTerm)) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }
    
    // Filter functionality
    const filterSelect = document.getElementById('messageFilter');
    
    if (filterSelect) {
        filterSelect.addEventListener('change', function() {
            const filterValue = this.value;
            
            conversationItems.forEach(item => {
                const isUnread = item.classList.contains('unread');
                
                switch(filterValue) {
                    case 'all':
                        item.style.display = 'flex';
                        break;
                    case 'unread':
                        item.style.display = isUnread ? 'flex' : 'none';
                        break;
                    case 'recent':
                        // Sort by timestamp would be handled server-side
                        item.style.display = 'flex';
                        break;
                }
            });
        });
    }
    
    // Add hover effects
    conversationItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#f5f5f5';
        });
        
        item.addEventListener('mouseleave', function() {
            if (!this.classList.contains('unread')) {
                this.style.backgroundColor = '#fff';
            } else {
                this.style.backgroundColor = '#f8f9fa';
            }
        });
    });
});