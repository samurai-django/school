from .models import Course, CourseDetail
from django import forms
from django.forms import ValidationError


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'semester', 'abstract', 'subjects', 'grades', 'slug')



class AddCourseDetailForm(forms.ModelForm):
    class Meta:
        model = CourseDetail
        fields = ['number', 'pdf_file', ]



