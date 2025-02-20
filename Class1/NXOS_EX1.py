#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass


#password = os.getenv("PASSWD") if os.getenv("PASSWD") else getpass()
password = os.getenv("PASSWD")
NXOS1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_nxos',
    "session_log": 'prompt_logs.txt',
}

net_connect = ConnectHandler(**NXOS1)
print(net_connect.find_prompt())
output = net_connect.send_command('sh ip arp')
print(output)
