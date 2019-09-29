from django.shortcuts import render, redirect, reverse
from django.views import View, generic
from django.views.generic import edit, CreateView
from django.contrib import messages

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
            messages.success(request, f'{email} accout successfully created. Sin In and enjoy.')
            return redirect('users:login')

        form = UserRegisterForm()
        messages.error(request, f'pleas check your infos and try again.')
        return render(request, 'users/register.html', {'form':form})


class CreateProfile(View):

    def get(self, request):
        if request.user.profile:
            url = 'main:home'
            return redirect(url)
        else:
            form = ProfileForm()
            return render(request, 'users/profile_create.html', {'form':form})
    
    def post(self, request):
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.instance.owner = request.user
                form.save()
                messages.success(request, f'Your profile is now created, you can update it at anytime.')
                return reverse('main:home')
            
            form = ProfileForm()
            messages.error(request, f'you have to complete the form')
        return render(request, 'users/profile_create.html', {'form':form})


class ProfileView(generic.DetailView):

    model = User
    template_name = 'users/profile.html'
    context_object_name = 'profile_user'
    