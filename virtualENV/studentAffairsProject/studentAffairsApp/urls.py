from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('Home/', views.Home, name = 'Home'),
    path('Home/Register/', views.Register, name='Register'),
    path('Home/Login/', views.Login, name='Login'),  
    path('Home-Registered/', views.Home_Registered, name = 'Home-Registered'),
    path('Home-Registered/Search/', views.search, name = 'search'),
    path('Home-Registered/Search/Change Department/', views.change_department, name = 'Change Department'),
    path('Home-Registered/logintoupdate/', views.loginToUpdate, name='loginToUpdate'),
    path('Home-Registered/logintoupdate/Update<int:id>/', views.Update, name='Update'),
    path('Home-Registered/change the status from table/', views.ListStudentPage, name='changeStatus'),
    path('Home-Registered/Add Student/', views.AddStudent, name='AddStudent'),
    path('Home-Registered/change the status from table/<int:id>/', views.changeStatus, name='change-status'),
]