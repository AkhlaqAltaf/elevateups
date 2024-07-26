from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from src.apps.project.models import Project, ProjectMedia, ProjectFeedback, ProjectTechnology



class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'full_description': CKEditorWidget(),
        }

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('title', 'client_owner')
    search_fields = ('title', 'client_owner')


@admin.register(ProjectMedia)
class ProjectMediaAdmin(admin.ModelAdmin):
    list_display = ['project']
    search_fields = ['project']


@admin.register(ProjectFeedback)
class ProjectFeedbackAdmin(admin.ModelAdmin):
    list_display = ['project']
    search_fields = ['project']


@admin.register(ProjectTechnology)
class ProjectTechnologyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
