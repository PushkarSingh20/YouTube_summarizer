document.getElementById('summarizerForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const videoUrl = document.getElementById('videoUrl').value;
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const error = document.getElementById('error');
    const submitBtn = document.getElementById('submitBtn');
    const btnText = document.getElementById('btnText');
    
    // Reset states
    error.style.display = 'none';
    results.style.display = 'none';
    
    // Validate URL
    if (!videoUrl.includes('youtube.com/watch?v=') && !videoUrl.includes('youtu.be/')) {
        showError('Please enter a valid YouTube URL');
        return;
    }
    
    // Show loading state
    loading.style.display = 'block';
    submitBtn.disabled = true;
    btnText.textContent = 'Processing...';
    
    try {
        // Call API
        const response = await fetch('/api/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: videoUrl })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Something went wrong');
        }
        
        // Show results
        showResults(data, videoUrl);
        
    } catch (err) {
        showError(err.message);
    } finally {
        // Hide loading
        loading.style.display = 'none';
        submitBtn.disabled = false;
        btnText.textContent = 'Generate Summary';
    }
});

function showError(message) {
    const error = document.getElementById('error');
    error.textContent = message;
    error.style.display = 'block';
}

function showResults(data, videoUrl) {
    // Update video info
    document.getElementById('videoTitle').textContent = `Video Analysis Complete`;
    document.getElementById('videoMeta').textContent = 
        `Video ID: ${data.video_id} • Transcript words: ${data.transcript_length}`;
    
    // Update summary
    document.getElementById('summaryContent').innerHTML = 
        data.summary.replace(/\n/g, '<br>');
    
    // Show results with animation
    const results = document.getElementById('results');
    results.style.display = 'block';
    results.classList.add('success-animation');
    
    // Scroll to results
    results.scrollIntoView({ behavior: 'smooth' });
}

// Auto-focus input on load
window.addEventListener('load', () => {
    document.getElementById('videoUrl').focus();
});

// Handle enter key in input
document.getElementById('videoUrl').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        document.getElementById('summarizerForm').dispatchEvent(new Event('submit'));
    }
});