# Generated by Django 4.1.3 on 2023-02-23 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_patientlist_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientList',
        ),
    ]
