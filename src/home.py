# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_registration(object):
    def setupUi(self, registration):
        registration.setObjectName("registration")
        registration.resize(1200, 790)
        registration.setMinimumSize(QtCore.QSize(1200, 790))
        registration.setMaximumSize(QtCore.QSize(1200, 790))
        self.centralwidget = QtWidgets.QWidget(registration)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.background.setMinimumSize(QtCore.QSize(1200, 800))
        self.background.setMaximumSize(QtCore.QSize(1200, 800))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.background.setFont(font)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../Assets/home.png"))
        self.background.setObjectName("background")
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(10, 450, 181, 51))
        self.settingsButton.setText("")
        self.settingsButton.setFlat(True)
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.clicked.connect(self.settingsButtonClick)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(10, 730, 191, 61))
        self.exitButton.setText("")
        self.exitButton.setFlat(True)
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(registration.close)
        self.pairButton = QtWidgets.QPushButton(self.centralwidget)
        self.pairButton.setGeometry(QtCore.QRect(10, 220, 181, 41))
        self.pairButton.setText("")
        self.pairButton.setFlat(True)
        self.pairButton.setObjectName("pairButton")
        self.pairButton.clicked.connect(self.pairButtonClick)
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(10, 150, 181, 41))
        self.registerButton.setText("")
        self.registerButton.setFlat(True)
        self.registerButton.setObjectName("registerButton")
        self.setupButton = QtWidgets.QPushButton(self.centralwidget)
        self.setupButton.setGeometry(QtCore.QRect(600, 680, 241, 61))
        self.setupButton.setText("")
        self.setupButton.setFlat(True)
        self.setupButton.setObjectName("setupButton")
        self.setupButton.clicked.connect(self.setupButtonClick)
        self.registerButton.clicked.connect(self.registerButtonClick)
        registration.setCentralWidget(self.centralwidget)

        self.retranslateUi(registration)
        QtCore.QMetaObject.connectSlotsByName(registration)
        registration.setTabOrder(self.settingsButton, self.exitButton)

    def retranslateUi(self, registration):
        _translate = QtCore.QCoreApplication.translate
        registration.setWindowTitle(_translate("registration", "MainWindow"))

    def registerButtonClick(self):
        registration.close()
        os.system("python registration.py")
    
    def pairButtonClick(self):
        registration.close()
        os.system("python pairing.py")

    def settingsButtonClick(self):
        registration.close()
        os.system("python settings.py")

    def setupButtonClick(self):
        os.system("pip install selenium")
        os.system("pip install gspread")
        os.system("pip install pyqt5-tools")
        os.system("pip install pyqt5")
        os.system("pip install configparser")
        os.system("pip install io")

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("v1.0.0")
        msg.setText("Dependencies have beenn installed! Click settings to configure Matcha!")
        msg.exec_()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registration = QtWidgets.QMainWindow()
    ui = Ui_registration()
    ui.setupUi(registration)
    registration.show()
    sys.exit(app.exec_())
