import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
}


net_connect = ConnectHandler(**device)
version = net_connect.send_command("show version", use_textfsm=True)
print(version, "\n")


lldp = net_connect.send_command("show lldp neighbors", use_textfsm=True)
print(lldp, "\n")


print()
type_version = type(version)
print("the type of version output is: " , type_version)
type_lldp = type(lldp)
print("the type of lldp output is: " , type_lldp)
print()


print()
print("The interface of the lldp neighbor is: ", lldp[0]['neighbor_interface'])
print()

net_connect.disconnect()


