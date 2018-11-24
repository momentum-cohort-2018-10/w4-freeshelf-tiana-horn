from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 500, null=False, blank=False)
    author = models.CharField(max_length = 255, null=False, blank=False)
    description = models.TextField()
    python = models.BooleanField(default=False)
    css = models.BooleanField(default=False)
    html = models.BooleanField(default=False)
    javascript = models.BooleanField(default=False)
    # pictures = models.ImageField(upload_to='books/', null=True)
    # slug = models.SlugField(unique=True)
    # user = models.OnetoOneField(User, on_delete=models.CASCADE,
    # blank=True, null=True)

    def get_categories(self):
        categories = []
        if self.python:
            categories.append("Python")
        if self.css:
            categories.append("CSS")
        if self.html:
            categories.append("HTML")
        if self.javascript:
            categories.append("Javascript")
    
    def __str__(self):
        return self.title
