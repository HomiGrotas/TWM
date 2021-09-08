from PyQt5 import QtCore, QtGui
from client.communication.communication import conn
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QPushButton, QLabel, QMessageBox


class Ui_LoginPage(object):
    def __init__(self, windows: dict):
        self.windows = windows
        self.current_win = None

    def setupUi(self, LoginPage):
        self.current_win = LoginPage
        LoginPage.setObjectName("LoginPage")
        LoginPage.setFixedSize(720, 710)
        LoginPage.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        LoginPage.setAutoFillBackground(False)
        LoginPage.setStyleSheet("background-color: rgba(255, 255, 255);")
        self.UsernameInputBox = QLineEdit(LoginPage)
        self.UsernameInputBox.setGeometry(QtCore.QRect(250, 200, 260, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UsernameInputBox.setFont(font)
        self.UsernameInputBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px\n"
"")
        self.UsernameInputBox.setObjectName("UsernameInputBox")
        self.LoginLabel = QLabel(LoginPage)
        self.LoginLabel.setGeometry(QtCore.QRect(250, 40, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.LoginLabel.setObjectName("LoginLabel")
        self.passwordInputBox = QLineEdit(LoginPage)
        self.passwordInputBox.setGeometry(QtCore.QRect(250, 290, 260, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordInputBox.setFont(font)
        self.passwordInputBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px\n"
"")
        self.passwordInputBox.setEchoMode(QLineEdit.Password)
        self.passwordInputBox.setObjectName("passwordInputBox")
        self.loginPushButton = QPushButton(LoginPage)
        self.loginPushButton.setGeometry(QtCore.QRect(250, 440, 260, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.loginPushButton.setFont(font)
        self.loginPushButton.clicked.connect(self.login_clicked)
        self.loginPushButton.setStyleSheet("QPushButton{\n"
"background-color:\n"
"qlineargradient(spread:pad,x1:0,x2:0, y1:0, y2:1,\n"
"stop: 0 rgba(11, 131, 120, 219),\n"
"stop: 1 rgba(85, 98, 112, 226));\n"
" border: none;\n"
"border-radius: 5px;\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"background-color:\n"
"qlineargradient(spread:pad,x1:0,x2:0, y1:0, y2:1,\n"
"stop: 0 rgba(150,150,150,230),\n"
"stop: 0.495 rgba(85, 81, 84, 226));\n"
"}\n"
" \n"
"QPushButton:pressed{\n"
"background-color: rgba(150, 123, 111, 255);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"}")
        self.loginPushButton.setObjectName("loginPushButton")
        self.forgotPasswordPushBox = QPushButton(LoginPage)
        self.forgotPasswordPushBox.clicked.connect(lambda: self.switch_window(self.windows['forgot_password']))
        self.forgotPasswordPushBox.setGeometry(QtCore.QRect(240, 370, 131, 23))
        font = QtGui.QFont("MS Shell Dlg 2", 11)
        font.setUnderline(True)
        self.forgotPasswordPushBox.setFont(font)
        self.forgotPasswordPushBox.setStyleSheet("QPushButton{\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-top:5px;\n"
"}")
        self.forgotPasswordPushBox.setObjectName("forgotPasswordPushBox")
        self.signupPushBox = QPushButton(LoginPage)
        self.signupPushBox.clicked.connect(lambda: self.switch_window(self.windows['sign_up']))
        self.signupPushBox.setGeometry(QtCore.QRect(410, 370, 131, 23))
        font = QtGui.QFont("MS Shell Dlg 2", 11)
        font.setUnderline(True)
        self.signupPushBox.setFont(font)
        self.signupPushBox.setStyleSheet("QPushButton{\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-top:5px;\n"
"}")
        self.signupPushBox.setObjectName("signupPushBox")
        self.signupPushBox.raise_()
        self.UsernameInputBox.raise_()
        self.LoginLabel.raise_()
        self.passwordInputBox.raise_()
        self.loginPushButton.raise_()
        self.forgotPasswordPushBox.raise_()

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "TWM by HomiGrotas"))
        self.UsernameInputBox.setPlaceholderText(_translate("LoginPage", "Username"))
        self.LoginLabel.setText(_translate("LoginPage", "Log In"))
        self.passwordInputBox.setPlaceholderText(_translate("LoginPage", "Password"))
        self.loginPushButton.setText(_translate("LoginPage", "L o g  I n "))
        self.forgotPasswordPushBox.setText(_translate("LoginPage", "Forgot password"))
        self.signupPushBox.setText(_translate("LoginPage", "Sign up"))

    def switch_window(self, switch_to, username:str= None):
        """
        switches window
        :param username: connected username
        :param switch_to: window to switch to
        """
        self.window = QMainWindow()
        if username:
            self.ui = switch_to(self.windows, username)
        else:
            self.ui = switch_to(self.windows)
        self.ui.setupUi(self.window)
        self.window.show()
        self.current_win.close()

    def login_clicked(self):
        """
        called when the login button was clicked
        :return:
        """
        username = self.UsernameInputBox.text()
        password = self.passwordInputBox.text()
        if username and password:
            print(f"logging... Username {username}, Password: {password}")

            # send auth request to server
            conn.send({
                'operation_section': 'db_operation',
                'operation': 'login',
                'response': 1,
                'kwargs': {
                    'username': username,
                    'password': password
                }
            })

            # getting user_id if user exists
            user_id = conn.receive()['response']
            if user_id:
                print("Connected", username, "with user id", user_id[0])
                self.switch_window(self.windows['lobby'], username)


            else:
                msg = QMessageBox()
                msg.setWindowTitle("Couldn't login")
                msg.setText("Wrong username or password")
                msg.exec_()

                # clear password and username fields
                self.passwordInputBox.clear()
                self.UsernameInputBox.clear()
