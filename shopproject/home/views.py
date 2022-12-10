from django.http import HttpResponse

def home(request):
    return HttpResponse('Home Page')

def categories(request):
    return HttpResponse('<h1>Article categories</h1>')