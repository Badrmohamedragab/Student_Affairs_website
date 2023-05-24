from django.db import models

class Student(models.Model):
    genderList = [('Male','Male'),
    ('Female','Female')]
    levelsList = [(1, 1),(2, 2), (3, 3), (4, 4) ]
    statusList = [('Active', 'Active'),('Inactive', 'Inactive')]
    departmentList = [('CS', 'CS'),('IS', 'IS'),('AI', 'AI'),('DS', 'DS'), ('IT', 'IT')]

    name = models.CharField(max_length=50)
    id = models.BigIntegerField(primary_key= True)
    Email = models.EmailField()
    phone = models.CharField(max_length=20)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    birthDate = models.DateField()
    gender = models.CharField(max_length=50, choices= genderList)
    level = models.IntegerField(choices=levelsList)
    status = models.CharField(max_length=50, choices=statusList)
    department = models.CharField(max_length=4, choices=departmentList)
    password = models.CharField(max_length=20)
     
    def __str__(self):
        return self.name

class Admin(models.Model):
    genderList = [('Male','Male'),
    ('Female','Female')]
    name = models.CharField(max_length=50)
    Email = models.EmailField()
    phone = models.CharField(max_length=20)
    birthDate = models.DateField()
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=50, choices= genderList)
    def __str__(self):
        return self.name

    

    

    
