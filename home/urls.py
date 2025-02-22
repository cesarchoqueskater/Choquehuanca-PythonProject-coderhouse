from home.views import home,sayHi

from django.urls import path

urlpatterns = [
    path('', home, name="home"),
    path('sayHi/<str:name>/<int:age>', sayHi, name="hi")
]