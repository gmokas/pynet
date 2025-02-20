import os
from getpass import getpass


username = "pyclass"
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "ios",
}

arista1 = {
    "hostname": "arista1.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "eos",
}

nxos1 = {
    "hostname": "nxos1.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "nxos",
    "optional_args": {"port": 8443},
}
