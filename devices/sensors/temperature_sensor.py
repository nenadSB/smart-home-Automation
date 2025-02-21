import logging
import random
import time
import paho.mqtt.client as mqtt
import threading

class TemperatureSensor:
    def __init__(self, mqtt_client, topic="home/temperature"):
        self.logger = logging.getLogger(__name__)
        self.mqtt_client = mqtt_client
        self.topic = topic
        self.running = False

    def read_temperature(self):
        # Simulate a temperature reading
        temperature = random.uniform(20.0, 30.0)
        self.logger.info(f"Temperature reading: {temperature}°C")
        return temperature

    def start(self):
        """Start the sensor in a separate thread."""
        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True  # Allow the thread to exit when the main program exits
        self.thread.start()

    def _run(self):
        """The function that runs in a separate thread to read and publish temperature."""
        self.logger.info("Starting temperature sensor...")
        while self.running:
            temperature = self.read_temperature()
            self.mqtt_client.publish(self.topic, temperature)
            time.sleep(5)  # Read every 5 seconds

    def stop(self):
        """Stop the sensor."""
        self.running = False
        if self.thread.is_alive():
            self.thread.join()  # Wait for the thread to finish
        self.logger.info("Stopping temperature sensor...")
