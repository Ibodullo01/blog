from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Blog, Comments

User = get_user_model()
class LoginForm(forms.Form):
    phone = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=100, error_messages={'exists': 'Username is already exists.'})
    class Meta:
        model = User
        fields = ('email', 'password1')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            # 'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
