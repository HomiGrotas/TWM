from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from client.communication.communication import conn


class Ui_SignUp(object):
    def __init__(self, windows: dict):
        self.windows = windows

    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.setFixedSize(720, 710)

        # ---- grid
        self.gridLayoutWidget = QtWidgets.QWidget(SignUp)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 150, 381, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 24)
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(7)
        self.formLayout_2.setObjectName("formLayout_2")
        self.gridLayout.addLayout(self.formLayout_2, 2, 1, 1, 1)

        # ---- signup label
        self.signUpLabel = QtWidgets.QLabel(SignUp)
        self.signUpLabel.setGeometry(QtCore.QRect(240, 60, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.signUpLabel.setFont(font)
        self.signUpLabel.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.signUpLabel.setObjectName("signUpLabel")

        # ---- username input box
        self.UsernameInputBox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UsernameInputBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UsernameInputBox.sizePolicy().hasHeightForWidth())
        self.UsernameInputBox.setSizePolicy(sizePolicy)
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
        self.gridLayout.addWidget(self.UsernameInputBox, 0, 0, 1, 1)

        # ---- email text edit
        self.EmailTextEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EmailTextEdit.setFont(font)
        self.EmailTextEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                         "border: none;\n"
                                         "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                         "color: rgba(0, 0, 0, 240);\n"
                                         "padding-bottom: 7px\n"
                                         "")
        self.EmailTextEdit.setText("")
        self.EmailTextEdit.setObjectName("EmailTextEdit")
        self.gridLayout.addWidget(self.EmailTextEdit, 3, 0, 1, 2)

        # ---- password input box
        self.passwordInputBox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwordInputBox.setFont(font)
        self.passwordInputBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                            "border: none;\n"
                                            "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                            "color: rgba(0, 0, 0, 240);\n"
                                            "padding-bottom: 7px\n"
                                            "")
        self.passwordInputBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInputBox.setObjectName("passwordInputBox")
        self.gridLayout.addWidget(self.passwordInputBox, 0, 1, 1, 1)

        # ---- password confirmation box
        self.passwordInputBox2 = QtWidgets.QLineEdit(self.gridLayoutWidget)

        self.passwordInputBox2.setFont(font)
        self.passwordInputBox2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                            "border: none;\n"
                                            "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                            "color: rgba(0, 0, 0, 240);\n"
                                            "padding-bottom: 7px\n"
                                            "")
        self.passwordInputBox2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInputBox2.setObjectName("passwordInputBox2")
        self.gridLayout.addWidget(self.passwordInputBox2, 1, 0, 1, 1)

        # ---- mobile num text edit
        self.MobileNumTextEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MobileNumTextEdit.setFont(font)
        self.MobileNumTextEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px\n"
"")
        self.MobileNumTextEdit.setText("")
        self.MobileNumTextEdit.setObjectName("MobileNumTextEdit")
        self.gridLayout.addWidget(self.MobileNumTextEdit, 1, 1, 1, 1)

        # ---- first name text box
        self.FirstNameTextBox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FirstNameTextBox.setFont(font)
        self.FirstNameTextBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                            "border: none;\n"
                                            "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                            "color: rgba(0, 0, 0, 240);\n"
                                            "padding-bottom: 7px\n"
                                            "")
        self.FirstNameTextBox.setText("")
        self.FirstNameTextBox.setObjectName("FirstNameTextBox")
        self.gridLayout.addWidget(self.FirstNameTextBox, 2, 0, 1, 1)

        # ---- last name text box
        self.LastNameTextBox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LastNameTextBox.setFont(font)
        self.LastNameTextBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px\n"
