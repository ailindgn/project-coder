from django.shortcuts import render
from .models import Avatar, Post, Category
from django.views import generic
from .forms import PostForm, UpdateForm, nuestracreacionuser
from django.db.models import Q 
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import nuestracreacionuser, nuestraedicionuser
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin #loginrequieredmixin a las clase basada en vista que le quiero poner, el mixin siempre debe estar primero 
from .models import Avatar
from django.urls import reverse, reverse_lazy
# Create your views here.


class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html' #para que solo los posts en estado "publicado" cean

class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'
  

class AddPostView(LoginRequiredMixin,generic.CreateView):
  model = Post
  form_class = PostForm
  template_name = 'add_post.html'
  # fields = '__all__' ## con el post form ya no va
   

class AddCategoryView(generic.CreateView):
  model = Category
  #form_class = PostForm
  template_name = 'add_category.html'
  fields = '__all__' 


class UpdatePostView(LoginRequiredMixin,generic.UpdateView):
  model = Post
  form_class = UpdateForm 
  #fields = '__all__'
  template_name = 'update_post.html'

class DeletePostView(LoginRequiredMixin,generic.DeleteView):
  model = Post
  template_name = 'delete_post.html'
  success_url = reverse_lazy('home')
  

def about_us(request):
  return render(request, 'about_us.html', {'':''})

def loggedin(request):
  return render(request, 'loggedin.html', {'':''})

def loggedout(request):
  return render(request, 'loggedin.html', {'':''})

#def registrado(request):
 #  return render(request,'registrado.html',{})   

@login_required
def search_venues(request):
  if request.method == "POST":
    searched = request.POST['searched']
    venues = Post.objects.filter(title__contains=searched)
    return render(request, 'search_venues.html', {'searched' : searched, 'venues': venues })
  
  else:
    return render(request, 'search_venues.html', {})
  
#Vista Creada para registrarse en el Blog

def signin(request):
  
  if request.method == 'POST':
    form = AuthenticationForm(request,data=request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
               
      user = authenticate(username = username, password = password)
               
      if user is not None:
        login(request,user)
        return render(request, 'loggedin.html')
      else:                        
        return render(request, 'inicio_sesion.html',{'form':form,'Msj':'No se autentico'})
    else:           
      return render(request, 'inicio_sesion.html',{'form':form,'Msj':'No se autentico'})
   
     
  else: 
    form = AuthenticationForm()    
    return render(request,'inicio_sesion.html',{'form':form, 'msj':''})
  
  
  
  
def register(request):
      
      if request.method == 'POST':
            form = nuestracreacionuser(request.POST)
            
            if form.is_valid():
                 username = form.cleaned_data['username'] 
                 form.save()
                 return render(request,'registered.html', {'msj': f'Se creo el user {username}'})
            else:
                 return render(request,'register.html', {'form':form, 'msj':'',}) 
      
      form = nuestracreacionuser()
      return render(request,'register.html',{'form':form, 'msj':'',})
      

@login_required
def edit(request):
    msj = ''
       
    if request.method =='POST':
          form = nuestraedicionuser(request.POST)
          
          if form.is_valid():
                
                data = form.cleaned_data()
                
                logued_user = request.user
                logued_user.email = data.get('email','')
                logued_user.first_name = data.get('first_name','')
                logued_user.last_name = data.get('last_name','')
            
                
                if data.get('pasword1') == data.get('pasword2') and len(data.get('pasword1')) > 8:
                      logued_user.set_password(data.get('pasword1'))
                else:
                      msj = 'Error en la Password'
                
                logued_user.save()
                
                return render(request,'index.html',{'msj':'msj'})
          else:
                return render(request,'edit_user.html',{'form':form, 'msj':'',})
          
    form = nuestraedicionuser()
    return render(request,'edit_user.html',{'form':form, 'msj':'',})
          
      
#def buscar_url_avatar(user):
  #return Avatar.objects.filter(user=user)[0].imagen.url 
 
# 'user_avatar_url': buscar_url_avatar(request.user)