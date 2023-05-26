from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name = 'index'),
    path('Home/', views.Home, name = 'Home'),
    path('Register/', views.Register, name='Register'),
<<<<<<< HEAD
    path('Register/addStudent', views.addStudent, name='addStudent'),
=======
>>>>>>> c18e534deb2045e01fababa29455b4974f4def6e
    path('Login/', views.Login, name='Login'),
]