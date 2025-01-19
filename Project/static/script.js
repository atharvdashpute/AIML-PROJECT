document.getElementById('career-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const response = await fetch('/predict', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    const suggestionsDiv = document.getElementById('suggestions');

    suggestionsDiv.innerHTML = `
        <p>Hello ${data.name}, based on your input, we suggest the following career paths:</p>
        <ul>
            ${data.suggested_careers.map(career => `<li>${career}</li>`).join('')}
        </ul>
    `;
});
