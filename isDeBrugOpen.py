import requests
from bs4 import BeautifulSoup
import time


# URL of the page to check
# Replace with the actual URL
# url = 'https://www.isdebrugopen.nl/zuid-holland/leiderdorp/leiderdorpsebrug'
url = 'https://www.isdebrugopen.nl/zeeland/terneuzen/oostsluis-binnenhoofd-brug'


while True:
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

    time.sleep(15)  # Sleep for 60 seconds
