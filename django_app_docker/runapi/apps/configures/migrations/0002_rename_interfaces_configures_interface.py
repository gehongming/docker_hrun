# Generated by Django 3.2.7 on 2021-10-02 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configures', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configures',
            old_name='interfaces',
            new_name='interface',
        ),
    ]
