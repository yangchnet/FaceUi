# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Profile(object):
    def setupUi(self, Profile):
        Profile.setObjectName("Profile")
        Profile.resize(480, 625)
        self.centralwidget = QtWidgets.QWidget(Profile)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(190, 142, 241, 51))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.prf_username_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_10)
        self.prf_username_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_username_edit.setFont(font)
        self.prf_username_edit.setObjectName("prf_username_edit")
        self.verticalLayout_10.addWidget(self.prf_username_edit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 142, 121, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.prf_username_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_username_label.setFont(font)
        self.prf_username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prf_username_label.setObjectName("prf_username_label")
        self.verticalLayout_2.addWidget(self.prf_username_label)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(190, 322, 241, 51))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.prf_job_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.prf_job_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_job_edit.setFont(font)
        self.prf_job_edit.setObjectName("prf_job_edit")
        self.verticalLayout_12.addWidget(self.prf_job_edit)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(40, 442, 121, 51))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.prf_email_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_email_label.setFont(font)
        self.prf_email_label.setScaledContents(False)
        self.prf_email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prf_email_label.setWordWrap(False)
        self.prf_email_label.setIndent(2)
        self.prf_email_label.setObjectName("prf_email_label")
        self.verticalLayout_5.addWidget(self.prf_email_label)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(190, 202, 241, 51))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.prf_age_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.prf_age_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_age_edit.setFont(font)
        self.prf_age_edit.setObjectName("prf_age_edit")
        self.verticalLayout_9.addWidget(self.prf_age_edit)
        self.prf_logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.prf_logout_button.setGeometry(QtCore.QRect(40, 510, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_logout_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prf_logout_button.setIcon(icon)
        self.prf_logout_button.setIconSize(QtCore.QSize(30, 30))
        self.prf_logout_button.setObjectName("prf_logout_button")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 202, 121, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.prf_age_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_age_label.setFont(font)
        self.prf_age_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prf_age_label.setObjectName("prf_age_label")
        self.verticalLayout_3.addWidget(self.prf_age_label)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 82, 121, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pr_fid_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pr_fid_label.setFont(font)
        self.pr_fid_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pr_fid_label.setObjectName("pr_fid_label")
        self.verticalLayout.addWidget(self.pr_fid_label)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(190, 82, 241, 51))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.prf_id_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.prf_id_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_id_edit.setFont(font)
        self.prf_id_edit.setObjectName("prf_id_edit")
        self.verticalLayout_8.addWidget(self.prf_id_edit)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(40, 322, 121, 51))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.prf_job_label = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_job_label.setFont(font)
        self.prf_job_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prf_job_label.setObjectName("prf_job_label")
        self.verticalLayout_7.addWidget(self.prf_job_label)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(190, 382, 241, 51))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.prf_tel_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_13)
        self.prf_tel_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_tel_edit.setFont(font)
        self.prf_tel_edit.setObjectName("prf_tel_edit")
        self.verticalLayout_13.addWidget(self.prf_tel_edit)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(40, 262, 121, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.prf_sex_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_sex_label.setFont(font)
        self.prf_sex_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prf_sex_label.setObjectName("prf_sex_label")
        self.verticalLayout_4.addWidget(self.prf_sex_label)
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(190, 442, 241, 51))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.prf_email_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_14)
        self.prf_email_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_email_edit.setFont(font)
        self.prf_email_edit.setObjectName("prf_email_edit")
        self.verticalLayout_14.addWidget(self.prf_email_edit)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(40, 382, 121, 51))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.prf_tel_label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_tel_label.setFont(font)
        self.prf_tel_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prf_tel_label.setObjectName("prf_tel_label")
        self.verticalLayout_6.addWidget(self.prf_tel_label)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(190, 262, 241, 51))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.prf_sex_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_11)
        self.prf_sex_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_sex_edit.setFont(font)
        self.prf_sex_edit.setObjectName("prf_sex_edit")
        self.verticalLayout_11.addWidget(self.prf_sex_edit)
        self.prf_update_button = QtWidgets.QPushButton(self.centralwidget)
        self.prf_update_button.setGeometry(QtCore.QRect(310, 10, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prf_update_button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prf_update_button.setIcon(icon1)
        self.prf_update_button.setIconSize(QtCore.QSize(30, 30))
        self.prf_update_button.setFlat(True)
        self.prf_update_button.setObjectName("prf_update_button")
        Profile.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Profile)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 27))
        self.menubar.setObjectName("menubar")
        Profile.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Profile)
        self.statusbar.setObjectName("statusbar")
        Profile.setStatusBar(self.statusbar)

        self.retranslateUi(Profile)
        QtCore.QMetaObject.connectSlotsByName(Profile)

    def retranslateUi(self, Profile):
        _translate = QtCore.QCoreApplication.translate
        Profile.setWindowTitle(_translate("Profile", "MainWindow"))
        self.prf_username_label.setText(_translate("Profile", "用户名"))
        self.prf_email_label.setText(_translate("Profile", "邮箱"))
        self.prf_logout_button.setText(_translate("Profile", "注销"))
        self.prf_age_label.setText(_translate("Profile", "年龄"))
        self.pr_fid_label.setText(_translate("Profile", "ID"))
        self.prf_job_label.setText(_translate("Profile", "职业"))
        self.prf_sex_label.setText(_translate("Profile", "性别"))
        self.prf_tel_label.setText(_translate("Profile", "Tel"))
        self.prf_update_button.setText(_translate("Profile", "更新信息"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Profile = QtWidgets.QMainWindow()
    ui = Ui_Profile()
    ui.setupUi(Profile)
    Profile.show()
    sys.exit(app.exec_())