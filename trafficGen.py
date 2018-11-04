#This script will generate a .pcap file containing N packets (where N is specified by user)
#There will be a single beacon with an interval specified by the user


from scapy.all import *
from random import randint, uniform
import sys

pcap_name = sys.argv[1]
labelfile_name = sys.argv[2]
num_packets = int(sys.argv[3])
beacon_interval = int(sys.argv[4])

last_beacon = 0

packet_list = []
label_list = []

network_ips = []

for i in range(10):
	network_ips.append("192.168." + str(randint(0,255)) + "." + str(randint(0,255)))

for i in network_ips:
	print(i)


for i in range(num_packets):
	time = uniform(i - 1, i + 1)
	#if beacon_interval seconds since last beacon
	if time - last_beacon >= beacon_interval:
		#create beacon signal
		last_beacon = time
		source_ip = network_ips[randint(0,len(network_ips)-1)]
		packet = IP(dst="8.8.8.8",src=source_ip)/ICMP()
		packet.time = time
		packet_list.append(packet)
		label_list.append("beacon")
	else:
		packet = IP(dst=str(randint(0,255)) + '.' + str(randint(0,255)) + '.' + str(randint(0,255)) + '.' + str(randint(0,255)))/ICMP()
		packet.time = time
		packet_list.append(packet)
		label_list.append("non-beacon")

print("Packets generated")
print(len(packet_list))
wrpcap(pcap_name, packet_list)
print("Written to " + pcap_name)



label_file = open(labelfile_name, "w+")
for i in label_list:
	label_file.write("%s\n" % i)
print("Labels written to " + labelfile_name)

sys.exit()
