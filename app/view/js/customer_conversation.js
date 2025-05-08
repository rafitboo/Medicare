document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('messagesContainer');
    
    function scrollToBottom() {
        container.scrollTop = container.scrollHeight;
    }
    
    scrollToBottom();
    
    const observer = new MutationObserver(scrollToBottom);
    observer.observe(container, {
        childList: true,
        subtree: true
    });
    
    window.addEventListener('resize', scrollToBottom);
    setTimeout(scrollToBottom, 300);
});