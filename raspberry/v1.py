import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)
led_external = machine.Pin(0, machine.Pin.OUT)


# Blink the onboard LED
while True:
    led.toggle()  # Toggle the LED state between on and off
    led_external.toggle()  # Set the LED to on

    time.sleep(1)  # Wait for 1 second
