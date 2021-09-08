from sys import exit, argv
from PyQt5 import QtWidgets
from client.UI.signUp import Ui_SignUp
from client.UI.forgotPassword import Ui_ForgotPassword
from client.UI.loginPage import Ui_LoginPage
from client.UI.lobby import Ui_Lobby
from client.UI.roomTemplate import Ui_Room
from client.communication.communication import conn


def main():
    """
    client main function
    """
    app = QtWidgets.QApplication(argv)

    if conn.connected:  # if connected successfully to the server
        form = QtWidgets.QWidget()
        login_page = Ui_Room({
            'login': Ui_LoginPage,
            'forgot_password': Ui_ForgotPassword,
            'sign_up': Ui_SignUp,
            'lobby': Ui_Lobby,
            'room': Ui_Room,
        }, 'sports', 'usr2')

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