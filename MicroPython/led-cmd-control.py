from machine import Pin
from time import sleep

Pin('LED', Pin.OUT).value(1)
led = Pin(15, Pin.OUT)

while True:
    CMD = input('What is Your Command (ON/OFF)')
    
    if CMD == 'ON':
        led.value(1)
    elif CMD == 'OFF':
        led.value(0)