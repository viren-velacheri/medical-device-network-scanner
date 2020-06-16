#!/usr/bin/python

from wireless import Wireless 
import sh
import os
import pyshark
import subprocess
from scapy.all import *
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
os.system("tshark -Ii en1 -c 10 > packets.txt")
with open("packets.txt") as file:
    file_contents = file.read()
    print(file_contents)

f = open("packets.txt", "r")
lines = f.readlines()
result=[]
for line in lines:
    result.append(line.split()[3])
f.close()
print(result)



