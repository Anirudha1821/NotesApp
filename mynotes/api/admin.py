from django.contrib import admin

# Register your models here. to see in admin on site
from .models import *
admin.site.register(Note)
