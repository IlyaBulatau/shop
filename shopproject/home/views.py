from django.http import HttpResponse, HttpResponseNotFound, Http404 
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *

menu = [{'title': 'About the site', 'url_name': 'about'},
        {'title': 'Add item', 'url_name': 'add_page'},
        {'title': 'Contacts', 'url_name': 'contact'},
        {'title': 'Sign in', 'url_name': 'login'},
]

class HomePage(ListView):
    model = Home
    template_name = 'home/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main Page'
        context['cat_selected'] = 0
        return context
    
    def get_queryset(self):
        return Home.objects.filter(is_published=True)


# def home(request):
#     posts = Home.objects.all()
#     context = {
#         'post': posts,
#         'menu': menu,
#         'title': 'Main Page',
#         'cat_selected': 0,
#     }
#     return render(request, 'home/index.html', context=context)


def about(request):
    return render(request, 'home/about.html', {'title': 'About Page', 'menu': menu})


class AddPage(CreateView):
    form_class = AddForm
    template_name = 'home/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Add Page'
        return context




# def addpage(request):
#     if request.method == 'POST':
#         form = AddForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddForm()
#     return render(request, 'home/addpage.html', {'title': 'Add Page', 'menu': menu, 'form': form})


def contact(request):
    return HttpResponse('Contacts')


def login(request):
    return HttpResponse('Sign in')


class ShowPost(DetailView):
    model = Home
    template_name = 'home/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Home, slug=post_slug)

#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }

#     return render(request, 'home/post.html', context=context)
    

class CarCategory(ListView):
    model = Home
    template_name = 'home/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Home.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Category - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context



# def show_category(request, cat_id):
#     posts = Home.objects.filter(cat_id=cat_id)
#     if len(posts) == 0:
#         raise Http404()
#     context = {
#         'post': posts,
#         'menu': menu,
#         'title': 'Main Page',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'home/index.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')