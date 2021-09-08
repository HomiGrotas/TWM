from server.db.db import DBConnection, db_conn
from server.utils.validations import valid_user_data
from server.utils.mail_service import send_welcome_email, send_reset_password_email
from server.utils.validations import valid_password
import random
import string


"""
functions to handle the client requests
"""

"""
DB related functions
"""


def db_operation(data: dict):
    operation = data['operation']  # DB operation that is going to be executed
    response = data['response']  # amount of responses (-1/0=commit/1/2+)
    kwargs = data['kwargs']  # arguments in form of dict
    result = "Unknown operation"

    if operation in DBConnection.commands:
        # if doesn't need validation check/ need and passed a check
        if operation not in ('sign_up', 'update_password'):
            result = db_conn.exec_command(
                command=DBConnection.commands[operation],
                response=response,
                **kwargs
            )
        elif operation == 'sign_up':  # sign_up operation
            result = sign_up(kwargs)
        elif operation == 'update_password':
            result = reset_password_operation(kwargs)
    return result


def reset_password_operation(kwargs):
    """
    reset user password if the given password is valid
    """
    print('kwargs', kwargs)
    validation_response = valid_password(kwargs['new_password'])

    if validation_response:          # update password if the arguments are valid
        result = db_conn.exec_command(
            command=DBConnection.commands['update_password'],
            response=0,
            **kwargs
        )

    else:  # return the validation message
        result = 'invalid password.'
    return result


def sign_up(kwargs):
    """
    register user if the given details are valid (username, password etc.)
    """
    validation_response = valid_user_data(kwargs)

    if validation_response['valid']:  # register if the arguments are valid
        result = db_conn.exec_command(
            command=DBConnection.commands['sign_up'],
            response=0,
            **kwargs
        )

        # send welcome message to new user
        if result == "success":
            send_welcome_email(kwargs['email'], kwargs['first_name'])

    else:  # return the validation message
        result = validation_response['message']
    return result


"""
Chat related functions
"""


def chat_operation(data: dict, rooms: dict, client_soc):
    """
    handle chat operation requests
    """
    response = 'Error'
    operation = data['operation']

    # user sent message
    if operation == 'room_msg':
        room = data['msg_info']['room_name']
        rooms[room].add_message(data['msg_info'])
        response = 'received message!'

    # user wants to join a room
    elif operation == 'join_room':
        room = data['msg_info']['room_name']
        username = data['msg_info']['username']
        rooms[room].add_client(client_soc, username)
        response = "Joined"

    # user wants to get new messages
    elif operation == 'get_messages':
        room = data['room_name']
        response = rooms[room].get_message(client_soc)

    # user in lobby and needs connected users for each room
    elif operation == 'get_rooms_users':
        users = dict()
        for name, room in rooms.items():
            users[name] = room.get_connected_users()
        response = users

    # get single room connected users
    elif operation == 'get_room_users':
        print(data)
        room = data['room_name']
        response = rooms[room].get_connected_users()
        print("got room", response)

    # user requests to exit from a specific room
    elif operation == 'exit_room':
        room = data['msg_info']['room_name']
        username = data['msg_info']['username']
        rooms[room].delete_client(client_soc, username)
        response = "Exit executed successfully"
    return response


"""
reset password related functions
"""


def mail_operation(data: dict):
    """
    handle mail operations (send code to user via mail)
    """
    result = "Email error"
    operation = data['operation']  # mail operation that is going to be executed

    if operation == 'reset_password':
        result = send_reset_password_code(data['kwargs'])
    return result


def send_reset_password_code(data: dict):
    """
    generate code to user if the email exists
    """
    # generate 6 digits and chars code
    code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(6))

    email = data['email']
    exists = db_conn.exec_command(
                command=DBConnection.commands['email_exists'],
                response=1,
                email=email,
    )
    if exists:
        # send_reset_password_email(email, code)
        print("send code", code)
    return code
