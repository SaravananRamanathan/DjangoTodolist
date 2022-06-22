#api-views
from cmath import exp
from urllib import response
from rest_framework import generics,permissions

from main.models import ToDoList,Item
from .serializers import TodoSerializer,ItemSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api import serializers

@api_view(['GET','PUT','DELETE'])
def todolistDetail(request,id,format=None):
    ""
    try:
        todolist=ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        ""
        serializer = TodoSerializer(todolist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        ""
        serializer = TodoSerializer(todolist,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ""
        todolist.delete()
        return Response(status=status.HTTP_200_OK)
@api_view(['GET','POST'])
def allTodoList(request,format=None):
    if request.method == 'GET':
        "a different approch without using generics.ListCreateAPIView"
        # user = request.user.id
        # print(f"user_id: {user}")
        todolist = ToDoList.objects.all()
        serializer = TodoSerializer(todolist,many=True)
        
        return Response(serializer.data)

        #return JsonResponse(serializer.data,safe=False)
        #return JsonResponse({"todolist:":serializer.data})
        #return JsonResponse({"error":"Not found"},safe=False)
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
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