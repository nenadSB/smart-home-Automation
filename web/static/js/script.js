// Use JavaScript to dynamically load data (you can improve it further with fetch/ajax)
setInterval(function() {
    fetch('/sensors/temperature')
        .then(response => response.json())
        .then(data => {
            document.getElementById('temperature-status').textContent = data.temperature + ' °C';
        });

    fetch('/sensors/motion')
        .then(response => response.json())
        .then(data => {
            document.getElementById('motion-status').textContent = data.motion;
        });

    fetch('/sensors/door_window')
        .then(response => response.json())
        .then(data => {
            document.getElementById('door-status').textContent = data.status;
        });

    fetch('/sensors/smoke')
        .then(response => response.json())
        .then(data => {
            document.getElementById('smoke-status').textContent = data.status;
        });
}, 5000); // Refresh every 5 seconds

// Handle light control form submission via AJAX
document.getElementById('control-light').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from reloading the page

    const state = document.getElementById('light').value;
    fetch('/devices/light', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ state: state })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('light-status').textContent = state;
    });
});

// Handle plug control form submission via AJAX
document.getElementById('control-plug').addEventListener('submit', function(event) {
    event.preventDefault();

    const state = document.getElementById('plug').value;
    fetch('/devices/plug', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ state: state })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('plug-status').textContent = state;
    });
});

// Handle thermostat control form submission via AJAX
document.getElementById('set-thermostat').addEventListener('submit', function(event) {
    event.preventDefault();

    const temperature = document.getElementById('thermostat').value;
    fetch('/devices/thermostat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ temperature: temperature })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('thermostat-status').textContent = temperature + ' °C';
    });
});
