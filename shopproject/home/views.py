from django.http import HttpResponse, HttpResponseNotFound, Http404 
from django.shortcuts import redirect, render
from .models import *

menu = [{'title': 'About the site', 'url_name': 'about'},
        {'title': 'Add item', 'url_name': 'add_page'},
        {'title': 'Contacts', 'url_name': 'contact'},
        {'title': 'Sign in', 'url_name': 'login'},
]

def home(request):
    posts = Home.objects.all()
    context = {
        'post': posts,
        'menu': menu,
        'title': 'Main Page'
    }
    return render(request, 'home/index.html', context=context)

def about(request):
    return render(request, 'home/about.html', {'title': 'About Page', 'menu': menu})

def addpage(request):
    return HttpResponse('Add page')

def contact(request):
    return HttpResponse('Contacts')

def login(request):
    return HttpResponse('Sign in')

def show_post(request, post_id):
    return HttpResponse(f'Items with number id =  {post_id}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')