from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 500)
    description = models.TextField()
    pictures = models.ImageField(upload_to='images/', null=True)
    slug = models.SlugField(unique=True)
    # user = models.OnetoOneField(User, on_delete=models.CASCADE,
    # blank=True, null=True)