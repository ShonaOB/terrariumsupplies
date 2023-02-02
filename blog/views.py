from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all.order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 12
