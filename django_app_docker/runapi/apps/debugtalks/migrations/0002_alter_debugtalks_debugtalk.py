# Generated by Django 3.2.7 on 2021-10-02 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debugtalks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debugtalks',
            name='debugtalk',
            field=models.TextField(default='debugtalk.py', help_text='debugtalk.py文件', null=True, verbose_name='debugtalk.py文件'),
        ),
    ]