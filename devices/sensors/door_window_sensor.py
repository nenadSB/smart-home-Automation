import logging
import random
import time

class DoorWindowSensor:
    def __init__(self, mqtt_client, topic="home/door_window"):
        self.logger = logging.getLogger(__name__)
        self.mqtt_client = mqtt_client
        self.topic = topic
    
    def check_status(self):
        # Simulate door/window status
        status = random.choice(["OPEN", "CLOSED"])
        self.logger.info(f"Door/Window status: {status}")
        self.mqtt_client.publish(self.topic, status)
    
    def start(self):
        self.logger.info("Starting door/window sensor...")
        while True:
            self.check_status()
            time.sleep(5)  # Check status every 5 seconds
    
    def stop(self):
        self.logger.info("Stopping door/window sensor...")