import network
import urequests
import time
from machine import Pin

wlan = network.WLAN(network.STA_IF)


def connect_to_wifi(ssid, password, timeout=10):
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(ssid, password)

        # Wait for connection with a timeout
        start_time = time.ticks_ms()
        while not wlan.isconnected():
            if time.ticks_diff(time.ticks_ms(), start_time) > timeout * 3000:
                print("Connection timed out.")
                return False
            time.sleep(1)

    print("Connected to Wi-Fi.")
    print("Network config:", wlan.ifconfig())
    return True


# Replace with your network credentials
ssid = 'wade  5G'
password = 'thao1305'

# Connect to Wi-Fi
connected = connect_to_wifi(ssid, password)

if connected:

    led = machine.Pin("LED", machine.Pin.OUT)

    # Blink the onboard LED
    while wlan.isconnected():  # check if the connection is made
        # while True:
        led.value(1)  # Set the LED to on

    print("Wi-Fi connection lost. Attempting to reconnect...")
