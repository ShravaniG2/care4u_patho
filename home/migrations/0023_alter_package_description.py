# Generated by Django 4.1.3 on 2023-02-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_package_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]