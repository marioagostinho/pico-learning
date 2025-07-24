from machine import Pin, PWM, ADC
from time import sleep

POT_PIN = 28
LED_PIN = 15

pot = ADC(POT_PIN)

anout = PWM(Pin(LED_PIN))
anout.freq(1000)
anout.duty_u16(0)

while True:
    adc_value = pot.read_u16()
    anout.duty_u16(adc_value)
    
    sleep(.1)