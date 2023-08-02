from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, allow_unicode=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
