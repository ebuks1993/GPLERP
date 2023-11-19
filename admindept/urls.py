from django.urls import path,include

from rest_framework.routers import DefaultRouter
# from .views import UploadView
from . import views

router=DefaultRouter()
router.register('carspec', views.carspecViewset ,basename='carspec')
router.register('car', views.CarViewset ,basename='car')
router.register('carPhoto', views.CarphotoViewset ,basename='carPhoto')
router.register('download', views.MyExampleViewSet ,basename='download')
router.register('Asset', views.AssetViewset ,basename='Asset')
router.register('employeecar', views.emplployeeCarViewset ,basename='employeecar')
router.register('localpaper', views.localPaperViewset ,basename='localpaper')
router.register('Insurancecheck', views.insurancecheckViewset ,basename='Insurancecheck')
router.register('InsuranceVendor', views.InsuranceVendorsViewset ,basename='InsuranceVendor')
router.register('Insurance', views.InsuranceViewset ,basename='Insurance')
router.register('employeecarentry', views.FullEmployeeCarViewset ,basename='employeecarentry')
router.register('Asset', views.AssetViewset,basename='Asset')







urlpatterns = [
    path("",include(router.urls)),
    # path("download",views.MyExampleViewSet)
    # path("upload", UploadView.as_view())
    ]