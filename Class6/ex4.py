import os
import time
import pyeapi
import yaml
from netmiko import ConnectHandler
from getpass import getpass
from dotenv import load_dotenv
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint
from my_funcs import yaml_load_devices


env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

password = getpass() 
template_file = "loopback_intf.j2"


yaml_out = yaml_load_devices("arista_devices_full.yml")
my_devices = yaml_out["my_devices"]



eapi_devices=[]

for device_name in my_devices:
    device_dict = yaml_out[device_name]
    device_dict["password"] = password

    j2_vars = device_dict.pop("data")
    template = env.get_template(template_file)
    cfg_lines = template.render(**j2_vars)
    cfg_lines = cfg_lines.strip()
    cfg_lines = cfg_lines.splitlines()

    eapi_conn = pyeapi.client.connect(**device_dict)
    device_obj = pyeapi.client.Node(eapi_conn)
    eapi_devices.append(device_obj)
    output = device_obj.config(cfg_lines)
    print(output)


for device_obj in eapi_devices:
    output = device_obj.enable("show ip interface brief")
    print()
    print("-" * 50)
    show_ip_dict = output[0]["result"]["interfaces"]
    for intf_name, v in show_ip_dict.items():
        ip_addr = v["interfaceAddress"]["ipAddr"]["address"]
        print(f"{intf_name} -> {ip_addr}")
    print("-" * 50)
print()
