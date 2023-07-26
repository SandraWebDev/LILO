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
    form = CreateLogForm()
    br = get_object_or_404(Bathroom, pk=pk)
    logs = Log.objects.filter(bathroom = br, Time_out = None)

    if request.method == 'POST':
        if request.POST['action'] == 'Enter':
            form = CreateLogForm(request.POST)
            if form.is_valid():
                student_id = form.cleaned_data['student']
                student = Student.objects.filter(student_id=student_id)[0]

                log = Log(
                    student_id = student,
                    bathroom = br
                )
                log.save()
                form = CreateLogForm()
        else:
            studentId = request.POST['action']
            logs.update(Time_out = datetime.datetime.now())


    return render(request, 'pages/student_login.html', {'form': form, 'logs':logs, "room": br.room})

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




