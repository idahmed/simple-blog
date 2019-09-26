from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import UserRegisterForm


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