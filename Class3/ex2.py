import os
import re
from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from dotenv import load_dotenv
from ciscoconfparse import CiscoConfParse



load_dotenv()

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()


cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}


devices = (cisco3, cisco4, nxos1, nxos2)

for device in devices:
    net_connect = ConnectHandler(**device)
    print("#"*40)
    print(net_connect.find_prompt())
    print("#"*40)
    net_connect.disconnect()

