# Generated by Django 4.1.3 on 2022-11-29 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_registermodel_dob'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registermodel',
            new_name='registeruser',
        ),
    ]