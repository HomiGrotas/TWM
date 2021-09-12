class Room:
    def __init__(self, room_id):
        """
        build a chat room
        with empty messages and without clients
        """
        self.room_id = room_id
        self.__messages = {}
        self.__users = []

    def add_message(self, message: dict):
        """
        add message to the clients
        """
        print("added message", message)
        m = {
            'from': message['from'],
            'msg': message['msg'],
            'type': message['type'],
        }
        for client_l in self.__messages.values():
            client_l.append(m)

    def get_message(self, client) -> list:
        """
        return the client's new messages
        """
        if client in self.__messages:
            messages = self.__messages[client]
            self.__messages[client] = list()
        else:
            messages = []
        return messages

    def add_client(self, client, username: str):
        """
        add user to the chat room
        """
        print("added", username)
        self.__users.append(username)
        self.__messages[client] = list()
        self.add_message({"msg": f"{username} joined the chat!", 'from': 'Server', 'type': 'str'})

    def get_connected_users(self):
        """
        return users connected to this room
        """
        return self.__users

    def delete_client(self, client, username: str):
        """
        try to remove client from the chat
        """
        print("removed", username)
        try:
            if username in self.__users:
                self.__users.remove(username)
            if client in self.__messages:
                del self.__messages[client]
        except (ValueError, KeyError) as e:  # user isn't in this room
            print('delete_client', e.__str__())
