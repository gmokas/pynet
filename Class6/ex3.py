import os
import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices, route_print
from pprint import pprint

def main():

    devices = yaml_load_devices()
    password = getpass()

    for name, device_dict in devices.items():
        output = []
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip route")
        route_list = output[0]["result"]["vrfs"]["default"]["routes"]
        pprint(route_list)
        for route,route_dict in route_list.items():
            route_type = route_list[route]["routeType"]
            next_hop = route_dict["vias"][0]["nexthopAddr"]
            print(type(route_dict))
            print(type(output))
            print(type(route_list))
            print(type(route_type))
            route_print(route_list,route,route_type,next_hop)


if __name__ == "__main__":
    main()


