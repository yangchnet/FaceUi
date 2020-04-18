from PyQt5 import QtCore, QtWidgets
import os
import requests
import json
import win
import cv2
import logging
import face_recognition

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

def checkImage(img) -> bool:
    image = face_recognition.load_image_file(img)
    if len(face_recognition.face_encodings(image)) > 0:
        return True
    return False


def clt_face() -> str:
    """
    采集人脸图片
    :param username:
    :return:
    """
    img_path=''
    face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
    cap = cv2.VideoCapture(0)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    delay = 15
    saved = 0

    while (True):
        if saved != 0 and delay <= 0:
            break
        # Capture frame-by-frame
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转化为灰度图
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            # print(x, y, w, h)
            roi_gray = gray[y: y + h, x:x + w]  # (ycord_start, ycord_end) 黑白图
            roi_color = frame[y: y + h, x:x + w]   # 原图

            if not saved:
                img_item = 'face.png'
                img_path = os.path.join(BASE_DIR, 'image', img_item)
                cv2.imwrite(img_path, roi_color)
                if checkImage(img_path):   # 检查采集的图像是否有效
                    logging.info('图像采集成功')
                    saved = 1
            else:
                delay -= 1   # 寻求展示效果，否则会一闪而过

            # draw a rectangle
            color = (255, 0, 0)  # BGR blue grenn red 0-255
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    # 释放摄像头资源
    cap.release()
    cv2.destroyAllWindows()
    return img_path

class IndexWindow(QtWidgets.QMainWindow, win.Ui_Index):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        #==================== bind button =======================
        # 跳转注册界面
        self.index_rigster_button.clicked.connect(self.register)

        # 登录
        self.index_id_login_button.clicked.connect(self.login)

        # 刷脸登录
        self.index_face_login_button.clicked.connect(self.login_with_face)
        #====================== end ==============================


    def build(self):
        """
        构造用户字典，存储输入的信息
        :return:
        """
        userObj = {}
        userObj['username'] = self.index_username_edit.text()
        userObj['password'] = self.index_password_edit.text()
        return userObj

    def login(self):
        userObj = self.build()
        if not self.checked(userObj):
            self.warning('存在空字段')
            return
        url = 'http://localhost:8000/pswdlogin/'
        res = requests.post(url, data=json.dumps(userObj))
        if 'no' in res.text:
            self.warning('用户不存在')
        elif 'incorrect' in res.text:
            self.warning('密码错误')
        else:
            dict = json.loads(res.text)
            self.info('登录成功')
            self.window = ProfileWindow(username=dict['username'])
            self.window.show()
            self.close()

    def login_with_face(self):
        img_path = clt_face()
        self.submit_face(img_path)

    def checked(self, userObj):
        for value in userObj.values():
            if len(value) <= 0:
                return 0
        return 1

    def warning(self, message, title='警告'):
        QtWidgets.QMessageBox.information(self, title, message, QtWidgets.QMessageBox.Ok)

    def info(self, message, title='message'):
        QtWidgets.QMessageBox.information(self, title, message, QtWidgets.QMessageBox.Ok)

    def register(self):
        self.window = RegisterWindow()
        self.window.show()
        self.close()

    def submit_face(self, img_path):
        file = {
            'face': open(img_path, 'rb')
        }
        url = 'http://localhost:8000/facelogin/'
        res = requests.post(url, files=file)
        if 'error' in res.text:
            self.info('登录失败！')
        else:
            dict = json.loads(res.text)
            self.info('登录成功')
            self.window = ProfileWindow(username=dict['username'])
            self.window.show()
            self.close()


class RegisterWindow(QtWidgets.QMainWindow, win.Ui_Register):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # ==================== bind button =======================
        self.reg_register_button.clicked.connect(self.register)
        # ====================== end =============================

    def build(self):
        userObj = {}
        userObj['username'] = self.reg_username_edit.text()
        userObj['password'] = self.reg_password_edit.text()
        userObj['email'] = self.reg_email_edit.text()
        return userObj

    def register(self):
        userObj = self.build()
        if not self.check(userObj):
            return
        logging.info('注册字段验证已通过')
        url = 'http://localhost:8000/fusers/'
        res = requests.post(url, data=json.dumps(userObj))
        logging.info('已发送注册信息，开始采集人脸图像')
        if 'already exists' in res.text:
            self.warning('用户名已存在')
            return
        logging.info('开始采集人脸图像')
        img_path = clt_face()
        self.submit_face(userObj['username'], img_path)

    def warning(self, message, title='警告'):
        QtWidgets.QMessageBox.information(self, title, message, QtWidgets.QMessageBox.Ok)

    def info(self, message, title='message'):
        QtWidgets.QMessageBox.information(self, title, message, QtWidgets.QMessageBox.Ok)

    def check(self, userObj):
        flag = 0
        for value in userObj.values():
            if len(value) <= 0:
                flag = 1
        if flag:
            self.warning("所有字段必须填写完整")
            return 0
        else:
            return 1

    def submit_face(self, username, img_path):
        data = {
            'username': username
        }
        file = {
            'face': open(img_path, 'rb')
        }
        url = 'http://localhost:8000/upload/'
        res = requests.post(url, data=data, files=file)

        # 信息上传完成，要求用户重新登录
        self.info('你已经完成注册，现在可以尝试登录了！')
        logging.info('用户已注册，跳转登录页面')
        self.window = IndexWindow()
        self.window.show()
        self.close()


