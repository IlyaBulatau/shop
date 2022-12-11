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
    cat = Category.objects.all()
    context = {
        'post': posts,
        'cat': cat,
        'menu': menu,
        'title': 'Main Page',
        'cat_selected': 0,
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

def show_category(request, cat_id):
    posts = Home.objects.filter(cat_id=cat_id)
    cat = Category.objects.all()
    if len(posts) == 0:
        raise Http404()
    context = {
        'post': posts,
        'cat': cat,
        'menu': menu,
        'title': 'Main Page',
        'cat_selected': cat_id,
    }
    return render(request, 'home/index.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')