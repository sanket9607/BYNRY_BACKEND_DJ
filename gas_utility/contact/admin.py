from django.contrib import admin
from .models import contactlist
from .models import contactform

# Register your models here.

admin.site.register(contactlist)
admin.site.register(contactform)