from django.contrib import admin
from .models import AppUser, Question


# Register your models here.
admin.site.register(AppUser)
admin.site.register(Question)