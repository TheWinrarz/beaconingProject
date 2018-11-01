#This script will generate a .pcap file containing N packets (where N is specified by user)
#There will be a single beacon with an interval specified by the user


from scapy.all import *
from random import randint, uniform
import sys

pcap_name = sys.argv[1]
num_packets = int(sys.argv[2])
beacon_interval = int(sys.argv[3])
last_beacon = 0

packet_list = []
label_list = []


for i in range(num_packets):
	time = uniform(i - 1, i + 1)

	if time - last_beacon >= beacon_interval:
		last_beacon = time
		packet = IP(dst="8.8.8.8")/ICMP()
		packet.time = time
		packet_list.append(packet)
	else:
		packet = IP(dst=str(randint(0,255)) + '.' + str(randint(0,255)) + '.' + str(randint(0,255)) + '.' + str(randint(0,255)))/ICMP()
		packet.time = time
		packet_list.append(packet)

print("Packets generated")
print(len(packet_list))
wrpcap(pcap_name, packet_list)
print("Written to " + pcap_name)

