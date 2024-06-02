# employees/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    # Your custom fields and methods
    additional_field = models.CharField(max_length=100, blank=True, null=True)  # Example of a custom field
    
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    # Override the groups field with a unique related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='employee_set',  # Change related_name to avoid clashes
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    
    # Override the user_permissions field with a unique related_name
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='employee_user_set',  # Change related_name to avoid clashes
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
