import logging
import random
import time

class SmokeDetector:
    def __init__(self, mqtt_client, topic="home/smoke"):
        self.logger = logging.getLogger(__name__)
        self.mqtt_client = mqtt_client
        self.topic = topic
    
    def check_smoke(self):
        # Simulate smoke detection
        smoke_detected = random.choice([True, False])
        status = "SMOKE DETECTED" if smoke_detected else "CLEAR"
        self.logger.info(f"Smoke status: {status}")
        self.mqtt_client.publish(self.topic, status)
    
    def start(self):
        self.logger.info("Starting smoke detector...")
        while True:
            self.check_smoke()
            time.sleep(10)  # Check for smoke every 10 seconds
    
    def stop(self):
        self.logger.info("Stopping smoke detector...")