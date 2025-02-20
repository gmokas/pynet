from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates/exercise2')


my_vars = {
    "interface" : "Ethernet1/1",
    "ip_address1" : "10.1.100.1",
    "ip_address2" : "10.1.100.2",
    "netmask" : "/24",
    "as_number" : 22,
}



template_file = 'nxos_bgp.j2'
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)

