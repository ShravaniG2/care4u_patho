# Generated by Django 4.1.3 on 2023-02-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0061_delete_myselectedoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySelectedOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('selected_options', models.ManyToManyField(to='home.patient_list')),
            ],
        ),
    ]
