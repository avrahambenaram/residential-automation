from machine import ADC, Pin
from core.observer import Subject

class GasSensor(Subject):
    def __init__(self, pin, threshold=2000):
        super().__init__()

        self.adc = ADC(Pin(pin))
        self.adc.atten(ADC.ATTN_11DB)

        self.threshold = threshold
        self.level = 0

    def check(self):
        self.level = self.adc.read()

        if self.level > self.threshold:
            self.notify("gas_alert", self.level)