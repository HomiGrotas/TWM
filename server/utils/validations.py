from re import match, search, compile
from server.db.db import db_conn, DBConnection


def valid_username(username: str) -> bool:
    """
    checks whether the username is valid
    :param username: username
    :return: length at least 5+ username doesn't exists in db
    """
    valid = False
    if len(username) >= 5:
        valid = db_conn.exec_command(DBConnection.commands['username_exists'], 1, username=username) is None
    return valid


def valid_name(name: str) -> bool:
    """
    whether the name is valid
    :param name: user name
    :return: True if consists only chars and length at least 2
    """
    return name.isalpha() and len(name) >= 2


def valid_family_name(family_name: str) -> bool:
    """
    whether the family name is valid
    :param family_name: user family name
    :return: consists only chars and length at least 2
    """
    return family_name.isalpha() and len(family_name) >= 2


def valid_mail(mail: str) -> bool:
    """
    checks for a valid email
    :param mail: user email address
    :return: whether the email address is valid (email format + doesn't exists in db)
    """
    valid = False
    if match(r"[^@]+@[^@]+\.[^@]+", mail) is not None:
        valid = db_conn.exec_command(DBConnection.commands['email_exists'], 1, email=mail) is None
    return valid


def valid_phone_num(phone_num: str) -> bool:
    """
    checks for a valid phone num
    :param phone_num: user phone number
    :return: whether the phone number is valid
    """
    if phone_num.startswith('972'):
        phone_num = '0' + phone_num[3:]
    return match(r"^[0][5][0|2|3|4|5|8|9][0-9]{7}$", phone_num) is not None


def valid_password(password: str) -> bool:
    """

    :param password: user password
    :return: * whether password length >= 8,
             * whether password has 1+ chars
             * whether password has 1+ digits
    """
    return len(password) >= 8 and any(map(str.isalpha, password)) and any(map(str.isdigit, password))


def password_strength(password: str) -> bool:
    """
    password length at least 8, has one char and one digit at least
    :param password: user password
    """
    return (
            any(map(str.isalpha, password)) and  # if has at least one char
            len(password) >= 8 and  # if password length > 8
            any(map(str.isdigit, password))  # if has at least one num
    )


def valid_user_data(user_data: dict) -> dict:
    """
    valid_user_data function
    :param user_data: user data for registration
    :return: whether the user data passes all the validation checks/ error message
    """
    rtr = {'valid': True}

    try:
        if not valid_username(user_data['username']):
            rtr['valid'] = False
            rtr['message'] = "username length must be at least 5. username already exist"
        elif not valid_password(user_data['password']):
            rtr['valid'] = False
            rtr['message'] = "password length must be at least 8, has 1+ chars and 1+ digits"
        elif not valid_mail(user_data['email']):
            rtr['valid'] = False
            rtr['message'] = "email address already exists/ invalid email format"
        elif not valid_name(user_data['first_name']):
            rtr['valid'] = False
            rtr['message'] = "name must be only a string and must contain at least 2 chars"
        elif not valid_family_name(user_data['last_name']):
            rtr['valid'] = False
            rtr['message'] = "name must be only a string and must contain at least 2 chars"
        elif not valid_phone_num(user_data['phone_number']):
            rtr['valid'] = False
            rtr['message'] = "the phone number format isn't valid"
    except KeyError:
        rtr['valid'] = False
        rtr['message'] = "missing details"
    return rtr
