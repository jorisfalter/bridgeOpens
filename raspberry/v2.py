import network
import urequests
import time
from machine import Pin


# this one includes network connection
# Replace with your network credentials
ssid = 'wade  5G'
password = 'thao1305'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connection to be established
while not wlan.isconnected():
    pass

# connect to server > postpone for now, I only want to see the connection
# The URL of your server endpoint that sends the LED command
server_url = 'http://your.server.com/ledstatus'

# Setup the onboard LED
led = Pin(25, Pin.OUT)

# Function to get the LED status from the server


def get_led_status(url):
    response = urequests.get(url)
    if response.text == 'on':
        led.value(1)
    elif response.text == 'off':
        led.value(0)
    response.close()


# Main loop to poll the server and update the LED
while True:
    try:
        get_led_status(server_url)
        time.sleep(1)  # Poll every second, adjust as needed
    except:
        pass  # Handle exceptions (e.g., network errors)
