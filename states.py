class SystemState:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0

        self.motion_detected = False

        self.light_level = 0
        self.gas_level = 0

        self.led_room = False
        self.led_bedroom = False

        self.alarm_active = False
        self.security_mode = True

        self.door_open = False