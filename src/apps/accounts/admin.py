from django.contrib import  admin

from src.apps.accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display =('full_name','status')
    search_fields = ('full_name', 'status')


