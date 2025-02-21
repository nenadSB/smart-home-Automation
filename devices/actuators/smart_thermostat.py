import logging
import time

class SmartThermostat:
    def __init__(self, mqtt_client, topic="home/thermostat"):
        self.logger = logging.getLogger(__name__)
        self.mqtt_client = mqtt_client
        self.topic = topic
        self.target_temperature = 22.0  # Default target temperature in Celsius
    
    def set_temperature(self, temperature):
        self.target_temperature = temperature
        self.logger.info(f"Thermostat set to {temperature}°C")
        self.mqtt_client.publish(self.topic, temperature)
    
    def start(self):
        self.logger.info("Starting smart thermostat...")
        # Subscribe to the topic to receive control commands
        self.mqtt_client.subscribe(self.topic)
        self.mqtt_client.message_callback_add(self.topic, self.handle_message)
    
    def stop(self):
        self.logger.info("Stopping smart thermostat...")
        self.mqtt_client.unsubscribe(self.topic)
    
    def handle_message(self, client, userdata, message):
        payload = message.payload.decode()
        try:
            temperature = float(payload)
            self.set_temperature(temperature)
        except ValueError:
            self.logger.error(f"Invalid temperature value: {payload}")