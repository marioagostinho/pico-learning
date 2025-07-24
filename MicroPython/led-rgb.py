from machine import Pin, PWM
from time import sleep

class RGBLED:
    def __init__(self, red_pin, green_pin, blue_pin, freq=1000):
        self.red = PWM(Pin(red_pin))
        self.green = PWM(Pin(green_pin))
        self.blue = PWM(Pin(blue_pin))
        
        for led in (self.red, self.green, self.blue):
            led.freq(freq)
            led.duty_u16(0)

    def set_color(self, r, g, b):
        self.red.duty_u16(r)
        self.green.duty_u16(g)
        self.blue.duty_u16(b)


# Program
RED_PIN = 13
GREEN_PIN = 14
BLUE_PIN = 15

rgb_led = RGBLED(RED_PIN, GREEN_PIN, BLUE_PIN)
rgb_led.set_color(4500, 0 , 4500)

