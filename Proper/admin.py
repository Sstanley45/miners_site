from django.contrib import admin

from .models import Mineral, Seller, Buyer

# Register your models here.
admin.site.register(Mineral)
admin.site.register(Seller)

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bought_from')
    list_filter = ('bought_from',)

    