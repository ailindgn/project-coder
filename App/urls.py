from random import random
from . import views
from django.urls import path
##from .views import numero_random ##prueba

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.DetailView.as_view(), name= 'post_detail'),
    path('add_post/', views.AddPostView.as_view(), name = 'add_post'),
    path('post/edit/<slug:slug>', views.UpdatePostView.as_view(), name= 'update_post'),
    path('add_category/', views.AddCategoryView.as_view(), name = 'add_category'),
    path('search_venues/', views.search_venues, name='search_venues'),
]
