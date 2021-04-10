from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmailModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=750)
    image = models.ImageField(blank=True, null=True, upload_to = "photos/")
    hour = models.CharField(max_length=2)
    date = models.DateField()