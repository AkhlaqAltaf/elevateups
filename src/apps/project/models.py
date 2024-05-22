from django.db import models
from src.apps.accounts.models import CustomUser


class Project(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    client_owner = models.CharField(max_length=100)
    purpose = models.TextField()
    technologies_involved = models.TextField()
    short_description = models.TextField()
    full_description = models.TextField()
    media = models.ImageField(upload_to='project_media/')
    team_members = models.ManyToManyField(CustomUser, related_name='projects_involved')
    reviews = models.TextField()
    feedbacks = models.TextField()
