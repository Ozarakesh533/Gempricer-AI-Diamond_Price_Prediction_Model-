document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const submitBtn = form ? form.querySelector('button[type="submit"]') : null;
    const submitText = submitBtn ? submitBtn.querySelector('#submit-text') : null;
    const spinner = submitBtn ? submitBtn.querySelector('.spinner-border') : null;

    if (form) {
        form.addEventListener('submit', async function(e) {
            // Let the browser submit by default unless we can safely handle redirect
            // Validate form
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
                form.classList.add('was-validated');
                return;
            }

            // Show loading state
            if (submitBtn && submitText && spinner) {
                submitBtn.disabled = true;
                submitText.textContent = 'Predicting...';
                spinner.classList.remove('d-none');
            }

            // Try fetch-based submit to improve UX; if redirect or error, fall back to normal submit
            try {
                e.preventDefault();
                const formData = new FormData(form);
                const data = Object.fromEntries(formData.entries());

                // Convert numeric fields to numbers
                const numericFields = ['carat', 'depth', 'table', 'x', 'y', 'z'];
                numericFields.forEach(field => {
                    if (data[field]) data[field] = String(data[field]);
                });

                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: new URLSearchParams(data).toString(),
                    redirect: 'follow'
                });

                // If server redirected (Flask returns 302 to /results), go there
                if (response.redirected && response.url) {
                    window.location.href = response.url;
                    return;
                }

                // Try JSON path (when backend returns JSON for AJAX)
                const contentType = response.headers.get('content-type') || '';
                if (contentType.includes('application/json')) {
                    const result = await response.json();
                    const queryParams = new URLSearchParams(data).toString();
                    window.location.href = `/results?${queryParams}&prediction=${result.prediction}`;
                    return;
                }

                // If HTML came back without redirect, replace document with it
                const text = await response.text();
                if (text && text.includes('<html')) {
                    document.open();
                    document.write(text);
                    document.close();
                    return;
                }

                // Fallback to normal submit
                form.submit();
            } catch (error) {
                // Fallback to normal submit on any error
                form.submit();
            }
        });
    }
});
