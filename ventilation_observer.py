class VentilationObserver:
    def __init__(self, relay):
        self.relay = relay

    def update(self, event, data):
        if event == "temperature_high":
            print("Ventilacao ligada")

            self.relay.on()

        elif event == "temperature_normal":
            print("Ventilacao desligada")

            self.relay.off()

        elif event == "gas_alert":
            print("Exaustor de emergencia ligado")

            self.relay.on()
