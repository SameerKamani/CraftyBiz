# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\DB project\DairyPro-main\Code-Connection\Screens\1 User Type.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 372)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(190, 60, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 90, 35, 10))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.loginAdmin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginAdmin.setGeometry(QtCore.QRect(160, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.loginAdmin.setFont(font)
        self.loginAdmin.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.loginAdmin.setObjectName("loginAdmin")
        self.loginCustomer = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginCustomer.setGeometry(QtCore.QRect(160, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.loginCustomer.setFont(font)
        self.loginCustomer.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.loginCustomer.setObjectName("loginCustomer")
        self.loginSupplier = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginSupplier.setGeometry(QtCore.QRect(300, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.loginSupplier.setFont(font)
        self.loginSupplier.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.loginSupplier.setObjectName("loginSupplier")
        self.createAccount = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createAccount.setGeometry(QtCore.QRect(160, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.createAccount.setFont(font)
        self.createAccount.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.createAccount.setObjectName("createAccount")
        self.loginDistributor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginDistributor.setGeometry(QtCore.QRect(300, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.loginDistributor.setFont(font)
        self.loginDistributor.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.loginDistributor.setObjectName("loginDistributor")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-80, 70, 751, 311))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\Users\\hp\\Documents\\CS_Undergrad\\Semester_3\\DATABASE\\DB project\\DairyPro-main\\Code-Connection\\Screens\\../../../../../../../../Downloads/image-from-rawpixel-id-7037372-original.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 10, 61, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("c:\\Users\\hp\\Documents\\CS_Undergrad\\Semester_3\\DATABASE\\DB project\\DairyPro-main\\Code-Connection\\Screens\\../../../../bd_final_project/DairyPro/DB_ConnectionsFiles/DB_project/—Pngtree—food elements hand drawn cute_4056724.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(-30, -20, 961, 821))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet("\n"
"\n"
"background-color: rgb(207, 232, 255);\n"
"")
        self.label_13.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_13.raise_()
        self.label_3.raise_()
        self.label_12.raise_()
        self.label_2.raise_()
        self.loginAdmin.raise_()
        self.loginCustomer.raise_()
        self.loginSupplier.raise_()
        self.createAccount.raise_()
        self.loginDistributor.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 18))
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
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Log In</span></p></body></html>"))
        self.loginAdmin.setText(_translate("MainWindow", "Log in as Admin"))
        self.loginCustomer.setText(_translate("MainWindow", "Log in as Customer"))
        self.loginSupplier.setText(_translate("MainWindow", "Log in as Supplier"))
        self.createAccount.setText(_translate("MainWindow", "Create Account"))
        self.loginDistributor.setText(_translate("MainWindow", "Log in as Distributor"))
