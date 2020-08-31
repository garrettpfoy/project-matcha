# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings-done.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        MainWindow.setStyleSheet("background: url(C:\\Users\\Garrett Foy\\Documents\\Project Matcha\\Assets\\mockup.png)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-10, -20, 1200, 800))
        self.background.setMinimumSize(QtCore.QSize(1200, 800))
        self.background.setMaximumSize(QtCore.QSize(1200, 800))
        self.background.setLineWidth(0)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../Assets/settings.png"))
        self.background.setScaledContents(True)
        self.background.setWordWrap(False)
        self.background.setIndent(0)
        self.background.setObjectName("background")
        self.chromebookButton = QtWidgets.QPushButton(self.centralwidget)
        self.chromebookButton.setGeometry(QtCore.QRect(10, 340, 171, 41))
        self.chromebookButton.setText("")
        self.chromebookButton.setFlat(True)
        self.chromebookButton.setObjectName("chromebookButton")
        self.hotspotButton = QtWidgets.QPushButton(self.centralwidget)
        self.hotspotButton.setGeometry(QtCore.QRect(10, 270, 171, 41))
        self.hotspotButton.setText("")
        self.hotspotButton.setFlat(True)
        self.hotspotButton.setObjectName("hotspotButton")
        self.pairButton = QtWidgets.QPushButton(self.centralwidget)
        self.pairButton.setGeometry(QtCore.QRect(0, 190, 191, 51))
        self.pairButton.setText("")
        self.pairButton.setFlat(True)
        self.pairButton.setObjectName("pairButton")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(10, 130, 171, 41))
        self.registerButton.setText("")
        self.registerButton.setFlat(True)
        self.registerButton.setObjectName("registerButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(10, 710, 171, 61))
        self.exitButton.setAutoFillBackground(False)
        self.exitButton.setText("")
        self.exitButton.setFlat(True)
        self.exitButton.setObjectName("exitButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(530, 640, 261, 81))
        self.saveButton.setText("")
        self.saveButton.setFlat(True)
        self.saveButton.setObjectName("saveButton")
        self.serviceKeyInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.serviceKeyInput.setGeometry(QtCore.QRect(420, 140, 701, 51))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(29)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.serviceKeyInput.setFont(font)
        self.serviceKeyInput.setAutoFillBackground(False)
        self.serviceKeyInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.serviceKeyInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.serviceKeyInput.setOverwriteMode(False)
        self.serviceKeyInput.setBackgroundVisible(False)
        self.serviceKeyInput.setPlaceholderText("")
        self.serviceKeyInput.setObjectName("serviceKeyInput")
        self.sheetKeyInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.sheetKeyInput.setGeometry(QtCore.QRect(420, 258, 701, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(29)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.sheetKeyInput.setFont(font)
        self.sheetKeyInput.setAutoFillBackground(False)
        self.sheetKeyInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.sheetKeyInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sheetKeyInput.setOverwriteMode(False)
        self.sheetKeyInput.setBackgroundVisible(False)
        self.sheetKeyInput.setPlaceholderText("")
        self.sheetKeyInput.setObjectName("sheetKeyInput")
        self.sheetNameInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.sheetNameInput.setGeometry(QtCore.QRect(420, 375, 701, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(29)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.sheetNameInput.setFont(font)
        self.sheetNameInput.setAutoFillBackground(False)
        self.sheetNameInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.sheetNameInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sheetNameInput.setOverwriteMode(False)
        self.sheetNameInput.setBackgroundVisible(False)
        self.sheetNameInput.setPlaceholderText("")
        self.sheetNameInput.setObjectName("sheetNameInput")
        self.speedInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.speedInput.setGeometry(QtCore.QRect(420, 495, 701, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(29)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.speedInput.setFont(font)
        self.speedInput.setAutoFillBackground(False)
        self.speedInput.setStyleSheet("background-color: rgb(17, 17, 19); border: 0px; color: rgb(150,150,150)")
        self.speedInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.speedInput.setOverwriteMode(False)
        self.speedInput.setBackgroundVisible(False)
        self.speedInput.setPlaceholderText("")
        self.speedInput.setObjectName("speedInput")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.serviceKeyInput.setPlainText(_translate("MainWindow", "SERVICE_KEY"))
        self.sheetKeyInput.setPlainText(_translate("MainWindow", "SHEET_KEY"))
        self.sheetNameInput.setPlainText(_translate("MainWindow", "SHEET_NAME"))
        self.speedInput.setPlainText(_translate("MainWindow", "SPEED_MULTIPLIER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
