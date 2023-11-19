from django.contrib import admin
from .models import Carspec,Car,carphoto,Asset,InsuranceVendors,insurance
# Register your models here.



@admin.register(Asset)
class Assetadmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class Caradmin(admin.ModelAdmin):
    pass

@admin.register(carphoto)
class carphotoadmin(admin.ModelAdmin):
    pass

@admin.register(InsuranceVendors)
class InsuranceVendorsadmin(admin.ModelAdmin):
    pass

@admin.register(Carspec)
class Carspecadmin(admin.ModelAdmin):
    pass

@admin.register(insurance)
class insuranceadmin(admin.ModelAdmin):
    pass
