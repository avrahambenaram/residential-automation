from machine import Pin, I2C
import ssd1306

class OLEDDisplay:
    def __init__(self):
        i2c = I2C(0, scl=Pin(22), sda=Pin(21))
        self.display = ssd1306.SSD1306_I2C(128, 64, i2c)

    def update(self, state):
        self.display.fill(0)

        self.display.text("Temp:{}C".format(state.temperature), 0, 0)
        self.display.text("Hum:{}%".format(state.humidity), 0, 10)

        self.display.text("Light:{}".format(state.light_level), 0, 20)

        motion = "YES" if state.motion_detected else "NO"
        self.display.text("Motion:{}".format(motion), 0, 30)

        gas = "ALERT" if state.gas_level > 2000 else "OK"
        self.display.text("Gas:{}".format(gas), 0, 40)

        alarm = "ON" if state.alarm_active else "OFF"
        self.display.text("Alarm:{}".format(alarm), 0, 50)

        self.display.show()