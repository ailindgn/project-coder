from enum import unique
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
  title = models.CharField(max_length = 200, unique = True)
  slug = models.SlugField(max_length = 200, unique = True)
  author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts') #para que si se elimina un autor, elimine todos los posts del autor
  created_on = models.DateTimeField(auto_now_add = True) #día actual
  updated_on = models.DateTimeField(auto_now = True) #el día que se modificó
  content = models.TextField()
  status = models.IntegerField(choices = STATUS, default = 0)
  
  class Meta:
      ## Metadata para ordenar posts con django en orden descendiente
    ordering = ['-created_on']
    

  def __str__(self):
      return self.title
    
  def get_absolute_url(self):
      return reverse(
        viewname="post_detail", kwargs= {'slug': self.slug} )
  
