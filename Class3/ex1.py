import os
import re
from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from dotenv import load_dotenv
from ciscoconfparse import CiscoConfParse



load_dotenv()


file = open("data.conf", "r")

data = file.read()

file.close()


data = data.strip()



data_list = data.splitlines()


new_list = []


for i in data_list:
    if re.search(r"^Protocol.*Interface", i):
        continue
    _, ip_addr, _, mac_addr, _, intf = i.split()
    arp_dict = {"mac_addr": mac_addr, "ip_addr": ip_addr, "interface": intf}
    new_list.append(arp_dict)


print()
pprint(new_list)
print()
