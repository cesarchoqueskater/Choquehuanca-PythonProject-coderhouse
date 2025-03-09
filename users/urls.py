from django.urls import path
from users.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/' , login , name='login'),
    path('logout/' , LogoutView.as_view(template_name = 'users/logout.html') , name='logout')
    #path('register/' , register , name='register')
]