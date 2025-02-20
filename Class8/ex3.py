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


cfg.lock()


try:
    cfg.lock()
    print("lock was successful")
except:
    print("the configuration is already locked")

cfg.unlock()


cfg.load("set system host-name python4life", format="set", merge=True)

print("Diff before rollback:\n")
cfg.pdiff()


cfg.rollback(0)

print("Diff after rollback:\n")
cfg.pdiff()


print("end of script")


