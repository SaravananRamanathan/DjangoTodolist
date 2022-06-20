"""
database modles
modling info-to make it easy to grab info
"""
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ToDoList(models.Model):
    "database object called ToDoList"
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="todolist",null=True)
    name=models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    description = models.CharField(max_length=300,null=True)
    category = models.TextField(max_length=50,null=True)
    due_date = models.DateField(null=True)
    image1 = models.TextField(max_length=100, null=True, blank=True)
    image2 = models.TextField(max_length=100, null=True, blank=True)
    image3 = models.TextField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.text)
