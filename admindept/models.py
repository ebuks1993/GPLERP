from django.db import models

from django.db import models
from general.models import Suppplier,Employees

class Asset(models.Model):
    Name = models.CharField(max_length=500)
    lifespan = models.IntegerField()

class Carspec(models.Model):
    Brand = models.CharField(max_length=500)
    model = models.CharField( max_length=500)

    def __str__(self):
        return f'{self.Brand} -- {self.model}'
class Caryear(models.Model):
    year = models.CharField( max_length=50)

    
## this is the asset information for all the assets we have 
class Car(models.Model):
    Asset = models.ForeignKey(Asset, on_delete=models.CASCADE,null=True,blank=False)
    Carspec = models.ForeignKey(Carspec, on_delete=models.DO_NOTHING,null=True,blank=False)
    Supplier = models.ForeignKey(Suppplier, on_delete=models.DO_NOTHING,null=True,blank=False)
    Color = models.CharField( max_length=500,null=True,blank=False)
    Vin = models.CharField( max_length=500,unique=True,null=True,blank=False)
    Amount = models.IntegerField(null=True,blank=False)
    Odometer = models.IntegerField(null=True,blank=False)
    Purchase_type = models.CharField( max_length=500,null=True,blank=False)
    Created_date = models.DateField(auto_now_add=True,null=True)
    PurchaseDate = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=False)
    Cartype = models.CharField( max_length=500,null=True,blank=False)
    modelyear = models.CharField(max_length=50,null=True,blank=False)
    ram = models.CharField( max_length=500,null=True,blank=False)
    Storage = models.CharField( max_length=500,null=True,blank=False)
    Operating_System = models.CharField(max_length=500,null=True,blank=False)
    ## check whether the assset has been paid for 
    status = models.CharField( max_length=500 , default="pending")
    bill_num = models.CharField( max_length=500, default=0)
    ## after the bill has been treated 
    payment_num = models.CharField( max_length=500, default=0)
    # check if the asset has been sold and to who 
    Sales_date = models.DateField(null=True)
    Availability = models.CharField( max_length=50, default="AVAILABLE")
    buyer = models.CharField(max_length=500,null=True)
    Sales_amount = models.IntegerField(default=0)
    
    # stoke = models.CharField( max_length=500,null=True)

    def __str__(self):
        return(f'{self.Carspec}')

class carphoto(models.Model):
    Car = models.OneToOneField(Car,on_delete=models.CASCADE,null=True)
    front = models.CharField(max_length=5000 ,null=True)


class localpaper(models.Model):
    Car = models.OneToOneField(Car,on_delete=models.CASCADE,null=True)
    PlateNumber = models.CharField(max_length=20 ,null=True,unique=True, )
    created = models.DateField( auto_now_add=True)

class InsuranceVendors(models.Model): ## this will take all vendor 
    Name = models.CharField(max_length=500)


class insurance(models.Model):
    Car = models.OneToOneField(Car, on_delete=models.CASCADE,null=True)
    vendor = models.ForeignKey(InsuranceVendors, on_delete=models.CASCADE)
    package = models.CharField( max_length=5000 ,null=True)   
    Premium = models.IntegerField( null=True)
    month = models.CharField(max_length=50, null=True)
    full_premium = models.IntegerField(default=0)
    full_claims=models.IntegerField(default=0)
    premium_status= models.CharField( max_length=5000 ,default='no')
    name = models.CharField(max_length=500, null=True)
    staff = models.CharField(max_length=1000 , null=True)   


class EmployeeCar(models.Model):
    Employees = models.ForeignKey(Employees, on_delete=models.DO_NOTHING,null=True)
    Car = models.ForeignKey(Car, on_delete=models.CASCADE,null=True)
    years = models.CharField(max_length=50,null=True)

    
class Carpaper(models.Model):
    name = models.CharField( max_length=500)








