from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
