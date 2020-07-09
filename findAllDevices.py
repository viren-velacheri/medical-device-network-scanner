#!/usr/bin/python

from wireless import Wireless 
import sh
import sys
import os
import pyshark
import subprocess
from scapy.all import *
from getmac import get_mac_address
from mac_vendor_lookup import MacLookup
from mac_vendor_lookup import AsyncMacLookup
import pandas as pd 
import numpy as np

# def find_manufacturers(potential_iot_devs):
#     companies = []
#     for mac in potential_iot_devs:
#         man = MacLookup().lookup(mac)
#     return companies

wireless = Wireless()
print(wireless.current() + "\n")
# capture = pyshark.LiveCapture(interface='en1')
# capture.sniff(timeout=10)
# for pkt in capture:
#     print(pkt)

# os.system("ifconfig")
# nmap = subprocess.Popen('nmap', stdout=subprocess.PIPE)
# ipout = nmap.communicate()[0]
# os.system("sudo nmap -sP 192.168.100.0/24")
# os.system("tshark -Ii en1 -c 10 > packets.txt")
# with open("packets.txt") as file:
#     file_contents = file.read()
#     print(file_contents)

# f = open("packets.txt", "r")
# lines = f.readlines()
# result=[]
# for line in lines:
#     result.append(line.split()[3])
# f.close()
# print(result)
# mac_addresses = get_mac_address(interface="en1")
# print(mac_addresses)
# The below line gets the list of interfaces 
os.system("tshark --list-interfaces") 
os.system("tshark -c 10 -i en1 -w mock.pcap")
os.system("tshark -r mock.pcap -T fields -e _ws.col.No. -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -E header=y -E separator=, -E occurrence=f > mock.pcap.csv")
f = open("mock.pcap.csv")
cols = {}
data = pd.read_csv(f)
for i, col in enumerate(data):
    if "_" in col:
        col = col[8:]
    cols[col.lower()] = i
devices_in_network = set()
for row in data.iterrows():
    data_row = row[1]
    dst = data_row[cols["destination"]]
    devices_in_network.add(dst)
mac = AsyncMacLookup()
# For some mac addresses like the below one I got an error for some reason...
# no idea why.
print(AsyncMacLookup().lookup("1:0:5e:0:0:fb"))
# for device in devices_in_network:
    # print(mac.lookup(device))
# Potential Commands that I could use from command line in program
# The below command lists IP and Mac Addresses as well as the affiliated company name
# arp-scan -I en1 -l    
# The below command lists all the found devices in network. 
# It shows their device name, IP address, and Mac Address
# arp -a
# Possible nmap commands to find more information on devices in network
# nmap -A -v -v 192.168.1.0/24 gives a lot of information, even SO in some cases
# nmap -sn 192.168.1.0/24 gives the MAC and IP addresses. Very useful information too
# The below command output could be put in text file to extract all the necessary details of devices.
# sudo nmap -PU 192.168.1.0/24 explains every IP address
# sudo nmap -sP 192.168.1.0/24    apparently is the same as one with -sn





