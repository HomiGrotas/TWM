import socket
from json import loads, dumps
from os import environ
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

AES_PUBLIC_KEY = environ['AES_PUBLIC_KEY'].encode()


class ServerConnection:
    SERVER_NAME = 'localhost'
    PORT = 6969
    PACKET_SIZE = 2048
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
        send requests to server using json
        """
        msg = dumps(msg).encode()
        encrypted_msg = ServerConnection.encrypt(msg)
        encrypted_msg_packet = bytes(f"{len(msg):<{ServerConnection.HEADER_SIZE_LENGTH}}", 'utf-8') + encrypted_msg
        self._connection.send(encrypted_msg_packet)

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

                    decrypted = ServerConnection.decrypt(full_msg[ServerConnection.HEADER_SIZE_LENGTH:])
                    if decrypted:
                        return loads(decrypted)
        except Exception as e:
            print('rcv', e.__str__())
            raise e

    @staticmethod
    def encrypt(msg_bytes: bytes):
        cipher = AES.new(AES_PUBLIC_KEY, AES.MODE_CBC)
        ciphertext = cipher.iv + cipher.encrypt(pad(msg_bytes, AES.block_size))
        return ciphertext

    @staticmethod
    def decrypt(cipher_text):
        iv = cipher_text[:16]
        cipher = AES.new(AES_PUBLIC_KEY, AES.MODE_CBC, iv)
        try:
            plain_text = unpad(cipher.decrypt(cipher_text), AES.block_size)[16:]
        except ValueError:
            plain_text = b''
        return plain_text


conn = ServerConnection()
