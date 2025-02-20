#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

NXOS1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "session_log": 'logs_nxos1.txt',
}

NXOS2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "session_log": 'logs_nxos2.txt',
}

device_list = [NXOS1, NXOS2]

for device in device_list:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show version")
    
    filename = f"show_version_{device['host']}.txt"
    with open(filename, "w") as f:
        f.write(output)

    net_connect.disconnect()

