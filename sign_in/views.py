from django.shortcuts import render
from .forms import CreateLogForm, ChooseBathroom
from .models import Student, Log, Bathroom

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def student(request):   
    form = CreateLogForm()

    if request.method == 'POST':
        form = CreateLogForm(request.POST)
        student_id = form['student'].value()
        student = Student.objects.filter(student_id=student_id)[0]
        print(student)
        log = Log(
            student_id = student
            # bathroom = bathroom(request)
        )
        log.save()
    #     print(form)
    #     # student_id = request.POST.get('student_id')
    #     # form.fields['student_id'].choices = [student_id, student_id]
    #     stu = Student.objects.filter(student_id=form['student_id'])
    #     print(stu)
    #     if form.is_valid():
    #         form.save() 
        # log = Logs(data['student_id'])
        #add to admin page
    else:
        form = CreateLogForm()

    return render(request, 'pages/student_login.html', {'form': form})

def logs(request):
    return render(request, 'pages/student_logs.html')

def bathroom(request):
    form = ChooseBathroom()
    
    if request.method == 'POST':
        form = ChooseBathroom(request.POST)
        bathroom = form['bathrooms'].value()
        print(bathroom)
        room = Bathroom(room = bathroom)
        room.save()
        return home(request)
        
        
    return render(request, 'pages/bathroom.html',{'form': form})

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




