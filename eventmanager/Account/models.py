from django.db import models

# Create your models here.
class UserTable(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10)
    password = models.CharField(max_length=30)

class AdminTable(models.Model):
    admin_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
