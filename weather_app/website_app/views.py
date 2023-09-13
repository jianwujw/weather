from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def log(request):
    return render(request,'login.html')

def authenticate_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(username = username, password = password)

 
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

def register(request):
    return render(request,'register.html')
    
def authenticate_register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

    if len(username) < 5:
        return render(request,'register.html',{'error': 'Username is too short'})


    #check db for user
    if User.objects.filter(username = username).exists():
        return render(request, 'register.html', {'error': 'Existing Username'})
        
    else:
        try:
            user = User.objects.create_user(username=username,password=password)
            user.save()
        except ValueError:
            return render(request, 'register.html',{'error': 'Not a valid Username'})

        return redirect('/log/')

