#!/usr/bin/python

# Note: In Scapy v2 use from scapy.all import * instead of from scapy import *.
from scapy.all import *

frame = Ether(dst="00:DE:AD:BE:EF:00")/IP(dst="10.10.10.100")/TCP()/"Check this out"

print(frame)
sendp(frame)