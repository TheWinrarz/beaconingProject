from scapy.all import *
import sys

num = int(sys.argv[1])
print("number specified " +  str(num))
#only captures TCP packets (probably not safe assumption)
packets = sniff(count=num, prn = lambda x: x.summary(), timeout=10, filter="tcp")
print("packets sniffed")
wrpcap("sampleTraffic.pcap", packets)
print("packets saved")
