# Generated by Django 3.0.5 on 2020-04-18 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
    ]
