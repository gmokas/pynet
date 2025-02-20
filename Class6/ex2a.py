import pyeapi
import os
import yaml
from getpass import getpass
from pprint import pprint


def yaml_load_devices(filename="arista.yml"):
    with open(filename, "r") as f:
        return yaml.safe_load(f)
    raise ValueError("Reading YAML file failed")


devices = yaml_load_devices()
password = getpass()


for name,device_dict in devices.items():
    print(name)
    device_dict["password"] = password
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable("show ip arp")

    arp_list = output[0]["result"]["ipV4Neighbors"]
    for arp_entry in arp_list:
        mac_address = arp_entry["hwAddress"]
        ip_address = arp_entry["address"]
        print("{} {} {}".format(ip_address, "-->", mac_address))


