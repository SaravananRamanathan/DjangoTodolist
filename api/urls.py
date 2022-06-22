"""
in here we gooan define paths
to select for respective view
"""
from django.urls import path,include,re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

#starting page path with ""

"""from rest_framework import routers
router = routers.DefaultRouter()    
router.register(r'id/(?P<id>\d+)/?$', views.viewItemsViaId)"""
#url(r'^api/', include(router.urls)),

urlpatterns = [
    #path('', include(router.urls)),
    #path("view-todolist/",views.viewTodoList.as_view()),
    path("view-todolist/",views.allTodoList),
    #testing a different approch to get the id
    path("view-todolist/<int:id>",views.todolistDetail),
    #/(?P<pk>[0-9]+)$
    re_path("view-todolist/id/(?P<id>\w+)$",views.viewItemsViaId.as_view()),

    #path("view-todolist/id/<int:id>",views.viewItemsViaId.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)