# Generated by Django 4.1.3 on 2022-11-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_registermodel_registeruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]