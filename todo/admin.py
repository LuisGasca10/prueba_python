from django.contrib import admin
from .models import Task

# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

admin.site.register(Task,TaskModelAdmin)