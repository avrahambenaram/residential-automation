from time import sleep

from dht_sensor import DHTSensor
from pir_sensor import PIRSensor
from gas_sensor import GasSensor

from climate_observer import ClimateObserver
from gas_observer import GasObserver
from lighting_observer import LightingObserver
from ventilation_observer import VentilationObserver

from leds import LED
from buzzer import Buzzer
from servo import Servo
from relay import Relay


# Atuadores
led = LED(26)

buzzer = Buzzer(25)

servo = Servo(33)

relay = Relay(32)

# Sensores
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

# Registro
dht.attach(climate)

pir.attach(lighting)

gas.attach(gas_observer)


dht.attach(ventilation)

gas.attach(ventilation)

# Loop
while True:
    print("Rodando")
    dht.check()

    pir.check()

    gas.check()

    sleep(1)
