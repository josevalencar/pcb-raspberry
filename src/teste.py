from machine import Pin
import time

led_pin = Pin(20, Pin.OUT)

while True:
    led_pin.low()
    time.sleep(1)
    
    led_pin.high()
    time.sleep(1)
