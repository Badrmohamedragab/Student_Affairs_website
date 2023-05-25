from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):
    return render(request, 'index.html')

def Home(request):
    return render(request, 'Home.html')

def Register(request):
    return render(request, 'Register.html')

def Login(request):
    return render(request, 'Login.html')