# this file is a test case of a server giving an indication

from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def test_ft():
    return 'ok', 200, {'Content-Type': 'text/plain'}


def get_led_state():
    # Get the current time
    current_time = time.time()

    # Find the time modulo 8 seconds (5 seconds on, 3 seconds off)
    cycle_time = current_time % 8

    # If the modulo is less than 5, the LED should be on
    return cycle_time < 5


@app.route('/ledstatus')
def led_status():
    # Use the function to determine the LED state
    if get_led_state():
        return 'on', 200, {'Content-Type': 'text/plain'}
    else:
        return 'off', 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
