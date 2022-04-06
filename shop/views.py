from datetime import date
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import Category, Product,Cart, Cart_detail, Delivery, Order, Order_detail, Favorites
from .serializer import CategorySerializer, ProductSerializer,CartSerializer, Cart_detailSerializer,DeliverySerializer, OrderSerializer, Order_detailSerializer, FavoritesSerializer
from django.shortcuts import get_list_or_404
from rest_framework import generics

from rest_framework import filters
from rest_framework.filters import SearchFilter
from account.models import User
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django_filters import DateFilter

from django.db.models import Count

class Product_DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()   

class ProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    search_fields = ["name"]#, "hight"]
    filterset_fields = ['hight', 'category']
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]

class Category_DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class FavoritesView(generics.ListCreateAPIView):
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()


class DateFilterOrder(django_filters.FilterSet):
    start_date=DateFilter(field_name='date' , lookup_expr=('gte'))
    end_date=DateFilter(field_name='date', lookup_expr=('lte'))
    class Meta:
        model= Order
        fields=['date', 'status']

class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    search_fields = ["user__number"]#, "status"]
    filterset_fields = ['status', 'date']
    filter_class = DateFilterOrder
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]
'''    def get(self, request):
        serializer=OrderSerializer(Order.objects.all().values_list('user__number', 'user__name'), many=True)
        return Response({"order": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})
'''

class DeliveryUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all() 
    
class DateFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name='date', lookup_expr=('gte'),)
    end_date=DateFilter(field_name='date', lookup_expr=('lte'))
    class Meta:
        model = Delivery
        fields = ['date', 'status', 'runner__id' ]


class Delivered_by(generics.ListCreateAPIView):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all()
    filter_class = DateFilter
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]
    
    def get(self, request, pk):
        serializer = DeliverySerializer(Delivery.objects.all().filter(runner=pk), many=True)
        d=Delivery.objects.values('date').annotate(delivery_count=Count('id'))
        
        return Response({"deliveries": d, 'user': str(request.user), 'auth': str(request.auth)})


class DeliveryView(generics.ListCreateAPIView):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all()
    search_fields = ["order__user__number", "order__id"]
    filterset_fields = ['status', 'date', 'runner__id']
    filter_class = DateFilter
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]
    def post(self, request):
        order=get_object_or_404(Order.objects.all(),pk=request.data.get('order'))
        #print(order)
        runner=get_object_or_404(User.objects.all(), pk=request.data.get('runner'))
        runner.salary+=order.total_sum/10
        order_detail=Order_detail.objects.filter(order__pk=order.pk)
        #print(order_detail)
        for i in order_detail:
            i.product.florist.salary+=i.product.price*15/100
            i.product.florist.save()
            #print(i.product.florist.salary)
        runner.save()
        #print('{}: {}'.format(runner.id,runner.salary))
        return Response({'Delivery': ''})

class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class Cart_detailView(generics.ListCreateAPIView):
    serializer_class = Cart_detailSerializer
    queryset = Cart_detail.objects.all()

#class TotalSumCart(APIView):
@property
def total_sum(self, request, pk):
    serializer = Cart_detailSerializer(Cart_detail.objects.filter(cart__id=pk), manu=True)
    total_sum=serializer__product__price*quantity
    #print(total_sum)
    #return self.total_sum
    #return Response({"id": serializer.id,'name':serializer.name, 'user': str(request.user), 'auth': str(request.auth)})
 
class StatisticView(APIView):
    def get(self, request):
        allobj=Order_detail.objects.all().count()
        l={}
        for i in Category.objects.all():
            l[i.name]=round((Order_detail.objects.filter(product__category=i.id).count()/allobj)*100)
        print(l)
        return Response(data=l)
 
class SecondStatisticView(APIView):
    def get(self, request):
        orders=Order.objects.all()
        allobj=Order.objects.all().count()
        l={'понедельник':0, 'вторник':0, 'среда':0,'четверг':0,'пятница':0,'суббота':0,'воскресенье':0}
        for i in orders:
            l[i.date]
        print(l)
        return Response(data=l)


class OrderUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all() 

class Order_detailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Order_detailSerializer
    queryset = Order_detail.objects.all()

class Order_detailView(generics.ListCreateAPIView):
    serializer_class = Order_detailSerializer
    queryset = Order_detail.objects.all()
    filterset_fields = ['product__category__name', 'order__user__id', 'order']
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]


'''
class Product_DetailView(APIView):
    def get(self, request, pk):
        serializer = get_object_or_404(Product.objects.all(), pk=pk)
        #return Response({"id": serializer.id,'name':serializer.name, 'user': str(request.user), 'auth': str(request.auth)})
        return Response({"id": serializer.id,"name":serializer.name, "complexity_of_care": serializer.complexity_of_care, "description":serializer.description, "florist":serializer.florist.id, "price":serializer.price, "category":serializer.category.id,"hight":serializer.hight, "image":serializer.image,'user': str(request.user), 'auth': str(request.auth)})
    def delete(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response({"success": "Product delete"})

class Category_DetailView(APIView):
    def get(self, request, pk):
        serializer = ProductSerializer(Product.objects.all().filter(category=pk), many=True)
        return Response({"products": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})
    def delete(self, request, pk):
        category = get_object_or_404(Category.objects.all(), pk=pk)
        category.delete()
        return Response({"success": "Category delete"})

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
        return Response({"success": "Category '{}' '{}' created successfully".format(category_saved.name, category_saved.id)})

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
        return Response({"success": "{} delivering".format(delivery_saved.runner.name)})

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
class Delivery_by_statusView(APIView):
    def get(self, request, pk):
        serializer=DeliverySerializer(Delivery.objects.all().filter(status=pk), many=True)
        return Response({"Delivery": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})

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
'''