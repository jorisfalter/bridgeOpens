import xml.etree.ElementTree as ET

# Add more namespaces if needed
namespaces = {'soap': 'http://schemas.xmlsoap.org/soap/envelope/'}


tree = ET.parse('brugopeningen.xml')
root = tree.getroot()

for child in root.findall('.//soap:Body', namespaces):  # Using the namespace
    print(child.tag, child.attrib)
