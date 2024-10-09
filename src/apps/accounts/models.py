from django.db import models

class CustomUser(models.Model):
    STATUS_CHOICES = [
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('developer', 'Developer'),
        ('member', 'Member')
    ]
    MEMBER_STATUS_CHOICES = [
        ('CTO', 'Chief Technology Officer'),
        ('CEO', 'Chief Executive Officer'),
        ('CFO', 'Chief Financial Officer'),
        ('project_manager', 'Project Manager'),
        ('team_leader', 'Team Leader')
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=100 , blank=True, null=True)
    experience_detail  = models.TextField(blank=True,null=True)
    links = models.TextField(blank=True, null=True)
    member_status = models.CharField(max_length=20, choices=MEMBER_STATUS_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='client')
    status_description = models.TextField(blank=False,null=True)
    profile_picture = models.ImageField(blank=True,null=True,upload_to='user/')
    is_display_on_site = models.BooleanField(default=False,blank=True,null=True)
