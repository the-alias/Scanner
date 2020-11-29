#!/usr/bin/python3
from netaddr import *
import socket,re
############################################################################
def porter(reg_port):
	if reg_port:
		reg_range = re.search("-",reg_port)
		reg_comma = re.search(",",reg_port)
		if reg_range:
			ports = range(int(reg_port.split('-')[0]),int(reg_port.split('-')[1]))
		elif reg_comma:
			ports=[]
			str_ports = reg_port.split(",")
			for port in str_ports:
				ports.append(int(port))
		else:
			ports = [int(reg_port)]
		return ports
	else:
		return range(1,65565)
############################################################################
def IPChooser(reg_target):
	ips=[]
	reg_range = re.search("-",reg_target)
	reg_net = re.search("/\S+",reg_target)
	if reg_range:
		reg_sides=reg_target.split('-')
		if valid_ipv4(reg_sides[0]) and valid_ipv4(reg_sides[1]):
			ips = IPRange(reg_sides[0],reg_sides[1])
	elif reg_net:
		test = reg_target.split("/")[0]
		if valid_ipv4(test):
			ips = IPNetwork(reg_target)
	else:
		if valid_ipv4(reg_target):
			ips = [IPAddress(reg_target)]
		else:
			test=hoster(reg_target)
			if valid_ipv4(test):
				ips = [IPAddress(test)]
	if ips==[]:
		print(reg_target,"is not a valid target!")
	return ips
	
############################################################################
def hoster(reg_host):
	return socket.gethostbyname(reg_host)
############################################################################
def target_parser(inp):
	#Deal with file based targets
	reg_file = re.search("\s-f\s\S+",inp)
	#################################################################
	#fill
	#################################################################
	#Make targets list
	ips=[]
	reg_target = re.search("\s-t\s\S+",inp)
	if reg_target:
		target_clean=reg_target.group().split(' ')[2]
	else:
		print("I'm here")
		return "Error","No targets specified"
	reg_comma = re.search(",",reg_target.group())
	if reg_comma:
		targets=target_clean.split(',')
	else:
		targets=[target_clean]
	#Make ip list
	for target in targets:
		if target:
			targets= target
			ips.extend(IPChooser(targets))
	#Make port list
	reg_port = re.search("\s-p\s\S+",inp)
	if reg_port:
		target_ports = reg_port.group().split(' ')[2]
		ports = porter(target_ports)
	else:
		ports = porter("")
	str_ips=[]
	for ip in ips:
		str_ips.append(str(ip))
	return str_ips,ports
############################################################################
