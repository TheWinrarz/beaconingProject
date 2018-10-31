from scapy.all import *

class Beacon:

	#interval and variance are in seconds 
	def __init__(self, c2, ip, interval, variance):
		self.c2IP = c2
		self.IP = ip
		self.interval = interval
		self.variance = variance

	def __str__(self):
		return ("Beacon IP: " + self.IP + "\nC2IP: " + self.c2IP + "\nInterval: " + str(self.interval) + "\nVariance: " + str(self.variance))

	#could there be other parameters?
	def signal(self):
		return IP(dst=self.c2IP, src=self.IP)/TCP()
