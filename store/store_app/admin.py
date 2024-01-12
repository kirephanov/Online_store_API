from django.contrib import admin
from .models import *


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket_user')
    list_display_links = ('id', 'basket_user')
    search_fields = ('basket_user',)


class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket_item_basket', 'basket_item_product', 'basket_item_quantity')
    list_display_links = ('id', 'basket_item_basket', 'basket_item_product', 'basket_item_quantity')


admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketItem, BasketItemAdmin)
