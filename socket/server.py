import socket
s = socket . socket (socket . AF_INET, socket . SOCK_STREAM)
port = 12345
s . bind (('', port))
s . listen (5)
print "Listening..."
while True:
c.addr = s . accept ()
print 'Connection from ', addr
req = c.recv(1024)
print 'Request: ', req
req_file = open(req, "r")
c.send(req_file.read ())
req_file.close ()
c.close ()