import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
    "session_log": "logs_ex4.txt",
    "fast_cli": True
}

cfg_list = [
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
]

start_time = datetime.now()
print("=" * 80)
print("The start time is : ", start_time)
print("=" * 80)

net_connect = ConnectHandler(**device)
cfg_output = net_connect.send_config_set(cfg_list)

end_time = datetime.now()
print("=" * 80)
print("The end time is : ", end_time)
print("=" * 80)



ping_output = net_connect.send_command("ping google.com")
if "!!" in ping_output:
    print("Ping Successful:")
    print("\n\nPing Output: {}\n\n".format(ping_output))
else:
    raise ValueError("\n\nPing Failed: {}\n\n".format(ping_output))
net_connect.disconnect()


print("Total Execution Time: {}\n".format(end_time - start_time))
