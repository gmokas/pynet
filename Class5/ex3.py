from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/exercise3")



vrf_vars = {
    "vrf_name": "blue",
    "rd_number": "100:1",
    "ipv4_enabled": True,
    "ipv6_enabled": False,
}

template_file = "vrf.j2"
template = env.get_template(template_file)
output = template.render(**vrf_vars)
print(output)

