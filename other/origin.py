import sys
import cv2
import face_recognition
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox, QLineEdit, QPushButton, QHBoxLayout, \
    QVBoxLayout, QTextBrowser
from PyQt5.QtCore import QTextCodec

user_dict = {
    'wyc':
        {
            'pwd': '123456',
            'num': '16114444',
            'addr': 'Chongqing'
        },
    'wjw':
        {
            'pwd': '123',
            'num': '16114448',
            'addr': 'Shenzhen'
        }
}


class Init_interface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle("基于opencv用户登陆系统")
        self.btn1 = QPushButton("使用用户名密码登录")
        self.btn2 = QPushButton("使用人脸识别登录")
        # btn.setGeometry()
        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(self.btn1)
        hboxLayout.addWidget(self.btn2)

        self.setLayout(hboxLayout)
        self.btn1.clicked.connect(self.jump_to_login)
        self.btn2.clicked.connect(self.jump_to_rec)

    def jump_to_login(self):
        self.hide()
        self.login = LoginWidget()
        self.login.show()

    def jump_to_rec(self):
        self.hide()
        self.ex = Recognition()
        self.ex.show()


class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle("用户名密码登录")
        userLabel = QLabel('用户名:')
        userLabel.setFixedWidth(100)
        passWordLabel = QLabel('密码：')
        passWordLabel.setFixedWidth(100)
        self.userLineEdit = QLineEdit()
        self.passWordLineEdit = QLineEdit()
        self.passWordLineEdit.setEchoMode(QLineEdit.Password)
        loginBtn = QPushButton('登录')

        hboxLayout_1 = QHBoxLayout()
        hboxLayout_1.addWidget(userLabel)
        hboxLayout_1.addWidget(self.userLineEdit)

        hboxLayout_2 = QHBoxLayout()
        hboxLayout_2.addWidget(passWordLabel)
        hboxLayout_2.addWidget(self.passWordLineEdit)

        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(hboxLayout_1)
        mainLayout.addLayout(hboxLayout_2)
        mainLayout.addWidget(loginBtn)

        self.setWindowTitle('登陆界面')
        # self.show()

        loginBtn.clicked.connect(self.loginSlot)

    def loginSlot(self):
        user = self.userLineEdit.text()
        psw = self.passWordLineEdit.text()

        if user in user_dict:
            if psw == user_dict[user]['pwd']:
                print("ok")
                self.hide()
                # ex = Recognition()
                # ex.show()
                self.iwfup = InfoWidgetFromUserPwd(user)
                self.iwfup.show()
            else:
                QMessageBox.warning(self, "未通过验证！", "密码输入错误", QMessageBox.Yes)
                print("密码输入错误")
        else:
            QMessageBox.warning(self, "未通过验证！", "用户名不存在", QMessageBox.Yes)
            print("用户名不存在")


