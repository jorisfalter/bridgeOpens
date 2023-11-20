import requests
import gzip
import xml.etree.ElementTree as ET


# URL of the file to be downloaded
file_url = "https://opendata.ndw.nu/brugopeningen.xml.gz"

# Send a GET request to the URL
response = requests.get(file_url)

# Check if the request was successful
if response.status_code == 200:
    # Write the content to a file
    with open("brugopeningen.xml.gz", "wb") as file:
        file.write(response.content)
    print("Download completed successfully.")
else:
    print("Failed to download the file.")


# Specify the names of the input and output files
input_file = 'brugopeningen.xml.gz'
output_file = 'brugopeningen.xml'

# Open the gzip file in read mode and the output file in write mode
with gzip.open(input_file, 'rt', encoding='utf-8') as f_in:
    xml_content = f_in.read()

print("Decompression complete.")
# print(xml_content)


# def print_element_info(elem, indent=""):
#     text = elem.text.strip() if elem.text is not None else None
#     print(f"{indent}{elem.tag}: {elem.attrib}, Text: {text}")
#     for child in elem:
#         print_element_info(child, indent + "  ")


# Parse the XML file
root = ET.fromstring(xml_content)

# Define the substring you are looking for in the ID
target_substring = "NLSPL002120533100119"
# target_substring = "NLLID002060528100496"  # leiderdorpsebrug

# Find elements whose ID attribute contains the specific substring
for elem in root.iter():
    id_value = elem.get('id')
    if id_value and target_substring in id_value:
        print("Found element with ID containing target substring:")
        # print_element_info(elem)
