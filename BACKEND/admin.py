from django.contrib import admin
from .models import Maps, Owner, Seller, SelledMapsOwner

class SelledMapsOwnerAdmin(admin.ModelAdmin):
    list_display = ('maps', 'owner', 'seller', 'Registered_date', 'Token_money', 'total_maps_owned', 'total_earnings')

    def get_form(self, request, obj=None, **kwargs):
        form = super(SelledMapsOwnerAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['maps'].widget.can_add_related = False
        form.base_fields['owner'].widget.can_add_related = False
        form.base_fields['seller'].widget.can_add_related = False
        return form

    def save_model(self, request, obj, form, change):
        if obj.maps:
            obj.maps_length = obj.maps.maps_length
            obj.maps_width = obj.maps.maps_width
        super().save_model(request, obj, form, change)

admin.site.register(Maps)
admin.site.register(Owner)
admin.site.register(Seller)
admin.site.register(SelledMapsOwner, SelledMapsOwnerAdmin)
