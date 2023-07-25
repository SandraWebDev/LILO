from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import CreateLogForm, ChooseBathroom
from .models import Student, Log, Bathroom
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import datetime

@login_required
def home(request):
    return render(request, 'pages/home.html')

@login_required
def bathroom(request, pk):   
    if request.method == 'POST':
        if request.POST['action'] == 'Enter':
            form = CreateLogForm(request.POST)
            student_id = form['student'].value()
            student = Student.objects.filter(student_id=student_id)[0]
            br = get_object_or_404(Bathroom, pk=pk)
            log = Log(
                student_id = student,
                bathroom = br
            )
            log.save()
        else:
            studentId = request.POST['action']
            Log.objects.filter(id = studentId).update(Time_out = datetime.datetime.now())

    form = CreateLogForm()
    br = get_object_or_404(Bathroom, pk=pk)
    return render(request, 'pages/student_login.html', {'form': form, 'logs':Log.objects.all().filter(Time_out = None).filter(bathroom = br)})

@permission_required('sign_in.can_view_log_history')
@login_required
def logs(request):
    return render(request, 'pages/student_logs.html', {'logs': Log.objects.all()})

@login_required
def bathroom_selector(request):
    form = ChooseBathroom()
    if request.method == "POST":
        form = ChooseBathroom(request.POST)
        br_id = form['bathrooms'].value()
        url = reverse('bathroom', args=([br_id]))
        print(url)
        return redirect(reverse('bathroom', args=([br_id])))  
        
    return render(request, 'pages/bathroom.html',{'form': form})

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




