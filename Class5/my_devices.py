from getpass import getpass



password=getpass()


nexus1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "session_log": "nx1_output.txt",
}

nexus2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "session_log": "nx2_output.txt",
}

