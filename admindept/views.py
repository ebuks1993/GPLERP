from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,ListModelMixin,UpdateModelMixin
from rest_framework.views import APIView
from django.db.models.aggregates import Count,Sum,Min,Max,Avg
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from .pagination import ProductPagination
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer

from .models import Carspec,Car,carphoto,Asset, InsuranceVendors,insurance,EmployeeCar,localpaper,Caryear
from .serializers import Carspecserializer,Carserializer,Car22serializer,CarPhotoserializer,Assetserializer,InsuranceVendorSerializer,InsuranceSerializer,EmployeeCarSerializer,LocalPaperserializer,Assetserializer,caryearserializer

class carspecViewset(ModelViewSet):
    queryset=Carspec.objects.all()
    serializer_class= Carspecserializer

class caryearViewset(ModelViewSet):
    queryset=Caryear.objects.all()
    serializer_class= caryearserializer

class AssetViewset(ModelViewSet):
    queryset=Asset.objects.all()
    serializer_class= Assetserializer

class CarViewset(ModelViewSet):
    queryset=Car.objects.select_related('Asset',"Carspec","Supplier").prefetch_related("carphoto","localpaper","insurance").filter(Availability="AVAILABLE").order_by('-Created_date','-id')
    serializer_class= Carserializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['status']
    # pagination_class=ProductPagination
    


class CarphotoViewset(ModelViewSet):
    queryset=carphoto.objects.all()
    serializer_class= CarPhotoserializer
 

class localPaperViewset(ModelViewSet):
    queryset=localpaper.objects.all()
    serializer_class= LocalPaperserializer

class MyExampleViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset=Car.objects.all()
    serializer_class= Carserializer
    renderer_classes = (XLSXRenderer,)
    filename = 'my_export.xlsx'


class AssetViewset(ModelViewSet):
    queryset=Asset.objects.all()
    serializer_class= Assetserializer

class emplployeeCarViewset(ModelViewSet):
    queryset=Car.objects.filter(employeecar__years__isnull=True)
    serializer_class= Carserializer


class insurancecheckViewset(ModelViewSet):
    queryset=Car.objects.filter(insurance__package__isnull=True)
    serializer_class= Carserializer


class InsuranceVendorsViewset(ModelViewSet):
    queryset=InsuranceVendors.objects.all()
    serializer_class= InsuranceVendorSerializer

class InsuranceViewset(ModelViewSet):
    queryset=insurance.objects.all()
    serializer_class= InsuranceSerializer

class FullEmployeeCarViewset(ModelViewSet):
    queryset=EmployeeCar.objects.all()
    serializer_class= EmployeeCarSerializer





