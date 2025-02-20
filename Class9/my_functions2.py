from pprint import pprint
from napalm import get_network_driver
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def open_napalm_connection(device):
    device = device.copy()
    device_type = device.pop("device_type")
    driver = get_network_driver(device_type)
    dev = driver(**device)
    
    
    dev.open()
    return dev


def create_checkpoint(dev):
    if "nxos" in dev.platform:
        filename = f"{dev.hostname}-checkpoint.txt"
        backup = dev._get_checkpoint_file()
        with open(filename, "w") as f:
            f.write(backup)
    else:
        raise ValueError("Checkpoint requires NX-OS")
