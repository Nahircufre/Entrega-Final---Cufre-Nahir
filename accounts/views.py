from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from .forms import ProfileForm, UserEditForm



def signup(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, "Usuario creado correctamente ✅")
            return redirect('index')

    return render(request, 'accounts/signup.html', {'form': form})



def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    return render(request, 'accounts/login.html', {'form': form})



@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, 'accounts/profile.html', {
        'profile': profile
    })



@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, "Perfil actualizado correctamente ✅")
            return redirect('profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })