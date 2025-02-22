from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def sayHi(request,name,age):
    current_time = datetime.now()
    return render(request, 'home/saludo.html', {'time' : current_time, 'name': name, 'age': age})