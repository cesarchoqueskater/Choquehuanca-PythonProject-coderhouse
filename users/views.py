from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.urls import reverse_lazy
from users.models import InfoExtra
# Create your views here.

def login(request):
    if request.method == "POST":
        formContent = AuthenticationForm(request, data=request.POST)
        if formContent.is_valid():
            usuario = formContent.get_user()

            django_login(request, usuario)

            InfoExtra.objects.get_or_create(user=usuario)

            return redirect("home")
    else:
        formContent = AuthenticationForm()

    return render(request, "users/login.html", {"formContent": formContent})

