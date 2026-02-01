from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_user

from .forms import RegisterForm


# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    ctx = {"form": form}

    if form.is_valid():
        form.save()

        username = form.cleaned_data.get("username")
        messages.success(
            request, f"Добро пожаловать {username}! Ваш аккаунт был усспешно создан!"
        )

        return redirect("users:login")

    return render(request, "users/register.html", ctx)


def logout(request):
    logout_user(request)

    return render(request, "users/logout.html")
