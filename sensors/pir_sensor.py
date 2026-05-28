from machine import Pin
from core.observer import Subject

class PIRSensor(Subject):
    def __init__(self, pin):
        super().__init__()

        self.sensor = Pin(pin, Pin.IN)

        self.last_state = 0

    def check(self):
        current = self.sensor.value()

        if current == 1 and self.last_state == 0:
            self.notify("motion_detected")

        self.last_state = current