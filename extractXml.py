import xml.etree.ElementTree as ET


def print_element_info(elem, depth=0):
    indent = "  " * depth
    print(f"{indent}{elem.tag}: {elem.attrib}")
    for child in elem:
        print_element_info(child, depth + 1)


# Parse the XML file
tree = ET.parse('brugopeningen4.xml')
root = tree.getroot()

# Start exploring from the root
print_element_info(root)
