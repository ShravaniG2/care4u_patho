# Generated by Django 4.1.3 on 2023-02-24 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_alter_patientlist_p_name_alter_patientlist_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientList',
        ),
    ]
