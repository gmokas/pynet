from __future__ import print_function, unicode_literals
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import network_devices
from my_functions import ssh_command2

if __name__ == "__main__":
    show_command = "show version"

    start_time = datetime.now()
    future_list = []
    max_procs = 5

    with ProcessPoolExecutor(max_procs) as pool:
        for device in network_devices:
            output = pool.submit(ssh_command2, device, show_command)
            future_list.append(output)

        for output in as_completed(future_list):
            print("#" * 100)
            print(output.result())
            print("#" * 100)

    end_time = datetime.now()
    print("*" * 100)
    message_time = f"  Time for the whole script is: {end_time - start_time}  "
    centered_message_time = message_time.center(100, "*")
    print(centered_message_time)
    print("*" * 100)

