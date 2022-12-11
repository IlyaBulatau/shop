from django.http import HttpResponse, HttpResponseNotFound, Http404 
from django.shortcuts import redirect, render
from .models import *

menu = ['About the site','Models car','Contacts','Sign in']

def home(request):
    posts = Home.objects.all()
    return render(request, 'home/index.html', {'title': 'Main Page', 'menu': menu, 'posts': posts})

def about(request):
    return render(request, 'home/about.html', {'title': 'About Page', 'menu': menu})


def categories(request, catid):
    return HttpResponse(f'<h1>Article categories</h1><p>{catid}</p>')

def archive(requst, year):
    if int(year) > 2023:
        return redirect('home/', permanent=True)

    return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')