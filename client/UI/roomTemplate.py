from PyQt5 import QtCore, QtGui, QtWidgets
from client.communication.chat_client import ChatClient
from threading import Thread
from time import sleep
import client.UI.lobby_resources


class Ui_Room(object):
    def __init__(self, windows: dict, room_name: str, username: str):
        self.windows = windows
        self.room_name = room_name
        self.username = username
        self.chat = ""
        self.current_win = None
        self.connection = ChatClient(username, room_name)
        self.msg_loader = Thread(target=self.load_messages)
        self.connected_users_loader = Thread(target=self.load_connected_users)
        self.load_bool = True

    def setupUi(self, room):
        self.current_win = room
        room.setObjectName("room")
        room.setFixedSize(1069, 761)
        room.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.connectedUsers = QtWidgets.QLabel(room)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(60)
        self.connectedUsers.setFont(font)
        self.connectedUsers.setAlignment(QtCore.Qt.AlignTop)
        self.connectedUsers.setGeometry(QtCore.QRect(0, 280, 361, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectedUsers.sizePolicy().hasHeightForWidth())
        self.connectedUsers.setSizePolicy(sizePolicy)
        self.connectedUsers.setStyleSheet("border: 1px solid rgb(0, 0, 0)\n"
        "")
        self.connectedUsers.setObjectName("connectedUsers")
        self.welcomeLabel = QtWidgets.QLabel(room)
        self.welcomeLabel.setGeometry(QtCore.QRect(10, 20, 361, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomeLabel.sizePolicy().hasHeightForWidth())
        self.welcomeLabel.setSizePolicy(sizePolicy)
        self.welcomeLabel.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setStyleSheet("background-color:rgb(165, 255, 245);\n"
        "")
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.participantsLabel = QtWidgets.QLabel(room)
        self.participantsLabel.setGeometry(QtCore.QRect(0, 250, 361, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.participantsLabel.sizePolicy().hasHeightForWidth())
        self.participantsLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.participantsLabel.setFont(font)
        self.participantsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.participantsLabel.setStyleSheet("background-color:rgb(165, 255, 245);\n"
        "")
        self.participantsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.participantsLabel.setObjectName("participantsLabel")
        self.backPushButton = QtWidgets.QPushButton(room)
        self.backPushButton.clicked.connect(lambda: self.switch_window(self.windows['lobby'], self.username))
        self.backPushButton.setGeometry(QtCore.QRect(0, 690, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.backPushButton.setFont(font)
        self.backPushButton.setStyleSheet("QPushButton{\n"
        "border: None;\n"
        "background-color:rgb(165, 255, 245);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "padding-right:5px;\n"
        "padding-top:5px;\n"
        "}")
        self.backPushButton.setObjectName("backPushButton")
        self.gamingPushButton = QtWidgets.QPushButton(room)
        self.gamingPushButton.setGeometry(QtCore.QRect(120, 100, 101, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gamingPushButton.sizePolicy().hasHeightForWidth())
        self.gamingPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gamingPushButton.setFont(font)
        self.gamingPushButton.setStyleSheet("QPushButton{\n"
        "border-radius:50;\n"
        "background-color:rgb(255, 255, 0);\n"
        "border : 2px solid black;\n"
        "}\n"
        "\n"
        "\n"
        "QPushButton:hover\n"
        "{\n"
        "background-color: rgb(106, 255, 233);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "padding-right:5px;\n"
        "padding-top:5px;\n"
        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/photos/photos/gaming-modified.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gamingPushButton.setIcon(icon)
        self.gamingPushButton.clicked.connect(lambda: self.switch_window(self.windows['room'], 'gaming', self.username))
        self.gamingPushButton.setObjectName("gamingPushButton")
        self.cookingPushButton = QtWidgets.QPushButton(room)
        self.cookingPushButton.setGeometry(QtCore.QRect(10, 100, 101, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cookingPushButton.sizePolicy().hasHeightForWidth())
        self.cookingPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cookingPushButton.setFont(font)
        self.cookingPushButton.clicked.connect(lambda: self.switch_window(self.windows['room'], 'cooking', self.username))
        self.cookingPushButton.setStyleSheet("QPushButton{\n"
        "border-radius:50;\n"
        "background-color:rgb(255, 255, 255);\n"
        "border : 2px solid black;\n"
        "}\n"
        "\n"
        "QPushButton:hover\n"
        "{\n"
        "background-color: rgb(106, 255, 233);\n"
        "}\n"
        "QPushButton:pressed{\n"
        "padding-right:5px;\n"
        "padding-top:5px;\n"
        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/photos/photos/chef-modified.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cookingPushButton.setIcon(icon1)
        self.cookingPushButton.setObjectName("cookingPushButton")
        self.sportsPushButton = QtWidgets.QPushButton(room)
        self.sportsPushButton.setGeometry(QtCore.QRect(230, 100, 101, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sportsPushButton.sizePolicy().hasHeightForWidth())
        self.sportsPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sportsPushButton.setFont(font)
        self.sportsPushButton.setStyleSheet("QPushButton{\n"
        "border-radius:50;\n"
        "background-color:rgb(255, 170, 0);\n"
        "border : 2px solid black;\n"
        "}\n"
        "\n"
        "QPushButton:hover\n"
        "{\n"
        "background-color: rgb(106, 255, 233);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "padding-right:5px;\n"
        "padding-top:5px;\n"
        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/photos/photos/basketball-modified.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sportsPushButton.setIcon(icon2)
        self.sportsPushButton.clicked.connect(lambda: self.switch_window(self.windows['room'], 'sports', self.username))
        self.sportsPushButton.setObjectName("sportsPushButton")
        self.textBrowser = QtWidgets.QTextBrowser(room)
        self.textBrowser.setGeometry(QtCore.QRect(450, 90, 531, 521))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(243, 233, 255);\n"
        "border: 1px solid rgb(0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.userTextEntryMessage = QtWidgets.QPlainTextEdit(room)
        self.userTextEntryMessage.setGeometry(QtCore.QRect(450, 640, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userTextEntryMessage.setFont(font)
        self.userTextEntryMessage.setStyleSheet("background-color:rgb(236, 233, 255)")
        self.userTextEntryMessage.setObjectName("userTextEntryMessage")
        self.userSendMessagePushButton = QtWidgets.QPushButton(room)
        self.userSendMessagePushButton.clicked.connect(self.send_msg)
        self.userSendMessagePushButton.setGeometry(QtCore.QRect(930, 640, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.userSendMessagePushButton.setFont(font)
        self.userSendMessagePushButton.setStyleSheet("QPushButton{\n"
        "background-color: rgb(147, 255, 169);\n"
        "border: none;\n"
        "border-radius: 5px;\n"
        "}\n"
        " \n"
        "QPushButton:hover{\n"
        "background-color:rgb(121, 255, 141);\n"
        "}\n"
        " \n"
        "QPushButton:pressed{\n"
        "background-color: rgb(13, 202, 29);\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "}")
        self.userSendMessagePushButton.setObjectName("userSendMessagePushButton")
        self.roomName = QtWidgets.QLabel(room)
        self.roomName.setGeometry(QtCore.QRect(450, 0, 531, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.roomName.setFont(font)
        self.roomName.setStyleSheet("background-color:rgb(165, 255, 245);\n"
        "")
        self.roomName.setObjectName("roomName")
        self.backgroundChat = QtWidgets.QLabel(room)
        self.backgroundChat.setGeometry(QtCore.QRect(0, -5, 1071, 771))
        self.backgroundChat.setStyleSheet("background-color:rgb(165, 255, 245);\n"
        "")
        self.backgroundChat.setText("")
        self.backgroundChat.setObjectName("backgroundChat")
        self.horizontalLayoutWidget = QtWidgets.QWidget(room)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 690, 251, 85))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.fileButton.clicked.connect(self.upload_file)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileButton.sizePolicy().hasHeightForWidth())
        self.fileButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.fileButton.setFont(font)
        self.fileButton.setStyleSheet("background-color:rgb(30, 30, 30); color:white;\n"
        "\n"
        "")
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout.addWidget(self.fileButton)
        self.imageButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.imageButton_3.clicked.connect(self.upload_pic)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageButton_3.sizePolicy().hasHeightForWidth())
        self.imageButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.imageButton_3.setFont(font)
        self.imageButton_3.setStyleSheet("background-color:rgb(30, 30, 30);\n"
        "")
        self.imageButton_3.setObjectName("imageButton_3")
        self.horizontalLayout.addWidget(self.imageButton_3)
        self.titleIcon = QtWidgets.QPushButton(room)
        self.titleIcon.setGeometry(QtCore.QRect(930, 20, 51, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleIcon.sizePolicy().hasHeightForWidth())
        self.titleIcon.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titleIcon.setFont(font)
        self.titleIcon.setStyleSheet("QPushButton{\n"
        "border-radius:50;\n"
        "background-color:rgb(165, 255, 245);\n"
        "}\n"
        "")
        self.titleIcon.setText("")
        self.titleIcon.setIconSize(QtCore.QSize(50, 50))
        self.titleIcon.setObjectName("titleIcon")
        self.backgroundChat.raise_()
        self.backPushButton.raise_()
        self.welcomeLabel.raise_()
        self.participantsLabel.raise_()
        self.gamingPushButton.raise_()
        self.cookingPushButton.raise_()
        self.sportsPushButton.raise_()
        self.textBrowser.raise_()
        self.userTextEntryMessage.raise_()
        self.userSendMessagePushButton.raise_()
        self.roomName.raise_()
        self.connectedUsers.raise_()
        self.horizontalLayoutWidget.raise_()
        self.titleIcon.raise_()

        self.retranslateUi(room)
        QtCore.QMetaObject.connectSlotsByName(room)

        # custom methods
        self.disable_room_button()
        self.set_title_icon(icon1, icon, icon2)
        self.msg_loader.start()
        self.connected_users_loader.start()

    def retranslateUi(self, room):
        _translate = QtCore.QCoreApplication.translate
        room.setWindowTitle(_translate("room", "TWM by HomiGrotas"))
        self.welcomeLabel.setText(_translate("room", f"Welcome {self.username}!"))
        self.participantsLabel.setText(_translate("room", "Participants"))
        self.backPushButton.setText(_translate("room", "🢀"))
        self.gamingPushButton.setText(_translate("room", "Gaming"))
        self.cookingPushButton.setText(_translate("room", "Cooking"))
        self.sportsPushButton.setText(_translate("room", "Sports"))
        self.textBrowser.setHtml(_translate("room", """
                                                                <html>
                                                                <body>
                                                                </body>
                                                                </html>
"""))
        self.userSendMessagePushButton.setText(_translate("room", "🡆"))
        self.roomName.setText(_translate("room", f"{self.room_name.capitalize()} Room"))
        self.fileButton.setText(_translate("room", "🗎"))
        self.imageButton_3.setText(_translate("room", "📷"))

    def switch_window(self, switch_to, *args):
        """
        switches window
        :param switch_to: window to switch to
        """
        self.connection.exit_room()
        self.load_bool = False

        self.window = QtWidgets.QMainWindow()
        if args:
            self.ui = switch_to(self.windows, *args)
        else:
            self.ui = switch_to(self.windows)
        self.ui.setupUi(self.window)
        self.window.show()
        self.current_win.close()

    def disable_room_button(self):
        if self.room_name == 'sports':
            self.sportsPushButton.setEnabled(False)
        elif self.room_name == 'cooking':
            self.cookingPushButton.setEnabled(False)
        elif self.room_name == 'gaming':
            self.gamingPushButton.setEnabled(False)
        else:
            raise KeyError(f'Invalid room name {self.room_name}')

    def set_title_icon(self, cooking_icon, gaming_icon, sports_icon):
        if self.room_name == 'sports':
            self.titleIcon.setIcon(sports_icon)
        elif self.room_name == 'cooking':
            self.titleIcon.setIcon(cooking_icon)
        else:
            self.titleIcon.setIcon(gaming_icon)

    def load_messages(self):
        while self.load_bool:
            messages = self.connection.load_messages()
            if messages:
                for msg in messages:
                    self.add_message(msg['msg'], msg['from'])
            sleep(0.5)

    def add_message(self, msg: str, sender: str):
        if sender == self.username:
            msg_ = f'<p style="color:blue">{msg}</p>'
        else:
            msg_ = f'<p>{sender}: {msg}</p>'

        self.textBrowser.append(msg_)

    def load_connected_users(self):
        while self.load_bool:
            try:
                users = self.connection.load_connected_users()
                self.connectedUsers.clear()
                self.connectedUsers.setText('\n'.join(users))
                sleep(5)
            except RuntimeError:
                self.load_bool = False

        # notify server when client quit
        self.connection.exit_room()

    def send_msg(self):
        msg = self.userTextEntryMessage.toPlainText()
        self.connection.send_msg(msg)
        self.userTextEntryMessage.clear()

    def upload_pic(self):
        print("uploaded_pic")

    def upload_file(self):
        print("uploaded_file")
