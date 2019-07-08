import sys
import time
import socket
import simplejson as json


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
        # create
        self.inputs = []
        self.channel = {}

    def loop(self):
        self.inputs.append(self.server)
        while True:
            time.sleep(0.016)

    def accept(self):
        pass

    def close(self):
        pass

    def receive(self):
        pass


if __name__ == '__main__':
        # load config
    with open('settings.json') as sj:
        config = json.load(sj)
    host = config['SERVER_IP']
    port = config['SERVER_PORT']
    # create server
    server = PongServer(host, port)
    # listen
    print(":: server initialized [" + server.host + ":" + str(server.port) + "]")
    try:
        server.loop()
    except KeyboardInterrupt:
        sys.exit(1)
