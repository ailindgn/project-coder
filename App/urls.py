from random import random
from . import views
from django.urls import path
##from .views import numero_random ##prueba
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.DetailView.as_view(), name= 'post_detail'),
    path('signin/add_post', views.AddPostView.as_view(), name = 'add_post'),
    path('logout/', views.PostList.as_view(), name='logout'), 
    path('signin/?next=/post/edit/<slug:slug>', views.UpdatePostView.as_view(), name= 'update_post'),
    #no nos puestra el Update view después del sign in! No logramos que redirija ahí
    path('add_post/', views.AddPostView.as_view(), name = 'add_post'),
    path('post/edit/<slug:slug>', views.UpdatePostView.as_view(), name= 'update_post'),
    path('add_category/', views.AddCategoryView.as_view(), name = 'add_category'),
    path('search_venues/', views.search_venues, name='search_venues'),
    path('about_us/', views.about_us, name= 'about_us'),
    path('signin/', views.signin, name='signin'),
    path('logged/', LogoutView.as_view(template_name='loggedout.html'), name='logout'),
    #no logramos que vuelva al home!
    path('register/', views.register, name='register'),
    #path('registrado/', views.registrado, name='registrado'),
    path('edit/', views.edit, name='edit'),
    path('post/remove/<slug:slug>', views.DeletePostView.as_view(template_name = 'delete_post.html'), name='delete_post')

]
