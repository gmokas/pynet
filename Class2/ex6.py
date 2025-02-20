#!/usr/bin/env python
import os
import time
from netmiko import ConnectHandler
from getpass import getpass


password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

net_connect = ConnectHandler(**device)
prompt = net_connect.find_prompt()
print("\n\n Below the device prompt response: \n", prompt)
print("=" *80)

net_connect.config_mode()
config_prompt = net_connect.find_prompt()
print("\n\n Below the device configuration prompt: \n", config_prompt)
print("=" *80)

net_connect.exit_config_mode()
new_prompt = net_connect.find_prompt()
print("\n\n Below the prompt after exit config mode: \n", new_prompt)
print("=" *80)

net_connect.write_channel("disable\n") 
time.sleep(2)
read_channel = net_connect.read_channel()
print("\n\n Below the output after disable command: \n", read_channel)
print("=" *80)

net_connect.enable()
enable_prompt = net_connect.find_prompt()
print("\n\n Below the prompt from enable mode: \n", enable_prompt)
print("=" *80)

net_connect.disconnect()

