from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Category, Product,Cart, Cart_detail,Delivery, Order, Order_detail, Favorites
import datetime

class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.complexity_of_care = validated_data.get('complexity_of_care', instance.complexity_of_care)
        instance.image = validated_data.get('image', instance.image)
        instance.florist = validated_data.get('florist', instance.florist)
        instance.hight = validated_data.get('hight', instance.hight)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

    class Meta:
        model=Product
        fields = ('id', 'name','complexity_of_care','description','florist','price','category', 'hight', 'image')


class DeliverySerializer(serializers.ModelSerializer):
    '''
    def validate(self, data):
        data['date'] = datetime.now()
        return data
    '''
    def create(self, validated_data):
        return Delivery.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.adress = validated_data.get('adress', instance.adress)
        instance.runner = validated_data.get('runner', instance.runner)
        instance.total_cost = validated_data.get('total_cost', instance.total_cost)
        instance.status=validated_data.get('status', instance.status)
        instance.save()
        return instance

    class Meta:
        model=Delivery
        fields = ('id','adress','runner','total_cost','status', 'date')

class CategorySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image= validated_data.get('image', instance.name)
        instance.save()
        return instance
    class Meta:
        model=Category
        fields = ('id', 'name', 'image')

class Cart_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_detail 
        fields=('id','cart', 'quantity', 'product')
    def create(self, validated_data):
        return Cart_detail.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.cart = validated_data.get('cart', instance.cart)
        instance.product = validated_data.get('product', instance.product)
        instance.quantity=validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Cart.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.total_sum = validated_data.get('total_sum', instance.total_sum)
        instance.save()
        return instance
    class Meta:
        model=Cart
        fields=( 'id', 'user','total_sum')

class Order_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_detail 
        fields=('id','order', 'quantity', 'product')
    def create(self, validated_data):
        return Order_detail.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.order = validated_data.get('order', instance.order)
        instance.product = validated_data.get('product', instance.product)
        instance.quantity=validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.status=validated_data.get('status', instance.status)
        instance.total_sum = validated_data.get('total_sum', instance.total_sum)
        instance.status = validated_data.get('status', instance.status)
        instance.delivery_type = validated_data.get('delivery_type', instance.delivery_type)
        instance.delivery = validated_data.get('delivery', instance.delivery)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
    class Meta:
        model=Order
        fields=( 'id', 'user','total_sum', 'delivery', 'status', 'delivery_type','date')

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields=('id','user', 'product')
    def create(self, validated_data):
        return Favorites.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.product = validated_data.get('product', instance.product)
        instance.save()
        return instance


