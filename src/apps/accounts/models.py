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

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='client')
    member_status = models.CharField(max_length=20, choices=MEMBER_STATUS_CHOICES, blank=True, null=True)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')

    class Meta:

        permissions = [('can_view_customuser', 'Can view custom user')]
        unique_together = ('email',)