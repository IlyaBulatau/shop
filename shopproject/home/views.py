from django.http import HttpResponse, HttpResponseNotFound, Http404 
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView
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
        return Home.objects.filter(is_published=True).select_related('cat')



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





class ContactForm(DataMixin, FormView):
    form_class = ContactFormView
    template_name = 'home/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Connect')
        return dict(list(context.items()) + list(c_def.items()))
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')
    


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
        return Home.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Category - ' + str(c.name),
                                     cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))
    

class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('login')
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign up')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'home/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign in')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')










def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
    