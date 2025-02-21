import logging
import time

class SmartLight:
    def __init__(self, mqtt_client, topic="home/light"):
        self.logger = logging.getLogger(__name__)
        self.mqtt_client = mqtt_client
        self.topic = topic
        self.state = "OFF"
    
    def turn_on(self):
        self.state = "ON"
        self.logger.info("Light turned ON")
        self.mqtt_client.publish(self.topic, "ON")
    
    def turn_off(self):
        self.state = "OFF"
        self.logger.info("Light turned OFF")
        self.mqtt_client.publish(self.topic, "OFF")
    
    def start(self):
        self.logger.info("Starting smart light...")
        # Subscribe to the topic to receive control commands
        self.mqtt_client.subscribe(self.topic)
        self.mqtt_client.message_callback_add(self.topic, self.handle_message)
    
    def stop(self):
        self.logger.info("Stopping smart light...")
        self.mqtt_client.unsubscribe(self.topic)
    
    def handle_message(self, client, userdata, message):
        payload = message.payload.decode()
        if payload == "ON":
            self.turn_on()
        elif payload == "OFF":
            self.turn_off()