class OLEDObserver:
    def __init__(self, oled):
        self.oled = oled

    def update(self, event, data):
        if event == "temperature_high":
            self.oled.alert("TEMP ALTA")

        elif event == "gas_alert":
            self.oled.alert("GAS DETECTADO")

        elif event == "motion_detected":
            self.oled.alert("MOVIMENTO")