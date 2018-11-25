#This script will generate a .pcap file containing N packets (where N is specified by user)

from scapy.all import *
from random import randint, uniform
import sys

#Assign arguments to variables
pcap_name = sys.argv[1]
labelfile_name = sys.argv[2]
num_packets = int(sys.argv[3])
num_hosts = int(sys.argv[4])
num_beacons = int(sys.argv[5])


#In seconds
beacon_intervals = [60, 120, 300, 600, 900, 1800, 3600]
#one minute, two minutes, 5 minutes, 10 minutes, 15 minutes, 30 minutes, one hour

beacon_list = []
packet_list = []
label_list = []
network_ips = []
internet_ips = []

for i in range(num_hosts):
	network_ips.append("192.168." + str(randint(0,255)) + "." + str(randint(0,255)))

for i in range(num_hosts*2):
	internet_ips.append(str(randint(1,255)) + "." + str(randint(0,255)) + "." + str(randint(0,255)) + "." + str(randint(0,255)))

for i in range(num_beacons):
	beacon_list.append([network_ips[randint(0, len(network_ips) - 1)], beacon_intervals[randint(0, len(beacon_intervals)-1)], 0])

for i in range(num_packets / num_beacons):
	time = uniform(i - 1, i + 1)
	#if beacon_interval seconds since last beacon
	for beacon in beacon_list:
		if time - beacon[2] >= beacon[1]:
			#create beacon signal
			beacon[2] = time
			packet = IP(dst="8.8.8.8",src=beacon[0])/ICMP()
			packet.time = time
			packet_list.append(packet)
			label_list.append("beacon")
		else:
			#create background traffic
			source_ip = network_ips[randint(0,len(network_ips)-1)]
			packet = IP(dst=internet_ips[randint(0,len(internet_ips) - 1 )], src=source_ip)/ICMP()
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

#Cleanup
label_file.close()
sys.exit()
