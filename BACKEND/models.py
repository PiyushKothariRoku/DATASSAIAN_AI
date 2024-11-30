from django.db import models
from django.utils import timezone
import uuid

class Maps(models.Model):
    maps_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    is_for_sale = models.BooleanField(default=False)
    maps_length = models.IntegerField()
    maps_width = models.IntegerField()
    Registered_date = models.DateTimeField(default=timezone.now)
    maps_name = models.CharField(max_length=100)

    def __str__(self):
        return self.maps_name

class Owner(models.Model):
    owner_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    owner_name = models.CharField(max_length=10, default='Unknown')
    owner_middle_name = models.CharField(max_length=10, default='Unknown')
    owner_last_name = models.CharField(max_length=10, default='Unknown')
    owner_address = models.CharField(max_length=200, default='Unknown')
    owner_pan = models.CharField(max_length=10, default='Unknown')
    owner_Addhar = models.CharField(max_length=10, default='Unknown')
    Token_money = models.CharField(max_length=10, default='0')
    total_maps_owned = models.IntegerField(default=0)
    total_expends = models.IntegerField(default=0)

    def __str__(self):
        return self.owner_name

class Seller(models.Model):
    seller_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    seller_name = models.CharField(max_length=10, default='Unknown')
    seller_middle_name = models.CharField(max_length=10, default='Unknown')
    seller_last_name = models.CharField(max_length=10, default='Unknown')
    seller_address = models.CharField(max_length=200, default='Unknown')
    seller_pan = models.CharField(max_length=10, default='Unknown')
    seller_Addhar = models.CharField(max_length=10, default='Unknown')
    Token_money = models.CharField(max_length=10, default='0')
    total_maps_owned = models.IntegerField(default=0)
    total_earnings = models.IntegerField(default=0)

    def __str__(self):
        return self.seller_name

class SelledMapsOwner(models.Model):
    maps = models.ForeignKey(Maps, on_delete=models.CASCADE, to_field='maps_id', null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    Registered_date = models.DateTimeField(default=timezone.now)
    Token_money = models.CharField(max_length=10, default='0')
    total_maps_owned = models.IntegerField(default=0)
    total_earnings = models.IntegerField(default=0)
    seller_owner_maps_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return f"{self.owner.owner_name} - {self.seller.seller_name} - {self.maps.maps_name}"

    def save(self, *args, **kwargs):
        super(SelledMapsOwner, self).save(*args, **kwargs)
