from django import forms
from teacher.models import TeacherFunction


class TeacherFunctionForms(forms.ModelForm):

    class Meta:
        model = TeacherFunction
        fields = ('title', )

