from django.contrib import admin
from .models import servicelist
from .models import serviceform

# Register your models here.

admin.site.register(servicelist)
admin.site.register(serviceform)

