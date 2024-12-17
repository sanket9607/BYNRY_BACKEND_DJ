from django.db import models
from django.db import models

# Create your models here.
class contact(models.Model):
    title = models.CharField(max_length=20, blank=False)
    description=models.CharField(max_length=20,blank=False)
