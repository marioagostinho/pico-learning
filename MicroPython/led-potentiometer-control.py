from machine import ADC, Pin
from time import sleep

ADC_MAX = 65535

POT_PIN = 28
GREEN_LED_PIN = 15
YELLOW_LED_PIN = 14
RED_LED_PIN = 13

pot = ADC(POT_PIN)
led_green = Pin(GREEN_LED_PIN, Pin.OUT)
led_yellow = Pin(YELLOW_LED_PIN, Pin.OUT)
led_red = Pin(RED_LED_PIN, Pin.OUT)

while True:
    adc_value = pot.read_u16()
    percentage = (adc_value * 100) / ADC_MAX

    if percentage >= 95:
        led_green.value(0)
        led_yellow.value(0)
        led_red.value(1)
    elif percentage >= 75:
        led_green.value(0)
        led_yellow.value(1)
        led_red.value(0)
    else:
        led_green.value(1)
        led_yellow.value(0)
        led_red.value(0)

    sleep(0.1)
