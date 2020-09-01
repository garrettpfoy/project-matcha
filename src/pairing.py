# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pairing.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pair


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
        self.background.setPixmap(QtGui.QPixmap("../Assets/pairing.png"))
        self.background.setObjectName("background")
        self.chromebookAssetInput = QtWidgets.QTextEdit(self.centralwidget)
        self.chromebookAssetInput.setGeometry(QtCore.QRect(470, 160, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        self.chromebookAssetInput.setFont(font)
        self.chromebookAssetInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.chromebookAssetInput.setObjectName("chromebookAssetInput")
        self.chromebookSerialInput = QtWidgets.QTextEdit(self.centralwidget)
        self.chromebookSerialInput.setGeometry(QtCore.QRect(470, 280, 661, 47))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        self.chromebookSerialInput.setFont(font)
        self.chromebookSerialInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.chromebookSerialInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chromebookSerialInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chromebookSerialInput.setObjectName("chromebookSerialInput")
        self.hotspotAssetInput = QtWidgets.QTextEdit(self.centralwidget)
        self.hotspotAssetInput.setGeometry(QtCore.QRect(470, 400, 661, 47))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        self.hotspotAssetInput.setFont(font)
        self.hotspotAssetInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.hotspotAssetInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hotspotAssetInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hotspotAssetInput.setObjectName("hotspotAssetInput")
        self.studentIDInput = QtWidgets.QTextEdit(self.centralwidget)
        self.studentIDInput.setGeometry(QtCore.QRect(470, 520, 661, 47))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
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
        self.pairButton = QtWidgets.QPushButton(self.centralwidget)
        self.pairButton.setGeometry(QtCore.QRect(560, 610, 271, 81))
        self.pairButton.setText("")
        self.pairButton.setFlat(True)
        self.pairButton.setObjectName("pairButton")
        self.pairButton.clicked.connect(self.pair)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(10, 730, 191, 61))
        self.exitButton.setText("")
        self.exitButton.setFlat(True)
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(registration.close)
        self.statusText = QtWidgets.QTextEdit(self.centralwidget)
        self.statusText.setGeometry(QtCore.QRect(580, 723, 331, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        self.statusText.setFont(font)
        self.statusText.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.statusText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.statusText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.statusText.setObjectName("statusText")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(10, 150, 181, 51))
        self.registerButton.setText("")
        self.registerButton.setFlat(True)
        self.registerButton.setObjectName("registerButton")
        self.registerButton.clicked.connect(self.registerButtonClick)
        registration.setCentralWidget(self.centralwidget)

        self.retranslateUi(registration)
        QtCore.QMetaObject.connectSlotsByName(registration)
        registration.setTabOrder(self.chromebookAssetInput, self.chromebookSerialInput)
        registration.setTabOrder(self.chromebookSerialInput, self.hotspotAssetInput)
        registration.setTabOrder(self.hotspotAssetInput, self.studentIDInput)
        registration.setTabOrder(self.studentIDInput, self.pairButton)
        registration.setTabOrder(self.pairButton, self.settingsButton)
        registration.setTabOrder(self.settingsButton, self.exitButton)

    def retranslateUi(self, registration):
        _translate = QtCore.QCoreApplication.translate
        registration.setWindowTitle(_translate("registration", "Matcha | Pairing v1.0.0"))
        self.chromebookAssetInput.setPlaceholderText(_translate("registration", "Enter Chromebook Asset [Required]"))
        self.chromebookSerialInput.setPlaceholderText(_translate("registration", "Enter Chromebook Serial [Preferred]"))
        self.hotspotAssetInput.setPlaceholderText(_translate("registration", "Enter Hotspot Asset [Required]"))
        self.studentIDInput.setPlaceholderText(_translate("registration", "Enter Student ID [Required to Register]"))
        self.statusText.setPlaceholderText(_translate("registration", "[NOTE] Enter in Student ID to AUTO-REGISTER!"))

    def pair(self):
        if(len(self.studentIDInput.toPlainText()) >= 5):
            pair.pairDevices(self, False, self.chromebookAssetInput.toPlainText(), self.chromebookSerialInput.toPlainText(), self.hotspotAssetInput.toPlainText(), self.studentIDInput.toPlainText())
        else:
            pair.pairDevices(self, False, self.chromebookAssetInput.toPlainText(), self.chromebookSerialInput.toPlainText(), self.hotspotAssetInput.toPlainText(), self.studentIDInput.toPlainText())    
    def updateStatus(self, message):
        print(message)
        _translate = QtCore.QCoreApplication.translate
        self.statusText.setPlainText(_translate("registration", message))

    def registerButtonClick(self):
        registration.close()
        os.system("python registration.py")

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
