from .models import Carspec,Car,carphoto,Asset,InsuranceVendors,insurance,EmployeeCar,localpaper,Asset
from rest_framework import serializers 
from django.db import transaction


class Assetserializer(serializers.ModelSerializer):
    class Meta:
        model=Asset
        fields='__all__'


class Carspecserializer(serializers.ModelSerializer):
    class Meta:
        model=Carspec
        fields='__all__'

class Carserializer(serializers.ModelSerializer):
    brand=serializers.SerializerMethodField(method_name='bla',read_only=True)
    modelname=serializers.SerializerMethodField(method_name='mdl',read_only=True)
    Supplyname=serializers.SerializerMethodField(method_name='sup',read_only=True)
    # paper=serializers.SerializerMethodField(method_name='pap',read_only=True)
    paper=serializers.CharField(source='carphoto.front',read_only=True)
    PlateNum=serializers.CharField(source='localpaper.PlateNumber',read_only=True)
    insure=serializers.CharField(source='insurance.package',read_only=True)
    prem=serializers.CharField(source='insurance.Premium',read_only=True)
    insurecoy=serializers.CharField(source='insurance.name',read_only=True)
    staff=serializers.CharField(source='insurance.staff',read_only=True)
    carseg=serializers.SerializerMethodField(method_name='Pla',read_only=True)

    class Meta:
        model=Car
        fields=['id','Asset','Color','Vin','Amount','Odometer','Purchase_type','Created_date','PurchaseDate','Cartype','modelyear','Carspec','Supplier','ram','Storage','brand','Operating_System','modelname','carseg','Supplyname','paper','PlateNum','insure','insurecoy',"Sales_date","Availability","buyer","Sales_amount",'prem','staff']

    def bla(self,carz:Car):
        return carz.Carspec.Brand
    
    def Pla(self,carz:Car):
        return carz.Asset.Name
    
    
    def mdl(self,carz:Car):
        return carz.Carspec.model
    
    def sup(self,carz:Car):
        return carz.Supplier.Name
    
    # def pap(self,carz:Car):
    #     bam=carz.id
    #     try:
    #         cam=carphoto.objects.get(Car_id=bam)
    #         return cam.front
    #     except:
    #         return ""

    # def pap(self,carz:Car):
    #     return [item.front for item in carz.carphoto_set.all()]

    


class CarPhotoserializer(serializers.ModelSerializer):
    class Meta:
        model=carphoto
        fields='__all__'

class LocalPaperserializer(serializers.ModelSerializer):
    class Meta:
        model=localpaper
        fields=['Car','PlateNumber']



class Car22serializer(serializers.ModelSerializer):
    brand=serializers.SerializerMethodField(method_name='bla',read_only=True)
    modelname=serializers.SerializerMethodField(method_name='mdl',read_only=True)
    Supplyname=serializers.SerializerMethodField(method_name='sup',read_only=True)
    class Meta:
        model=Car
        fields=['id','Asset','Color','Vin','Amount','Odometer','Purchase_type','Created_date','PurchaseDate','Cartype','modelyear','Carspec','Supplier','brand','modelname','Supplyname']

    def bla(self,carz:Car):
        return carz.Carspec.Brand
    
    
    def mdl(self,carz:Car):
        return carz.Carspec.model
    
    def sup(self,carz:Car):
        return carz.Supplier.Name
    

class Assetserializer(serializers.ModelSerializer):
    class Meta:
        model=Asset
        fields='__all__'


class InsuranceVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=InsuranceVendors
        fields='__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    # Brand=serializers.SerializerMethodField(method_name='dok')
    # Vin=serializers.SerializerMethodField(method_name='zok')
    class Meta:
        model=insurance
        fields=['id', 'package', 'Premium', 'month', 'Car', 'vendor',"full_claims","premium_status","full_premium","name","staff"]

    # def dok(self,ins:insurance):
    #     return f"{ins.Car.Carspec.Brand} {ins.Car.Carspec.model}"
    
    # def zok(self,ins:insurance):
    #     return ins.Car.Vin
    
    def save(self, **kwargs):
        with transaction.atomic():
            iddo=self.validated_data['vendor'].Name
            carting=insurance.objects.create(name=iddo,**self.validated_data)
            self.instance=carting
            return carting
    

class EmployeeCarSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeCar
        fields='__all__'




  




