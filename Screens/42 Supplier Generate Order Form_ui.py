# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\bd_final_project\DairyPro\DB_ConnectionsFiles\DB_project\42 Supplier Generate Order Form.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 419)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 40, 281, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Matt_id = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.Matt_id.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.Matt_id.setObjectName("Matt_id")
        self.verticalLayout.addWidget(self.Matt_id)
        self.mat_name = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.mat_name.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.mat_name.setObjectName("mat_name")
        self.verticalLayout.addWidget(self.mat_name)
        self.supp_id = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.supp_id.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.supp_id.setObjectName("supp_id")
        self.verticalLayout.addWidget(self.supp_id)
        self.order_date = QtWidgets.QDateEdit(parent=self.layoutWidget)
        self.order_date.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.order_date.setObjectName("order_date")
        self.verticalLayout.addWidget(self.order_date)
        self.quantity = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.quantity.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.quantity.setObjectName("quantity")
        self.verticalLayout.addWidget(self.quantity)
        self.viewButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.viewButton_5.setGeometry(QtCore.QRect(310, 320, 121, 31))
        self.viewButton_5.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.viewButton_5.setObjectName("viewButton_5")
        self.order_gen = QtWidgets.QPushButton(parent=self.centralwidget)
        self.order_gen.setGeometry(QtCore.QRect(180, 320, 121, 31))
        self.order_gen.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.order_gen.setObjectName("order_gen")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, -10, 721, 401))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("\n"
"\n"
"background-color: rgb(207, 232, 255);\n"
"")
        self.label_4.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(180, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 90, 45))
        self.label_3.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"font-color: rgb(0, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 190, 90, 57))
        self.label_7.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"font-color: rgb(0, 0, 127);")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 130, 90, 77))
        self.label_5.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"font-color: rgb(0, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 90, 81))
        self.label_2.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"font-color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 90, 51))
        self.label.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"font-color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.label_4.raise_()
        self.layoutWidget.raise_()
        self.viewButton_5.raise_()
        self.order_gen.raise_()
        self.label_12.raise_()
        self.label_3.raise_()
        self.label_7.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 18))
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
        self.Matt_id.setText(_translate("MainWindow", "56"))
        self.mat_name.setText(_translate("MainWindow", "1001"))
        self.supp_id.setText(_translate("MainWindow", "112244"))
        self.quantity.setText(_translate("MainWindow", "500"))
        self.viewButton_5.setText(_translate("MainWindow", "Cancel"))
        self.order_gen.setText(_translate("MainWindow", "Generate Order"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Generate Order</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Quantity:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Order Date:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Supplier ID:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Material Name:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Material ID:</span></p></body></html>"))
