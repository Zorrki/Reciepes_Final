from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    steps = models.TextField()
    cook_time = models.PositiveIntegerField(help_text="Время приготовления в минутах")
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    categories = models.ManyToManyField(Category, related_name='recipes')
    ingredients = models.TextField(blank=True)

    def __str__(self):
        return self.title