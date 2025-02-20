from netmiko import ConnectHandler






def ssh_command(device,show_command):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(show_command)
    device_output = f"{device['host']}, output"
    print(device_output.center(100, "#"))
    print("#"*100)
    print(output)
    print("#"*100)
    net_connect.disconnect()


def ssh_command2(device,show_command):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(show_command)
    net_connect.disconnect()
    return output
