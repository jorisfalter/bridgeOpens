# this file is a test case of a server giving an indication

from flask import Flask
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)


# The default route
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
    url = 'https://www.isdebrugopen.nl/zuid-holland/leiderdorp/leiderdorpsebrug'
    # url = 'https://www.isdebrugopen.nl/zeeland/terneuzen/oostsluis-binnenhoofd-brug'

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
                return False
            elif "ja" in status_text.lower():
                print("Ja")
                return True
            else:
                print("Status not found or unrecognized.")
                return ("Not found")
        else:
            print("Status section not found in the HTML.")
            return ("Not found")
    else:
        print("Failed to fetch the webpage.")
        return ("Can't Load Webpage")


@app.route('/ledstatus')
def led_status():
    # Use the function to determine the LED state
    # need to add additional error handling here based on the errors from the function
    gls_response = get_led_state()
    if gls_response:
        return 'open', 200, {'Content-Type': 'text/plain'}
    else:
        return 'gesloten', 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    # Get port from environment variable or default to 3000
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)


# I'm not sure I need this, maybe the Raspberry triggers the function
# while True:
#     led_status()

#     time.sleep(15)  # Sleep for 15 seconds
