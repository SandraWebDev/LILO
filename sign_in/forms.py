from django import forms
from django.forms import ModelForm
from sign_in.models import Student, Log, Bathroom

# class CreateLogForm(ModelForm):
#     class Meta:
#         model = Logs
#         fields = ["student_id"]
#         widgets = {"student_id": forms.TextInput(attrs={'rows':1, 'cols': 20})}
# # , "bathroom", "user"

from django.core.exceptions import ValidationError

class CreateLogForm(forms.Form):

    student = forms.CharField(
        max_length=6,
    )

    def clean_student(self):
        stu = self.cleaned_data["student"]
        if len(stu) < 6:
            raise ValidationError("must be 6 numbers")
        if (stu.isnumeric() == False):
            raise ValidationError("Student Id's don't contain letters")

        student = Student.objects.filter(student_id=stu)
        if len(student) < 1:
            raise ValidationError("Must be a valid student ID")
        
        return stu

#form to create choices of the bathrooms
class ChooseBathroom(forms.Form):
    bathrooms = Bathroom.objects.all()
    b_options = []
    for b in bathrooms:
        b_options.append( (b.id, b.room) )

    bathroom_choices = tuple(b_options)

    bathrooms = forms.ChoiceField(choices = bathroom_choices)



# def clean_student(self):

#         student_string = self.clean('student_id')

#         try:
#             student = Student.objects.get(id=student_string)
#         except Student.DoesNotExist:
#             raise forms.ValidationError("id does not exist.")

#         return student


# def clean_student_id(self):
#     data = self.cleaned_data['id']

   