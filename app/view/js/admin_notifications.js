document.addEventListener('DOMContentLoaded', function() {
    // Handle single notification mark as read
    document.querySelectorAll('.mark-read-btn').forEach(button => {
        button.addEventListener('click', function() {
            const notificationId = this.getAttribute('data-notification-id');
            const notificationItem = this.closest('.notification-item');
            
            // Visual feedback before form submission
            this.disabled = true;
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Marking...';
            notificationItem.style.opacity = '0.7';
            
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = `/admin/notifications/${notificationId}/mark-read`;
            
            document.body.appendChild(form);
            form.submit();
        });
    });

    // Handle mark all as read
    const markAllBtn = document.getElementById('markAllReadBtn');
    if (markAllBtn) {
        markAllBtn.addEventListener('click', function() {
            // Visual feedback before form submission
            this.disabled = true;
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Marking All...';
            
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/admin/notifications/mark-all-read';
            
            document.body.appendChild(form);
            form.submit();
        });
    }

    // Optional: Click anywhere on notification to mark as read
    document.querySelectorAll('.notification-item.unread').forEach(item => {
        item.addEventListener('click', function(e) {
            // Only trigger if not clicking a button or link
            if (!e.target.closest('button') && !e.target.closest('a')) {
                const markReadBtn = this.querySelector('.mark-read-btn');
                if (markReadBtn) markReadBtn.click();
            }
        });
    });

    // Add hover effects for unread notifications
    document.querySelectorAll('.notification-item.unread').forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.backgroundColor = 'rgba(0, 123, 255, 0.05)';
            this.style.cursor = 'pointer';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '';
        });
    });

    // Add transition effects for notification items
    document.querySelectorAll('.notification-item').forEach(item => {
        item.style.transition = 'all 0.3s ease';
    });
});