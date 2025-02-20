from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise4")


my_vrfs = [
    {"vrf_name": "blue", "rd_number": "100:1", "ipv4_enabled": True, "ipv6_enabled": True},
    {"vrf_name": "red", "rd_number": "100:2", "ipv4_enabled": True, "ipv6_enabled": True},
    {"vrf_name": "yellow", "rd_number": "100:3", "ipv4_enabled": True, "ipv6_enabled": True},
    {"vrf_name": "green", "rd_number": "100:4", "ipv4_enabled": True, "ipv6_enabled": False},
    {"vrf_name": "purple", "rd_number": "100:5", "ipv4_enabled": False, "ipv6_enabled": True},
]

j2_vars = {"my_vrfs": my_vrfs}

template_file = "vrfs.j2"
template = env.get_template(template_file)
output = template.render(**j2_vars)
print(output)

