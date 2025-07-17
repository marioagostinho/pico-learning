from machine import Pin
from time import sleep

Pin('LED', Pin.OUT).value(1)

led1 = Pin(12, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led4 = Pin(14, Pin.OUT)
led8 = Pin(15, Pin.OUT)

count = 0

while True:
    led1.value((count >> 0) & 1)
    led2.value((count >> 1) & 1)
    led4.value((count >> 2) & 1)
    led8.value((count >> 3) & 1)
    
    count += 1
    
    if (count == 16):
        count = 0
    
    sleep(0.25)