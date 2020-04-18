# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Index(object):
    def setupUi(self, Index):
        Index.setObjectName("Index")
        Index.resize(600, 336)
        font = QtGui.QFont()
        font.setPointSize(20)
        Index.setFont(font)
        Index.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Index)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 60, 104, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.index_username_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Thai UI")
        font.setPointSize(20)
        self.index_username_label.setFont(font)
        self.index_username_label.setStyleSheet("QLabel {\n"
                                                "       border: 2px ;\n"
                                                "    border-radius: 4px;\n"
                                                "    padding: 2px;\n"
                                                "   \n"
                                                "}")
        self.index_username_label.setObjectName("index_username_label")
        self.horizontalLayout.addWidget(self.index_username_label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 130, 73, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.index_pass_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.index_pass_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.index_pass_label.sizePolicy().hasHeightForWidth())
        self.index_pass_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic UI")
        font.setPointSize(20)
        self.index_pass_label.setFont(font)
        self.index_pass_label.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.index_pass_label.setStyleSheet("QLabel {\n"
                                            "       border: 2px ;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 2px;\n"
                                            "   \n"
                                            "}")
        self.index_pass_label.setTextFormat(QtCore.Qt.PlainText)
        self.index_pass_label.setObjectName("index_pass_label")
        self.horizontalLayout_2.addWidget(self.index_pass_label)
        self.index_username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.index_username_edit.setGeometry(QtCore.QRect(160, 60, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.index_username_edit.setFont(font)
        self.index_username_edit.setStyleSheet("QLineEdit {\n"
                                               "    border: 2px solid gray;\n"
                                               "    border-radius: 10px;\n"
                                               "    padding: 0 8px;\n"
                                               "    background: white;\n"
                                               "    selection-background-color: darkgray;\n"
                                               "}")
        self.index_username_edit.setText("")
        self.index_username_edit.setObjectName("index_username_edit")
        self.index_password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.index_password_edit.setGeometry(QtCore.QRect(160, 130, 381, 61))
        self.index_password_edit.setAutoFillBackground(False)
        self.index_password_edit.setStyleSheet("QLineEdit {\n"
                                               "    border: 2px solid gray;\n"
                                               "    border-radius: 10px;\n"
                                               "    padding: 0 8px;\n"
                                               "    background: white;\n"
                                               "    selection-background-color: darkgray;\n"
                                               "}")
        self.index_password_edit.setText("")
        self.index_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.index_password_edit.setObjectName("index_password_edit")
        self.index_face_login_button = QtWidgets.QPushButton(self.centralwidget)
        self.index_face_login_button.setGeometry(QtCore.QRect(310, 230, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.index_face_login_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.index_face_login_button.setIcon(icon)
        self.index_face_login_button.setObjectName("index_face_login_button")
        self.index_id_login_button = QtWidgets.QPushButton(self.centralwidget)
        self.index_id_login_button.setGeometry(QtCore.QRect(60, 230, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.index_id_login_button.setFont(font)
        self.index_id_login_button.setMouseTracking(False)
        self.index_id_login_button.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/icons8-logout-rounded-up-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.index_id_login_button.setIcon(icon1)
        self.index_id_login_button.setDefault(False)
        self.index_id_login_button.setFlat(False)
        self.index_id_login_button.setObjectName("index_id_login_button")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(370, 190, 185, 38))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.index_no_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.index_no_label.setFont(font)
        self.index_no_label.setObjectName("index_no_label")
        self.horizontalLayout_3.addWidget(self.index_no_label)
        self.index_rigster_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.index_rigster_button.setFont(font)
        self.index_rigster_button.setStyleSheet("QButton{\n"
                                                "    color: blue;\n"
                                                "}")
        self.index_rigster_button.setFlat(True)
        self.index_rigster_button.setObjectName("index_rigster_button")
        self.horizontalLayout_3.addWidget(self.index_rigster_button)
        Index.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Index)
        self.statusbar.setObjectName("statusbar")
        Index.setStatusBar(self.statusbar)

        self.retranslateUi(Index)
        QtCore.QMetaObject.connectSlotsByName(Index)

    def retranslateUi(self, Index):
        _translate = QtCore.QCoreApplication.translate
        Index.setWindowTitle(_translate("Index", "登录"))
        self.index_username_label.setText(_translate("Index", "用户名"))
        self.index_pass_label.setText(_translate("Index", "密码"))
        self.index_username_edit.setPlaceholderText(_translate("Index", "Please input your username"))
        self.index_password_edit.setPlaceholderText(_translate("Index", "Please input your password"))
        self.index_face_login_button.setText(_translate("Index", "人脸识别登录"))
        self.index_id_login_button.setText(_translate("Index", "账号密码登录"))
        self.index_no_label.setText(_translate("Index", "没有账号？"))
        self.index_rigster_button.setText(_translate("Index", "注册一个"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Index = QtWidgets.QMainWindow()
    ui = Ui_Index()
    ui.setupUi(Index)
    Index.show()
    sys.exit(app.exec_())
