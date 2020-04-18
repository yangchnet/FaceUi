from django.db import models
from django.contrib.auth.models import User, AbstractUser
from rest_framework import serializers
# Create your models here.


class Fuser(AbstractUser):
    """
        继承抽象用户，抽象用户中已定义用户名以及邮箱
    """
    email = models.CharField(max_length=50, null=False, verbose_name='邮箱')
    job = models.CharField(max_length=50, blank=True, verbose_name='职业', null=True)
    age = models.IntegerField(blank=True, verbose_name='年龄', null=True)
    sex = models.BooleanField(blank=True, verbose_name='性别',  null=True)  # 布尔型，1代表男，0代表女
    tel = models.CharField(max_length=20, blank=True, verbose_name='电话', null=True)


class Face(models.Model):
    username = models.CharField(max_length=50, verbose_name='用户名', unique=True)
    face = models.ImageField(blank=False, verbose_name='人脸图像')

    def __str__(self):
        return self.username
