#!/usr/bin/python3
from scapy.all import *
import random
############################################################################
def full_open_port(ips,ports):
	result=""
	for ipx in ips:
		for dport in ports:
			print("Checking",ipx,dport)
			ip = IP(dst=str(ipx))
			sport=random.randint(50000,65635)
			seq = random.randint(0,2**32)
			SYN = TCP(sport=sport,dport=dport,flags='S',seq=seq)
			p = ip/SYN
			a = sr1(p,verbose=0,timeout=1)
			if a:
				ack = a[TCP].seq
				ACK = TCP(sport=sport,dport=dport,flags='A',ack=ack+1,seq=seq+1)
				a2 = sr1(ip/ACK,verbose=0,timeout=1)
				result+=str(ipx)+" "+str(dport)+" "+str(a2.load)+" "+"Open\n"
			else:
				result+=str(ipx)+" "+str(dport)+" "+"Closed\n"
	return result
############################################################################
def half_open_port(ips,ports):
	result=""
	for ipx in ips:
		for dport in ports:
			print("Checking",ipx,dport)
			ip = IP(dst=str(ipx))
			sport=random.randint(50000,65635)
			seq = random.randint(0,2**32)
			SYN = TCP(sport=sport,dport=dport,flags='S',seq=seq)
			p = ip/SYN
			a = sr1(p,verbose=0,timeout=1)
			if a:
				if a[TCP].flags == 'SA':
					result+=str(ipx)+" "+str(dport)+" "+'Open\n'
				else:
					result+=str(ipx)+" "+str(dport)+" "+'Closed\n'
			else:
				result+=str(ipx)+" "+str(dport)+" "+'Closed\n'
	return result
############################################################################
def xmas(ip,ports):
	
	passfrom scapy.all import *
############################################################################

