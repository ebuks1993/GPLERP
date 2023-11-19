from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email=models.EmailField(unique=True) 


class Team(models.Model):
    Name = models.CharField( max_length=50)

    def __str__(self):
        return self.Name

class Product(models.Model):
    Name = models.CharField( max_length=1500)
    uom = models.CharField( max_length=50)
    qtyperctn = models.IntegerField()
    createdby = models.CharField( max_length=50, default="nobody")
    Alteredby = models.CharField( max_length=1500, default="nobody")
    createdat = models.DateField(auto_now_add=True)
    alteredat = models.DateField( auto_now=True)
    Price = models.IntegerField()
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class Customer(models.Model):
    BusinessName = models.CharField( max_length=50)
    State = models.CharField( max_length=50)
    Adress = models.CharField( max_length=2500)
    createdby = models.CharField( max_length=50, default="nobody")
    Alteredby = models.CharField( max_length=1500, default="nobody")
    createdat = models.DateField(auto_now_add=True)
    alteredat = models.DateField( auto_now=True)
    # Price = models.IntegerField()
    personnel = models.CharField( max_length=50)
    phone_num = models.CharField(max_length=50)
    Completion_status = models.IntegerField(default=0)
    Balance = models.IntegerField(default=0)

    def __str__(self):
        return self.BusinessName

class Suppplier(models.Model):
    Name = models.CharField(max_length=500)
    Type = models.CharField(max_length=500)

class Department(models.Model):
    Department = models.CharField(max_length=1500,null=True)
    Team = models.CharField( max_length=500,null=True)

    def __str__(self):
        return(f'{self.Department}--{self.Team}')
# Create your models here.

class Employees(models.Model):
    # User = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # Department = models.CharField(max_length=1500)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    First_name = models.CharField( max_length=1500,null=True)
    Last_name = models.CharField( max_length=1500,null=True)

    def __str__(self):
        return f'{self.Last_name}--{self.First_name}'


class transtrigger(models.Model):
    created_date = models.DateField(auto_now_add=True)
    approval_status = models.CharField(max_length=500,null=True)
    idenitier = models.CharField(max_length=500)
    Amount = models.IntegerField()
    tabname = models.CharField(max_length=5000)
