from django.contrib import admin
from main import models
# Register your models here.
#linking dashboard with the database part

admin.site.register(models.ToDoList)
admin.site.register(models.Item)