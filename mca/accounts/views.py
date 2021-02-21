from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import reverse_lazy
from django.views import generic
from .forms import ProfileForm

class SignUpView(generic.CreateView):
    form_class = ProfileForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'