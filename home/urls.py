from home.views import home,sayHi,create_blog,list_blog, details_blog, update_blog, delete_blog, UpdateBlogView, DeleteBlogView

from django.urls import path

urlpatterns = [
    path('', home, name="home"),
    #path('sayHi/<str:name>/<int:age>', sayHi, name="hi"),
    path('create-blog', create_blog, name="create_blog"),
    path('list-blog', list_blog, name="list_blog"),
    path('details-blog/<str:id>/', details_blog, name='details_blog'),
    
    #path('update-blog/<str:id>/', update_blog, name='update_blog'),
    
    path('update-blog/<str:pk>/', UpdateBlogView.as_view(), name='update_blog'),
    path('delete-blog/<str:pk>/', DeleteBlogView.as_view(), name='delete_blog')
]