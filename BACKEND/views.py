from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, MapsForm, OwnerForm, SellerForm, SelledMapsOwnerForm
from .models_pymongo import Maps, Owner, Seller, SelledMapsOwner
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
            data = form.cleaned_data
            maps = Maps(
                maps_name=data['maps_name'],
                maps_length=data['maps_length'],
                maps_width=data['maps_width'],
                is_for_sale=data['is_for_sale']
            )
            maps.save()
            return redirect('success')
    else:
        form = MapsForm()
    return render(request, 'register_maps.html', {'form': form})

@login_required
def register_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            owner = Owner(
                owner_name=data['owner_name'],
                owner_middle_name=data.get('owner_middle_name', 'Unknown'),
                owner_last_name=data['owner_last_name'],
                owner_address=data['owner_address'],
                owner_pan=data['owner_pan'],
                owner_addhar=data['owner_addhar']
            )
            owner.save()
            return redirect('success')
    else:
        form = OwnerForm()
    return render(request, 'register_owner.html', {'form': form})

@login_required
def register_seller(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            seller = Seller(
                seller_name=data['seller_name'],
                seller_middle_name=data.get('seller_middle_name', 'Unknown'),
                seller_last_name=data['seller_last_name'],
                seller_address=data['seller_address'],
                seller_pan=data['seller_pan'],
                seller_addhar=data['seller_addhar']
            )
            seller.save()
            return redirect('success')
    else:
        form = SellerForm()
    return render(request, 'register_seller.html', {'form': form})

@login_required
def register_deal(request):
    if request.method == 'POST':
        form = SelledMapsOwnerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            deal = SelledMapsOwner(
                maps_id=data['maps_id'],
                owner_id=data['owner_id'],
                seller_id=data['seller_id'],
                token_money=data['token_money']
            )
            deal.save()
            return redirect('success')
    else:
        form = SelledMapsOwnerForm()
    return render(request, 'register_deal.html', {'form': form})

def success(request):
    return render(request, 'success.html')
