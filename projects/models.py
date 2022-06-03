from pydoc import describe
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    image = models.FilePathField(path='/img')