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
        return redirect('Home-Registered')

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
        return redirect('Home-Registered')

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
                else:
                    messages.error(request, 'Invalid password.')
                    return redirect('Login')
            else:
                messages.error(request, 'Invalid email.')
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
    if request.method == "POST":
        dep = request.POST.get("depart")
        student_id = request.POST.get("id")
        student = Student.objects.get(id=student_id)
        student.department = dep
        student.save()
        return redirect('Home-Registered')
    else:
        name = request.GET.get('name')
        student_id = request.GET.get('id')
        department = request.GET.get('department')
        return render(request, 'Change Department.html', {'name': name, 'id': student_id, 'department': department})


def changeStatus(request):

    return render(request, 'change the status from table .html')


def loginToUpdate(request):
    if request.method == 'POST':
        Id = request.POST.get("ID")
        register = Student.objects.all()
        for x in register:
            if x.id == int(Id):
                return redirect('Update', id = Id)

        return redirect('loginToUpdate')
    return render(request, 'logintoupdate.html')


def Update(request, id):
    student = Student.objects.get(id=id)

    # Handle HTTP POST request from form
    if request.method == 'POST':
        if 'delete' in request.POST:
            student.delete()
            return redirect('Home-Registered')
        else:
            n = request.POST['n']
            e = request.POST['e']
            Phone = request.POST['Phone']
            gpa = request.POST['gpa']
            d = request.POST['d']
            l = request.POST['l']
            Status = request.POST['Status']

            # Update the student's data
            student.name = n
            student.Email = e
            student.phone = Phone
            student.gpa = gpa
            student.birthDate = d
            student.level = l
            student.status = Status
            # Save the student's data
            student.save()
            return redirect('Home-Registered')

    # Render the HTML template with the student's data
    studentname = student.name
    studentid = student.id
    studentemail = student.Email
    studentphone = student.phone
    studentgpa = student.gpa
    studentbirth = student.birthDate
    studentgander = student.gender
    studentlevel = student.level
    studentstatu = student.status
    studentdept = student.department
    return render(request, 'Update.html', {'name': studentname, 'id': studentid,
                                            'email': studentemail, 'phone': studentphone,
                                            'gpa': studentgpa, 'birth': studentbirth, 'gander': studentgander,
                                            'level': studentlevel, 'statu': studentstatu, 'department': studentdept})


def ListStudentPage(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'change the status from table .html', context)


def changeStatus(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.status = request.POST["Status"]
        student.save()
        return redirect('changeStatus')  # Redirect to the student table page
    else:
        return render(request, 'change-status.html', {'student': student})