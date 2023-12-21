import network
import urequests
import time
from machine import Pin

# TODO this one goes on when we're not connected to wifi yet
led_status_indicator = machine.Pin(0, machine.Pin.OUT)


wlan = network.WLAN(network.STA_IF)


def connect_to_wifi(ssid, password, which_wifi, timeout=50):
    wlan.active(True)

    while not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        print(which_wifi)
        wlan.connect(ssid, password)

        # Wait for connection with a timeout
        start_time = time.ticks_ms()
        while not wlan.isconnected():
            if time.ticks_diff(time.ticks_ms(), start_time) > timeout * 1000:
                print("Connection timed out.")
                break
            time.sleep(1)

    print("Connected to Wi-Fi.")
    print(which_wifi)
    print("Network config:", wlan.ifconfig())
    return True


# Replace with your network credentials
ssid_home = 'wade  2.4G'
password_home = ''
# Replace with your network credentials

# Connect to Wi-Fi
connected_home = connect_to_wifi(ssid_home, password_home, "home")

while connected_home:
    led = machine.Pin("LED", machine.Pin.OUT)
    led_external = machine.Pin(0, machine.Pin.OUT)
    server_url = 'https://bridgeopen-0fd60d885493.herokuapp.com/ledstatus'

    # while wlan.isconnected():  # check if the connection is made
    # no blinking
    # led.value(1)  # Set the LED to on
    # led_external.value(1)  # Set the LED to on

    # blinking
    # led.toggle()  # Toggle the LED state between on and off
    # led_external.toggle()  # Set the LED to on
    # time.sleep(2)  # Wait for 1 second

    # Function to get the LED status from the server
    def get_led_status(url):
        try:
            response = urequests.get(url)
            if response.text == 'open':
                # can I make it blink instead?
                led.value(0)
                print("open")
            elif response.text == 'gesloten':
                led.value(1)
                print("gesloten")
            response.close()
        except Exception as e:
            print("Failed to get connection:", str(e))
            connect_to_wifi(ssid, password)
            # Optionally, re-attempt Wi-Fi connection or handle error

    try:
        get_led_status(server_url)
        time.sleep(15)  # Poll every second, adjust as needed
    except:
        pass  # Handle exceptions (e.g., network errors)


print("disconnected from Wi-Fi.")
