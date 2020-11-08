from django import forms
from .models import Students


class DateInput(forms.DateInput):
    input_type = 'date'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students

        widgets = {'exam_date': DateInput()}
        fields = ('teacher', 'student_name', 'student_email', 'class_number', 'section', 'roll_number', 'maths',
                  'english', 'social', 'evs', 'hindi', 'exam_date')
        labels = {'teacher': 'Teacher Name', 'student_name': 'Student Name', 'student_email': 'Email',
                  'class_number': 'Class', 'section': 'Section', 'roll_number': 'Roll Number', 'maths': 'Maths',
                 'english': 'Endlish', 'social':'Social', 'evs':'EVS', 'hindi':'Hindi', 'exam_date':'Exam Date'
        }
