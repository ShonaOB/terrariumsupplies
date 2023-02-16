from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog.html'


class AddPost(LoginRequiredMixin, generic.CreateView):
    """
    adding a blog post
    """
    model = Post
    template_name = 'add_post.html'
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog')


def post_detail(request, post_id):
    """ A view to show individual post """

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'post_detail.html', context)


@login_required
def edit_post(request, post_id):
    """ A view to edit an existing post"""
    if not request.user.is_superuser:
        messages.error(requests, "Sorry"
                       "You need to be an administrator to do this!")
        return redirect(reverse('home'))
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated blog post')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            form = PostForm(instance=post)
            messages.info(request, 'Failed to update post.'
                          'Please check your form and try again.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.id}')

    template = 'edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, "Sorry,"
                       "you need to be an administrator to do this!")
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted')

    return redirect(reverse('blog'))
