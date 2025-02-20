#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass


NXOS2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "global_delay_factor": 2,
    "fast_cli": False
}


net_connect = ConnectHandler(**NXOS2)
output = net_connect.send_command("show lldp neighbors detail")

print()
print(output)
print()

print("This is OUTPUT 2")

output2 = net_connect.send_command("show lldp neighbors detail", delay_factor=8)


print()
print(output2)
print()


