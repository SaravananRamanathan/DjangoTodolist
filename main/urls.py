"""
in here we gooan define paths
to select for respective view
"""
from django.urls import path
from . import views
#starting page path with ""
urlpatterns = [
    path("",views.home, name="home"),#home page
    path("create/",views.create,name="createList"),
    path("display/",views.display,name="displayList"),
    path("api_access/",views.apiAccess,name="api-access"),
    path("id/<int:idValue>/",views.id, name="id"),
    path("ajax/",views.ajax_view,name="ajax"),
    path("delete-todolist-item/",views.todolist_item_delete_request,name="delete-todolist-item")
]
