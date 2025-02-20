from jnpr.junos import Device
from getpass import getpass
from pprint import pprint
from jnpr_devices import srx2
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.utils.config import Config
from lxml import etree

device = Device(**srx2)
device.open()
device.timeout = 60



my_xml = device.rpc.get_software_information()

print(etree.tostring(my_xml, pretty_print=True,encoding="unicode"))


interfaces = device.rpc.get_interface_information(terse=True)
print(etree.tostring(interfaces, encoding="unicode"))


xml_out = device.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))


