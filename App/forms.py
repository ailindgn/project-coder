from pickle import FALSE
from tkinter import Widget
from turtle import width
from django import forms
from .models import Post, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
  choice_list.append(item)



class PostForm (forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'slug', 'category', 'author', 'content', 'status','imagen')
    
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
    fields = ('title', 'slug', 'category', 'content', 'status', 'imagen')
    
    widget = {
      'title': forms.TextInput(attrs = {'class' : 'form-control'}), 
      'slug': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Este es un identificador único del post, escribe el titulo sin espacios, con guiones' }), 
      'category': forms.Select(attrs = {'class' : 'form-control'}), 
      'content': forms.Textarea(attrs = {'class' : 'form-control'}), 
      'status': forms.Select(attrs = {'class' : 'form-control'}),
    }


class nuestracreacionuser(UserCreationForm):
      
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir contraseña', widget=forms.PasswordInput)
  
    class Meta: 
      model = User
      fields = ['username','email', 'password1', 'password2']
      help_texts = { k: '' for k in fields }



class nuestraedicionuser(forms.Form):
  
    #username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField(label = 'Primer nombre',max_length=20, required= FALSE)
    last_name = forms.CharField(label = 'Apellido',max_length=20)
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir contraseña', widget=forms.PasswordInput)
    
  
    #class Meta: 
     # model = User
     # fields = ['username','email', 'password1', 'password2']
     # help_texts = { k: '' for k in fields }