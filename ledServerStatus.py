# this file is a test case of a server giving an indication

from flask import Flask
app = Flask(__name__)


@app.route('/ledstatus')
def led_status():
    # Logic to determine whether the LED should be on or off
    led_state = get_led_state()  # This function is hypothetical
    return 'on' if led_state else 'off', 200, {'Content-Type': 'text/plain'}


def get_led_state():
    # Your logic here to determine the LED state
    # For example, it could check a database or a file
    return True  # or False, depending on the desired state


if __name__ == '__main__':
    app.run(host='0.0.0.0')
