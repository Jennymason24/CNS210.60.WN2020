# /usr/bin/python3

# import pcapy library
import pcapy

# Find and print devices
devices = pcapy.findalldevs()
print(devices)

# device, # of byte to capture per pocket, promiscuous mode, timeout (ms)
capture = pcapy.open_live("eno", 65536, 1, 0)

count = 1
while count:
    # print count of captured pockets
    (header, payload) = capture.next()
    print(count)
    count = count + 1