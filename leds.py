from machine import Pin

class LED:
    def __init__(self, pin):
        self.led = Pin(pin, Pin.OUT)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)

    def set(self, state):
        self.led.value(state)