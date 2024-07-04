from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from forumapp.forms import RegistrationForm, RegistrationForm, AuthenticationUserForm
from forumapp.models import User


# Create your views here.
def login(request: HttpRequest):
    return render(request, 'login.html')


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    extra_context = {'title': 'Registration'}
    success_url = reverse_lazy("login")


class LoginUserView(LoginView):
    form_class = AuthenticationUserForm
    template_name = 'login.html'
    extra_context = {'title': 'Login'}

    def get_success_url(self):
        re = self.request.user.username
        return reverse_lazy('home', kwargs={'username': re})


def home(request: HttpRequest, username: str = "New User"):
    return render(request, 'home.html', context={"username": username})


def start(request: HttpRequest):
    return render(request, 'home.html')
