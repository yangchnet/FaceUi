from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class Fuser(AbstractUser):
    """
        继承抽象用户，抽象用户中已定义用户名以及邮箱
    """
    job = models.CharField(max_length=50, blank=True, verbose_name='职业')
    age = models.IntegerField(blank=True, verbose_name='年龄')
    sex = models.BooleanField(blank=True, verbose_name='性别')  # 布尔型，1代表男，0代表女
    tel = models.CharField(max_length=20, blank=True, verbose_name='电话')
    face = models.ImageField(blank=False, verbose_name='照片')  # 用于人脸识别
