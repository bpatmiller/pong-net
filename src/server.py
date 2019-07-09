import sys
import time
import socket
import simplejson as json
import settings
import select

paddles = {}


def getHost():
    """  returns the local host address of the machine
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    host = sock.getsockname()[0]
    sock.close()
    return host


class PongServer:
    def __init__(self, host, port):
        self.inputs = []
        self.channel = {}
        # AF_INET corresponds to IPV4 host:port addressing
        # SOCK_STREAM corresponds to sending data via TCP packets
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # SOL_SOCKET specifies the level we operate on
        # SO_REUSEADDRE indicates that we can reuse local addresses - a socket
        # can bind unless when there is an active listening socket already
        # bound to that address. the 1 that follows indicates we enable this
        # option
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # now we get our local host address if not provided
        if host == "":
            host = getHost()
        # bing our server to the chosen host:port and then listen
        self.host = host
        self.port = port
        self.server.bind((host, port))
        self.server.listen(0)

    def loop(self):
        self.inputs.append(self.server)
        while True:
            time.sleep(settings.DELAY)
            inp, outp, exceptr = select.select(self.inputs, [], [])
            for self.i in inp:
                if self.i == self.server:
                    self.accept()
                    break
                else:
                    self.data = self.i.recv(settings.BUFFER_SIZE)
                if len(self.data) == 0:
                    self.close()
                else:
                    self.receive()

    def accept(self):
        csock, caddr = self.server.accept()
        paddles[caddr[1]] = {}
        self.inputs.append(csock)
        print("client at", caddr, "connected")

    def close(self):
        caddr = self.i.getpeername()
        del(paddles[caddr[1]])
        self.inputs.remove(self.i)
        print("client at", caddr, "disconnected")

    def receive(self):
        pid = self.i.getpeername()[1]
        paddles[pid] = json.loads(self.data)
        self.i.send(json.dumps(paddles).encode())


if __name__ == '__main__':
    host = settings.SERVER_IP if len(sys.argv) < 1 else sys.argv[1]
    port = settings.SERVER_PORT if len(sys.argv) < 2 else sys.argv[2]
    # create server
    server = PongServer(host, port)
    print(":: server initialized [" +
          server.host + ":" + str(server.port) + "]")
    # listen
    try:
        server.loop()
    except KeyboardInterrupt:
        sys.exit(1)
