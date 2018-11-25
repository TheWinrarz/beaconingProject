#This python program should take a .pcap file as input and output a data file of observations

from scapy.all import *
import sys




pcap_filename = sys.argv[1]
#label_filename = sys.argv[2]


pcap = rdpcap(pcap_filename)
#labels = []
packet_list = []
#f = open(label_filename, "r")
#I think i may need to use ^this^ now

#Saves a list of packets, source ip, dest ip, and time
#time will be used to calculate period & variance
for packet in (pcap):
	packet_list.append((packet[IP].src, packet[IP].dst, packet.time))

#extract features from packets
#srcIP: Done
#dstIP: Done
#numRepitions: Done
#AvgPeriod: Done
#varPeriod: Not Done

#Dictionary where keys are (srcIP, dstIP) tuples and value is amount of times a packet is sent
repititions = {}

#Python, where everything is a dictionary!
start_end_times = {}
period_log = {}
avg_period = {}

for pkt in packet_list:
	srcIP = pkt[0]
	dstIP = pkt[1]
	time = pkt[2]

	if (srcIP, dstIP) not in repititions:
		repititions[(srcIP,dstIP)] = 0

	else:
		#should this be 0 or 1
		repititions[(srcIP,dstIP)] += 1

	if (srcIP, dstIP) not in start_end_times:
		start_end_times[(srcIP,dstIP)] = [time, time]
		period_log[(srcIP, dstIP)] = []
	else:
		period_log[(srcIP,dstIP)].append(time - start_end_times[(srcIP, dstIP)][1])
		start_end_times[(srcIP,dstIP)][1] = time

for entry in repititions:
	srcIP = entry[0]
	dstIP = entry[1]
	if repititions[entry] != 0:

		avg_period[entry] = sum(period_log[entry]) / repititions[entry]

for key in avg_period:
	if repititions[key] > 20:
		print(key, avg_period[key], repititions[key])

#calculate variance
#observation_list = []
#for key in repititions:
#	print(key)
#	print(str(key[0]) + ":" + str(key[1]) + ":" + str(repititions[key]) + ":" + str(avg_period[key]))
#	observation_list.append((str(key[0]), str(key[0]), repititions[key], avg_period[key]))

#Cleanup
#f.close()
sys.exit()


