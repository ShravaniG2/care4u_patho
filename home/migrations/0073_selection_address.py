# Generated by Django 4.1.3 on 2023-02-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0072_rename_options_selection_listof_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='selection',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
    ]
