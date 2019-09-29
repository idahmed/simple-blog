from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View, generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)


from .models import Post, Comment
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


class PostUpdate(UserPassesTestMixin, generic.edit.UpdateView):

    model = Post
    context_object_name = 'post'
    form_class = PostForm
    template_name = 'main/post_update.html'
    
    def get_success_url(self):
        return reverse("main:post", kwargs={'pk':self.get_object().pk})

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False


class PostDelete(UserPassesTestMixin, generic.edit.DeleteView):

    model = Post
    context_object_name = 'post'
    
    def get_success_url(self):
        return reverse("main:home")

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False


class CommentDelete(UserPassesTestMixin, generic.edit.DeleteView):

    model = Comment
    context_object_name = 'comment'
    

    def get_success_url(self):
        post_id = self.get_object().post.pk
        return reverse("main:post", kwargs={'pk':post_id})

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.owner:
            return True
        return False