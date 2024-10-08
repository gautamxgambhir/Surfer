document.getElementById('submit').addEventListener('click', function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
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

const storageKey = 'theme-preference';
const themeToggle = document.getElementById('theme-toggle');

const onClick = () => {
    theme.value = theme.value === 'light' ? 'dark' : 'light';
    setPreference();
};

const getColorPreference = () => {
    if (localStorage.getItem(storageKey)) {
        return localStorage.getItem(storageKey);
    } else {
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
};

const setPreference = () => {
    localStorage.setItem(storageKey, theme.value);
    reflectPreference();
};

const reflectPreference = () => {
    document.firstElementChild.setAttribute('data-theme', theme.value);
    themeToggle.setAttribute('aria-label', theme.value);

    if (theme.value === 'dark') {
        document.body.classList.add('dark-theme');
        localStorage.setItem('theme', 'dark-theme');
    } else {
        document.body.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light-theme');
    }
};

const theme = {
    value: getColorPreference(),
};

reflectPreference();

window.onload = () => {
    reflectPreference();
    themeToggle.addEventListener('click', onClick);
};

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', ({ matches: isDark }) => {
    theme.value = isDark ? 'dark' : 'light';
    setPreference();
});

document.getElementById('summaryContainer').addEventListener('click', function () {
    const summaryText = document.getElementById('summaryContainer').innerText;
  
    if (summaryText) {
      navigator.clipboard.writeText(summaryText).then(() => {
        const summaryContainer = document.getElementById('summaryContainer');
        const copiedText = document.getElementById('copiedText');
  
        // Blur the summary and show the copied message
        summaryContainer.classList.add('blur');
        copiedText.style.display = 'block';
  
        setTimeout(() => {
          summaryContainer.classList.remove('blur');
          copiedText.style.display = 'none';
        }, 1500);
      }).catch((err) => {
        console.error('Could not copy text: ', err);
      });
    }
  });