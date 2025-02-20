import os
import re
from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from dotenv import load_dotenv
from ciscoconfparse import CiscoConfParse





data = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""


bgp_obj = CiscoConfParse(data.splitlines(), ignore_blank_lines=False)

bgp_peers = []

neighbors = bgp_obj.find_objects_w_parents(parentspec=r"^router bgp 44", childspec=r"neighbor")

for neighbor in neighbors:
    _,neighbor_ip = neighbor.text.split()
    for child in neighbor.children:
        if "remote-as" in child.text:
             _, remote_as = child.text.split()
    bgp_peers.append((neighbor_ip, remote_as))
print()
print("BGP Peers: ")
pprint(bgp_peers)
print()
