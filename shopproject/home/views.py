from django.http import HttpResponse, HttpResponseNotFound, Http404 
from django.shortcuts import redirect, render

def home(request):
    return HttpResponse('Home Page')

def categories(request, catid):
    return HttpResponse(f'<h1>Article categories</h1><p>{catid}</p>')

def archive(requst, year):
    if int(year) > 2023:
        return redirect('home/', permanent=True)

    return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')