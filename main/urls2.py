"""
urls2
/id/.....
"""
from django.urls import path
from . import views
urlpatterns = [
    path("<int:idValue>",views.id, name="id"),#enter todolist id
]
