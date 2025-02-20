from pprint import pprint
from napalm import get_network_driver
from my_devices import cisco3, arista1
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from my_functions2 import open_napalm_connection

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

devices = [cisco3, arista1]

for device in devices:
    dev = open_napalm_connection(device)
    dev.load_merge_candidate(filename="{}-loopbacks".format(dev.hostname))
    diff = dev.compare_config()
    print("Diff before commiting for device {}".format(dev.hostname))    
    print(diff)
    if diff:
        dev.commit_config()
    print("Diff after commiting for device {}".format(dev.hostname))
    print(dev.compare_config())
    dev.close()
    
