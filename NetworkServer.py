#/usr/bin/python3

import socket 

#open IPv4 socket, TCP
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT stat e, without waiting for its natural timeout to expire.
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binds service to port 5555
mysocket.bind(('', 5555))

# listens on the socket
mysocket.listen(0)

# Saves output data coming in of size 512
c, addr = mysocket.accept()
data = c.recv(512)

# if there is data print out where it came from, the IP address and the data itself
if data:
    print("connection from: ", addr[0], ":", data)

# close socket
mysocket.close()
