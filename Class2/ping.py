#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

cisco4 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_xe',
    "session_log": 'ping_logs.txt'
}


net_connect = ConnectHandler(**cisco4)
net_connect.send_command("ping\n", expect_string=r'ip')
net_connect.send_command('\n', expect_string=r'address')
net_connect.send_command("8.8.8.8\n", expect_string=r'count')
net_connect.send_command('\n', expect_string=r'size')
net_connect.send_command('\n', expect_string=r'seconds')
net_connect.send_command('\n', expect_string=r'commands')
net_connect.send_command('\n', expect_string=r'sizes')
output = net_connect.send_command('\n')
print(output)

