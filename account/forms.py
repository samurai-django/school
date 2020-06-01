# {% user register %}

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from .models import Account
from django.contrib.auth import get_user_model

from .models import MessageToStudent

User = get_user_model()



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email=email, is_active=False).delete()
        return email




# class UploadUserForm(UserChangeForm):
# {{ Login form}}
class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid login')

# {%student login %}
class StudentForm(forms.ModelForm):

    password = forms.CharField(label='password', widget=forms.PasswordInput)
    is_student = True


    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid login')

class MessageToStudentForm(forms.ModelForm):

    class Meta:
        model = MessageToStudent
        fields = '__all__'







class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('image', 'email', 'username')

    def clean_image(self):
        image = self.cleaned_data['image']
        return image


    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('username "%s" is already in use. ' % account.username)


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('image',)

    # def clean_email(self):
    #     if self.is_valid():
    #         image = self.cleaned_data['image']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
