#!/usr/bin/python3

import socket

# send to multicast group on port 5775
mgrp = "224.1.1.1"
mport = 5775

# creating socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_SGRAM, socket.IPPROTO_UDP)
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

for i in range(1,10):
    mysocket.sendto(b"HELLO", (mgrp, mport))

print("Message sent to multicast")