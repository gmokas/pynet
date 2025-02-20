import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)


output = device.show("show interface Ethernet1/1")

print("*******  EX7a  *******")

print("Interface: ", output.find(".//interface").text)
print("State: ", output.find(".//state").text)
print("MTU: ", output.find(".//eth_mtu").text)



print("*******  EX7b  *******")


commands = ["show system uptime", "show system resources"]

for command in commands:
    command_output = device.show(command)
    command_output = etree.tostring(command_output).decode()
    pprint(command_output)



cfg_cmd = [
    "interface lo161",
    "des 161_first_loopack",
    "interface lo162",
    "des 162_second_loopack",
]

output_config = device.config_list(cfg_cmd)
print(etree.tostring(output_config[0]).decode())
    

