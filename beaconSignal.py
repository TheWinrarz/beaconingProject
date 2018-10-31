from scapy.all import *

while True:
	packet = IP(dst="8.8.8.8", src="1.1.1.1")
	sleep(6000)