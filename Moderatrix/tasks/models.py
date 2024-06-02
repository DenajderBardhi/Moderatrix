from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('Backlog', 'Backlog'),
        ('In Progress', 'In Progress'),
        ('In Review', 'In Review'),
        ('Ready for Schedule', 'Ready for Schedule'),
        ('Scheduled', 'Scheduled'),
        ('Done', 'Done')
    ])
    priority = models.CharField(max_length=10, choices=[
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ])
    due_date = models.DateField()
    created_by = models.ForeignKey(User, related_name='tasks_created', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='tasks_assigned', on_delete=models.CASCADE, null=True, blank=True)
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subtasks')

    def __str__(self):
        return self.title
