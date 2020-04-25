#!/usr/bin/python3

# import ftp library
import ftplib

# Connect to my VM(
f = ftplib.FTP("192.168.2.166")

try:
    # Username and password for login 
    f.login("kateo", "P@ssw0rd")
    # expect welcome
    print(f.getwelcome())
    # f.delete("test")
    print(f.dir())
    f.set_pasv(1)
    # f.storbinary("STOR test", open("test", "rb"))
    # print(f.dir())
except Exception as e:
    print("Exeption: ", e)
finally:
    f.close()