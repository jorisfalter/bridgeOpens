import xml.etree.ElementTree as ET


def print_element_info(elem, indent=""):
    text = elem.text.strip() if elem.text is not None else None
    print(f"{indent}{elem.tag}: {elem.attrib}, Text: {text}")
    for child in elem:
        print_element_info(child, indent + "  ")


# Parse the XML file
tree = ET.parse('brugopeningen.xml')
root = tree.getroot()

# Define the substring you are looking for in the ID
# target_substring = "NLSPL002120533100119"
target_substring = "NLLID002060528100496"  # leiderdorpsebrug

# Find elements whose ID attribute contains the specific substring
for elem in root.iter():
    id_value = elem.get('id')
    if id_value and target_substring in id_value:
        print("Found element with ID containing target substring:")
        print_element_info(elem)
