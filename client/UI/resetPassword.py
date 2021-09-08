from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResetPassword(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(714, 689)
        self.LoginLabel = QtWidgets.QLabel(Form)
        self.LoginLabel.setGeometry(QtCore.QRect(80, 30, 581, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.LoginLabel.setObjectName("LoginLabel")
        self.UsernameInputBox = QtWidgets.QLineEdit(Form)
        self.UsernameInputBox.setGeometry(QtCore.QRect(260, 300, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UsernameInputBox.setFont(font)
        self.UsernameInputBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px\n"
"")
        self.UsernameInputBox.setText("")
        self.UsernameInputBox.setObjectName("UsernameInputBox")
        self.UsernameInputBox_2 = QtWidgets.QLineEdit(Form)
        self.UsernameInputBox_2.setGeometry(QtCore.QRect(260, 210, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UsernameInputBox_2.setFont(font)
        self.UsernameInputBox_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: rgba(0, 0, 0, 240);\n"
"padding-bottom: 7px\n"
"")
        self.UsernameInputBox_2.setText("")
        self.UsernameInputBox_2.setObjectName("UsernameInputBox_2")
        self.loginPushButton = QtWidgets.QPushButton(Form)
        self.loginPushButton.setGeometry(QtCore.QRect(260, 400, 230, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.loginPushButton.setFont(font)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LoginLabel.setText(_translate("Form", "Reset Password"))
        self.UsernameInputBox.setPlaceholderText(_translate("Form", "New Password"))
        self.UsernameInputBox_2.setPlaceholderText(_translate("Form", "Code (Sent via mail)"))
        self.loginPushButton.setText(_translate("Form", "Reset Password"))
