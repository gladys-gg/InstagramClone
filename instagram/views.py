from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Profile
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        pasword2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'That Email is already taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'That username is already taken')
                return redirect('register')
        else:
            messages.info(request,'Passwords are not matching')
            return redirect('register')
    else:
        user = User.objects.create_user(username=username, email=email,password=password)
        user.save()
    return render(request, 'register.html')

def login(request):
    if request.method ==POST:
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:   #user exists
            auth.login(request,user)
            messages.info(request,'You are logged in successfully')
            return redirect ('index')
    else:
        messages.info(request,'Invalid credentials')
        return redirect ('login')

def logout(request):
    auth.logout(request)
    return redirect ('login')        