#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

NXOS1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    # "session_log": 'prompt_logs.txt',
}

NXOS2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    # "session_log": 'prompt_logs.txt',
}

device_list = [NXOS1, NXOS2]

for device in device_list:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    print(net_connect.send_command("show ip interface brief vrf management"))


