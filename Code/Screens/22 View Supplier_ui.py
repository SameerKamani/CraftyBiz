# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\DB project\DairyPro-main\Code-Connection\Screens\22 View Supplier.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 403)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 60, 221, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.supp_name = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.supp_name.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-bottom-color: rgb(0, 0, 127);")
        self.supp_name.setObjectName("supp_name")
        self.verticalLayout.addWidget(self.supp_name)
        self.supp_id = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.supp_id.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.supp_id.setObjectName("supp_id")
        self.verticalLayout.addWidget(self.supp_id)
        self.supp_address = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.supp_address.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.supp_address.setObjectName("supp_address")
        self.verticalLayout.addWidget(self.supp_address)
        self.supp_contact = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.supp_contact.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.supp_contact.setObjectName("supp_contact")
        self.verticalLayout.addWidget(self.supp_contact)
        self.email = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.email.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.email.setObjectName("email")
        self.verticalLayout.addWidget(self.email)
        self.status = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.status.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 60, 87, 221))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_2.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_4.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_5.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_6.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_7.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 127);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.closeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(270, 300, 121, 31))
        self.closeButton.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.closeButton.setObjectName("closeButton")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(-10, -20, 921, 771))
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("\n"
"\n"
"background-color: rgb(207, 232, 255);\n"
"")
        self.label_12.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_12.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.closeButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 18))
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
        self.supp_name.setText(_translate("MainWindow", "Ali"))
        self.supp_id.setText(_translate("MainWindow", "0101"))
        self.supp_address.setText(_translate("MainWindow", "222-A, XYZ Street, Gulshan-e-Iqbal"))
        self.supp_contact.setText(_translate("MainWindow", "0324-546765"))
        self.email.setText(_translate("MainWindow", "ali@gmai.com"))
        self.status.setText(_translate("MainWindow", "Active"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "ID"))
        self.label_4.setText(_translate("MainWindow", "Address:"))
        self.label_5.setText(_translate("MainWindow", "Contact:"))
        self.label_6.setText(_translate("MainWindow", "Email"))
        self.label_7.setText(_translate("MainWindow", "Activity Status:"))
        self.closeButton.setText(_translate("MainWindow", "Cancel"))
