import xmltodict
from pprint import pprint



def filename(file):
    f = open(file)
    file_list = []
    xmldata = f.read().strip()
    
    my_xml = xmltodict.parse(xmldata)
    
    pprint(my_xml)
    x = my_xml
    file_list.append(x)
    return file_list


files = ["show_security_zones.xml", "show_security_zones_single_trust.xml"]


print("*** EX3a ***")

file_list = []
for file in files:
    print("#"*100)
    print("this is file :", file)    
    filename(file)

print(file_list)
 



