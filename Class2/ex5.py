#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

NXOS1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_nxos',
    "session_log": 'logs1ex5.txt',
}

NXOS2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_nxos',
    "session_log": 'logs2ex5.txt',
}

device_list = [NXOS1, NXOS2]

i=0

for device in device_list:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file('vlans.txt')
    net_connect.save_config()
    print("=" *80)
    print("The configuration at ", device_list[i]['host'], "is completed")
    print("=" *80)
    i=i+1
    net_connect.disconnect()



