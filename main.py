from time import sleep

from sensors.dht_sensor import DHTSensor
from sensors.pir_sensor import PIRSensor
from sensors.gas_sensor import GasSensor

from observers.climate_observer import ClimateObserver
from observers.gas_observer import GasObserver
from observers.lighting_observer import LightingObserver
from observers.ventilation_observer import VentilationObserver

from actuators.leds import LED
from actuators.buzzer import Buzzer
from actuators.servo import Servo
from actuators.relay import Relay


# Actors
led = LED(26)

buzzer = Buzzer(25)

servo = Servo(33)

relay = Relay(32)

# Sensors
dht = DHTSensor(15)

pir = PIRSensor(13)

gas = GasSensor(35)

# Observers
climate = ClimateObserver(buzzer)

lighting = LightingObserver(led)

gas_observer = GasObserver(
    buzzer,
    servo
)

ventilation = VentilationObserver(relay)

# Attach observers
dht.attach(climate)

pir.attach(lighting)

gas.attach(gas_observer)


dht.attach(ventilation)

gas.attach(ventilation)

while True:
    dht.check()

    pir.check()

    gas.check()

    sleep(1)
