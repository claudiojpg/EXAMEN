from django import forms
from .models import Noticia

from django.contrib.auth.models import User


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'


class userForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
