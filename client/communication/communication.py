import socket
from pickle import loads, dumps


class ServerConnection:
    SERVER_NAME = 'localhost'
    PORT = 6969
    PACKET_SIZE = 16
    HEADER_SIZE_LENGTH = 4

    def __init__(self):
        """
        initialize connection to db
        """
        try:
            self._connection = socket.socket()
            self._connection.connect((ServerConnection.SERVER_NAME, ServerConnection.PORT))
            self.connected = True
        except ConnectionRefusedError:
            self.connected = False

    def send(self, msg: dict):
        """
        send requests to server using pickle
        """
        msg = dumps(msg)
        msg = bytes(f"{len(msg):<{ServerConnection.HEADER_SIZE_LENGTH}}", 'utf-8') + msg
        self._connection.send(msg)

    def receive(self):
        """
        receive responses from server
        """
        full_msg = b''

        try:
            while True:
                full_msg += self._connection.recv(ServerConnection.PACKET_SIZE)
                if full_msg:
                    msg_len = int(full_msg[:ServerConnection.HEADER_SIZE_LENGTH].strip())

                    while len(full_msg) - ServerConnection.HEADER_SIZE_LENGTH < msg_len:
                        msg = self._connection.recv(ServerConnection.PACKET_SIZE)
                        full_msg += msg

                    return loads(full_msg[ServerConnection.HEADER_SIZE_LENGTH:])
        except Exception as e:
            print(e.__str__())


conn = ServerConnection()
