from django.contrib import admin
from .models import Student, Bathroom, Log
# Register your models here.

admin.site.register(Student)
admin.site.register(Bathroom)
# admin.site.register(Logs)

class LogsAdmin(admin.ModelAdmin):
    readonly_fields = ("Time_in","Time_out")

admin.site.register(Log, LogsAdmin)