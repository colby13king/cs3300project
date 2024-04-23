# forms.py
from django import forms
from .models import AppUser
from .models import Question

class AppUserForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['name', 'email', 'experience', 'age']  

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'image']

