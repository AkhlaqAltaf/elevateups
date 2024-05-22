from django.contrib import admin

from src.apps.project.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','client_owner')
    search_fields = ('title','client_owner')

