# Generated by Django 4.1.3 on 2023-03-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0082_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('online', 'Online Payment'), ('offline', 'Offline Payment')], max_length=7)),
                ('payment_method', models.CharField(choices=[('card', 'Card Payment'), ('upi', 'UPI Payment'), ('net-banking', 'Net Banking Payment')], max_length=12)),
            ],
        ),
    ]