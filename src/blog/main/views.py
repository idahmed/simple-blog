from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View, generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)


from .models import Post
from .forms import PostForm, CommentForm

class Home(View):
    """
    main page view.
    """

    def get(self, request):
        form = PostForm()
        posts = Post.objects.all().order_by('-created_date')
        return render(request, 'main/home.html', {'form':form, 'posts':posts})

    @method_decorator(login_required)
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.owner = request.user
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'{title} post has been published.')
            return redirect('main:home')
        else:
            form = PostForm()
            messages.error(request, 'Ops! Something went wrong, Pleas try again later.')
        return render(request, 'main/home.html', {'form':form})


class PostDetails(View):
    """
    view details of a specific post.
    """
    def get(self, request, pk):
        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'main/post_details.html', {'form':form, 'post':post})

    @method_decorator(login_required)
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        
        if form.is_valid():
            form.save(commit=False)
            form.instance.owner = request.user
            form.instance.post = post
            form.save()
            return redirect(f'/blog/post/{pk}')