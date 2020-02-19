from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile, Project, Rate

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','contact','bio']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['image', 'title','url','detail_desciption']