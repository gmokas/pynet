from jnpr.junos import Device
from getpass import getpass
from pprint import pprint
from jnpr_devices import srx2
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.utils.config import Config

device = Device(**srx2)
device.open()
device.timeout = 60

cfg = Config(device)

def gather_routes(device):
    routes = RouteTable(device)
    routes.get()
    return routes


routes = gather_routes(device)
print("Below you could find the routing table before any change:\n")
pprint(routes.items())



cfg.lock()

cfg.load(path="static_routes.conf", format="text", merge=True)

cfg.pdiff()

cfg.commit()

cfg.unlock()

routes = gather_routes(device)
print("Below you could find the routing table after the change:\n")
pprint(routes.items())



cfg.lock()
cfg.load("delete routing-options static route 203.0.113.5/32", format="set", merge=True)
cfg.load("delete routing-options static route 203.0.113.200/32", format="set", merge=True)
if cfg.diff() is not None:
    cfg.commit()
cfg.pdiff()


cfg.unlock()

routes = gather_routes(device)
print("Below you could find the routing table after the deletion of the routes:\n")
pprint(routes.items())



print("end of script")


