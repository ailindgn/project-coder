from django.contrib import admin


# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'status', 'created_on')
  list_filter = ('status',)
  search = ['title', 'content']

admin.site.register(Post, PostAdmin)