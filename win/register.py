# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(640, 370)
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 100, 73, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.reg_password_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.reg_password_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reg_password_label.sizePolicy().hasHeightForWidth())
        self.reg_password_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic UI")
        font.setPointSize(20)
        self.reg_password_label.setFont(font)
        self.reg_password_label.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.reg_password_label.setStyleSheet("QLabel {\n"
"       border: 2px ;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"   \n"
"}")
        self.reg_password_label.setTextFormat(QtCore.Qt.PlainText)
        self.reg_password_label.setObjectName("reg_password_label")
        self.horizontalLayout_2.addWidget(self.reg_password_label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 104, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reg_username_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Thai UI")
        font.setPointSize(20)
        self.reg_username_label.setFont(font)
        self.reg_username_label.setStyleSheet("QLabel {\n"
"       border: 2px ;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"   \n"
"}")
        self.reg_username_label.setObjectName("reg_username_label")
        self.horizontalLayout.addWidget(self.reg_username_label)
        self.reg_password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.reg_password_edit.setGeometry(QtCore.QRect(160, 100, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.reg_password_edit.setFont(font)
        self.reg_password_edit.setAutoFillBackground(False)
        self.reg_password_edit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.reg_password_edit.setText("")
        self.reg_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reg_password_edit.setObjectName("reg_password_edit")
        self.reg_register_button = QtWidgets.QPushButton(self.centralwidget)
        self.reg_register_button.setGeometry(QtCore.QRect(70, 270, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.reg_register_button.setFont(font)
        self.reg_register_button.setMouseTracking(False)
        self.reg_register_button.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/icons8-logout-rounded-up-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reg_register_button.setIcon(icon)
        self.reg_register_button.setDefault(False)
        self.reg_register_button.setFlat(False)
        self.reg_register_button.setObjectName("reg_register_button")
        self.reg_username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.reg_username_edit.setGeometry(QtCore.QRect(160, 30, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.reg_username_edit.setFont(font)
        self.reg_username_edit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.reg_username_edit.setText("")
        self.reg_username_edit.setObjectName("reg_username_edit")
        self.reg_email_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.reg_email_edit.setGeometry(QtCore.QRect(160, 180, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.reg_email_edit.setFont(font)
        self.reg_email_edit.setAutoFillBackground(False)
        self.reg_email_edit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.reg_email_edit.setText("")
        self.reg_email_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.reg_email_edit.setObjectName("reg_email_edit")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(70, 180, 73, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.reg_email_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.reg_email_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reg_email_label.sizePolicy().hasHeightForWidth())
        self.reg_email_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic UI")
        font.setPointSize(20)
        self.reg_email_label.setFont(font)
        self.reg_email_label.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.reg_email_label.setStyleSheet("QLabel {\n"
"       border: 2px ;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"   \n"
"}")
        self.reg_email_label.setTextFormat(QtCore.Qt.PlainText)
        self.reg_email_label.setObjectName("reg_email_label")
        self.horizontalLayout_3.addWidget(self.reg_email_label)
        Register.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Register)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
        self.menubar.setObjectName("menubar")
        Register.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Register)
        self.statusbar.setObjectName("statusbar")
        Register.setStatusBar(self.statusbar)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "注册"))
        self.reg_password_label.setText(_translate("Register", "密码"))
        self.reg_username_label.setText(_translate("Register", "用户名"))
        self.reg_password_edit.setPlaceholderText(_translate("Register", "your password"))
        self.reg_register_button.setText(_translate("Register", "注册"))
        self.reg_username_edit.setPlaceholderText(_translate("Register", "your username"))
        self.reg_email_edit.setPlaceholderText(_translate("Register", "your email"))
        self.reg_email_label.setText(_translate("Register", "邮箱"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
