import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)

# Blink the onboard LED
while True:
    led.toggle()  # Toggle the LED state between on and off
    time.sleep(1)  # Wait for 1 second
