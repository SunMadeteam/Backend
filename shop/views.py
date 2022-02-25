from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import Category, Product,Cart, Cart_detail,Delivery, Order, Order_detail, Favorites
from .serializer import CategorySerializer, ProductSerializer,CartSerializer, Cart_detailSerializer,DeliverySerializer, OrderSerializer, Order_detailSerializer, FavoritesSerializer

class Product_DetailView(APIView):
    def get(self, request, pk):
        serializer = get_object_or_404(Product.objects.all(), pk=pk)
        #return Response({"id": serializer.id,'name':serializer.name, 'user': str(request.user), 'auth': str(request.auth)})
        return Response({"id": serializer.id,"name":serializer.name, "complexity_of_care": serializer.complexity_of_care, "description":serializer.description, "florist":serializer.florist.id, "price":serializer.price, "category":serializer.category.id,"hight":serializer.hight, "image":serializer.image,'user': str(request.user), 'auth': str(request.auth)})

class ProductView(APIView):
    def get(self, request):
        serializer = ProductSerializer(Product.objects.all(), many=True)
        return Response({"products": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})
    def post(self, request):
        product = request.data.get('product')
        # Create an article from the above data
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"success": "Product {} {} created successfully".format(product_saved.name,product_saved.id)})
    def put(self, request, pk):
        saved_product = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data.get('product')
        serializer = ProductSerializer(instance=saved_product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({
            "success": "Product '{}' updated successfully".format(product_saved.name)
        })
    def delete(self, request, pk):
        # Get object with this pk
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response({
            "message": "Product with id `{}` has been deleted.".format(pk)
        }, status=204)
        
class CategoryView(APIView):
    def get(self, request):
        serializer=CategorySerializer(Category.objects.all(), many=True)
        return Response({"categories": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})
    def post(self, request):
        category = request.data.get('category')
        # Create an article from the above data
        serializer = CategorySerializer(data=category)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"success": "Category '{}' created successfully".format(category_saved.name)})
    def put(self, request, pk=None):
        saved_category = get_object_or_404(Category.objects.all(), pk=pk)
        data = request.data.get('category')
        serializer = CategorySerializer(instance=saved_category, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({
            "success": "Category '{}' updated successfully".format(category_saved.name)
        })
    def delete(self, request, pk):
        # Get object with this pk
        category = get_object_or_404(Category.objects.all(), pk=pk)
        category.delete()
        return Response({
            "message": "Category with id `{}` has been deleted.".format(pk)
        }, status=204)

class FavoritesView(APIView):
    def get(self, request):
        serializer=FavoritesSerializer(Favorites.objects.all(), many=True)
        return Response({"Favorites": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})

    def post(self, request):
        favorites = request.data.get('favorites')
        # Create an article from the above data
        serializer = FavoritesSerializer(data=favorites)
        if serializer.is_valid(raise_exception=True):
            favorites_saved = serializer.save()
        return Response({"success": "{} liked {}".format(favorites_saved.user, favorites_saved.product)})
    '''
    def put(self, request, pk):
        saved_favorites = get_object_or_404(Favorites.objects.all(), pk=pk)
        data = request.data.get('favorites')
        serializer = FavoritesSerializer(instance=saved_favorites, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            favorites_saved = serializer.save()
        return Response({
            "success": "Favorites '{}' updated successfully".format(favorites_saved.author)
        })
    '''
    def delete(self, request, pk):
        # Get object with this pk
        favorites = get_object_or_404(Favorites.objects.all(), pk=pk)
        Favorites.delete()
        return Response({
            "message": "Favorites with id `{}` has been deleted.".format(pk)
        }, status=204)


class DeliveryView(APIView):
    def get(self, request):
        serializer=DeliverySerializer(Delivery.objects.all(), many=True)
        return Response({"Delivery": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})

    def post(self, request):
        delivery = request.data.get('delivery')
        # Create an article from the above data
        serializer = DeliverySerializer(data=delivery)
        if serializer.is_valid(raise_exception=True):
            delivery_saved = serializer.save()
        return Response({"success": "{} deliver".format(delivery_saved.runner.name)})
    
    def put(self, request, pk):
        saved_delivery = get_object_or_404(Delivery.objects.all(), pk=pk)
        data = request.data.get('delivery')
        serializer = DeliverySerializer(instance=saved_delivery, data=data, partial=True)
        if delivery.is_valid(raise_exception=True):
            delivery_saved = serializer.save()
        return Response({
            "success": "Delivery '{}' updated successfully".format(delivery_saved.author)
        })
    
    def delete(self, request, pk):
        # Get object with this pk
        delivery = get_object_or_404(Delivery.objects.all(), pk=pk)
        Delivery.delete()
        return Response({
            "message": "Delivery with id `{}` has been deleted.".format(pk)
        }, status=204)

class CartView(APIView):
    def get(self, request):
        serializer=CartSerializer(Cart.objects.all(), many=True)
        return Response({"cart": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})
    def post(self, request):
        cart = request.data.get('cart')
        # Create an article from the above data
        serializer = CartSerializer(data=cart)
        if serializer.is_valid(raise_exception=True):
            cart_saved = serializer.save()
        return Response({"success": "Cart '{}' created successfully".format(cart_saved.id)})
    def put(self, request, pk):
        saved_cart = get_object_or_404(Cart.objects.all(), pk=pk)
        data = request.data.get('cart')
        serializer = CartSerializer(instance=saved_cart, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            cart_saved = serializer.save()
        return Response({
            "success": "Cart '{}' updated successfully".format(cart_saved.id)
        })
    def delete(self, request, pk):
        # Get object with this pk
        cart = get_object_or_404(Cart.objects.all(), pk=pk)
        cart.delete()
        return Response({
            "message": "Cart with id `{}` has been deleted.".format(pk)
        }, status=204)

class Cart_detailView(APIView):
    def get(self, request):
        serializer=Cart_detailSerializer(Cart_detail.objects.all(), many=True)
        return Response({"cart_detail": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})

    def post(self, request):
        cart_detail = request.data.get('cart_detail')
        # Create an article from the above data
        serializer = Cart_detailSerializer(data=cart_detail)
        if serializer.is_valid(raise_exception=True):
            cart_detail_saved = serializer.save()
        return Response({"success": "Cart_detail '{}' created successfully".format(cart_detail_saved.product)})
    
    def put(self, request, pk):
        saved_cart_detail = get_object_or_404(Cart_detail.objects.all(), pk=pk)
        data = request.data.get('cart_detail')
        serializer = Cart_detailSerializer(instance=saved_cart_detail, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            cart_detail_saved = serializer.save()
        return Response({
            "success": "Cart_detail '{}' updated successfully".format(cart_detail_saved.product)
        })
    
    def delete(self, request, pk):
        # Get object with this pk
        cart_detail = get_object_or_404(cart_detail.objects.all(), pk=pk)
        cart_detail.delete()
        return Response({
            "message": "Cart_detail with id `{}` has been deleted.".format(pk)
        }, status=204)


class OrderView(APIView):
    def get(self, request):
        serializer=OrderSerializer(Order.objects.all(), many=True)
        return Response({"order": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})
    def post(self, request):
        order = request.data.get('order')
        # Create an article from the above data
        serializer = OrderSerializer(data=order)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Order '{}' created successfully".format(order_saved.id)})
    def put(self, request, pk):
        saved_order = get_object_or_404(Order.objects.all(), pk=pk)
        data = request.data.get('order')
        serializer = OrderSerializer(instance=saved_order, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({
            "success": "Order '{}' updated successfully".format(order_saved.id)
        })
    def delete(self, request, pk):
        # Get object with this pk
        order = get_object_or_404(Order.objects.all(), pk=pk)
        order.delete()
        return Response({
            "message": "Order with id `{}` has been deleted.".format(pk)
        }, status=204)

class Order_detailView(APIView):
    def get(self, request):
        serializer=Order_detailSerializer(Order_detail.objects.all(), many=True)
        return Response({"order_detail": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})

    def post(self, request):
        order_detail = request.data.get('order_detail')
        # Create an article from the above data
        serializer = Order_detailSerializer(data=order_detail)
        if serializer.is_valid(raise_exception=True):
            order_detail_saved = serializer.save()
        return Response({"success": "Order_detail '{}' created successfully".format(order_detail_saved.product)})
    
    def put(self, request, pk):
        saved_order_detail = get_object_or_404(Order_detail.objects.all(), pk=pk)
        data = request.data.get('order_detail')
        serializer = Order_detailSerializer(instance=saved_order_detail, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            order_detail_saved = serializer.save()
        return Response({
            "success": "Order_detail '{}' updated successfully".format(order_detail_saved.product)
        })
    
    def delete(self, request, pk):
        # Get object with this pk
        order_detail = get_object_or_404(order_detail.objects.all(), pk=pk)
        order_detail.delete()
        return Response({
            "message": "Order_detail with id `{}` has been deleted.".format(pk)
        }, status=204)