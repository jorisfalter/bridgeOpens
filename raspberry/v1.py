import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)

# Blink the onboard LED
while True:
    led.toggle()  # Toggle the LED state between on and off
    time.sleep(1)  # Wait for 1 second

# Function to safely turn off the LED


def turn_off_led():
    onboard_led.value(0)  # Set the LED to off


# Try-except block to handle the program interruption
try:
    while True:
        led.toggle()  # Toggle the LED state
        time.sleep(1)
except:
    turn_off_led()  # Ensure the LED is turned off when the loop is interrupted
