"""
site views
can create multiple views here.
"""
from urllib import response
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import CreateNewList,CreateNewItem
from . import models
from bootstrap_datepicker_plus.widgets import DateTimePickerInput #TODO --sort of stoped working with bootstrap date picker for now.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
#from django.contrib.auth.models import User

# Create your views here.

def todolist_item_delete_request(request):
    if request.method=="POST":
        "post method"
        print("received from ajax to delete todolist item: {}".format(request.POST))
        data={
            "msg":"post method for deleting todolist item received.",
        }
        id=request.POST.get("id")
        print(f"received id={id}")
        temp=models.Item.objects.all();
        print(f"about to delete items: {temp.filter(id=id)}")
        temp.filter(id=id).delete();
        #print(f"about to delete: {temp.filter(id=id)}");   
        #HttpResponseRedirect("/display")
        return JsonResponse(data);
    else:
        data={
          "msg":"get method test ok",
        }
        return JsonResponse(data)

def ajax_view(request):
    if request.method=="POST":
        "post method"
        print("received from ajax: {}".format(request.POST))
        data={
            "msg":"post method test ok",
        }
        id=request.POST.get("id")
        print(f"received id={id}")
        temp=models.ToDoList.objects.all();
        print(f"about to delete todolist: {temp.filter(id=id)}")
        temp.filter(id=id).delete()   
        #HttpResponseRedirect("/display")
        return JsonResponse(data);
    else:
        data={
          "msg":"get method test ok",
        }
        return JsonResponse(data)

def home(response):
    "home page"
    #return HttpResponse("<h1>testing- srvnn %s</h1>"%id)
    #testing tables ,so replaced home.html --testing done
    return render(response,"main/home.html",{})

@csrf_exempt
def apiAccess(response):
    "api access"
    userId=response.user.id
    token = Token.objects.filter(user_id=userId)
    print(f"access token: {token[0]}")
    return render(response,"main/api_access.html",{"token":token[0]})


def id(response,idValue:int):
    "displaying all of todolist"
    #todolist = models.ToDoList.objects.raw(f"SELECT *,row_number() OVER(ORDER BY Id) AS sno FROM main_todolist WHERE id={idValue}")#.filter(id=idValue)
    userId=response.user.id
    todolist = models.ToDoList.objects.filter(id=idValue , user_id=userId)
    print(todolist)
    headingName:str=None
    if todolist.exists() :
        headingName=todolist[0].name;
    print(f"heading name = {headingName}")
    if response.method=="POST":
        ""
        form = CreateNewItem(response.POST)

        print(f'testing response: {response.POST}')
        if response.POST.get("save"):
            ""
            print("testing save button")
            if todolist[0].item_set.all().exists():
                for i in todolist[0].item_set.all():
                    i.text = response.POST.get('item-name'+str(i.id))
                    i.description = response.POST.get('description'+str(i.id))
                    if response.POST.get('c'+str(i.id)):
                        ""
                        print("checked case")
                        i.complete=True
                        #print(f"{i.complete} {i.text}")
                        #print(f"{'c'+str(i.id)}={response.POST.get('c'+str(i.id))}")
                    else:
                        print("not checked")
                        i.complete=False
                        #print(f"{i.complete} {i.text}")
                        #print(f"{'c'+str(i.id)}={response.POST.get('c'+str(i.id))}")
                    i.save()
        
        elif form.is_valid():
            "if data entererd in form is valid"            
            #Name=form.cleaned_data["name"]
            #old method
            """temp = models.ToDoList(name=form.cleaned_data["name"])
            temp.save()
            
            response.user.todolist.add(temp)"""
            if response.POST.get("newItem"):
                ""

                #print(form.cleaned_data)
                print("testing newItem button")
                itemName:str= form.cleaned_data["title"]
                description:str = form.cleaned_data["description"]
                category:str = form.cleaned_data["category"]
                due_date:str = form.cleaned_data["due_date"]
                print(f"name={itemName} desc={description} category={category} due_date={due_date}")#testing fields data
                print(f"New item name:{itemName}.")
                if not itemName.isspace():
                    if len(itemName)>0:
                        if itemName[0]!=' ':
                            #print("elibible") 
                            temp=todolist[0].item_set.all();
                            print(f"testing  temp {temp}")       
                            todolist[0].item_set.create(text=itemName,complete=False,description=description,category=category,due_date=due_date)
                            print(f"testing  temp after create: {temp}")   
                #todolist[0].item_set.create(text=itemName,complete=False)

        elif not form.is_valid():
            "form to add newitems not valid"
            print("form is not valid.")
            return render(response,"main/lists.html",{"list":todolist,"id":idValue,"form":form,"headingName":headingName})
            #return render(request, "form_template.html", ctx}


        elif response.POST.get("deleteItem"):
            "deleting item"
            id=response.POST.get("deleteItem");
            print(f"about to delete id: {id}")
            temp=models.Item.objects.all();
            print(f"about to delete items: {temp.filter(id=id)}")
            temp.filter(id=id).delete();
        return HttpResponseRedirect(response.path_info)#return to the same page.

    class sendToTemplate:
        temp=0
        def num(self,):
            self.temp+=1
            return self.temp

    
    
    form = CreateNewItem()
    
    return render(response,"main/lists.html",{"list":todolist,"id":idValue,"form":form,"sno":sendToTemplate(),"headingName":headingName})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            "if data entererd in form is valid"            
            #Name=form.cleaned_data["name"]
            #old method
            temp = models.ToDoList(name=form.cleaned_data["name"])
            temp.save()
            
            response.user.todolist.add(temp)
            #response.user.todolist_set.create(name=Name)

            return HttpResponseRedirect("/display") #just "/" to redirect to home page 
    else:    
        form=CreateNewList()
    return render(response,"main/createList.html",{"form":form})

def display(response):
    #todolist = models.ToDoList.objects.all()
    #TODO: this display function probs will fail if there is no data in list.
    #print(f"testing display id: {response.user.id}")
    todolist = models.ToDoList.objects.raw(f"SELECT *,row_number() OVER(ORDER BY Id) AS ROWNUM FROM main_todolist where user_id={response.user.id}")
        #print(i.ROWNUM)
    
    
    return render(response,"main/display.html",{"data":todolist})
