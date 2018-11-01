from scapy.all import *
import sys
import time

c2IP = sys.argv[1]
interval = int(sys.argv[2])
beacon = IP(dst=c2IP)/ICMP()

while True:
	uns, ans = sr(beacon, timeout=interval/2)
	ans.summary()
	print("#######")
	uns.summary()
	time.sleep(interval/2)
