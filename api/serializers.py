from rest_framework import serializers
from main.models import ToDoList,Item

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ToDoList
        fields=['name','id']
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=['todolist_id','id','complete','text','category','description','due_date']

