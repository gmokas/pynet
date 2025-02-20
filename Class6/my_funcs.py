import pyeapi
import os
import yaml
from getpass import getpass
from pprint import pprint


def yaml_load_devices(filename="arista.yml"):
    with open(filename, "r") as f:
        return yaml.safe_load(f)
    raise ValueError("Reading YAML file failed")

def arp_print(arp_list):
    for arp_entry in arp_list:
        mac_address = arp_entry["hwAddress"]
        ip_address = arp_entry["address"]
        print("{} {} {}".format(ip_address, "-->", mac_address))

def route_print(route_list,route,route_type,next_hop):
    if route_type == "static":
        print("The route type is ",route_type , "for route ", route, "and the next hop is:", next_hop)
    else:
        print("The route type is ",route_type , "for route ", route)
    print("#"*80)

