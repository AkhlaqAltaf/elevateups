from django.db import models

class WebsiteInfo(models.Model):
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logo/')
    tagline = models.CharField(max_length=255)
    services_provided = models.TextField()
    total_clients_dealt = models.PositiveIntegerField(default=0)
    total_team_members = models.PositiveIntegerField(default=0)
