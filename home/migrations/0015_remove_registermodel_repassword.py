# Generated by Django 4.1.3 on 2022-11-30 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rename_registeruser_registermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registermodel',
            name='repassword',
        ),
    ]