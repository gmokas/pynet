#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    host='nxos1.lasthop.io',
    username='pyclass',
    password=getpass(),
    device_type='cisco_nxos',
    session_log='prompt_logs.txt',
)

print(net_connect.find_prompt())
output = net_connect.send_command('sh ip arp')
print(output)
