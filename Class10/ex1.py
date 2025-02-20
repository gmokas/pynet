import time
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import network_devices



def ssh_conn(device,show_command):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(show_command)
    return output




if __name__ == "__main__":
    
    show_command = "show version"

    start_time = datetime.now()

    for device in network_devices:
        output = ssh_conn(device,show_command)
        print("#"*100)
        print(output)
        end_time = datetime.now()
        print("#"*100)
        print("Time for ", device['host'], " is: ", end_time - start_time)
        print("#"*100)
    end_time = datetime.now()
    print("*"*100)
    print("Time for the whole script is:", end_time - start_time)
    print("*"*100)


