from django.contrib import  admin

from src.apps.website.models import WebsiteInfo

@admin.register(WebsiteInfo)
class WebsiteInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name','tagline')

