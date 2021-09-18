from sys import exit, argv
from PyQt5 import QtWidgets
from client.UI.sign_up import Ui_SignUp
from client.UI.forgot_password import Ui_ForgotPassword
from client.UI.login_page import Ui_LoginPage
from client.UI.lobby import Ui_Lobby
from client.UI.room_template import Ui_Room
from client.communication.communication import conn


def main():
    """
    client main function
    """
    app = QtWidgets.QApplication(argv)

    if conn.connected:  # if connected successfully to the server
        form = QtWidgets.QWidget()
        login_page = Ui_LoginPage({
            'login': Ui_LoginPage,
            'forgot_password': Ui_ForgotPassword,
            'sign_up': Ui_SignUp,
            'lobby': Ui_Lobby,
            'room': Ui_Room,
        })

        login_page.setupUi(form)
        form.show()
        exit(app.exec_())  # close program when app is closed

    else:   # if server is offline
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Oops")
        msg.setText("Error: the server seems to be offline")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()
        exit()


if __name__ == '__main__':
    main()
