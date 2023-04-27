import datetime
from django.db import models
import pytz
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# set timezone to IST
settings.TIME_ZONE = 'Asia/Kolkata'
timezone.activate(settings.TIME_ZONE)



# Create your models here.
class registermodel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,null=True)
    dob= models.DateField(null=True)
    email=models.EmailField()
    phone= models.CharField(max_length=50,null=True)
    username= models.CharField(max_length=150)
    password= models.CharField(max_length=150)

class test(models.Model):
    t_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=13)
    t_amt=models.IntegerField(primary_key=False)
    preparation= models.CharField(max_length=100,null=True)
    sample= models.CharField(max_length=100)
    test_id= models.CharField(max_length=100,primary_key=True)

class package(models.Model):
    package_name=models.CharField(max_length=200)
    gender=models.CharField(max_length=13)
    package_amt=models.IntegerField(primary_key=False)
    preparation= models.CharField(max_length=200)
    sample= models.CharField(max_length=200)
    package_id= models.CharField(max_length=100,primary_key=True)
    description= models.CharField(max_length=1000)

class adminmodel(models.Model):
    first_n=models.CharField(max_length=50)
    last_n=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    dob= models.DateField()
    email=models.EmailField()
    phone= models.CharField(max_length=50)
    id= models.CharField(max_length=150,primary_key=True)
    password= models.CharField(max_length=150)

class doctor(models.Model):
    qualification = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    loc = models.CharField(max_length=200)
    d_email=models.EmailField(null=True)
    d_phone=models.IntegerField(null=True)
    d_id= models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=100)

class Patient_List(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,db_column='username',to_field='username')
    p_name = models.CharField(max_length=100)
    p_age = models.IntegerField()
    

class feedback(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,db_column='username',to_field='username')
    experience=models.CharField(max_length=500)
    improvement=models.CharField(max_length=500)
    rate=models.CharField(max_length=50)

class Booking(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,db_column='username',to_field='username',default=True)
    listof_patient = models.ManyToManyField(Patient_List)
    doctors = models.ManyToManyField(doctor)
    address = models.CharField(max_length=255)
    sch_date = models.DateField()
    sch_time = models.CharField(max_length=255)
    d_name = models.CharField(max_length=255)
    d_email = models.CharField(max_length=255)
    items=models.CharField(max_length=1000,default="")
    b_date = models.DateTimeField(auto_now_add=True)


class appointment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,db_column='username',to_field='username')
    doc_name = models.CharField(max_length=255)
    patient_name = models.CharField(max_length=255)
    appointment_date = models.DateTimeField(auto_now_add=True)
    sch_date = models.DateField()
    sch_time = models.CharField(max_length=255)


    def save(self, *args, **kwargs):
        tz = pytz.timezone('Asia/Kolkata')  # Set timezone to IST
        self.appointment_date = datetime.datetime.now(tz)  # Set b_date to current time in IST
        super(appointment, self).save(*args, **kwargs)

class Payment(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,db_column='username',to_field='username')
    pay_id = models.AutoField(primary_key=True)

    PAYMENT_TYPE_CHOICES = [
        ('Online', 'Online Payment'),
        ('Offline', 'Offline Payment'),
    ]
   
    payment_type = models.CharField(max_length=7, choices=PAYMENT_TYPE_CHOICES)
    p_date = models.DateTimeField(default=timezone.now, verbose_name='Date and Time')
    

