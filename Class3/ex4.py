import json

filename = "arp.json"
with open(filename) as f:
    arp_data = json.load(f)

arp_dict = {}

for ipaddr_dict, mac_addr in arp_data.items()     
    if ip == "address":
       ip = "
        ip_list.append("{}/{}".format(ip_addr, prefix_length))
    elif ipv4_or_ipv6 == "ipv6":
            ipv6_list.append("{}/{}".format(ip_addr, prefix_length))

print("\nIPv4 Addresses: {}\n".format(ipv4_list))
print("\nIPv6 Addresses: {}\n".format(ipv6_list))
