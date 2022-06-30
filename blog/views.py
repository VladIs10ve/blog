from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home(request):
    return render(request, "lvlup/base.html")


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        context = {'form': form}

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created')
                return redirect('/')
            else:
                messages.error(request, 'Try Again')

        return render(request, "lvlup/registration.html", context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'User not found')

        return render(request, "lvlup/login.html")


def logout_user(request):
    logout(request)
    return redirect('/login')
