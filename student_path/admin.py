from django.contrib import admin

# Register your models here.
from .models import Path, Student

admin.site.register(Path)
admin.site.register(Student)
