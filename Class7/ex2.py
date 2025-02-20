import xmltodict
from pprint import pprint


f = open("show_security_zones.xml")

xmldata = f.read().strip()

my_xml = xmltodict.parse(xmldata)


print("#"*100)
print("*** EX2a ***")

pprint(my_xml)
print(type(my_xml))


zones = my_xml['zones-information']['zones-security']

print("#"*100)
print("*** EX2b ***")

i = 1
for zone in zones:
    print("Security Zone #",i,": ", zone['zones-security-zonename'])
    i += i



