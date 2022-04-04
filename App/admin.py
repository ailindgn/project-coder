from django.contrib import admin
from .models import Avatar


# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'status', 'created_on')
  list_filter = ('status',)
  search = ['title', 'content']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

admin.site.register(Avatar)



