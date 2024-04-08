from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.name}'


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title} - {self.project.name}'
