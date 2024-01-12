from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = ['url', 'id', 'product_title', 'product_price',
                  'product_discount', 'product_total_cost', 'product_photo', 
                  'product_description', 'product_specifications', 'product_delivery',
                  'product_seller', 'owner', 'product_category']


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_title = serializers.CharField(required=False, allow_blank=True, max_length=150)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.category_title = validated_data.get('category_title', instance.category_title)
        instance.save()
        return instance
    

class SellerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    seller_title = serializers.CharField(required=False, allow_blank=True, max_length=150)

    def create(self, validated_data):
        return Seller.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.seller_title = validated_data.get('seller_title', instance.seller_title)
        instance.save()
        return instance


class BasketItemSerializer(serializers.HyperlinkedModelSerializer):
    basket_item_basket = serializers.ReadOnlyField(source='basket_item_basket.basket_user.username')

    class Meta:
        model = BasketItem
        fields = ['url', 'id', 'basket_item_basket', 'basket_item_product',
                  'basket_item_quantity']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', 
                                                  read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'product']