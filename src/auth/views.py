from django.contrib import messages
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from auth import services
from auth.errors import InvalidCredentials
from auth.forms import RegistrationForm, LoginForm
from users.services import user_create


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('users:me'))
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user_create(email=form.cleaned_data['email'],
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'])
        messages.info(request, 'Account successfully created.')
        return redirect('auth:login')
    return render(request, 'auth/register.html', {
        'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('users:me'))
    form = LoginForm(request.POST or None)
    if form.is_valid():
        try:
            user = services.login(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
        except InvalidCredentials as e:
            messages.error(request, str(e))
            return redirect('auth:login')
        django_login(request, user)
        next = request.GET.get('next', None)
        return redirect(next or reverse('users:me'))
    return render(request, 'auth/login.html', {
        'form': form})


@login_required
def logout(request):
    django_logout(request)
    return redirect(reverse('auth:login'))
