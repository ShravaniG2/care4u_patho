# Generated by Django 4.1.3 on 2023-02-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='gender',
            field=models.CharField(max_length=13),
        ),
    ]
