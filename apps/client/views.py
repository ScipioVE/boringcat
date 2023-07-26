from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
            return HttpResponse("user created successfully")
           except:
               context.update({"error": "username already exists!"})
               return render(request,'signup.html', context)
        else : 
            context.update({"error": "passwords dont match"})
            return render(request,'signup.html', context)



    