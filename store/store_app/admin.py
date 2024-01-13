from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_title', 'product_price', 'product_discount', 
                    'product_total_cost', 'product_seller', 'owner', 
                    'product_category', 'product_photo')
    list_display_links = ('id', 'product_title', 'product_price', 'product_discount', 
                    'product_total_cost', 'product_seller', 'owner', 
                    'product_category', 'product_photo')
    search_fields = ('product_title', 'product_price', 'product_discount', 
                     'product_total_cost')
    list_filter = ('product_seller', 'product_category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_title')
    list_display_links = ('id', 'category_title')
    search_fields = ('category_title',)


class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller_title')
    list_display_links = ('id', 'seller_title')
    search_fields = ('seller_title',)


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket_user')
    list_display_links = ('id', 'basket_user')
    search_fields = ('basket_user',)


class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket_item_basket', 'basket_item_product', 'basket_item_quantity')
    list_display_links = ('id', 'basket_item_basket', 'basket_item_product', 'basket_item_quantity')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketItem, BasketItemAdmin)

admin.site.site_title = 'Online Store API'
admin.site.site_header = 'Online Store API'
