import logging
from devices.sensors.temperature_sensor import TemperatureSensor
from devices.sensors.motion_sensor import MotionSensor
from devices.actuators.smart_light import SmartLight
from devices.actuators.smart_thermostat import SmartThermostat
from devices.actuators.smart_plug import SmartPlug
from devices.sensors.door_window_sensor import DoorWindowSensor
from devices.sensors.smoke_detector import SmokeDetector

class DeviceController:
    def __init__(self, mqtt_client):
        self.logger = logging.getLogger(__name__)
        self.mqtt_client = mqtt_client
        self.temperature_sensor = TemperatureSensor(self.mqtt_client)
        self.smart_light = SmartLight(self.mqtt_client)
        self.smart_thermostat = SmartThermostat(self.mqtt_client)
        self.motion_sensor = MotionSensor(self.mqtt_client)
        self.smart_plug = SmartPlug(self.mqtt_client)
        self.door_window_sensor = DoorWindowSensor(self.mqtt_client)
        self.smoke_detector = SmokeDetector(self.mqtt_client)

    def start(self):
        self.logger.info("Starting device controller...")

        # Start each device in its own thread
        self.temperature_sensor.start()
        self.smart_light.start()
        self.smart_thermostat.start()
        self.motion_sensor.start()
        self.smart_plug.start()
        self.door_window_sensor.start()
        self.smoke_detector.start()

    def stop(self):
        self.logger.info("Stopping device controller...")

        # Stop each device cleanly
        self.temperature_sensor.stop()
        self.smart_light.stop()
        self.smart_thermostat.stop()
        self.motion_sensor.stop()
        self.smart_plug.stop()
        self.door_window_sensor.stop()
        self.smoke_detector.stop()
