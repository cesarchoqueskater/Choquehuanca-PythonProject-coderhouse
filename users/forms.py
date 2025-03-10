from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms

from django.contrib.auth.models import User


class MyCreationForm(UserCreationForm):

    #Nombres definidos email, password1, password2

    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = { field: '' for field in fields }

class MyUpdateForm(UserChangeForm):

    email = forms.EmailField()
    password = None
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','avatar']