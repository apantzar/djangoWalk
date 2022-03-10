from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=80, default='SOME STRING')
    content  = models.TextField()

    def __str__(self):
        return self.title

