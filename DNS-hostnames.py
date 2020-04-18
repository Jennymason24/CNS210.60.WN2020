#/usr/bin/python3
import socket

print("DNS lookup by IP Address:", socket.gethostbyaddr("8.8.8.8"))

#Lookup IP via host name server:
print("\n")
print("DNS lookup by name:", socket.gethostbyname("yahoo.com"))

#Hardcoded from /etc/hosts, this will NOT WORK on your machine unless you add this entry:
print("\n")
print("DNS lookup by name:", socket.gethostbyname("ctf.carhackingvillage.com"))

#This lookup includes all IP address responses instead of just one
print("\n")
print("DNS lookup with getaddrinfo:", socket.getaddrinfo("amazon.com", 53))

#This is to lookup the fully qualified domain name 
print("\n")
print("FQDN lookup:", socket.getfqdn("google.com"))