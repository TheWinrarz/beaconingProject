#This python program should take a .pcap file as input and output a data file of observations

from scapy.all import *
import sys
import feather


pcap_filename = sys.argv[1]
label_filename = sys.argv[2]


pcap = rdpcap(pcap_filename)
labels = []
packet_dict = {}
f = open(label_filename, "r")
for i in f.readlines():
	labels.append(i)

for num, packet in enumerate(pcap):
	packet_dict["packet" + str(num)] = (packet[IP].src, packet[IP].dst, packet.time, labels[num].rstrip())


feather.write_dataframe(packet_dict, 'test.feather')

#Cleanup
f.close()
sys.exit()


