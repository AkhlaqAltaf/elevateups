from django.contrib import  admin

from src.apps.accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display =('username','status')
    search_fields = ('username', 'status')


