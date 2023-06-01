from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Student, Admin

def index(request):
    return render(request, 'index.html')

def Home(request):
    return render(request, 'Home.html')

def Home_Registered(request):

    return render(request, 'Home-Registered.html')

def Register(request):
    if request.method == "POST":
        Name = request.POST["Name"]
        Id = request.POST["Id"]
        email = request.POST["Email"]
        Phone = request.POST["Phone"]
        Brith = request.POST["BirthDate"]
        Gender = request.POST["Gender"]
        Password = request.POST["Password"]

        admin = Admin(name = Name, id = Id, Email = email, phone = Phone,
                        birthDate = Brith, gender = Gender, password = Password)
        
        admin.save()
    
    return render(request, 'Register.html')
    

def AddStudent(request):
    if request.method == "POST":
        Name = request.POST["Name"]
        Id = request.POST["Id"]
        email = request.POST["Email"]
        Phone = request.POST["Phone"]
        GPA = request.POST["GPA"]
        Brith = request.POST["BirthDate"]
        Level = request.POST["Level"]
        Gender = request.POST["Gender"]
        Department = request.POST["Department"]
        Status = request.POST["Status"]
        Password = request.POST["Password"]

        student = Student(name = Name, id = Id, Email = email, phone = Phone, gpa = GPA,
                        birthDate = Brith, gender = Gender, level = Level, status = Status,
                        department = Department, password = Password)
        
        student.save()
    
    return render(request, 'Add Student.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        register = Admin.objects.all()
        for x in register:
            if email == x.Email:
                if password == x.password:
                    return redirect('Home-Registered')
                
        messages.error(request, 'Invalid email or password.')
        return redirect('Login')

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
        

def loginToUpdate(request):
    
    return render(request, 'logintoupdate.html')


def Update(request):
    
    return render(request, 'Update.html')


def changeStatus(request):
    return render(request, 'change the status from table .html')
