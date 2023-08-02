from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
         return f"{self.first_name} {self.last_name}, Id: {self.student_id}"

class Bathroom(models.Model):
    room = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='')
    max_people_allowed = models.PositiveIntegerField(default = 2)

    def __str__(self):
         return f"{self.room}"
    
import pytz
from datetime import datetime, timezone

class Log(models.Model):
    Time_in = models.DateTimeField(auto_now=True)
    Time_out = models.DateTimeField(blank=True, null=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    bathroom = models.ForeignKey(Bathroom, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        permissions = (("can_view_log_history", "can_edit_log_history"),)

    def __str__(self):  
            self.Time_in = datetime.now()
           
            return f"Teacher: {self.user}, Bathroom: {self.bathroom}, Student: {self.student_id}, Time_in: {self.Time_in}, Time_out: x{self.Time_out} "
    
class building(models.Model):
    building = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.building}"

class Profile(models.Model):
    bathroom = models.ForeignKey(Bathroom, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user}, {self.bathroom},"