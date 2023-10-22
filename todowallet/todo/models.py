from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

