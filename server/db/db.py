import sqlite3 as sq
import hashlib
from os.path import isfile
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class DBConnection:
    db_name = "db.db"
    commands = {
        'login': """SELECT usrID FROM tblUser WHERE usrName = ? AND usrPWD = ? LIMIT 1""",  # params: username, password
        'sign_up': """
                    INSERT INTO tblUser (
                        usrName,
                        usrLastName,
                        usrFirstName,
                        usrEmail,
                        usrMobileNumber,
                        usrPWD
                        )
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,     # params: username, first_name, last_name, email, phone_num, birth_date,
                             # password, question_id, answer

        'username_exists': """SELECT usrID FROM tblUser WHERE usrName = ? LIMIT 1""",  # params: username
        'email_exists': """SELECT usrID FROM tblUser WHERE usrEmail = ? LIMIT 1""",    # params: email
        'update_password': """UPDATE tblUser SET usrPWD = ? WHERE usrEmail = ?""",# params: new password, mail
    }

    def __init__(self):
        assert isfile(ROOT_DIR + r"\\" + DBConnection.db_name), "Database doesn't exists!"

        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

    @staticmethod
    def create_connection():
        """ create a database connection to the SQLite database
            :return: Connection object or None
        """
        try:
            conn = sq.connect(ROOT_DIR + r"\\" + DBConnection.db_name)
        except sq.Error as e:
            raise e

        return conn

    def exec_command(self, command: str, response: int, **kwargs):
        """
        execute commands to database
        :param command: sql command
        :param response: amount of responses (-1=all, 0=None(success/error), 1=one, 2+=many)
        :param kwargs: arguments the sql command needs
        :return: depends on response parameter
        """
        result = "Error"
        print(kwargs)
        # hashing the arguments
        args = [hashlib.sha256(arg.encode('utf-8')).hexdigest()
                if type(arg) is str
                else hashlib.sha256(str(arg).encode('utf-8')).hexdigest() for arg in kwargs.values()]

        try:
            if response:    # without commit
                if response == -1:
                    result = self.cursor.execute(command, args).fetchall()
                elif response == 1:
                    result = self.cursor.execute(command, args).fetchone()
                else:
                    result = self.cursor.execute(command, args).fetchmany(response)
            else:
                self.cursor.execute(command, args)
                self.conn.commit()                      # commit the changes
                result = "success"
        except (sq.Error, sq.IntegrityError) as e:
            print("Error:", e)

        return result

    def close_db(self):
        """
        closes database
        """
        self.conn.close()

    def __del__(self):
        if hasattr(self, 'conn'):
            self.close_db()
        print("Database is closed")


db_conn = DBConnection()
