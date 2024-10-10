from ckeditor.fields import RichTextField
from django.db import models

class WebsiteInfo(models.Model):
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logo/')
    tagline = models.CharField(max_length=255)
    services_provided = models.TextField()
    total_clients_dealt = models.PositiveIntegerField(default=0)
    total_team_members = models.PositiveIntegerField(default=0)


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    content = models.TextField(max_length=400)
    number = models.CharField(max_length=10)

    def __str__(self):
        return (self.name)


# class OurServices(models.Model):
#     picture = models.ImageField(upload_to='services/')
#     titile  = models.CharField(max_length=300)
#     define = models.TextField()
#     content = RichTextField(null=True,blank=True)
#
