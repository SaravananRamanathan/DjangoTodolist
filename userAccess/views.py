import time
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():

            user = User.objects.create_user(form.cleaned_data['username'],password=form.cleaned_data['password1'])
            user.save()
            #form.save()
            print("register form is valid")
            
            #creating tokens.
            token = Token.objects.create(user=user)
            print(f"token is {token}")
            """messages.success(response, 'Registration completed.you will be logged in soon...')
            time.sleep(3)
            print("after sleep")"""
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(response, new_user)
            #return redirect("/registerSuccess")
            return render(response,"userAccess/registerSuccess.html")
        else:
            "not valid form:"
            messages.error(response, 'Invalid form submission.')
    else:
        form=RegisterForm()
    return render(response,"userAccess/register.html",{"form":form})