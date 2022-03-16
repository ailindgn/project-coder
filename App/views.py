from django.shortcuts import render
from .models import Post
from django.views import generic
from .forms import PostForm, UpdateForm

# Create your views here.

class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html' #para que solo los posts en estado "publicado" cean

class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'
  
  
class AddPostView(generic.CreateView):
  model = Post
  form_class = PostForm
  template_name = 'add_post.html'
  # fields = '__all__' ## con el post form ya no va 

class UpdatePostView(generic.UpdateView):
  model = Post
  form_class = UpdateForm 
  template_name = 'update_post.html'
