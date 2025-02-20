from jnpr.junos import Device
from getpass import getpass
from pprint import pprint
from jnpr_devices import srx2
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable

device = Device(**srx2)
device.open()


def check_connected():
    connection = device.connected
    print("The connection to the device is :", connection)
    
def port_check():
    port = device.port
    print("the port that is used for this netconf connection is :", port)

def gather_routes():
    routes = RouteTable(device)
    routes.get()
    print("Below you could fine the routing table:\n")
    pprint(routes.items())

def gather_arp_table():
    arp = ArpTable(device)
    arp.get()
    print("Below you could fine the arp entries:\n")
    pprint(arp.items())
    return arp

def print_output():

    print("#"*100, "\n")
    check_connected()

    print("#"*100, "\n")
    
    print("This is the hostname :")
    print("Device hostname: ", device.hostname)
    print("username: ", device.user)
    print("#"*100, "\n")
    
    port_check()

    print("#"*100, "\n")

    gather_routes()

    print("#"*100, "\n")
    gather_arp_table()




print_output()




#This program should have four separate functions:
#1. check_connected() - Verify that your NETCONF connection is working. You can use the .connected attribute to check the status of this connection.
#2. gather_routes() - Return the routing table from the device.
#3. gather_arp_table() - Return the ARP table from the device.
#4. print_output() - A function that takes the Juniper PyEZ Device object, the routing table, and the ARP table and then prints out the: hostname, NETCONF port, username, routing table, ARP table

