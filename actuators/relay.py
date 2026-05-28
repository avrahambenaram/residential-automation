from machine import Pin


class Relay:
    def __init__(self, pin):
        self.relay = Pin(pin, Pin.OUT)

    def on(self):
        self.relay.value(1)

    def off(self):
        self.relay.value(0)
