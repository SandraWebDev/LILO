from django.db import models
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Student_id = models.CharField(max_length=100)


class Logs(models.Model):
    Time_in = models.DateTimeField(auto_now=True)
    #Time_out
    student_id = models.ForeignKey("Student", on_delete=models.PROTECT)
    bathroom = models.ForeignKey("Bathroom", on_delete=models.PROTECT)
    user = models.ForeignKey(User, default="", on_delete=models.PROTECT)

class Bathroom(models.Model):
    room = models.CharField(max_length=100)