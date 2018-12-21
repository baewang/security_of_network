import socket
s = socket . socket (socket . AF_INET, socket . SOCK_STREAM)
port = 12345
s.bind (('', port))
s.listen (5)
print "Listening..."
while True:
c, addr = s.accept ()
print 'Connection from ', addr
req = c.recv(1024)
print 'Request: ', req
data = c.recv(1024)
print 'Request: ', data
rcv_file = open (req, "w")
rcv_file.write (data)
c.send("ok")
rcv_file.close ()
c.close ()
