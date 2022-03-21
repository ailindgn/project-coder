from tkinter import Widget
from turtle import width
from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
  choice_list.append(item)



class PostForm (forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'slug', 'category', 'author', 'content', 'status')
    
    widget = {
      'title': forms.TextInput(attrs = {'class' : 'form-control'}), 
      'slug': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Este es un identificador único del post, escribe el titulo sin espacios, con guiones' }), 
      'category': forms.Select(choices = choice_list, attrs = {'class' : 'form-control'}), 
      'author': forms.Select(attrs = {'class' : 'form-control'}), 
      'content': forms.Textarea(attrs = {'class' : 'form-control'}), 
      'status': forms.Select(attrs = {'class' : 'form-control'}),
    }

class UpdateForm (forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'slug', 'category', 'content', 'status')
    
    widget = {
      'title': forms.TextInput(attrs = {'class' : 'form-control'}), 
      'slug': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Este es un identificador único del post, escribe el titulo sin espacios, con guiones' }), 
      'category': forms.Select(attrs = {'class' : 'form-control'}), 
      'content': forms.Textarea(attrs = {'class' : 'form-control'}), 
      'status': forms.Select(attrs = {'class' : 'form-control'}),
    }