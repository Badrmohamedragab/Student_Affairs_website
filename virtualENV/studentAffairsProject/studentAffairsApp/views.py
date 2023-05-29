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

def search(request):
    if request.method == "GET":
        search_query = request.GET.get('q')
        if search_query:
            students = Student.objects.filter(name__startswith = search_query)
        else:
            students = None
        return render(request, 'search.html', {'students': students})


def change_department(request):
    name = request.GET.get('name')
    id = request.GET.get('id')
    department = request.GET.get('department')
    return render(request, 'Change Department.html', {'name': name, 'id': id, 'department': department})
        
