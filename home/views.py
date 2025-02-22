from django.shortcuts import redirect, render
from django.http import HttpResponse

from datetime import datetime

from home.models import Blog
from home.forms import CreateBlog, SearchBlog

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def sayHi(request,name,age):
    current_time = datetime.now()
    return render(request, 'home/saludo.html', {'time' : current_time, 'name': name, 'age': age})

def create_blog(request):
    print(request.POST)
    formContent = CreateBlog()

    if request.method == "POST":
        formContent = CreateBlog(request.POST)
        if formContent.is_valid():
            title = formContent.cleaned_data.get('title')
            content = formContent.cleaned_data.get('content')
            author = formContent.cleaned_data.get('author')
            description = formContent.cleaned_data.get('description')
            publication_date = formContent.cleaned_data.get('publication_date')
            is_published = formContent.cleaned_data.get('is_published')
            tags = formContent.cleaned_data.get('tags')

            blog = Blog(title = title, content = content , author = author, description = description, publication_date = publication_date, is_published = is_published ,tags = tags)
            blog.save()

            return redirect("list_blog")

    return render(request, 'home/create_blog.html', { 'formContent': formContent} )

def list_blog(request):
    blogs = Blog.objects.all()
    #print("Printer Blogs")
    #print(blogs)
    formContent = SearchBlog(request.GET)
    if formContent.is_valid():
        title_to_search = formContent.cleaned_data.get('title')
        author_to_search = formContent.cleaned_data.get('author')
        blogs = Blog.objects.filter( title__icontains = title_to_search , author__icontains= author_to_search)
    return render(request, 'home/list_blog.html', {'blogs' : blogs, 'formContent' : formContent})