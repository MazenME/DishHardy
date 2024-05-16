from django.shortcuts import render,redirect
from . form import UserCreateForm,UserLoginForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Profile
from django.contrib.auth.decorators import login_required





# Create your views here.

def register(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the User instance and get it back
            role = form.cleaned_data.get('role')  # Get the role from the form
            Profile.objects.create(user=user, role=role)  # Create the Profile instance with the role
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'registerr.html', context)



# def register(request):
#     form = UserCreateForm()

#     if request.method == 'POST':
#         form = UserCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = UserCreateForm()
#             return redirect('login')

#     context = {
#         'form': form
#     }
#     return render(request, 'register.html', context)

# def login_user(request):
#     form = UserLoginForm()
    
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
            
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect('view_recipes')
            
#     context = {
#         'form': form
#     }
#     return render(request, 'login.html', context)

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if user.profile.role == 'admin':
                    return redirect('homeadmin')  
                else:
                    return redirect('homeuser') 
    else:
        form = UserLoginForm()
    
    return render(request, 'loginn.html', {'form': form})


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def homeuser(request):
    return render(request,'homeUser.html')


@login_required(login_url='login')
def homeadmin(request):
    return render(request,'home.html')

