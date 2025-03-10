from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms

from django.contrib.auth.models import User

from users.models import InfoExtra


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

    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    workplace = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control mt-3 mb-3'})
    )

    skills = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control mt-3 mb-3', 'rows': 3})
    )

    class Meta:
        model = User
        fields = ['username','email','password1','password2','birth_date', 'workplace', 'skills']
        help_text = { field: '' for field in fields }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Crear o actualizar el modelo InfoExtra con los nuevos campos
            InfoExtra.objects.create(
                user=user,
                birth_date=self.cleaned_data["birth_date"],
                workplace=self.cleaned_data.get("workplace"),
                skills=self.cleaned_data.get("skills")
            )
        return user
        
class MyUpdateForm(UserChangeForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control mt-3 mb-3'}))
    password = None
    first_name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class': 'form-control mt-3 mb-3'}))
    last_name = forms.CharField(label='LastName',widget=forms.TextInput(attrs={'class': 'form-control mt-3 mb-3'}))

    avatar = forms.ImageField(required=False)

    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control mt-3 mb-3', 'type': 'date'})
    )

    workplace = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control mt-3 mb-3'})
    )
    skills = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control mt-3 mb-3', 'rows': 3})
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','avatar', 'birth_date', 'workplace', 'skills']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            info_extra, created = InfoExtra.objects.get_or_create(user=user)
            info_extra.birth_date = self.cleaned_data["birth_date"]
            info_extra.workplace = self.cleaned_data.get("workplace")
            info_extra.skills = self.cleaned_data.get("skills")
            info_extra.save()
        return user
    
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