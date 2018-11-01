from scapy.all import *
import sys

# host에 연결된 host 스캐닝하는 코드
print("Scanning...")
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") /
                 ARP(pdst=sys.argv[1]), timeout=0.5)

print '\nMAC\t\t\tIP\n'
for snd, rcv in ans:
    print rcv.sprintf(r"%Ether.src% %ARP.psrc%")

print("\n>>>scan complete")
