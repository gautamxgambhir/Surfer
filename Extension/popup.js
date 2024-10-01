document.getElementById('submit').addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        const url = tabs[0].url;
        const action = document.querySelector('input[name="action"]:checked').value;

        let endpoint = '';
        if (action === 'website_info') {
            endpoint = 'http://127.0.0.1:5000/website_info';
        } else if (action === 'webpage_summary') {
            endpoint = 'http://127.0.0.1:5000/summarize_webpage';
        }

        fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: url }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('summaryContainer').innerText = data.summary || data.error;
        })
        .catch(error => {
            console.error('Fetch error:', error);
            document.getElementById('summaryContainer').innerText = 'Error: ' + error.message;
        });
    });
});

// Show/hide bullet points input based on checkbox
document.querySelector('input[name="action"]').forEach(radio => {
    radio.addEventListener('change', function() {
        const bulletPointsContainer = document.getElementById('bulletPointsContainer');
        if (this.value === 'webpage_summary') {
            bulletPointsContainer.style.display = 'block';
        } else {
            bulletPointsContainer.style.display = 'none';
        }
    });
});

// Show/hide bullet points number input based on checkbox
document.getElementById('bulletPointsCheck').addEventListener('change', function() {
    const bulletPointsInput = document.getElementById('bulletPointsInput');
    bulletPointsInput.style.display = this.checked ? 'block' : 'none';
});
