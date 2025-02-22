from home.views import home,sayHi,create_blog,list_blog

from django.urls import path

urlpatterns = [
    path('', home, name="home"),
    #path('sayHi/<str:name>/<int:age>', sayHi, name="hi"),
    path('create-blog', create_blog, name="create_blog"),
    path('list-blog', list_blog, name="list_blog")
]