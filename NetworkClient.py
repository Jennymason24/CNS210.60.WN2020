#/usr/bin/python3
#-*- coding: utf-8
import socket

# create an INET (IPv4) streaming socket (TCP)
mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now connecting to my own system on port 5555
mysocket.connect(('localhost', 5555))

# Set msg to be a byte string
msg=b"hi, sending data over a socket \n"

# attempt to send the message over the socket
try:
    mysocket.endall(msg)
except mysocket.errno as e:
      print("Socket error", e)
finally:
      # close socket when we're done
      mysocket.close()