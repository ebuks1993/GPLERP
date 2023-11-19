from django.contrib import admin


from django.conf import settings 
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



@admin.register(User)
class UserAdmin(BaseUserAdmin):
     add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","email","password1", "password2","first_name")
            },
        ),
    )

# Register your models here.
