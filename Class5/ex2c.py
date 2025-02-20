import os
import time
from netmiko import ConnectHandler
from getpass import getpass
from dotenv import load_dotenv
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from my_devices import nexus1, nexus2


env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise2")

interface = "Ethernet1/4"


nxos1 = {
    "device_name": "nxos1",
    "local_as": 22,
    "interface": interface,
    "ipv4_address": "10.4.100.1",
    "ipv4_netmask": "24",
}

nxos2 = {
    #"device_name": "nxos2",
    "local_as": 22,
    "interface": interface,
    "ipv4_address": "10.4.100.2",
    "ipv4_netmask": "24",
}

nxos1["peer_ip"] = nxos2["ipv4_address"]
nxos2["peer_ip"] = nxos1["ipv4_address"]


config_list=[]

print()
for device in (nxos1, nxos2):
    template_file = "nxos_bgp.j2"
    template = env.get_template(template_file)
    config = template.render(**device)
    config_list.append(config)

for i in range(0,2):
    config_list[i] = config_list[i].splitlines()

for nexus in (nexus1,nexus2):
    #net_connect = ConnectHandler(**nexus)
    time.sleep(2)
    if nexus == nexus1:
        net_connect = ConnectHandler(**nexus)
        net_connect.config_mode()
        net_connect.send_config_set(config_list[0], read_timeout=10)
        net_connect.exit_config_mode()
        prompt = net_connect.find_prompt()
        print(prompt)
        net_connect.disconnect()
    else:
        net_connect = ConnectHandler(**nexus)
        net_connect.config_mode()
        #net_connect.send_command(config_list[1])
        net_connect.send_config_set(config_list[1], read_timeout=10)
        net_connect.exit_config_mode()
        net_connect.disconnect()
    print("#"*80)

time.sleep(5)

for nexus in (nexus1,nexus2):
    net_connect = ConnectHandler(**nexus)
    command_output = net_connect.send_command("show ip bgp summary", expect_string=r"#", strip_prompt=False, strip_command=False)
    print(command_output)
    if nexus == nexus1:
        ping_output = net_connect.send_command("ping {}".format(nxos2['ipv4_address']))
        print(ping_output)
        net_connect.disconnect()
    else:
        ping_output = net_connect.send_command("ping {}".format( nxos1['ipv4_address']))
        print(ping_output)
        net_connect.disconnect()



