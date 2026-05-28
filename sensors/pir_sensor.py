from machine import Pin
from core.observer import Subject

class PIRSensor(Subject):
    def __init__(self, pin):
        super().__init__()

        self.sensor = Pin(pin, Pin.IN)

        self.last_state = 0
        self.motion_detected = False

    def check(self):
        current = self.sensor.value()

        if current == 1 and self.last_state == 0:
            self.motion_detected = True
            self.notify("motion_detected")
        elif current == 0:
            self.motion_detected = False

        self.last_state = current