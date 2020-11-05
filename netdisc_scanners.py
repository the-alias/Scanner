#!/usr/bin/python3
from scapy.all import *
import random
############################################################################
def check_alive_ping(ips,timeout=1):
	ping_alive_list = []
	ping_dead_list =[]
	ans,unans = sr(IP(dst=ips)/ICMP(),timeout=timeout,verbose=0)
	#print(ips)
	for answer in ans:
		ping_alive_list.append(answer[0].dst)
		#print("Alive",answer[0].dst)
	for un in unans:
		ping_dead_list.append(un[0].dst)
		#print("Unalive",un[0].dst)
	if ping_alive_list == [] and timeout<5:
		ping_alive_list,ping_dead_list = check_alive_ping(ips,timeout+1)
	return ping_alive_list,ping_dead_list
############################################################################
#level:
#0 - tcp 2-6 most common ports
#1 - tcp 20-60 most common ports
#2 - tcp 1000 most common
#3 - tcp last resort (all ports)
#4 - udp 2-6 common 
############################################################################
def check_alive_sample(ips,level):
	#sample 2-6 most common ports
	with open('1000_pop_ports','r') as f:
		tmp=[]
		for i in f.readlines():
			tmp.append(int(i))
		lvl_list=[
		[22,445,53,80,443],
		tmp[0:50],
		tmp,
		list(range(1,65535))
		]
	sample_alive_list=[]
	sample_dead_list=[]
	ans,unans = sr(IP(dst=ips)/
		TCP(dport=lvl_list[level],
		sport=random.randint(50000,65635),
		flags='S',
		seq=random.randint(0,2**32)),
		timeout=1,
		verbose=0)
	for answer in ans:
		if answer[0].dst not in sample_alive_list:
			sample_alive_list.append(answer[0].dst)
	for un in unans:
		if un[0].dst not in sample_dead_list and un[0].dst not in sample_alive_list:
			sample_dead_list.append(un[0].dst)
	return sample_alive_list,sample_dead_list
######################################	ans,unans = sr(IP(dst=ips)/TCP(dport=lvl,sport=random.randint(50000,65635),flags='S',se######################################
def arp_scan(ips):
	pass
