from django.shortcuts import render

from .models import Student, Logs, Bathroom
# Create your views here.

def home(request):
    return render(request, 'home.html')

def student(request):
    return render(request, 'student_login.html')

def logs(request):
    return render(request, 'student_logs.html')


   