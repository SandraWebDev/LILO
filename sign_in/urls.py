from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bathroom, name='bathroom'),
    path('home/', views.home, name='home'),
    path('student_login/', views.student, name='student'),
    path('student_logs/', views.logs, name='logs'),
    path('bathroom/', views.bathroom, name = 'bathroom')
]
