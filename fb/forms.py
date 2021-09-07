from fb.models import Post
from django import forms
from .models import *

class Post_create_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image']