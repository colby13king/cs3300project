# forms.py
from django import forms
from .models import AppUser
from .models import Question, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AppUserForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['name', 'email', 'experience', 'age']  

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')