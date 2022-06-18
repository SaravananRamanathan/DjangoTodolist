"""
in here we gooan define paths
to select for respective view
"""
from django.urls import path,include,re_path
from . import views
#starting page path with ""

"""from rest_framework import routers
router = routers.DefaultRouter()    
router.register(r'id/(?P<id>\d+)/?$', views.viewItemsViaId)"""
#url(r'^api/', include(router.urls)),

urlpatterns = [
    #path('', include(router.urls)),
    path("view-todolist/",views.viewTodoList.as_view()),
    #/(?P<pk>[0-9]+)$
    re_path("view-todolist/id/(?P<id>\w+)$",views.viewItemsViaId.as_view()),
    #path("view-todolist/id/<int:id>",views.viewItemsViaId.as_view()),
]
