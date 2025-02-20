from pprint import pprint
from napalm import get_network_driver
from my_devices import cisco3, arista1
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from my_functions import open_napalm_connection, create_backup

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

devices = [cisco3, arista1]

for device in devices:
    dev = open_napalm_connection(device)
    conn = dev
    backup = create_backup(conn)
    filename = f"{conn.hostname}-running.txt"
    with open(filename, "w") as f:
        f.write(backup["running"])
