from django.urls import path, re_path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('cat/<slug:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)

]