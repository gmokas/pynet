from lxml import etree
import xmltodict

data = open("show_version.xml","rb")

data = data.read().strip()


my_xml = etree.fromstring(data)


print("**** 5a ****")
print("Print default document namespace mapping\n")

print(my_xml.nsmap)



print("**** 5b ****")
print("Print the proc_board_id element using namespace wildcard\n")
print(my_xml.find(".//{*}proc_board_id").text)


