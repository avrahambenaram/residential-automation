from machine import Pin

class Buzzer:
    def __init__(self, pin):
        self.buzzer = Pin(pin, Pin.OUT)

    def on(self):
        self.buzzer.value(1)

    def off(self):
        self.buzzer.value(0)