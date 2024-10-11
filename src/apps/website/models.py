from ckeditor.fields import RichTextField
from django.db import models


class OurServices(models.Model):
    picture = models.ImageField(upload_to='services/')
    title  = models.CharField(max_length=300)
    define = models.TextField()
    content = RichTextField(null=True,blank=True)



class Blogs(models.Model):
    primary_picture =  models.ImageField(upload_to='blogs/')
    author_name = models.CharField(max_length=100 )
    author_picture = models.ImageField(upload_to='blogs/',blank=True , null=True)
    author_description = models.TextField(blank=True,null=True,max_length=500 )
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_created=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    is_display_on_first_page = models.BooleanField(default=False)

