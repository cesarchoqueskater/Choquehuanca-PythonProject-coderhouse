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
            user = formContent.save(commit=False)  # Guarda el usuario pero aún no lo envía a la BD
            user.save()  # Ahora sí se guarda en la BD

            # Guardar la información extra
            InfoExtra.objects.create(
                user=user,
                birth_date=formContent.cleaned_data["birth_date"],
                workplace=formContent.cleaned_data.get("workplace"),
                skills=formContent.cleaned_data.get("skills"),
                avatar=formContent.cleaned_data.get("avatar"),
            )
            
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

            user = formContent.save(commit=False) 

            info_extra.birth_date = formContent.cleaned_data["birth_date"]
            info_extra.workplace = formContent.cleaned_data.get("workplace")
            info_extra.skills = formContent.cleaned_data.get("skills")

            if formContent.cleaned_data.get('avatar'):
                info_extra.avatar = formContent.cleaned_data.get('avatar')

            user.save()
            info_extra.save()

            formContent.save()

            return redirect("home")
    else:
        formContent = MyUpdateForm(instance=request.user, initial={
            'avatar' : info_extra.avatar,
            "birth_date": info_extra.birth_date,
            "workplace": info_extra.workplace,
            "skills": info_extra.skills,
            })

    return render(request, "users/edit_profile.html", {"formContent": formContent})

class change_password(PasswordChangeView):
    template_name = 'users/change_password.html'
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('home')


def about_me(request):
    user_info = request.user.infoextra 
    return render(request, "users/about_me.html", {"user_info": user_info})