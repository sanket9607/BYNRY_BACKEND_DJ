from django.db import models
from django.utils import timezone





# Create your models here.
class servicelist(models.Model):
    address = models.TextField(max_length=100, blank=False)
    email=models.CharField(max_length=100,blank=False)
    phone = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.email

class serviceform(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100,blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=800, blank=False)
    service_request_type = models.TextField(max_length=100,default="",blank=False)
    submission_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100, default='Pending')
    resolution_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

