#/usr/bin/python

import pcapy 
from struct import *

pcap_file = pcapy.open_offline("file.pcap")
count = 1

while count:
    print("Packet #: ", count)
    count = count + 1
    (header, payload) = pcap_file.next()
    12hdr = payload[:14]
    12data = unpack("!6s6sH", 12hdr)
    srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(12hdr[0]), ord(12hdr[1]), ord(12hdr[2]), ord(12hdr[3]), ord(12hdr[4]), ord(12hdr[5]))
    dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(12hdr[6]), ord(12hdr[7]), ord(12hdr[8]), ord(12hdr[9]), ord(12hdr[10]), ord(12hdr[11]))
    print("Source MAC: ", scrmac," Destination MAC: ", dstmac)

# get IP header, which is 20 bytes long
# then upack it into what it is 

    ipheader = unpack('!BBHHHBBH4s4s' , payload[14:34])
    timetolive = ipheader[5]
    protocol = ipheader[6]
    print("Protocol ", str(protocol), "Time To Live: ", str(timetolive))