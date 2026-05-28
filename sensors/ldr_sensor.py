from machine import ADC, Pin

class LDRSensor:
    def __init__(self, pin):
        self.adc = ADC(Pin(pin))
        self.adc.atten(ADC.ATTN_11DB)

    def read(self):
        return 4095 - self.adc.read()
