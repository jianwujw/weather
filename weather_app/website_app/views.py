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
            messages.error(request, 'invalid')
            return render(request, 'login.html', {'error': 'Invalid credentials'})

def register(request):
    return render(request,'register.html')
    
def authenticate_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
    if User.objects.filter(username = username).exists():
        messages.error(request, 'Invalid credentials')
        return render(request, 'register.html', {'error': 'Existing Username'})
        
    else:
        user = User.objects.create(username=username,password=password)
        user.save()
        return redirect('/log/')