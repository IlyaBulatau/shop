from django.http import HttpResponse, HttpResponseNotFound, Http404 
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from .utils import *


class HomePage(DataMixin, ListView):
    model = Home
    template_name = 'home/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main Page')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Home.objects.filter(is_published=True)



def about(request):
    return render(request, 'home/about.html', {'title': 'About Page', 'menu': menu})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddForm
    template_name = 'home/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add Page')
        return dict(list(context.items()) + list(c_def.items()))





def contact(request):
    return HttpResponse('Contacts')


def login(request):
    return HttpResponse('Sign in')


class ShowPost(DataMixin, DetailView):
    model = Home
    template_name = 'home/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


    

class CarCategory(DataMixin,ListView):
    model = Home
    template_name = 'home/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Home.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - ' + str(context['posts'][0].cat),
                                     cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))





def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')