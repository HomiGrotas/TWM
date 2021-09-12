from client.communication.communication import conn
from threading import Lock


def network_method(func):
    """"
    wrapper method to wait until it's possible to send message to server
    (meaning, there isn't another function waiting for response from server)
    """
    def wrapper_network(self, *args):
        # wait for another function to end (acquiring lock)
        self.busy_lock.acquire()
        try:
            value_returned = func(self, *args)
        except Exception as e:
            raise e

        # release lock
        self.busy_lock.release()
        return value_returned

    return wrapper_network


class ChatClient:
    def __init__(self, username, room_name):
        self.username = username
        self.room_name = room_name
        self.join_room()    # auto join to the room
        self.busy_lock = Lock()

    def join_room(self):
        """
        send join room request to server
        """
        send_msg_format = \
            {
                'operation_section': 'chat_operation',
                'operation': 'join_room',
                'msg_info': {
                    'username': self.username,
                    'room_name': self.room_name,
                }
            }
        conn.send(send_msg_format)
        response = conn.receive()
        return response

    @network_method
    def exit_room(self):
        """
        send exit room request to server
        """
        send_msg_format = \
            {
                'operation_section': 'chat_operation',
                'operation': 'exit_room',
                'msg_info': {
                    'username': self.username,
                    'room_name': self.room_name,
                }
            }
        conn.send(send_msg_format)
        response = conn.receive()
        return response

    @network_method
    def send_msg(self, msg: str):
        """
        send msg to server
        """
        if msg:
            print("sent message", msg)
            send_msg_format = \
                {
                    'operation_section': 'chat_operation',
                    'operation': 'room_msg',
                    'msg_info':
                        {
                            'from': self.username,
                            'room_name': self.room_name,
                            'msg': msg,
                            'type': 'string'
                        }
                }
            conn.send(send_msg_format)
            response = conn.receive()
            return response

    @network_method
    def load_messages(self):
        """
        send get messages request to server
        """
        load_messages_format = \
            {
                'operation_section': 'chat_operation',
                'operation': 'get_messages',
                'room_name': self.room_name,
            }
        conn.send(load_messages_format)
        response = conn.receive()['response']
        return response

    @network_method
    def load_connected_users(self):
        send_msg_format = \
            {
                'operation_section': 'chat_operation',
                'operation': 'get_room_users',
                'room_name': self.room_name
            }
        conn.send(send_msg_format)
        response = conn.receive()['response']
        return response
