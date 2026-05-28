class GasObserver:
    def __init__(self, buzzer, servo):
        self.buzzer = buzzer
        self.servo = servo

    def update(self, event, data):
        if event == "gas_alert":
            print("ALERTA DE GAS:", data)
            self.buzzer.on()
            self.servo.open()
        elif event == "gas_normal":
            print("GAS NORMALIZADO:", data)
            self.buzzer.off()
            self.servo.close()