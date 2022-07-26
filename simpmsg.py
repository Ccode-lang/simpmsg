import socket

class simpserve(object):
    def __init__(self):
        self.host = None
        self.port = None
        self.msgsocket = None
        self.serverstatus = False
    def initserver(self, host1, port1):
        self.host = host1
        self.port = port1
        self.msgsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.msgsocket.bind((self.host, self.port))
        self.msgsocket.listen(100)
        self.serverstatus = True
    def getmsg(self):
        if self.serverstatus:
            clientsocket, address = self.msgsocket.accept()
            return [address[0], str(clientsocket.recv(1024).decode())]
        else:
            raise OSError("Server never started, can't reacive message")
    def sendmsg(self, msg, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host,port))
        s.send(msg.encode())
        s.close()
