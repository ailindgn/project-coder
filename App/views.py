from django.shortcuts import render
from .models import Post, Category
from django.views import generic
from .forms import PostForm, UpdateForm
from django.db.models import Q 


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

class AddCategoryView(generic.CreateView):
  model = Category
  #form_class = PostForm
  template_name = 'add_category.html'
  fields = '__all__' 

class UpdatePostView(generic.UpdateView):
  model = Post
  form_class = UpdateForm 
  #fields = '__all__'
  template_name = 'update_post.html'


def search_venues(request):
  if request.method == "POST":
    searched = request.POST['searched']
    venues = Post.objects.filter(title__contains=searched)
    return render(request, 'search_venues.html', {'searched' : searched, 'venues': venues })
  
  else:
    return render(request, 'search_venues.html', {})