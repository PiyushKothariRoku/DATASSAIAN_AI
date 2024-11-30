# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, MapsForm, OwnerForm, SellerForm, SelledMapsOwnerForm
from django.contrib.auth.decorators import user_passes_test


def superuser_required(view_func):
    decorated_view_func = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url='login'
    )(view_func)
    return decorated_view_func

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Print statement to check if the user is not correct
                print("User is not correct")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@superuser_required
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def register_maps(request):
    if request.method == 'POST':
        form = MapsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MapsForm()
    return render(request, 'register_maps.html', {'form': form})

@login_required
def register_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = OwnerForm()
    return render(request, 'register_owner.html', {'form': form})

@login_required
def register_seller(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SellerForm()
    return render(request, 'register_seller.html', {'form': form})

@login_required
def register_deal(request):
    if request.method == 'POST':
        form = SelledMapsOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SelledMapsOwnerForm()
    return render(request, 'register_deal.html', {'form': form})

def success(request):
    return render(request, 'success.html')
