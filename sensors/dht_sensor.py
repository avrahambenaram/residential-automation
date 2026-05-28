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
        self.temperature = 0
        self.humidity = 0

    def check(self):
        self.sensor.measure()

        self.temperature = self.sensor.temperature()
        self.humidity = self.sensor.humidity()

        self.notify("dht_read", {
            "temperature": self.temperature,
            "humidity": self.humidity
        })

        if self.temperature > self.temp_threshold:
            if not self.high_temp_triggered:
                self.notify("temperature_high", self.temperature)
                self.high_temp_triggered = True
        else:
            if self.high_temp_triggered:
                self.notify("temperature_normal", self.temperature)
                self.high_temp_triggered = False

        if self.humidity < self.humidity_low:
            self.notify("humidity_low", self.humidity)

        if self.humidity > self.humidity_high:
            self.notify("humidity_high", self.humidity)
