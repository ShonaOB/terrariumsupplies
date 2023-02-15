from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog.html'


@login_required
def add_post(request):
    """
    adding a blog post
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry"
                       "you need to be an administrator to do this!")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Great! Your blog post is successfully posted')
            return redirect(reverse('home'))
        else:
            messages.error(request, "Uh oh!"
                           "There was an error. Please check your form.")
    else:
        form = PostForm()

    form = PostForm()
    template = 'add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
