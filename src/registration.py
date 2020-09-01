# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import config
import register


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
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../Assets/registration.png"))
        self.background.setObjectName("background")
        self.chromebookAssetInput = QtWidgets.QTextEdit(self.centralwidget)
        self.chromebookAssetInput.setGeometry(QtCore.QRect(470, 160, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(18)
        self.chromebookAssetInput.setFont(font)
        self.chromebookAssetInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.chromebookAssetInput.setObjectName("chromebookAssetInput")
        self.chromebookSerialInput = QtWidgets.QTextEdit(self.centralwidget)
        self.chromebookSerialInput.setGeometry(QtCore.QRect(470, 280, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(18)
        self.chromebookSerialInput.setFont(font)
        self.chromebookSerialInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.chromebookSerialInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chromebookSerialInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chromebookSerialInput.setObjectName("chromebookSerialInput")
        self.hotspotAssetInput = QtWidgets.QTextEdit(self.centralwidget)
        self.hotspotAssetInput.setGeometry(QtCore.QRect(470, 400, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(18)
        self.hotspotAssetInput.setFont(font)
        self.hotspotAssetInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.hotspotAssetInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hotspotAssetInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hotspotAssetInput.setObjectName("hotspotAssetInput")
        self.studentIDInput = QtWidgets.QTextEdit(self.centralwidget)
        self.studentIDInput.setGeometry(QtCore.QRect(470, 520, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(18)
        self.studentIDInput.setFont(font)
        self.studentIDInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.studentIDInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.studentIDInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.studentIDInput.setObjectName("studentIDInput")
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(10, 450, 181, 51))
        self.settingsButton.setText("")
        self.settingsButton.setFlat(True)
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.clicked.connect(self.settingsButtonClick)
        self.submitButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton_2.setGeometry(QtCore.QRect(560, 660, 271, 81))
        self.submitButton_2.setText("")
        self.submitButton_2.setFlat(True)
        self.submitButton_2.setObjectName("submitButton_2")
        self.submitButton_2.clicked.connect(self.submit)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(10, 730, 191, 61))
        self.exitButton.setText("")
        self.exitButton.setFlat(True)
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(registration.close)
        registration.setCentralWidget(self.centralwidget)
        self.pairButton = QtWidgets.QPushButton(self.centralwidget)
        self.pairButton.setGeometry(QtCore.QRect(0, 190, 191, 51))
        self.pairButton.setText("")
        self.pairButton.setFlat(True)
        self.pairButton.setObjectName("pairButton")
        self.pairButton.clicked.connect(self.pairingButtonClick)
        self.retranslateUi(registration)
        QtCore.QMetaObject.connectSlotsByName(registration)
        registration.setTabOrder(self.chromebookAssetInput, self.chromebookSerialInput)
        registration.setTabOrder(self.chromebookSerialInput, self.hotspotAssetInput)
        registration.setTabOrder(self.hotspotAssetInput, self.studentIDInput)
        registration.setTabOrder(self.studentIDInput, self.submitButton_2)
        registration.setTabOrder(self.submitButton_2, self.settingsButton)
        registration.setTabOrder(self.settingsButton, self.exitButton)

    def retranslateUi(self, registration):
        _translate = QtCore.QCoreApplication.translate
        registration.setWindowTitle(_translate("registration", "Matcha | Registration"))
        
        self.chromebookAssetInput.setPlaceholderText(_translate("registration", "Enter Chromebook Asset Number"))
        self.chromebookSerialInput.setPlaceholderText(_translate("registration", "Enter Chromebook Serial Number"))
        self.hotspotAssetInput.setPlaceholderText(_translate("registration", "Enter Hotspot Asset Number"))
        self.studentIDInput.setPlaceholderText(_translate("registration", "Enter Student ID Number"))

    def submit(self):
        register.register(self.chromebookAssetInput.toPlainText(), self.chromebookSerialInput.toPlainText(), self.hotspotAssetInput.toPlainText(), self.studentIDInput.toPlainText())        

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("v1.0.0")
        msg.setText("You have registered STUDENT ID: " + self.studentIDInput.toPlainText())
        msg.exec_()

    def pairingButtonClick(self):
        registration.close()
        os.system("python pairing.py")

    def settingsButtonClick(self):
        registration.close()
        os.system("python settings.py")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registration = QtWidgets.QMainWindow()
    ui = Ui_registration()
    ui.setupUi(registration)
    registration.show()
    sys.exit(app.exec_())
