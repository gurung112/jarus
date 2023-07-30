from django.db import models

# Create your models here.

class roger():
    name=models.CharField(max_length=40)
    email=models.EmailField()
    phone_no=models.BigIntegerField()
    gender=models.CharField(max_length=30)
    
