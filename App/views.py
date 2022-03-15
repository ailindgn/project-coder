from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html' #para que solo los posts en estado "publicado" cean

class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'
  
  
class AddPostView(generic.CreateView):
  model = Post
  template_name = 'add_post.html'
  fields = '__all__'


##
############################################3

## pruebas ###
from django.http import HttpRequest, HttpResponse 
import random
from django.template import Context, Template, loader



def otra_vista(request):
  return HttpResponse('''
                      <h1> Este es un título en h1 </h1>
                      ''')

## pruebas
# def numero_random(request):
#   numero = random.randrange(15,100)
#   texto = f'<h1> Este es tu número random: {numero} </h1>'
#   return HttpResponse(texto)