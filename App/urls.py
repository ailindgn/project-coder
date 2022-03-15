from random import random
from . import views
from django.urls import path
from .views import otra_vista
##from .views import numero_random ##prueba

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('', otra_vista),
    path('post/<str:slug>/', views.DetailView.as_view(), name= 'post_detail'),
    path('add_post/', views.AddPostView.as_view(), name = 'add_post'),
]
