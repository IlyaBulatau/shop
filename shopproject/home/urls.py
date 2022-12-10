from django.urls import path, re_path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('cat/<slug:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]