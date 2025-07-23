from machine import PWM, Pin
from time import sleep

PWM_MAX = 65535
VOLT_MAX = 3.3

OUT_PIN = 16

analog_out = PWM(Pin(OUT_PIN))
analog_out.freq(1000)
analog_out.duty_u16(0)

while True:
    voltage = float(input('What Voltage Do You Want? '))
    pwmVal = (PWM_MAX/VOLT_MAX) * voltage
    analog_out.duty_u16(int(pwmVal))