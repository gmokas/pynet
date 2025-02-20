#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()


NXOS2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_nxos',
    "global_delay_factor": 2,
    "fast_cli": False
}


net_connect = ConnectHandler(**NXOS2)
output = net_connect.send_command("show lldp neighbors detail")

print()
print(output)
print()

