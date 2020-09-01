# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import config


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
        self.background.setPixmap(QtGui.QPixmap("../Assets/settings.png"))
        self.background.setObjectName("background")
        self.rootDirectoryInput = QtWidgets.QTextEdit(self.centralwidget)
        self.rootDirectoryInput.setGeometry(QtCore.QRect(460, 120, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        self.rootDirectoryInput.setFont(font)
        self.rootDirectoryInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.rootDirectoryInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rootDirectoryInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rootDirectoryInput.setObjectName("rootDirectoryInput")
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(10, 450, 181, 51))
        self.settingsButton.setText("")
        self.settingsButton.setFlat(True)
        self.settingsButton.setObjectName("settingsButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(560, 670, 271, 81))
        self.saveButton.setText("")
        self.saveButton.setFlat(True)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.saveSettings)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(10, 730, 191, 61))
        self.exitButton.setText("")
        self.exitButton.setFlat(True)
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(registration.close)
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(10, 150, 181, 51))
        self.registerButton.setText("")
        self.registerButton.setFlat(True)
        self.registerButton.setObjectName("registerButton")
        self.registerButton.clicked.connect(self.registerButtonClick)
        self.pairButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pairButton_2.setGeometry(QtCore.QRect(10, 210, 191, 61))
        self.pairButton_2.setText("")
        self.pairButton_2.setFlat(True)
        self.pairButton_2.setObjectName("pairButton_2")
        self.pairButton_2.clicked.connect(self.pairButtonClick)
        self.registerKeyInput = QtWidgets.QTextEdit(self.centralwidget)
        self.registerKeyInput.setGeometry(QtCore.QRect(460, 198, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        self.registerKeyInput.setFont(font)
        self.registerKeyInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.registerKeyInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.registerKeyInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.registerKeyInput.setObjectName("registerKeyInput")
        self.dataKeyInput = QtWidgets.QTextEdit(self.centralwidget)
        self.dataKeyInput.setGeometry(QtCore.QRect(460, 273, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        self.dataKeyInput.setFont(font)
        self.dataKeyInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.dataKeyInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dataKeyInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dataKeyInput.setObjectName("dataKeyInput")
        self.sheetNameInput = QtWidgets.QTextEdit(self.centralwidget)
        self.sheetNameInput.setGeometry(QtCore.QRect(460, 348, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        self.sheetNameInput.setFont(font)
        self.sheetNameInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.sheetNameInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sheetNameInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sheetNameInput.setObjectName("sheetNameInput")
        self.pullSheetInput = QtWidgets.QTextEdit(self.centralwidget)
        self.pullSheetInput.setGeometry(QtCore.QRect(460, 425, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        self.pullSheetInput.setFont(font)
        self.pullSheetInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.pullSheetInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pullSheetInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pullSheetInput.setObjectName("pullSheetInput")
        self.pushSheetInput = QtWidgets.QTextEdit(self.centralwidget)
        self.pushSheetInput.setGeometry(QtCore.QRect(460, 500, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        self.pushSheetInput.setFont(font)
        self.pushSheetInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.pushSheetInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pushSheetInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pushSheetInput.setObjectName("pushSheetInput")
        self.firstPasswordInput = QtWidgets.QTextEdit(self.centralwidget)
        self.firstPasswordInput.setGeometry(QtCore.QRect(460, 575, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        self.firstPasswordInput.setFont(font)
        self.firstPasswordInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.firstPasswordInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.firstPasswordInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.firstPasswordInput.setObjectName("firstPasswordInput")
        registration.setCentralWidget(self.centralwidget)

        self.retranslateUi(registration)
        QtCore.QMetaObject.connectSlotsByName(registration)
        registration.setTabOrder(self.rootDirectoryInput, self.saveButton)
        registration.setTabOrder(self.saveButton, self.settingsButton)
        registration.setTabOrder(self.settingsButton, self.exitButton)

    def retranslateUi(self, registration):
        _translate = QtCore.QCoreApplication.translate
        registration.setWindowTitle(_translate("registration", "Matcha | Settings v1.0.0"))
        self.rootDirectoryInput.setPlaceholderText(_translate("registration", config.getRootDirectory()))
        self.sheetNameInput.setPlaceholderText(_translate("registration", config.getSheetName()))
        self.pullSheetInput.setPlaceholderText(_translate("registration", config.getWorksheetPull()))
        self.pushSheetInput.setPlaceholderText(_translate("registration", config.getWorksheetPush()))
        self.registerKeyInput.setPlaceholderText(_translate("registration", config.getRegisterKey()))
        self.dataKeyInput.setPlaceholderText(_translate("registration", config.getSheetKey()))
        self.firstPasswordInput.setPlaceholderText(_translate("registration", config.getLikelyPassword()))

    def registerButtonClick(self):
        registration.close()
        os.system("python registration.py")
    
    def pairButtonClick(self):
        registration.close()
        os.system("python pairing.py")

    def saveSettings(self):
        try:
            config.setRootDirectory(self.rootDirectoryInput.toPlainText())
        except:
            print("Didn't set value!")
        try:
            config.setSheetName(self.sheetNameInput.toPlainText())
        except:
            print("Didn't set value!")
        try:
            config.setWorksheetPull(self.pullSheetInput.toPlainText())
        except:
            print("Didn't set value!")
        try:
            config.setWorksheetPush(self.pushSheetInput.toPlainText())
        except:
            print("Didn't set value!")
        try:
            config.setRegisterKey(self.registerKeyInput.toPlainText())
        except:
            print("Didn't set value!")
        try:
            config.setSheetKey(self.dataKeyInput.toPlainText())
        except:
            print("Didn't set value!")
        try:
            config.setLikelyPassword(self.firstPasswordInput.toPlainText)
        except:
            print("Didn't set value!")

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("v1.0.0")
        msg.setText("Settings have been saved!")
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registration = QtWidgets.QMainWindow()
    ui = Ui_registration()
    ui.setupUi(registration)
    registration.show()
    sys.exit(app.exec_())
