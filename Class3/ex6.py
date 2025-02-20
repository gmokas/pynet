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

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}


net_connect = ConnectHandler(**cisco4)
config = net_connect.send_command("show run")
net_connect.disconnect()
cisco_cfg = CiscoConfParse(config.splitlines(), ignore_blank_lines=False)

interfaces = cisco_cfg.find_objects_w_child(
        parentspec=r"^interface", childspec=r"^\s+ip address"
)

print()
for intf in interfaces:
    print("Interface Line: {}".format(intf.text))
    ip_address = intf.re_search_children(r"ip address")[0].text
    print("IP Address Line: {}".format(ip_address))
    print()
print()