class UpdateWindow(QtWidgets.QMainWindow, win.Ui_Update):
    def __init__(self, username):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.username = username


        # ==================== bind button =======================
        # 返回profile页
        self.upt_return_button.clicked.connect(self.profile)

        # 更新信息
        self.update_button.clicked.connect(self.update)
        # ====================== end ==============================
        self.setinfo()


    def getinfo(self) -> dict:
        data = {"username": self.username}
        url = 'http://localhost:8000/getinfo/'
        res = requests.post(url, data=data)
        return json.loads(res.text)

    def setinfo(self):
        info = self.getinfo()
        self.upt_id_edit.setText(str(info['id']))
        self.upt_username_edit.setText(info['username'])
        self.upt_email_edit.setText(info['email'])
        self.upt_age_edit.setText(str(info['age']))
        self.upt_job_edit.setText(info['job'])
        self.upt_tel_edit.setText(str(info['tel']))
        if info['sex']:
            self.upt_sex_edit.setText('男')
        else:
            self.upt_sex_edit.setText('女')

    def warning(self, message, title='警告'):
        QtWidgets.QMessageBox.information(self, title, message, QtWidgets.QMessageBox.Ok)

    def info(self, message, title='message'):
        QtWidgets.QMessageBox.information(self, title, message, QtWidgets.QMessageBox.Ok)

    def build(self) -> dict:
        info = {}
        info['id'] = int(self.upt_id_edit.text())
        info['username'] = self.upt_username_edit.text()
        info['email'] = self.upt_email_edit.text()
        info['age'] = int(self.upt_age_edit.text())
        info['job'] = self.upt_job_edit.text()
        info['tel'] = int(self.upt_tel_edit.text())
        if self.upt_sex_edit.text() != '男' and self.upt_sex_edit.text() != '女':
            self.warning('性别输入有误')
            return {}
        elif self.upt_sex_edit.text() == '男':
            info['sex'] = True
        elif self.upt_sex_edit.text() == '女':
            info['sex'] = False
        return info

    def update(self):
        info = self.build()
        if info == {}:
            return
        url = 'http://127.0.0.1:8000/updateinfo/'
        res = requests.post(url, data=json.dumps(info))
        if res.status_code == 200:
            self.info('信息更新完成')

        self.profile()

    def profile(self):
        self.window = ProfileWindow(username=self.username)
        self.window.show()
        self.close()




class ProfileWindow(QtWidgets.QMainWindow, win.Ui_Profile):
    def __init__(self, username):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.username = username


        # ==================== bind button =======================
        # 跳转更新界面
        self.prf_update_button.clicked.connect(self.update)

        # 注销退出
        self.prf_logout_button.clicked.connect(self.logout)
        # ====================== end ==============================

        self.setinfo()

    def getinfo(self) -> dict:
        data = {"username": self.username}
        url = 'http://localhost:8000/getinfo/'
        res = requests.post(url, data=data)
        return json.loads(res.text)

    def setinfo(self):
        info = self.getinfo()
        self.prf_id_edit.setText(str(info['id']))
        self.prf_username_edit.setText(info['username'])
        self.prf_email_edit.setText(info['email'])
        self.prf_age_edit.setText(str(info['age']))
        self.prf_job_edit.setText(info['job'])
        self.prf_tel_edit.setText(str(info['tel']))
        if info['sex'] :
            self.prf_sex_edit.setText('男')
        else:
            self.prf_sex_edit.setText('女')

    def logout(self):
        data = {"username": self.username}
        url = 'http://localhost:8000/logout/'
        res = requests.post(url, data=data)

        self.window = IndexWindow()
        self.window.show()
        self.close()


    def update(self):
        self.window = UpdateWindow(username=self.username)
        self.window.show()
        self.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = IndexWindow()
    w.show()
    sys.exit(app.exec_())
