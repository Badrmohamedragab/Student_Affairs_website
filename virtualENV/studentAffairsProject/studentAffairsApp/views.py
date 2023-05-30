from pyexpat.errors import messages
from pyexpat.errors import messages
from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Admin


def index(request):
    return render(request, 'index.html')


def Home(request):
    return render(request, 'Home.html')


def Register(request):
    return render(request, 'Register.html')



def Login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        register = Admin.objects.all()
        for x in register:
            if email == x.Email:
                if password == x.password:
                    # messages.success(request, 'Login successful!')
                    return redirect('Home')
        messages.error(request, 'Invalid email or password.')
        return redirect('Login')

    return render(request, 'Login.html')



# def Login(request):
#     #get email and pass from login form
#     email = request.POST.get('un')
#     password = request.POST.get('Pass')
#     #check if email and pass are correct
#     if Admin.objects.filter(Email=email, password=password).exists():
#         return HttpResponse("login success")
#         # return render(request, 'Home.html', {'email': email, 'password': password})
#     else:
#         return render(request, 'Login.html', {'error': 'Invalid email or password'})
#




    #
    # if request.method == "POST":
    #     Name = request.POST["Name"]
    #     Id = request.POST["Id"]
    #     email = request.POST["Email"]
    #     Phone = request.POST["Phone"]
    #     GPA = request.POST["GPA"]
    #     Brith = request.POST["BirthDate"]
    #     Level = request.POST["Level"]
    #     Gender = request.POST["Gender"]
    #     Department = request.POST["Department"]
    #     Status = request.POST["Status"]
    #     Password = request.POST["Password"]
    #
    #     student = Student(name=Name, id=Id, Email=email, phone=Phone, gpa=GPA,
    #                       birthDate=Brith, gender=Gender, level=Level, status=Status,
    #                       department=Department, password=Password)
    #
    #     student.save()
    # return render(request, 'Login.html')


def search(request):
    if request.method == "GET":
        search_query = request.GET.get('q')
        if search_query:
            students = Student.objects.filter(name__startswith=search_query)
        else:
            students = None
        return render(request, 'search.html', {'students': students})


def change_department(request):
    name = request.GET.get('name')
    id = request.GET.get('id')
    department = request.GET.get('department')
    return render(request, 'Change Department.html', {'name': name, 'id': id, 'department': department})
