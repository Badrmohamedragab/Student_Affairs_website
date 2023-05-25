from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name = 'index'),
    path('Home/', views.Home, name = 'Home'),
    path('Register/', views.Register, name='Register'),
    path('Login/', views.Login, name='Login'),
]