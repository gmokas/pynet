from pprint import pprint
from napalm import get_network_driver
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def open_napalm_connection(device):
    device_type = device.pop("device_type")
    driver = get_network_driver(device_type)
    dev = driver(**device)
    
    
    dev.open()
    print("#"*100)
    pprint(dev)
    output = dev.get_facts()
    print("#"*100)
    pprint(output)
    print("#"*100)
    print("Device type :", dev.platform)
    print("#"*100)
    pprint(dev.get_arp_table())
    print("#"*100)
    try:
        pprint(dev.get_ntp_peers())
    except NotImplementedError:
        print("At this device type, ntp peers are not implemented")
    return dev

def create_backup(conn):
    backup = conn.get_config()
    return backup
