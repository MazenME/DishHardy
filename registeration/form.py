from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput



# user registeration form
class UserCreateForm(UserCreationForm):

    ROLE_CHOICES = [('user', 'User'), ('admin', 'Admin')]

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    username = forms.CharField(
        max_length=100,
        
    )
    email = forms.EmailField(
        max_length=255,
        
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput,
       
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
       
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role'] 


# user login form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput()        
    )
    password = forms.CharField(
        widget=PasswordInput()
    )

