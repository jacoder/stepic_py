__author__ = 'oleg'
### Sequential Echo-server

import socket

CLIENTS_NUM = 10
MSG_QUEUE_LNT =10
STOP_CMD="close"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(MSG_QUEUE_LNT)
for i in range( 0,CLIENTS_NUM):
# while True:
    conn, addr = s.accept()
    print "Client #%i from %s"%(i,addr)
    while True:
        data = conn.recv(7)
        # if not data: break
        print(data)
        print "STOP cmd position: %i"%data.find(STOP_CMD)
        # __debug__.
        if (data.find(STOP_CMD)==0):
            print "STOP command ReCeiVeD from %s"%addr
            break
        else:
            conn.send(data)
    conn.close()
# break
