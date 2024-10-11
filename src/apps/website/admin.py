from django.contrib import  admin

from src.apps.website.models import  Blogs, OurServices



@admin.register(OurServices)
class OurServicesAdmin(admin.ModelAdmin):
    list_display = ('title','define')
    search_fields =  ('title','define')
@admin.register(Blogs)
class BlogWritingAdmin(admin.ModelAdmin):
    list_display = ('title','category','author_name')
    list_filter = ('title','category','author_name')
    search_fields = ('title','category','author_name')