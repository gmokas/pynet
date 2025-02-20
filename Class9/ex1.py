from pprint import pprint
from napalm import get_network_driver
from my_devices import cisco3, arista1
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

devices = [cisco3, arista1]

for device in devices:
    device_type = device.pop("device_type")
    driver = get_network_driver(device_type)
    dev = driver(**device)
    
    dev.open()
    output = dev.get_facts()
    pprint(dev)
    print("#"*100)
    pprint(output)
    print("#"*100)
    print("Device type :", dev.platform)






