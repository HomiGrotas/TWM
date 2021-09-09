from PyQt5 import QtCore, QtGui, QtWidgets
from client.communication.communication import conn


class Ui_ForgotPassword(object):
    def __init__(self, windows: dict):
        self.windows = windows
        self.reset_code = None
        self.expecting_code = False
        self.expecting_password = False

    def setupUi(self, Form):
        self.current_win = Form
        Form.setObjectName("Form")
        Form.setFixedSize(720, 710)
        self.forgotPasswordLabel = QtWidgets.QLabel(Form)
        self.forgotPasswordLabel.setGeometry(QtCore.QRect(50, 20, 601, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.forgotPasswordLabel.setFont(font)
        self.forgotPasswordLabel.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.forgotPasswordLabel.setObjectName("forgotPasswordLabel")
        self.email = QtWidgets.QLineEdit(Form)
        self.email.setGeometry(QtCore.QRect(230, 260, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px\n"
"")
        self.email.setObjectName("email")

        self.code = QtWidgets.QLineEdit(Form)
        self.code.setGeometry(QtCore.QRect(230, 335, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.code.setFont(font)
        self.code.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                    "border: none;\n"
                                    "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                    "color: rgba(0, 0, 0, 240);\n"
                                    "padding-bottom: 7px\n"
                                    "")
        self.code.setObjectName("code")
        self.code.setHidden(True)

        self.new_password = QtWidgets.QLineEdit(Form)
        self.new_password.setGeometry(QtCore.QRect(230, 260, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.new_password.setFont(font)
        self.new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                "border: none;\n"
                                "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                "color: rgba(0, 0, 0, 240);\n"
                                "padding-bottom: 7px\n"
                                "")
        self.new_password.setObjectName("code")
        self.new_password.setHidden(True)

        self.sendEmailPushButton = QtWidgets.QPushButton(Form)
        self.sendEmailPushButton.setGeometry(QtCore.QRect(230, 420, 230, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.sendEmailPushButton.setFont(font)
        self.sendEmailPushButton.setStyleSheet("QPushButton{\n"
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
        self.sendEmailPushButton.setObjectName("sendEmailPushButton")
        self.sendEmailPushButton.clicked.connect(self.send_email_push_button_clicked)
        self.backPushButton = QtWidgets.QPushButton(Form)
        self.backPushButton.clicked.connect(lambda: self.switch_window(self.windows['login']))
        self.backPushButton.setGeometry(QtCore.QRect(0, 630, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.backPushButton.setFont(font)
        self.backPushButton.setStyleSheet("QPushButton{\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-right:5px;\n"
"padding-top:5px;\n"
"}")
        self.backPushButton.setObjectName("backPushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TWM by HomiGrotas"))
        self.forgotPasswordLabel.setText(_translate("Form", "Forgot Password"))
        self.email.setPlaceholderText(_translate("Form", "email"))
        self.new_password.setPlaceholderText(_translate("Form", "new password"))
        self.code.setPlaceholderText(_translate("Form", "Code"))
        self.sendEmailPushButton.setText(_translate("Form", "Send Email"))
        self.backPushButton.setText(_translate("Form", "🢀"))

    def send_email_push_button_clicked(self):
        msg = QtWidgets.QMessageBox()

        # entered correct code, now changing the password
        if self.expecting_password:
            response = self.change_password()
            msg.setWindowTitle(response)
            msg.setText(response)

        # waiting for code sent via mail
        elif not self.expecting_code:
            email = self.email.text()

            get_code_form = {
                'operation_section': 'mail_operation',
                'operation': 'reset_password',
                'kwargs': {
                    'email': email,
                }
            }
            conn.send(get_code_form)

            # register user
            self.reset_code = conn.receive()['response']

            print("CODE", self.reset_code)

            msg.setWindowTitle("Mail was sent if exists")
            msg.setText("Email with the new password was sent to the email you entered, if it exists.")
            self.code.setHidden(False)      # show code entry box
            self.email.setDisabled(True)    # prevent email change after code was sent to a specific address
            self.sendEmailPushButton.setText("Submit code")
            self.expecting_code = True      # waiting to the code sent via mail

        else:   # if an email was supposed to be sent already
            submitted_code = self.code.text()
            success = submitted_code == self.reset_code

            if success:
                msg.setWindowTitle("Success")
                msg.setText("please enter a new password")
                self.email.hide()
                self.code.hide()
                self.new_password.show()
                self.sendEmailPushButton.setText("Change password")
                self.expecting_password = True
                self.expecting_code = False

            else:
                msg.setWindowTitle("Oops")
                msg.setText("wrong code or email")

        msg.exec_()

    def change_password(self):
        password = self.new_password.text()
        email = self.email.text()

        update_password_form = {
            'operation_section': 'db_operation',
            'response': 0,
            'operation': 'update_password',
            'kwargs': {
                'new_password': password,
                'email': email,
            }
        }

        conn.send(update_password_form)

        response = conn.receive()['response']
        print(response)

        if response == 'success':
            self.switch_window(self.windows['login'])
        return response

    def switch_window(self, switch_to):
        """
        switches window
        :param current_win: current window
        :param switch_to: window to switch to
        """
        self.window = QtWidgets.QMainWindow()
        self.ui = switch_to(self.windows)
        self.ui.setupUi(self.window)
        self.window.show()
        self.current_win.close()
