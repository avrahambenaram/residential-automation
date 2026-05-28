class LightingObserver:
    def __init__(self, led):
        self.led = led

    def update(self, event, data):
        if event == "motion_detected":
            self.led.on()