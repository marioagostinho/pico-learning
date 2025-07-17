from machine import Pin
from time import sleep

Pin('LED', Pin.OUT).value(1)

led = Pin(15, Pin.OUT)

while True:
    led.toggle()
    sleep(.25)