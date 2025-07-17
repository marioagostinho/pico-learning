from machine import Pin
from time import sleep

Pin('LED', Pin.OUT).value(1)

redLED = Pin(15, Pin.OUT)

while True:
    redLED.toggle()
    sleep(.1)
    