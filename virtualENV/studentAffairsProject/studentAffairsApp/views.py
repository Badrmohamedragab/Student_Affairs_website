from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):
    return render(request, 'index.html')

def Home(request):
    return render(request, 'Home.html')

def Register(request):
    return render(request, 'Register.html')

def addStudent(request):
    Name = request.POST["UserName"]
    Id = request.POST["Id"]
    email = request.POST["Email"]
    Phone = request.POST["Phone"]
    GPA = request.POST["GPA"]
    Brith = request.POST["Brith"]
    Level = request.POST["Level"]
    Gender = request.POST["Gender"]
    Department = request.POST["Department"]
    Status = request.POST["Status"]
    Password = request.POST["Password"]

    student = Student(name = Name, id = Id, Email = email, phone = Phone, gpa = GPA,
                      birthDate = Brith, gender = Gender, level = Level, status = Status,
                      department = Department, password = Password)
    
    student.save()
    return HttpResponse("Student added")
    

def Login(request):
    return render(request, 'Login.html')