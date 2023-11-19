from django.urls import path,include

from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('Team', views.TeamViewset ,basename='Team')
router.register('Product', views.ProductViewset ,basename='Product')
router.register('Supplier', views.SupplierViewset ,basename='Supplier')
router.register('Employee', views.EmployeeViewset ,basename='Employee')
router.register('Department', views.DepartmentViewset ,basename='Department')


urlpatterns = [
    path("",include(router.urls))
    ]