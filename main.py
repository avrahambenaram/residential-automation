from time import sleep

from sensors.dht_sensor import DHTSensor
from sensors.pir_sensor import PIRSensor
from sensors.gas_sensor import GasSensor
from sensors.ldr_sensor import LDRSensor

from observers.climate_observer import ClimateObserver
from observers.gas_observer import GasObserver
from observers.lighting_observer import LightingObserver
from observers.ventilation_observer import VentilationObserver
from observers.oled_observer import OLEDObserver

from actuators.leds import LED
from actuators.buzzer import Buzzer
from actuators.servo import Servo
from actuators.relay import Relay

from display.oled import OLEDDisplay
from core.states import SystemState

# Actors
led = LED(26)
buzzer = Buzzer(25)
servo = Servo(33)
relay = Relay(32)

# Sensors
dht = DHTSensor(15)
pir = PIRSensor(13)
gas = GasSensor(35)
ldr = LDRSensor(34)

# Display + State
oled = OLEDDisplay()
state = SystemState()

# Observers
climate = ClimateObserver(buzzer)
lighting = LightingObserver(led)
gas_observer = GasObserver(buzzer, servo)
ventilation = VentilationObserver(relay)
oled_observer = OLEDObserver(oled)

# Attach observers
dht.attach(climate)
pir.attach(lighting)
gas.attach(gas_observer)
dht.attach(ventilation)
gas.attach(ventilation)
dht.attach(oled_observer)
gas.attach(oled_observer)
pir.attach(oled_observer)

while True:
    dht.check()
    pir.check()
    gas.check()

    state.temperature = dht.temperature
    state.humidity = dht.humidity
    state.motion_detected = pir.motion_detected
    state.gas_level = gas.level
    state.light_level = ldr.read()

    oled.update(state)
    sleep(1)
