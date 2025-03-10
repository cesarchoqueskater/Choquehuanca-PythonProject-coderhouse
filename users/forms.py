from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms

from django.contrib.auth.models import User


class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mt-3 mb-3', 'placeholder': 'Usuario'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-3 mb-3', 'placeholder': 'Contraseña'})
    )
    class Meta:
        model = User
        fields = ['username','password']
        help_text = { field: '' for field in fields }

class MyCreationForm(UserCreationForm):

    #Nombres definidos email, password1, password2
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mt-3 mb-3'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control mt-3 mb-3'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control mt-3 mb-3'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'form-control mt-3 mb-3'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = { field: '' for field in fields }

class MyUpdateForm(UserChangeForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control mt-3 mb-3'}))
    password = None
    first_name = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'class': 'form-control mt-3 mb-3'}))
    last_name = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'class': 'form-control mt-3 mb-3'}))

    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','avatar']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter old password'})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new passwod'})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'})
    )