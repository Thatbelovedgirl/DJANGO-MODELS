from django.db import models
from django.contrib.auth import get_user_model
from django.forms import DateTimeField
# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=200)
    text=models.CharField
    author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    published_date=models.DateTimeField()