LIGHT_THRESHOLD = 1000


class LightingObserver:
    def __init__(self, led, ldr):
        self.led = led
        self.ldr = ldr

    def update(self, event, data):
        if event == "motion_detected":
            if self.ldr.read() < LIGHT_THRESHOLD:
                self.led.on()
        elif event == "motion_clear":
            self.led.off()
