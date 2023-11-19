from .models import Team,Product,Suppplier,Employees,Department
from rest_framework import serializers 


class Teamserializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=['id','Name']


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','Name']


class Supplierserializer(serializers.ModelSerializer):
    class Meta:
        model=Suppplier
        fields='__all__'

class Departmentserializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class Employeeserializer(serializers.ModelSerializer):
    Department_name=serializers.SerializerMethodField(method_name='pan')
    class Meta:
        model=Employees
        fields=['id', 'First_name', 'Last_name', 'Department','Department_name']

    def pan(self,emp:Employees):
        return f'{emp.Department.Department}--{emp.Department.Team}'

