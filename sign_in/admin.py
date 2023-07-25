from django.contrib import admin
from .models import Student, Bathroom, Log
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field

admin.site.register(Student)
admin.site.register(Bathroom)


class LogAdminResource(resources.ModelResource):
    student_id = Field(attribute = "student_id")
    bathroom = Field(attribute = "bathroom")
    
    class Meta:
        model = Log
        exclude = ('id',)
        fields = ('student_id', 'bathroom', 'Time_in', 'Time_out')

class LogsImportExportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LogAdminResource
    
    readonly_fields = ("Time_in","Time_out")
    list_filter = ('Time_in', 'Time_out', "student_id", "bathroom")
    list_display = ('student_id', 'bathroom', 'Time_in', 'Time_out')

admin.site.register(Log, LogsImportExportAdmin)