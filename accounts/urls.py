from django.urls import path
from .views import *


urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("signup/", MySignupView.as_view(), name="signup"),
]
