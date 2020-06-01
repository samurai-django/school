from django import forms
from .models import Class, Relationship2, ClassDetail



class ClassCreateForm(forms.ModelForm):
    class Meta:
        model = Class
        # fields = ['subject', 'semester', 'abstract', ]
        # fields = '__all__'
        fields = ['semester', 'abstract', 'subjects', 'slug', ]






class StudentClassRegisterForm(forms.ModelForm):

    class Meta:
        model = Relationship2
        fields = ['classes']

class ClassDetailForm(forms.ModelForm):
    class Meta:
        model = ClassDetail
        fields = ['name', 'is_class', 'pdf_file', ]
