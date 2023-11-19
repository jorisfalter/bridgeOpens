import requests
import time

# replace with the specific endpoint you're interested in
DATA_URL = "https://opendata.ndw.nu/your_specific_endpoint_here"


def fetch_data():
    response = requests.get(DATA_URL)
    if response.status_code == 200:
        # Process the data as needed
        # ... your data processing code here ...
        pass
    else:
        print(f"Error fetching data. Status code: {response.status_code}")


# Poll for data every hour (3600 seconds)
while True:
    fetch_data()
    time.sleep(3600)
