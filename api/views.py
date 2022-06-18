#api-views
from rest_framework import generics,permissions

from main.models import ToDoList,Item
from .serializers import TodoSerializer,ItemSerializer
from django.http import JsonResponse


class viewItemsViaId(generics.ListCreateAPIView):
    ""
     #specify a serializer class.
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        """
        test ok.
        print(f"user id: {user}")
        print(f"user is : {self.request.user}")
        print(f"{self.request}")
        print(f"id? : {self.kwargs['post_id']}")
        """

        #print(ToDoList.objects.filter(user_id=user,id=self.kwargs['id'])) #test ok.
        
        #return JsonResponse({'msg':'test'})
        if(ToDoList.objects.filter(user_id=user,id=self.kwargs['id'])):
            return Item.objects.filter(todolist_id=self.kwargs['id'])
        #return Item.objects.all()

class viewTodoList(generics.ListAPIView):
    ""
    #specify a serializer class.
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        print(f"user id: {user}")
        #todolist = ToDoList.objects.all().filter(user_id=user)
        
        """testing
        todolist = ToDoList.objects.raw(f"SELECT * FROM main_todolist where user_id={user}")
        new_data={}
        for i in todolist:
            temp={"name":i.name,"id":i.id}
            new_json.update(temp);
        print(f"testing api's: {new_data}")
        """
        #return new_json

        return ToDoList.objects.filter(user_id=user)
        #return super().get_queryset()