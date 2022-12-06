from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from .forms import RegisterUserForm, EditProfileForm
from django.urls import reverse

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return redirect('home')
        else:
                messages.success(request,("Invalid input. Please try again."))
                return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,("Logged out. See you next time!"))
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            first_name= form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request,("Registration successful. Welcome to Up!"))
            return redirect('login')
    else:
        form = RegisterUserForm

    return render(request, 'authenticate/register_user.html',{'form':form,})

def view_profile(request):
    args ={'user': request.user}
    return render(request, 'profile/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,("Edit profile successful!"))
            return redirect('view_profile')

        else:
            messages.success(request,("Invalid input. Please try again!"))
            return redirect('edit-password')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profile/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,("Change password successful!"))
            return redirect('view_profile')
        else:
            messages.success(request,("Invalid input. Please try again!"))
            return redirect('change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'profile/change_password.html', args)