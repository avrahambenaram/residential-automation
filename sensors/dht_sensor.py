from machine import Pin
import dht

from core.observer import Subject


class DHTSensor(Subject):
    def __init__(
        self,
        pin,
        temp_threshold=35,
        humidity_low=30,
        humidity_high=80
    ):
        super().__init__()

        self.sensor = dht.DHT22(Pin(pin))

        self.temp_threshold = temp_threshold

        self.humidity_low = humidity_low
        self.humidity_high = humidity_high

        self.high_temp_triggered = False

    def check(self):
        self.sensor.measure()

        temp = self.sensor.temperature()
        hum = self.sensor.humidity()

        self.notify("dht_read", {
            "temperature": temp,
            "humidity": hum
        })

        if temp > self.temp_threshold:
            if not self.high_temp_triggered:
                self.notify("temperature_high", temp)

                self.high_temp_triggered = True

        else:
            if self.high_temp_triggered:
                self.notify("temperature_normal", temp)

                self.high_temp_triggered = False

        if hum < self.humidity_low:
            self.notify("humidity_low", hum)

        if hum > self.humidity_high:
            self.notify("humidity_high", hum)
