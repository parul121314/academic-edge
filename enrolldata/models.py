from django.db import models
from distutils.command.upload import upload

# class enrolldata(models.Model):
#     regno=models.CharField(max_length=50)
#     name=models.CharField(max_length=50)
#     fname=models.CharField(max_length=50)
#     mname=models.CharField(max_length=50)
#     dob=models.CharField(max_length=50)
#     email=models.CharField(max_length=50)
#     phone=models.CharField(max_length=50)
#     address=models.CharField(max_length=50)
#     city=models.CharField(max_length=50)
#     gender=models.CharField(max_length=50)
#     photo=models.CharField(max_length=50)
#     btime=models.CharField(max_length=50)
#     pay_mode=models.CharField(max_length=50)
#     name_on_card=models.CharField(max_length=50)
#     card_no=models.CharField(max_length=50)
#     expiry=models.CharField(max_length=50)
#     cvv=models.CharField(max_length=50)

class EnrollFormData(models.Model):
    regno=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='static/studentimage',default="")
    btime=models.CharField(max_length=50)
    pay_mode=models.CharField(max_length=50)
    name_on_card=models.CharField(max_length=50)
    card_no=models.CharField(max_length=50)
    expiry=models.CharField(max_length=50)
    cvv=models.CharField(max_length=50)
   