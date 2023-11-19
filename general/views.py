from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Team,Product,Suppplier,Employees,Department
from .serializers import Teamserializer,Productserializer,Supplierserializer,Employeeserializer,Departmentserializer

class TeamViewset(ModelViewSet):
    queryset=Team.objects.all()
    serializer_class= Teamserializer

class ProductViewset(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class= Productserializer


class SupplierViewset(ModelViewSet):
    queryset=Suppplier.objects.all()
    serializer_class= Supplierserializer

class EmployeeViewset(ModelViewSet):
    queryset=Employees.objects.all()
    serializer_class= Employeeserializer

class DepartmentViewset(ModelViewSet):
    queryset=Department.objects.all()
    serializer_class= Departmentserializer

# Create your views here.
