import sys
import feather
import pandas as pd
from random import randint, uniform

num_packets = int(sys.argv[1])
beacon_interval = int(sys.argv[2])

last_beacon = 0

#include labels
packet_dict = {}

network_ips = []
internet_ips = []

for i in range(10):
	network_ips.append("192.168." + str(randint(0,255)) + "." + str(randint(0,255)))

for i in range(100):
	internet_ips.append(str(randint(1,255)) + "." + str(randint(0,255)) + "." + str(randint(0,255)) + "." + str(randint(0,255)))

beacon_ip = network_ips[randint(0, len(network_ips) - 1)]

for i in range(num_packets):
	time = uniform(i - 1, i + 1)
	if time - last_beacon >= beacon_interval:
		last_beacon = time
		packet_dict["packet" + str(i)] = (beacon_ip, "8.8.8.8", time, "beacon")

	else:
		source_ip = network_ips[randint(0, len(network_ips) - 1)]
		destination_ip = internet_ips[randint(0, len(internet_ips) - 1)]
		packet_dict["packet" + str(i)] = (source_ip, destination_ip, time, "non-beacon")

df = pd.DataFrame(packet_dict)

df.T.to_csv("test")


