from pprint import pprint
from napalm import get_network_driver
from my_devices import nxos1
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from my_functions2 import open_napalm_connection, create_checkpoint

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



NXOS_REPLACE_CANDIDATE = "nxos1_replacement_cfg"

device = nxos1
dev = open_napalm_connection(device)


create_checkpoint(dev)

dev.load_replace_candidate(NXOS_REPLACE_CANDIDATE)

print("Config staged: pending differences {}".format(dev.hostname))
print("#" * 80)
print(dev.compare_config())
print("#" * 80)
print("Discarding candidate config for device {}".format(dev.hostname))
dev.discard_config()
print("Diff after discarding candidate config for device {}".format(dev.hostname))
print("#" * 80)
print(dev.compare_config())
print("#" * 80)
dev.close()
