document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const messagesContainer = document.getElementById('messagesContainer');
    const textarea = document.querySelector('.form-control');
    const sendButton = document.querySelector('.send-button');
    const form = document.querySelector('.message-form');

    // Auto-scroll to bottom on load
    function scrollToBottom() {
        if (messagesContainer) {
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
    }

    // Auto-resize textarea
    if (textarea) {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
            
            if (this.scrollHeight > 120) {
                this.style.overflowY = 'auto';
            } else {
                this.style.overflowY = 'hidden';
            }
        });

        // Handle Enter key (submit on Enter, new line on Shift+Enter)
        textarea.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                form.dispatchEvent(new Event('submit'));
            }
        });
    }

    // Form submission handler
    if (form) {
        form.addEventListener('submit', function(e) {
            if (sendButton) {
                sendButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
                sendButton.disabled = true;
            }
            
            // In a real app, you would have AJAX submission here
            // For now, we'll just simulate a successful send
            setTimeout(() => {
                if (sendButton) {
                    sendButton.innerHTML = '<i class="fas fa-paper-plane"></i>';
                    sendButton.disabled = false;
                }
                scrollToBottom();
            }, 500);
        });
    }

    // Initial scroll to bottom
    scrollToBottom();

    // Observe for new messages (for real-time updates)
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length) {
                scrollToBottom();
            }
        });
    });

    if (messagesContainer) {
        observer.observe(messagesContainer, {
            childList: true,
            subtree: true
        });
    }

    // Keep scroll position when window resizes
    window.addEventListener('resize', scrollToBottom);
});