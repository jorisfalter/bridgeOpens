# this file is a test case of a server giving an indication

from flask import Flask
import time
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def test_ft():
    return 'ok', 200, {'Content-Type': 'text/plain'}


def get_led_state():
    # # test case
    # # Get the current time
    # current_time = time.time()

    # # Find the time modulo 8 seconds (5 seconds on, 3 seconds off)
    # cycle_time = current_time % 8

    # # If the modulo is less than 5, the LED should be on
    # return cycle_time < 5

    # real case
    # URL of the page to check
    # Replace with the actual URL
    # url = 'https://www.isdebrugopen.nl/zuid-holland/leiderdorp/leiderdorpsebrug'
    url = 'https://www.isdebrugopen.nl/zeeland/terneuzen/oostsluis-binnenhoofd-brug'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the relevant section (adjust the selector as needed)
        status_div = soup.find('div', class_='top-banner')

        if status_div:
            status_text = status_div.get_text(strip=True)

            if "nee" in status_text.lower():
                print("Nee")
            elif "ja" in status_text.lower():
                print("Ja")
            else:
                print("Status not found or unrecognized.")
        else:
            print("Status section not found in the HTML.")
    else:
        print("Failed to fetch the webpage.")


@app.route('/ledstatus')
def led_status():
    # Use the function to determine the LED state
    if get_led_state():
        return 'on', 200, {'Content-Type': 'text/plain'}
    else:
        return 'off', 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
