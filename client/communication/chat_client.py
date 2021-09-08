from client.communication.communication import conn


class ChatClient:
    def __init__(self, username, room_name):
        self.username = username
        self.room_name = room_name
        self.join_room()    # auto join to the room

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
