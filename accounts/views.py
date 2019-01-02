from django.shortcuts import render
import django.contrib.auth.views as auth_views
from .forms import *
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.conf import settings

User = settings.AUTH_USER_MODEL


class MyLoginView(auth_views.LoginView):
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['local_css'] = ['css/myforms.css']
        return context


class MySignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = '/view/all/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['local_css'] = ['css/myforms.css']
        return context
