from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class ClientProject(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    tasks = models.ManyToManyField('tasks.Task', related_name='client_projects')

    def __str__(self):
        return self.project_name
