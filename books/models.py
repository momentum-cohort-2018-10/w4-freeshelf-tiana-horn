from django.contrib.auth.models import User, AbstractUser
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
    picture = models.ImageField(upload_to='books/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(unique=True)
    slug = models.SlugField(unique=True)
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
        return categories
    
    def __str__(self):
        return self.title


# class Suggestion(models.Model):
#     # user = models.OneToOneField(to='User', on_delete=models.CASCADE)
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     name = models.CharField("Your name", max_length=255)
#     book_suggestion = models.CharField("Name of Book", max_length=255)
#     link_to_book = models.URLField(unique=True)
