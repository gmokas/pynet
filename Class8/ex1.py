from jnpr.junos import Device
from getpass import getpass
from pprint import pprint


a_device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())
a_device.open()

print("These are all the facts of the device:\n")
pprint(a_device.facts)


print("#"*100, "\n")

print("This is the hostname :")
print(a_device.facts['hostname'])


