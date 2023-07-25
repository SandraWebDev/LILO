from django.contrib import admin
from .models import Student, Bathroom, Log
from import_export.admin import ImportExportModelAdmin

admin.site.register(Student)
admin.site.register(Bathroom)

class LogsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("Time_in","Time_out")
    list_filter = ('Time_in', 'Time_out', "student_id", "bathroom")
    list_display = ('student_id', 'bathroom', 'Time_in', 'Time_out')

admin.site.register(Log, LogsAdmin)