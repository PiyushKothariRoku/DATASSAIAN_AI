from django import forms
from .models import Maps, Owner, Seller, SelledMapsOwner
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class MapsForm(forms.ModelForm):
    class Meta:
        model = Maps
        fields = ['maps_name', 'is_for_sale', 'maps_length', 'maps_width', 'Registered_date']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['owner_name', 'owner_middle_name', 'owner_last_name', 'owner_address', 'owner_pan', 'owner_Addhar', 'Token_money', 'total_maps_owned', 'total_expends']

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['seller_name', 'seller_middle_name', 'seller_last_name', 'seller_address', 'seller_pan', 'seller_Addhar', 'Token_money', 'total_maps_owned', 'total_earnings']

class SelledMapsOwnerForm(forms.ModelForm):
    class Meta:
        model = SelledMapsOwner
        fields = ['maps', 'owner', 'seller', 'Registered_date', 'Token_money', 'total_maps_owned', 'total_earnings']
