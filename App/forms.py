from tkinter import Widget
from turtle import width
from django import forms
from .models import Post

class PostForm (forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'slug', 'author', 'content')
    
    widget = {
      'title': forms.TextInput(attrs = {'class' : 'form-control'}), 
      'slug': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Este es un identificador único del post, escribe el titulo sin espacios, con guiones' }), 
      'author': forms.Select(attrs = {'class' : 'form-control'}), 
      'content': forms.Textarea(attrs = {'class' : 'form-control'}), 
      
    }