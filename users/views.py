from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login
from users.models import InfoExtra

from users.forms import MyAuthenticationForm,MyCreationForm, MyPasswordChangeForm,MyUpdateForm

from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.

def login(request):
    if request.method == "POST":
        formContent = MyAuthenticationForm(request, data=request.POST)
        if formContent.is_valid():
            usuario = formContent.get_user()

            django_login(request, usuario)

            InfoExtra.objects.get_or_create(user=usuario)

            return redirect("home")
    else:
        formContent = MyAuthenticationForm()

    return render(request, "users/login.html", {"formContent": formContent})


def register(request):
    if request.method == "POST":
        formContent = MyCreationForm(request.POST)
        if formContent.is_valid():
            formContent.save()
            
            return redirect("login")
    else:
        formContent = MyCreationForm()

    return render(request, "users/register.html", {"formContent": formContent})

def edit_profile(request):

    #Lo llamamos en minuscula el request.user.infoextra
    info_extra = request.user.infoextra
    
    if request.method == "POST":
        formContent = MyUpdateForm(request.POST, request.FILES , instance=request.user)
        if formContent.is_valid():

            if formContent.cleaned_data.get('avatar'):
                info_extra.avatar = formContent.cleaned_data.get('avatar')

            info_extra.save()

            formContent.save()

            return redirect("home")
    else:
        formContent = MyUpdateForm(instance=request.user, initial={'avatar' : info_extra.avatar})

    return render(request, "users/edit_profile.html", {"formContent": formContent})

class change_password(PasswordChangeView):
    template_name = 'users/change_password.html'
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('home')