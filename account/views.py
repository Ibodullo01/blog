from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from account.forms import User, SignUpForm

User = get_user_model()

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'sign_up.html'
    success_url = '/'