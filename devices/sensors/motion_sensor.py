import logging
import random
import time

class MotionSensor:
    def __init__(self, mqtt_client, topic="home/motion"):
        self.logger = logging.getLogger(__name__)
        self.mqtt_client = mqtt_client
        self.topic = topic
    
    def detect_motion(self):
        # Simulate motion detection
        motion_detected = random.choice([True, False])
        self.logger.info(f"Motion detected: {motion_detected}")
        self.mqtt_client.publish(self.topic, "ON" if motion_detected else "OFF")
    
    def start(self):
        self.logger.info("Starting motion sensor...")
        while True:
            self.detect_motion()
            time.sleep(5)  # Check for motion every 5 seconds
    
    def stop(self):
        self.logger.info("Stopping motion sensor...")