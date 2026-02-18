from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = UserAdmin
    list_display = ('email', 'username', 'phone', 'is_active', 'password', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username', 'phone')}),
        (_('permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'gtoups', 'user_permissions')})
        (_('Important date'),{'fields': ('last_login', 'date_joinse')})
    )
    
    
    search_fields = ('email' , 'username')
    ordering = ('email')
  #  fields_horizontal 
    