class Recognition(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.hide()
        self.setWindowOpacity(0)
        self.rec()
        # self.show()
        # pass

    def print_name(self, user):
        self.iwffr = InfoWidgetFromFaceRecognition(user)
        self.iwffr.show()

    def rec(self):
        wyc = cv2.imread('image/my-face/lichang.jpg')
        ### 填写别人图片的路径
        # 例如 wjw = cv2.imread('')

        # 1.2 对图片中的人脸进行编码
        wyc_face_encoding = face_recognition.face_encodings(wyc)[0]
        ### 设置编码
        # 例如 wjw_face_encoding = face_recognition.face_encodings(wjw)[0]

        # 1.3 准备人脸库的人脸编码列表
        known_face_encodings = [wyc_face_encoding]
        ### 上面一行代码 包括多人脸库 可改为:
        # known_face_encodings = [wyc_face_encoding, wjw_face_encoding]

        # 1.4 准备人脸库中人脸编码对应的姓名
        known_face_names = ['wyc']
        ### 上面一行代码 包括多人脸库 可改为:
        # known_face_names = ['wyc','wjw']

        # 2. 捕获视频中图片
        vc = cv2.VideoCapture(0)
        while True:
            # 获取视频中，每一帧的图片；
            ret, img = vc.read()
            if not ret:
                print('没有捕获到视频')
                break

            # 3. 发现视频中图片中人脸位置
            locations = face_recognition.face_locations(img)

            # 3.1 图片中人脸进行编码
            face_encodings = face_recognition.face_encodings(img, locations)

            # 遍历 locations， face_encodings, 识别图片中人脸
            # location: top, right, bottom, left
            for (top, right, bottom, left), face_encodings in zip(locations, face_encodings):

                # 4. 识别视频中图片中人脸的姓名
                matchs = face_recognition.compare_faces(known_face_encodings, face_encodings)
                self.name = 'unknown'
                for match, known_name in zip(matchs, known_face_names):
                    if match:
                        self.name = known_name
                        # str = "人脸识别成功，该用户为：" + self.name
                        # QMessageBox.information(self, "消息框标题", str, QMessageBox.Yes)
                        vc.release()
                        cv2.destroyAllWindows()
                        self.print_name(self.name)
                        break
                    else:
                        QMessageBox.warning(self, "未通过验证！标题", "人脸匹配失败", QMessageBox.Yes)
                        break
                # 4.1 标记人脸的位置
                cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

                # 4.2 标记人脸的姓名
                cv2.putText(img, self.name, (left, top - 20), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 2)

            # 5. 展示

            # cv2.startWindowThread()
            cv2.imshow('Video', img)

            # 6. 释放资源
            if cv2.waitKey(1) != -1:
                # 关闭摄像头
                vc.release()
                # 销毁窗口
                cv2.destroyAllWindows()
                # 结束循环
            break

    # @staticmethod
    # def print_name(self):
    #     return self.name
    #     print(self.name)


class InfoWidgetFromUserPwd(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle("登录成功")

        # print(Recognition.print_name())
        # self.name
        num = user_dict[self.name]['num']
        addr = user_dict[self.name]['addr']
        str_out = self.name + "登录成功！\n" + "学号是" + num + "地址是" + addr
        print(str_out)
        # QMessageBox.about(self, '学号:'+num+'登录成功', "地址："+addr)
        # self.num = user_dict[rec.name]['num']
        # self.addr = user_dict[rec.name]['addr']
        # QMessageBox.about(self, '学号:'+num+'登录成功', "地址："+addr)
        self.text_browser = QTextBrowser()
        self.text_browser.move(160, 30)
        self.text_browser.resize(200, 200)
        self.cursot = self.text_browser.textCursor()
        self.text_browser.moveCursor(self.cursot.End)
        # self.text_browser.setGeometry(30, 30, 500, 500)
        self.text_browser.append(str_out)
        print(str_out)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.text_browser)
        self.setLayout(mainLayout)


class InfoWidgetFromFaceRecognition(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.initUI()

    def initUI(self):
        self.setGeometry(655, 35, 400, 400)
        self.setWindowTitle("登录成功")

        # print(Recognition.print_name())
        # self.name
        num = user_dict[self.name]['num']
        addr = user_dict[self.name]['addr']
        str_out = self.name + "登录成功！\n" + "学号是" + num + "地址是" + addr
        # QMessageBox.about(self, '学号:'+num+'登录成功', "地址："+addr)
        # self.num = user_dict[rec.name]['num']
        # self.addr = user_dict[rec.name]['addr']
        # QMessageBox.about(self, '学号:'+num+'登录成功', "地址："+addr)
        self.text_browser = QTextBrowser()
        self.text_browser.move(160, 30)
        self.text_browser.resize(200, 200)
        self.cursot = self.text_browser.textCursor()
        self.text_browser.moveCursor(self.cursot.End)
        self.text_browser.append(str_out)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.text_browser)
        self.setLayout(mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ii = Init_interface()
    ii.show()
    sys.exit(app.exec_())



# 三个界面： 登录（账号密码以及人脸识别登录）、查看个人信息、更新个人信息
# 用户数据字段： ID，姓名、邮箱、职业、年龄、性别、电话、
# 提供后台管理功能：使用API方式实现
