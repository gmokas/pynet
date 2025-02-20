from lxml import etree
import xmltodict

data = open("show_security_zones.xml")

data = data.read().strip()


my_xml = etree.fromstring(data)

print("--------------------")
print("------ EX 4a -------")
print("--------------------")

print("Find tag of the first zones-security element")
print("--------------------")
print(my_xml.find("zones-security").tag)

print("Find tag of all child elements of the first zones-security element")
print("--------------------")

zones_security = my_xml.find("zones-security")
children = zones_security.getchildren()

for child in children:
   print(child.tag)

print("--------------------")
print("------ EX 4b -------")
print("--------------------")
print(my_xml.find(".//zones-security-zonename").text)

print("--------------------")
print("------ EX 4c -------")
print("--------------------")

zones = []


zones = my_xml.findall("zones-security")

for zone in zones:
    print(zone.find(".//zones-security-zonename").text)