"")
        self.LastNameTextBox.setText("")
        self.LastNameTextBox.setObjectName("LastNameTextBox")
        self.gridLayout.addWidget(self.LastNameTextBox, 2, 1, 1, 1)

        # ---- already registered push button
        self.alreadyRegisteredPushBox = QtWidgets.QPushButton(SignUp)
        self.alreadyRegisteredPushBox.setGeometry(QtCore.QRect(290, 500, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.alreadyRegisteredPushBox.setFont(font)
        self.alreadyRegisteredPushBox.clicked.connect(lambda: self.switch_window(SignUp, self.windows['login']))
        self.alreadyRegisteredPushBox.setStyleSheet("QPushButton{\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-top:5px;\n"
"}")
        self.alreadyRegisteredPushBox.setObjectName("alreadyRegisteredPushBox")

        # ---- signup push button
        self.signUpPushButton = QtWidgets.QPushButton(SignUp)
        self.signUpPushButton.clicked.connect(lambda: self.sign_up_clicked(SignUp))
        self.signUpPushButton.setGeometry(QtCore.QRect(190, 550, 350, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.signUpPushButton.setFont(font)
        self.signUpPushButton.setStyleSheet("QPushButton{\n"
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
        self.signUpPushButton.setObjectName("signUpPushButton")

        self.backPushButton = QtWidgets.QPushButton(SignUp)
        self.backPushButton.clicked.connect(lambda: self.switch_window(SignUp, self.windows['login']))
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
        
        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "TWM by HomiGrotas"))
        self.backPushButton.setText(_translate("Form", "🢀"))
        self.signUpLabel.setText(_translate("SignUp", "Sign Up"))
        self.signUpPushButton.setText(_translate("SignUp", "S i g n  U p"))
        self.EmailTextEdit.setPlaceholderText(_translate("SignUp", "Email"))
        self.MobileNumTextEdit.setPlaceholderText(_translate("SignUp", "Mobile Num."))
        self.LastNameTextBox.setPlaceholderText(_translate("SignUp", "Last name"))
        self.passwordInputBox.setPlaceholderText(_translate("SignUp", "Password"))
        self.passwordInputBox2.setPlaceholderText(_translate("SignUp", "Password Confirmation"))
        self.UsernameInputBox.setPlaceholderText(_translate("SignUp", "Username"))
        self.FirstNameTextBox.setToolTip(_translate("SignUp", "<html><head/><body><p><br/></p></body></html>"))
        self.FirstNameTextBox.setPlaceholderText(_translate("SignUp", "First name"))
        self.alreadyRegisteredPushBox.setText(_translate("SignUp", "Already registered?"))

    def switch_window(self, current_win, switch_to):
        """
        switches window
        :param current_win: current window
        :param switch_to: window to switch to
        """
        self.window = QtWidgets.QMainWindow()
        self.ui = switch_to(self.windows)
        self.ui.setupUi(self.window)
        self.window.show()
        current_win.close()

    def sign_up_clicked(self, SignUp):
        """
        called when the signup button was clicked
        data is valid -> send to server, else -> raise error
        :return: if there was an error
        """

        def data_valid(values):
            """
            :param values: user data values
            :return: whether the user data was completed
            """
            for val in values:
                if type(val) is str:
                    if not val:
                        return False
            return True

        msg = QtWidgets.QMessageBox()
        user_data = dict()  # total of 6
        user_data['username'] = self.UsernameInputBox.text()
        user_data['last_name'] = self.LastNameTextBox.text()
        user_data['first_name'] = self.FirstNameTextBox.text()
        user_data['email'] = self.EmailTextEdit.text()
        user_data['phone_number'] = self.MobileNumTextEdit.text()
        user_data['password'] = self.passwordInputBox.text()
        password_confirmation = self.passwordInputBox2.text()

        # password fits confirmation
        if user_data['password'] == password_confirmation:

            # if all the boxes are filled
            if data_valid(user_data.values()):
                sign_up_form = {
                    'operation_section': 'db_operation',
                    'operation': 'sign_up',
                    'response': 0,  # success/error only
                    'kwargs': {
                        **user_data
                    }
                }
                conn.send(sign_up_form)

                # register user
                response = conn.receive()['response']
                try:
                    if response == 'success':
                        msg.setWindowTitle("Success")
                        msg.setText("You are registered")
                        self.switch_window(SignUp, self.windows['login'])
                    else:
                        msg.setWindowTitle("Couldn't register")
                        msg.setText(response)
                except Exception as e:
                    msg.setWindowTitle("Error")
                    msg.setText(e.__str__())

            # not all field are completed
            else:
                msg.setWindowTitle("Error")
                msg.setText("You didn't fill all the fields")

        # password and confirmation don't match
        else:
            msg.setWindowTitle("Oops")
            msg.setText("password and password confirmation don't match")
        msg.exec_()
