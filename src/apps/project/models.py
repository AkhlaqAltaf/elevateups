from ckeditor.fields import RichTextField
from django.db import models
from src.apps.accounts.models import CustomUser


class ProjectTechnology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Project Technology'
        verbose_name_plural = 'Project Technologies'


class Project(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    client_owner = models.CharField(max_length=100,null=True,blank=True)
    purpose = models.TextField(null=True,blank=True)
    technologies_involved = models.ManyToManyField(ProjectTechnology, related_name='projects')
    short_description = models.TextField(null=True,blank=True)
    full_description = RichTextField(null=True,blank=True)
    team_members = models.ManyToManyField(CustomUser,related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    media = models.FileField(upload_to='project_media/',null=True,blank=True)

    def __str__(self):
        return f"Media for {self.project.title}"


class ProjectFeedback(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length = 100,null=True,blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='feedbacks')
    reviews = models.IntegerField(null=True,blank=True)
    feedback = models.TextField(null=True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.project.title} by {self.user_name or 'Anonymous'}"


    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project Feedback'
        verbose_name_plural = 'Project Feedbacks'




