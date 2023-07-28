from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth  import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def signupform(request):
    context = { 'signupform' : UserCreationForm}

    if request.method == "GET" :
        return render(request,'signup.html', context)
    else :
        if request.POST['password1'] == request.POST['password2']:
           try:
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            new_user.save()
            login(request,new_user)
            return redirect('Home')
           except:
               context.update({"error": "username already exists!"})
               return render(request,'signup.html', context)
        else : 
            context.update({"error": "passwords dont match"})
            return render(request,'signup.html', context)

@login_required
def signout(request):
   logout(request)
   return redirect('Home')

def loginform(request):
    context = {'loginform': AuthenticationForm}
    if request.method == 'GET':
         return render(request, 'signin.html',context)
    else:
        user = authenticate(request,username= request.POST['username'],password=request.POST['password'])
        if user is None:
             context.update({'error': 'Username or Password incorrect'})
             return render(request, 'signin.html',context)
        else:
             login(request,user)
             return redirect('Home')
           