import socket
from pickle import loads, dumps
from select import select
from server.rooms import Room
from server.utils.operations import db_operation, chat_operation, mail_operation

__author__ = "Nadav Shani"

# chat rooms
rooms = {
    'cooking': Room(0),
    'sports': Room(1),
    'gaming': Room(2),
}


class Server:
    PACKET_SIZE = 16
    HEADER_SIZE_LENGTH = 4

    def __init__(self, host='localhost', port=6969, users=50):
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # ipv4, TCP
        self.__server_socket.bind((host, port))  # bind on localhost on specific port
        self.__server_socket.listen(users)       # max amount of connections

        self.__clients = [self.__server_socket]  # ClientConnection list
        self._run()

    def _run(self):
        """
        run server functions
        :return: None
        """
        print("SERVER IS RUNNING")
        while True:
            readable, writable, exceptional = select(self.__clients, self.__clients, [])
            self.__handle_readable(readable)

    def __handle_readable(self, readable: list):
        """
        handles all the readable sockets
        """
        for socket_obj in readable:

            # if there is a new connection
            if socket_obj is self.__server_socket:
                connection, client_address = self.__server_socket.accept()
                self.__clients.append(connection)
                print("+ New connection from:", client_address)

            else:
                try:
                    # get request from client and return an appropriate response
                    msg = Server.receive_data(socket_obj)
                    if msg:
                        response = Server.handle_client_data(msg, socket_obj)
                        Server.send(socket_obj, {'response': response})

                # client disconnected
                except ConnectionResetError:
                    print("+ Client disconnected")
                    self.__clients.remove(socket_obj)

    @staticmethod
    def receive_data(socket_obj) -> dict:
        """
        receives messages from the client socket
        :param socket_obj: client socket
        :return: generator object (with messages)
        """
        # get messages from client
        full_msg = socket_obj.recv(Server.PACKET_SIZE)

        if full_msg:
            msg_len = int(full_msg[:Server.HEADER_SIZE_LENGTH].strip())  # get msg length

            while len(full_msg) - Server.HEADER_SIZE_LENGTH < msg_len:   # load the full message
                msg = socket_obj.recv(Server.PACKET_SIZE)
                full_msg += msg

            return loads(full_msg[Server.HEADER_SIZE_LENGTH:])

    @staticmethod
    def send(socket_obj_c: socket.socket, msg_s: dict) -> None:
        """
        send message to client socket
        :param socket_obj_c: client socket
        :param msg_s: msg (dict)
        :return: None
        """
        msg_s = dumps(msg_s)
        msg_s = bytes(f"{len(msg_s):<{Server.HEADER_SIZE_LENGTH}}", 'utf-8') + msg_s
        socket_obj_c.send(msg_s)

    @staticmethod
    def handle_client_data(data: dict, client_soc):
        """
        responsible to handle client requests and commands
        """
        data_keys = data.keys()
        result = "The command was malformed"

        # operations
        if 'operation_section' in data_keys:
            operation_section = data['operation_section']

            # DB operations
            if operation_section == 'db_operation':
                result = db_operation(data)

            # Chat operations
            elif operation_section == 'chat_operation':
                result = chat_operation(data, rooms, client_soc)

            # mail operations
            elif operation_section == 'mail_operation':
                result = mail_operation(data)
        return result


s = Server()
