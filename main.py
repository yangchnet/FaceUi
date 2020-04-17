from PyQt5 import QtCore, QtWidgets
import os
import win


class IndexWindow(QtWidgets.QMainWindow, win.Ui_Index):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # bind button
        self.index_rigster_button.clicked.connect(self.register)

    def register(self):
        self.window = RegisterWindow()
        self.window.show()
        self.close()



class RegisterWindow(QtWidgets.QMainWindow, win.Ui_Register):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


class UpdateWindow(QtWidgets.QMainWindow, win.Ui_Update):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


class ProfileWindow(QtWidgets.QMainWindow, win.Ui_Profile):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = IndexWindow()
    w.show()
    sys.exit(app.exec_())
