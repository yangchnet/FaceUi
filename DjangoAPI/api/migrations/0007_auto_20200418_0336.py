# Generated by Django 3.0.5 on 2020-04-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200418_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('face', models.ImageField(upload_to='', verbose_name='人脸图像')),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.RemoveField(
            model_name='fuser',
            name='face',
        ),
    ]
