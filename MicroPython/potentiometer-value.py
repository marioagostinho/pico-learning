import machine
from time import sleep

potPin = 28
pot = machine.ADC(potPin)

while True:
    potVal = pot.read_u16()
    voltage = (3.3/65106) * potVal - (96*3.3/65106)
    print(voltage)
    sleep(.5)