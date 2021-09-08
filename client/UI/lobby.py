from PyQt5 import QtCore, QtGui, QtWidgets
from client.communication.communication import conn
from threading import Thread
from time import sleep


class Ui_Lobby(object):
    def __init__(self, windows: dict, username: str):
        self.windows = windows
        self.username = username
        self.current_win = None
        self.load_connected_users_bool = True

    def setupUi(self, lobby):
        self.current_win = lobby
        lobby.setObjectName("lobby")
        lobby.setFixedSize(967, 708)
        lobby.setAutoFillBackground(False)
        lobby.setStyleSheet("background-color: rgba(236, 229, 221)")
        self.LoginLabel = QtWidgets.QLabel(lobby)
        self.LoginLabel.setGeometry(QtCore.QRect(230, 0, 591, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.LoginLabel.setObjectName("LoginLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(lobby)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 150, 731, 561))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sportsLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.sportsLabel.setFont(font)
        self.sportsLabel.setMouseTracking(False)
        self.sportsLabel.setAutoFillBackground(False)
        self.sportsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sportsLabel.setObjectName("sportsLabel")
        self.verticalLayout.addWidget(self.sportsLabel)
        self.sportsButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sportsButton.clicked.connect(lambda: self.switch_window(self.windows['room'], 'sports', self.username))
        self.sportsButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sportsButton.sizePolicy().hasHeightForWidth())
        self.sportsButton.setSizePolicy(sizePolicy)
        self.sportsButton.setMinimumSize(QtCore.QSize(160, 180))
        self.sportsButton.setAutoFillBackground(False)
        self.sportsButton.setStyleSheet("")
        self.sportsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/photos/photos/basketball-modified.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.sportsButton.setIcon(icon)
        self.sportsButton.setIconSize(QtCore.QSize(180, 180))
        self.sportsButton.setFlat(True)
        self.sportsButton.setObjectName("sportsButton")
        self.sportsButton.setStyleSheet("border-radius : 50")
        self.verticalLayout.addWidget(self.sportsButton)
        self.sportOnlineUsers = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.sportOnlineUsers.setSelectionMode(QtWidgets.QListWidget.NoSelection)
        self.sportOnlineUsers.setObjectName("sportOnlineUsers")
        self.verticalLayout.addWidget(self.sportOnlineUsers)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gamingLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.gamingLabel.setFont(font)
        self.gamingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gamingLabel.setObjectName("gamingLabel")
        self.verticalLayout_3.addWidget(self.gamingLabel)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.clicked.connect(lambda: self.switch_window(self.windows['room'], 'gaming', self.username))
        self.pushButton_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(160, 180))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/photos/photos/gaming-modified.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(180, 180))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("border-radius : 50")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.gamingOnlineUsers = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.gamingOnlineUsers.setSelectionMode(QtWidgets.QListWidget.NoSelection)
        self.gamingOnlineUsers.setObjectName("gamingOnlineUsers")
        self.verticalLayout_3.addWidget(self.gamingOnlineUsers)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cookingLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.cookingLabel.setFont(font)
        self.cookingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cookingLabel.setObjectName("cookingLabel")
        self.verticalLayout_2.addWidget(self.cookingLabel)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.clicked.connect(lambda: self.switch_window(self.windows['room'], 'cooking', self.username))
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(160, 180))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/photos/photos/chef-modified.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(180, 180))
        self.pushButton.setFlat(True)
        self.pushButton.setStyleSheet("border-radius : 150")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.cookingOnlineUsers = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.cookingOnlineUsers.setSelectionMode(QtWidgets.QListWidget.NoSelection)
        self.cookingOnlineUsers.setObjectName("cookingOnlineUsers")
        self.verticalLayout_2.addWidget(self.cookingOnlineUsers)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.backPushButton = QtWidgets.QPushButton(lobby)
        self.backPushButton.setGeometry(QtCore.QRect(-10, 640, 141, 61))
        self.backPushButton.clicked.connect(lambda: self.switch_window(self.windows['login']))
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
        self.backPushButton.raise_()
        self.LoginLabel.raise_()
        self.horizontalLayoutWidget.raise_()

        self.retranslateUi(lobby)
        QtCore.QMetaObject.connectSlotsByName(lobby)
        Thread(target=self.load_connected_users).start()

    def retranslateUi(self, lobby):
        _translate = QtCore.QCoreApplication.translate
        lobby.setWindowTitle(_translate("lobby", "TWM by HomiGrotas"))
        self.LoginLabel.setText(_translate("lobby", f"Welcome {self.username}"))
        self.sportsLabel.setText(_translate("lobby", "Sports"))
        self.gamingLabel.setText(_translate("lobby", "Gaming"))
        self.cookingLabel.setText(_translate("lobby", "Cooking"))
        self.backPushButton.setText(_translate("lobby", "🢀"))

    def switch_window(self, switch_to, *args):
        """
        switches window
        :param current_win: current window
        :param switch_to: window to switch to
        """
        self.load_connected_users_bool = False
        self.window = QtWidgets.QMainWindow()
        if args:
            self.ui = switch_to(self.windows, *args)
        else:
            self.ui = switch_to(self.windows)
        self.ui.setupUi(self.window)
        self.window.show()
        self.current_win.close()

    def add_user_online(self, username: str, room: str):
        """
        add user to the online users tables
        """
        if room == 'sports':
            self.sportOnlineUsers.addItem(username)
        elif room == 'cooking':
            self.cookingOnlineUsers.addItem(username)
        elif room == 'gaming':
            self.gamingOnlineUsers.addItem(username)
        else:
            print(f"Unknown room {room}")

    def load_connected_users(self):
        """
        load connected users and add them to table
        """
        send_msg_format = \
            {
                'operation_section': 'chat_operation',
                'operation': 'get_rooms_users'
            }

        try:
            while self.load_connected_users_bool:
                # clear previous records
                self.gamingOnlineUsers.clear()
                self.cookingOnlineUsers.clear()
                self.sportOnlineUsers.clear()

                conn.send(send_msg_format)
                response = conn.receive()['response']

                # add users to the rooms tables
                for room, users in response.items():
                    for user in users:
                        self.add_user_online(user, room)
                sleep(0.5)
        except Exception as e:
            print(e.__str__())
