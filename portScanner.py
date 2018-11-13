#PortSacnner 란

#Nmap이라는 자체 명령어를 사용하거나
#Scapy를 사용하여 py코드 작성 가능

from scapy.all import *
for x in range(1, 127):
    syn = IP (dst = "10.0.2.15") / TCP (sport = RandShort (), dport = x, flags = "S")
    rst = sr1 (syn, verbose = 0)
    if rst [tcp] . flags == "SA":
        print (str (x) + " is open")
