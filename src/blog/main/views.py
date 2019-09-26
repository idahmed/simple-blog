from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

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

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.owner = self.request.user
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'{title} post has been published.')
            return redirect('main:home')
        else:
            form = PostForm()
            messages.error(request, 'Ops! Something went wrong, Pleas try again later.')
        return render(request, 'main/home.html', {'form':form})