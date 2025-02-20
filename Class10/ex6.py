from __future__ import print_function, unicode_literals
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import network_devices
from my_functions import ssh_command2


def ssh_command3(device):
    """Establish an SSH connection. Execute show command, return results."""
    
    if device['device_type'] == "juniper_junos":
        device = ConnectHandler(**device)
        output = device.send_command("show arp")
        device.disconnect()
        return output
    else:
        device = ConnectHandler(**device)
        output = device.send_command("show ip arp")
        device.disconnect()
        return output



if __name__ == "__main__":

    start_time = datetime.now()
    max_procs = 5

    with ProcessPoolExecutor(max_procs) as pool:
        results_generator = pool.map(ssh_command3, network_devices)

        for output in results_generator:
            print("#" * 100)
            print(output)
            print("#" * 100)

    end_time = datetime.now()
    print("*" * 100)
    message_time = f"  Time for the whole script is: {end_time - start_time}  "
    centered_message_time = message_time.center(100, "*")
    print(centered_message_time)
    print("*" * 100)

