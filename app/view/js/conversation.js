document.addEventListener('DOMContentLoaded', function() {
    const messagesContainer = document.getElementById('messagesContainer');
    const textarea = document.querySelector('.form-control');
    const form = document.querySelector('.message-form');

    function scrollToBottom() {
        if (messagesContainer) {
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
    }

    scrollToBottom();

    if (textarea) {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });

        textarea.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey && form) {
                e.preventDefault();
                form.submit();
            }
        });
    }

    if (messagesContainer) {
        const observer = new MutationObserver(scrollToBottom);
        observer.observe(messagesContainer, { childList: true, subtree: true });
    }

    window.addEventListener('resize', scrollToBottom);
    setTimeout(scrollToBottom, 300);
});