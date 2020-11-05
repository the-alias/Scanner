#!/usr/bin/python3
from port_scanners import *
from netdisc_scanners import *
from data_set_parsers import *
import sys,re
############################################################################
def cli(inp):
	#Help message for tool usage
	help_msg='''
	Disclaimer: Does not support IPV6
	Usage: python sweep_scan.py -t <targets> <options>:
	Options:
		-t <target_set> 				# Targets for scan 
										# (0.0.0.0 or 0.0.0.0-0.0.0.5 or 0.0.0.0/10 or <target_domain>)
		-h 								# Print Help message
		-S								# Syn Scan/Half Open Scan
		-F 								# SA Scan/Full Open Scan (with banners)
		-p 	<ports>						# Ports for scanning - default all ports
										# (22 or 22,25,50 or 22-200)
		-P 								# Ping scan
		-f 								# Use file as target list
	'''
#	try:
	#Regex for each option in the help menu, all are mutually exclusive
	ips,ports=target_parser(inp)
	if ips=="Error":
		print("No targets specified",help_msg)
		sys.exit()
	reg_help = re.search("\s-h",inp)
	reg_half_open= re.search("\s-S",inp)
	reg_full_open  = re.search("\s-F",inp)
	reg_ping = re.search("\s-P",inp)
	if reg_ping:
		a,d=check_alive_ping(ips)
		for i in a:
			print(i,"Is a alive according to icmp")
		for i in d:
			print(i,"Is a dead according to icmp")
	elif reg_half_open:
		print("Running half open scan:")
		print(half_open_port(ips,ports))
	elif reg_full_open:
		print("Running full open scan:")
		print(full_open_port(ips,ports))
	elif reg_help:
		print(help_msg)
	else:
		print(help_msg)
	#except:
	#	print(help_msg)
############################################################################
def main():
	user_input=' '.join(sys.argv)
	ips,ports=target_parser(user_input)
	ping_live,ping_dead = check_alive_ping(ips)
	print(ping_live,ping_dead)
	sample_live,sample_dead = check_alive_sample(ping_dead,2)
	print(sample_live,sample_dead)
	#cli(user_input)
############################################################################
if __name__ == '__main__':
	main()
