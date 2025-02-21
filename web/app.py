from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

class MockMQTTClient:
    def connect(self):
        print("Mock MQTT client connected")

    def publish(self, topic, message):
        print(f"Mock MQTT client published to {topic}: {message}")

class MockDeviceController:
    def start(self):
        print("Mock device controller started")

    def stop(self):
        print("Mock device controller stopped")

mqtt_client = MockMQTTClient()
mqtt_client.connect()

device_controller = MockDeviceController()
device_controller.start()

@app.route('/', methods=['GET'])
def index():
    # Passing the data you want to display on the index page
    devices = {
        "temperature_sensor": "running",
        "smart_light": "running",
        "smart_thermostat": "running",
        "motion_sensor": "running",
        "smart_plug": "running",
        "door_window_sensor": "running",
        "smoke_detector": "running"
    }
    return render_template('index.html', devices=devices)  # Passing the devices data to the template

@app.route('/devices', methods=['GET'])
def get_devices():
    print("Handling GET request for /devices")
    devices = {
        "temperature_sensor": "running",
        "smart_light": "running",
        "smart_thermostat": "running",
        "motion_sensor": "running",
        "smart_plug": "running",
        "door_window_sensor": "running",
        "smoke_detector": "running"
    }
    return jsonify(devices)

@app.route('/devices/light', methods=['POST'])
def control_light():
    print("Handling POST request for /devices/light")
    data = request.json
    if data.get('state') == 'ON':
        mqtt_client.publish("home/light", "ON")
    elif data.get('state') == 'OFF':
        mqtt_client.publish("home/light", "OFF")
    return jsonify({"status": "success", "light_state": data.get('state')})

@app.route('/devices/plug', methods=['POST'])
def control_plug():
    print("Handling POST request for /devices/plug")
    data = request.json
    if data.get('state') == 'ON':
        mqtt_client.publish("home/plug", "ON")
    elif data.get('state') == 'OFF':
        mqtt_client.publish("home/plug", "OFF")
    return jsonify({"status": "success", "plug_state": data.get('state')})

@app.route('/devices/thermostat', methods=['POST'])
def control_thermostat():
    print("Handling POST request for /devices/thermostat")
    data = request.json
    mqtt_client.publish("home/thermostat", data['temperature'])
    return jsonify({"status": "success", "temperature": data['temperature']})

# Simulated sensor data routes
@app.route('/sensors/temperature', methods=['GET'])
def get_temperature():
    temperature = 22.5  # Simulate temperature
    print(f"Temperature: {temperature}°C")
    return jsonify({"temperature": temperature})

@app.route('/sensors/motion', methods=['GET'])
def get_motion():
    motion = "DETECTED"  # Simulate motion detection
    print(f"Motion: {motion}")
    return jsonify({"motion": motion})

@app.route('/sensors/door_window', methods=['GET'])
def get_door_window():
    status = "OPEN"  # Simulate door/window status
    print(f"Door/Window: {status}")
    return jsonify({"status": status})

@app.route('/sensors/smoke', methods=['GET'])
def get_smoke():
    status = "CLEAR"  # Simulate smoke detection status
    print(f"Smoke: {status}")
    return jsonify({"status": status})

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)  # By default, runs on http://127.0.0.1:5000
