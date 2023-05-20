from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .UserRegistrationForm import UserRegistrationForm

# Create your views here.
class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('user-profile')
