from machine import Pin, PWM

class Servo:
    def __init__(self, pin):
        self.pwm = PWM(Pin(pin), freq=50)

    def set_angle(self, angle):
        duty = int((angle / 180) * 102 + 26)
        self.pwm.duty(duty)

    def open(self):
        self.set_angle(90)

    def close(self):
        self.set_angle(0)