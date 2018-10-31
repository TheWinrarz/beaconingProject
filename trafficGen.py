from scapy.all import *
from beaconClass import Beacon

#define network, class, network ip, number of hosts...

#define beacon form (done in Beacon class)

beacon1 = Beacon("10.20.30.40", "192.168.1.77", 300, 5)
print(beacon1.signal().show())
#generate N beacon signals

#inject into captured traffic
