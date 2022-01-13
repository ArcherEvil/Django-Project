from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    username = request.POST('username')
    password = request.POST('password')

    return render(request, 'register.html')