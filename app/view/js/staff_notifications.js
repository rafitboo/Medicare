document.addEventListener('DOMContentLoaded', function() {
    // Handle individual notification mark as read
    document.querySelectorAll('.mark-read-btn').forEach(button => {
        button.addEventListener('click', function() {
            const notificationId = this.dataset.notificationId;
            markAsRead(notificationId);
        });
    });

    // Handle mark all as read
    document.getElementById('markAllReadBtn').addEventListener('click', markAllAsRead);
});

function markAsRead(notificationId) {
    fetch(`/admin_chat/notifications/${notificationId}/mark-read`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const notificationItem = document.querySelector(`[data-notification-id="${notificationId}"]`);
            if (notificationItem) {
                notificationItem.classList.remove('unread');
                const markReadBtn = notificationItem.querySelector('.mark-read-btn');
                if (markReadBtn) {
                    markReadBtn.remove();
                }
            }
        }
    })
    .catch(error => {
        console.error('Error marking notification as read:', error);
    });
}

function markAllAsRead() {
    fetch('/admin_chat/notifications/mark-all-read', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Remove unread class from all notifications
            document.querySelectorAll('.notification-item.unread').forEach(item => {
                item.classList.remove('unread');
                const markReadBtn = item.querySelector('.mark-read-btn');
                if (markReadBtn) {
                    markReadBtn.remove();
                }
            });
        }
    })
    .catch(error => {
        console.error('Error marking all notifications as read:', error);
    });
} 