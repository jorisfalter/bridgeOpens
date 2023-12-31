import time
import os
from dotenv import load_dotenv
import certifi
import pymongo
import xml.etree.ElementTree as ET
import io
import gzip
import requests
from pymongo import MongoClient

# This file downloads the xml every minute and stores it in mongodb
# Instead we'll use the "isdebrugopen" website


def print_element_info(elem, indent=""):
    text = elem.text.strip() if elem.text is not None else None
    print(f"{indent}{elem.tag}: {elem.attrib}, Text: {text}")
    for child in elem:
        print_element_info(child, indent + "  ")


# make data insertable into db
def parse_element_info(elem):
    # Create a dictionary to store element info
    elem_dict = {
        'tag': elem.tag,
        'attributes': elem.attrib,
        'text': elem.text.strip() if elem.text is not None else None,
        'children': []
    }

    # Recursively parse child elements
    for child in elem:
        child_dict = parse_element_info(child)
        elem_dict['children'].append(child_dict)

    return elem_dict


# initiate the DB
ca = certifi.where()

# Load environment variables from .env file
load_dotenv()
mongoPass = os.getenv("MONGO_ATLAS_PASS")

client = pymongo.MongoClient(
    f'mongodb+srv://joris:{mongoPass}@cluster0.igx7ca5.mongodb.net/?retryWrites=true&w=majority&connectTimeoutMS=5000', tlsCAFile=ca)

db = client['bridgeOpenDb']
collection = db['bridgeOpenCollection']

# this makes everything below run in a loop. Disabling now.
# while True:

# URL of the file to be downloaded
file_url = "https://opendata.ndw.nu/brugopeningen.xml.gz"

# Send a GET request to the URL
response = requests.get(file_url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Write the content to a file
#     with open("brugopeningen.xml.gz", "wb") as file:
#         file.write(response.content)
#     print("Download completed successfully.")
# else:
#     print("Failed to download the file.")

# Check if the request was successful
if response.status_code == 200:
    # Decompress the content in memory
    with gzip.open(io.BytesIO(response.content), 'rt', encoding='utf-8') as f_in:
        xml_content = f_in.read()

    # Process the XML content
    # (Example: Parse the XML and do something with it)
    root = ET.fromstring(xml_content)

    # Define the substring you are looking for in the ID
    # target_substring = "NLSPL002120533100119"
    target_substring = "NLLID002060528100496"  # leiderdorpsebrug

    # Find elements whose ID attribute contains the specific substring
    for elem in root.iter():
        id_value = elem.get('id')
        if id_value and target_substring in id_value:
            print("Found element with ID containing target substring:")
            print_element_info(elem)

            # Parse the filtered element
            dataBridge = parse_element_info(elem)

            # Insert into MongoDB
            result = collection.insert_one(dataBridge)

    print("Processing completed successfully.")
    # now = datetime.datetime.now()
    # collection.insert_one({"test1": now})
else:
    print("Failed to download the file.")

time.sleep(60)  # Sleep for 60 seconds
