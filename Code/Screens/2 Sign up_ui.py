# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\DB project\DairyPro-main\Code-Connection\Screens\2 Sign up.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(378, 699)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 40, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password.setGeometry(QtCore.QRect(90, 500, 201, 21))
        self.password.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.password.setObjectName("password")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 480, 71, 16))
        self.label_5.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 120, 55, 16))
        self.label_6.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_6.setObjectName("label_6")
        self.name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(90, 140, 201, 21))
        self.name.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.name.setInputMask("")
        self.name.setObjectName("name")
        self.reEnterPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.reEnterPassword.setGeometry(QtCore.QRect(90, 560, 201, 21))
        self.reEnterPassword.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.reEnterPassword.setObjectName("reEnterPassword")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 540, 131, 16))
        self.label_7.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 180, 131, 16))
        self.label_8.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_8.setObjectName("label_8")
        self.phoneNum = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.phoneNum.setGeometry(QtCore.QRect(90, 200, 201, 21))
        self.phoneNum.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.phoneNum.setInputMask("")
        self.phoneNum.setCursorPosition(11)
        self.phoneNum.setObjectName("phoneNum")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(90, 240, 131, 16))
        self.label_9.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(90, 420, 131, 16))
        self.label_10.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_10.setObjectName("label_10")
        self.email = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.email.setGeometry(QtCore.QRect(90, 440, 201, 21))
        self.email.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.email.setObjectName("email")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(90, 360, 131, 16))
        self.label_11.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_11.setObjectName("label_11")
        self.userType = QtWidgets.QComboBox(parent=self.centralwidget)
        self.userType.setGeometry(QtCore.QRect(90, 380, 201, 22))
        self.userType.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.userType.setObjectName("userType")
        self.userType.addItem("")
        self.userType.addItem("")
        self.userType.addItem("")
        self.cancel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(200, 610, 121, 31))
        self.cancel.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.cancel.setObjectName("cancel")
        self.createAccount_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createAccount_button.setGeometry(QtCore.QRect(60, 610, 121, 31))
        self.createAccount_button.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.createAccount_button.setObjectName("createAccount_button")
        self.address = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.address.setGeometry(QtCore.QRect(90, 260, 201, 87))
        self.address.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.address.setObjectName("address")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(-70, -70, 861, 731))
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("\n"
"\n"
"background-color: rgb(207, 232, 255);\n"
"")
        self.label_12.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_12.raise_()
        self.label_4.raise_()
        self.password.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.name.raise_()
        self.reEnterPassword.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.phoneNum.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.email.raise_()
        self.label_11.raise_()
        self.userType.raise_()
        self.cancel.raise_()
        self.createAccount_button.raise_()
        self.address.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#00007f;\">Sign Up</span></p></body></html>"))
        self.password.setText(_translate("MainWindow", "************"))
        self.label_5.setText(_translate("MainWindow", "Password:"))
        self.label_6.setText(_translate("MainWindow", "Name:"))
        self.name.setText(_translate("MainWindow", "Sami Ali"))
        self.reEnterPassword.setText(_translate("MainWindow", "************"))
        self.label_7.setText(_translate("MainWindow", "Re-Enter Password:"))
        self.label_8.setText(_translate("MainWindow", "Phone Number:"))
        self.phoneNum.setText(_translate("MainWindow", "313-1234455"))
        self.label_9.setText(_translate("MainWindow", "Address:"))
        self.label_10.setText(_translate("MainWindow", "Email:"))
        self.email.setText(_translate("MainWindow", "0313-1234455"))
        self.label_11.setText(_translate("MainWindow", "User Type:"))
        self.userType.setItemText(0, _translate("MainWindow", "Customer"))
        self.userType.setItemText(1, _translate("MainWindow", "Distributor"))
        self.userType.setItemText(2, _translate("MainWindow", "Supplier"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.createAccount_button.setText(_translate("MainWindow", "Create Account"))
        self.address.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">222-A, XYZ Street, Gulshan-e-Iqbal</span></p></body></html>"))