from scapy.all import *
from beaconClass import Beacon
import sys

interval = int(sys.argv[1])
print("interval specified " +  str(num))
packets = []
beacon = Beacon("10.20.30.40", "192.168.1.77", 300, 5)
#only captures TCP packets (probably not safe assumption)
while True:
	packets.append(sniff(prn = lambda x: x.summary(), timeout=interval, filter="tcp"))

print("packets sniffed")
wrpcap("sampleTraffic.pcap", packets)
print("packets saved")
