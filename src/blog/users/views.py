from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View, generic
from django.views.generic import edit, CreateView
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import UserRegisterForm, ProfileForm
from .models import Profile, User

class Register(View):
    """
    register view.
    """

    def get(self, request):
        if request.user.is_authenticated:
            messages.success(request, 'You already logged in!')
            return redirect('main:home')
        form = UserRegisterForm()
        message = 'Hello , you are more than welcomed to join us and shear with us the beautiful experiences and moments.'
        return render(request, 'users/register.html', {'message':message, 'form':form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            user = User.objects.get(email=email)
            Profile.objects.create(owner=user)
            messages.success(request, f'{email} accout successfully created. Sin In and enjoy.')
            return redirect('login')

        form = UserRegisterForm()
        messages.error(request, f'pleas check your infos and try again.')
        return render(request, 'users/register.html', {'form':form})


class ProfileView(View):

    def get(self, request, email):
        usr = get_object_or_404(User, email=email)
        profile = usr.profile
        if request.user == usr:
            form = ProfileForm(
                request.POST or None,
                request.FILES or None,
                instance = profile
            )
            return render(request, 'users/profile.html', {'profile': profile, 'form': form})
        
        return render(request, 'users/profile.html', {'profile': profile})
    
    @method_decorator(login_required)
    def post(self, request, email):
        usr = get_object_or_404(User, email=email)
        if request.user == usr:
            profile = usr.profile
            form = ProfileForm(
                request.POST or None,
                request.FILES or None,
                instance = profile)
            if form.is_valid():
                form.save()
                messages.success(request, f'Profile updated success.')
                return render(request, 'users/profile.html', {'profile': profile, 'form': form})