from machine import ADC, Pin
from core.observer import Subject

class GasSensor(Subject):
    def __init__(self, pin, threshold=2000):
        super().__init__()

        self.adc = ADC(Pin(pin))
        self.adc.atten(ADC.ATTN_11DB)

        self.threshold = threshold

    def check(self):
        value = self.adc.read()

        if value > self.threshold:
            self.notify("gas_alert", value)