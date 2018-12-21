import socket
import sys
s = socket . socket (socket . AF_INET, socket . SOCK_STREAM)
s . connect ((sys . argv [1], int (sys . argv [2])))
s . send (sys . argv [3])
data = s . recv (1024)
rcv_file = open (sys . argv [3], "w")
rcv_file . write (data)
rcv_file . close ()
s . close ()
print 'Done!'

import socket
import sys
s = socket . socket (socket . AF_INET, socket . SOCK_STREAM)
s . connect ((sys . argv [1], int (sys . argv [2])))
s.send (sys.argv[3])
req_file = open(sys.argv[3], "r")
s.send(req_file.read())
data = s.recv(1024)
req_file.close ()
s.close ()
print 'Done!'