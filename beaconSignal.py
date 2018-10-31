from scapy.all import *
import sys
import time

c2IP = sys.argv[1]
beacon = IP(dst=c2IP)/TCP()

while True:
	send(beacon)
	time.sleep(600)
