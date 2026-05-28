class ClimateObserver:
    def __init__(self, buzzer):
        self.buzzer = buzzer

    def update(self, event, data):
        if event == "temperature_high":
            print("Temperatura alta:", data)

            self.buzzer.on()

        elif event == "temperature_normal":
            print("Temperatura normal:", data)

            self.buzzer.off()

        elif event == "humidity_low":
            print("Umidade baixa:", data)

        elif event == "humidity_high":
            print("Umidade alta:", data)