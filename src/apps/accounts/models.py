from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
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


    is_display_on_site = models.BooleanField(default=False,blank=True,null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='client')
    member_status = models.CharField(max_length=20, choices=MEMBER_STATUS_CHOICES, blank=True, null=True)
    status_description = models.TextField(blank=False,null=True)

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')
    profile_pic = models.ImageField(blank=True,null=True,upload_to='project_media/')
    class Meta:

        permissions = [('can_view_customuser', 'Can view custom user')]
        unique_together = ('email',)