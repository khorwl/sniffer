import socket


class Reader:
    def __init__(self):
        self.s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

    def get_package(self):
        return self.s.recvfrom(70000)[0]
