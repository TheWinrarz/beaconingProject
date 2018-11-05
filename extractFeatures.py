#This python program should take a .pcap file as input and output a data file of observations

from scapy.all import *
import sys

pcap_filename = sys.argv[1]
label_filename = sys.argv[2]


pcap = rdpcap(pcap_filename)
labels = []
packet_dict = {}
f = open(label_filename, "r")
for i in f.readlines():
	labels.append(i)

for num, packet in enumerate(packets):
	packet_dict["packet" + str(num)] = (packet[IP].src, packet[IP].dst, packet.time, labels[num])



#Cleanup
f.close()
sys.exit()


