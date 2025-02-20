from __future__ import print_function, unicode_literals
import threading
import time
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import network_devices
from my_functions import ssh_command




if __name__ == "__main__":
    
    show_command = "show version"

    start_time = datetime.now()
    threads = []
    for device in network_devices:
        my_thread = threading.Thread(target=ssh_command, args=(device,show_command))
        threads.append(my_thread)
        my_thread.start()
        end_time = datetime.now()
        print("#"*100)
        print("Time for ", device['host'], " is: ", end_time - start_time)
        print("#"*100)
    for thread in threads:
        thread.join()

    end_time = datetime.now()
    print("*"*100)
    print("*"*100)
    message_time = f"  Time for the whole script is: {end_time - start_time}  "
    centered_message_time = message_time.center(100, "*")
    print(centered_message_time)
    print("*"*100)
    print("*"*100)


