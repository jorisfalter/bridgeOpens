import requests
import gzip
import shutil

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
with gzip.open(input_file, 'rb') as f_in:
    with open(output_file, 'wb') as f_out:
        # Copy the decompressed data to the output file
        shutil.copyfileobj(f_in, f_out)

print("Decompression complete.")
