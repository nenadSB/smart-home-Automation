import paho.mqtt.client as mqtt
import logging
from communication.protocols.protocol_handler import ProtocolHandler

class MQTTClient:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.client = mqtt.Client()
        self.protocol_handler = ProtocolHandler()
    
    def on_message(self, client, userdata, message):
        self.protocol_handler.handle_message(message.payload.decode())
    
    def connect(self):
        self.logger.info("Connecting to MQTT broker...")
        self.client.on_message = self.on_message
        self.client.connect("localhost", 1883, 60)
        self.client.loop_start()
    
    def disconnect(self):
        self.logger.info("Disconnecting from MQTT broker...")
        self.client.loop_stop()
        self.client.disconnect()
    
    def publish(self, topic, message):
        self.client.publish(topic, message)
    
    def subscribe(self, topic):
        self.client.subscribe(topic)
    
    def message_callback_add(self, topic, callback):
        self.client.message_callback_add(topic, callback)