from django import forms
from .models import *


class AddForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField(required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category')