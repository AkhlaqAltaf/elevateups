from django.contrib import  admin

from src.apps.website.models import WebsiteInfo, Contact


@admin.register(WebsiteInfo)
class WebsiteInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name','tagline')




@admin.register(Contact)
class WebsiteInfoAdmin(admin.ModelAdmin):
    list_display = ('name','email')

