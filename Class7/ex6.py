import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)


output = device.show("show interface Ethernet1/1")

print("Interface: ", output['TABLE_interface']['ROW_interface']['interface'])
print("State: ", output['TABLE_interface']['ROW_interface']['state'])
print("MTU: ", output['TABLE_interface']['ROW_interface']['eth_mtu'])
