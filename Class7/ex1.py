from lxml import etree
import xmltodict

data = open("show_security_zones.xml")

data = data.read().strip()


my_xml = etree.fromstring(data)

print("#"*80)
print("*** EX1a ***\n")

print(my_xml)

print(type(my_xml))


xml_string = etree.tostring(my_xml).decode()

print("#"*80)
print("*** EX1b ***\n")

print(xml_string)


print("#"*80)
print("*** EX1c ***\n")

print(my_xml.tag)

print(len(my_xml))

print("#"*80)
print("*** EX1d ***\n")


children = my_xml.getchildren()

print(children[0].tag)


print("#"*80)
print("*** EX1e ***\n")

my_xml[0].tag = "trust_zone"

print("The text of the 'zones-security-zonename' child is ", my_xml[0][0].text, " whose father is ", my_xml[0].tag)


print("#"*80)
print("*** EX1f ***\n")

for clild in my_xml[0]:
    print(clild.tag)

