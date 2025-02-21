import sys
import os
import paho.mqtt.client as mqtt
import logging

# Ensure the parent directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from devices.controllers.device_controller import DeviceController
from communication.mqtt.mqtt_client import MQTTClient
from utils.logging.logger import setup_logging

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected to MQTT Broker!")
    else:
        logging.error(f"Failed to connect, return code {rc}")

def main():
    setup_logging()
    
    mqtt_client = MQTTClient()
    mqtt_client.connect()
    
    device_controller = DeviceController(mqtt_client)
    device_controller.start()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        mqtt_client.disconnect()
        device_controller.stop()

if __name__ == "__main__":
    main()