'''from shop.models import Cart, Delivery, Product, Order_detail
from account.models import User
from django.shortcuts import render, get_object_or_404

class Logic:
    def get_salary(self, usertype, id):
    if usertype=='florist' and Order_detail__order__status!=null:
        salary=salary+Product.objects.all(Order_detail__product__florist=id).price*0.15
    if usertype=='runner' and Delivery.objects.get()status=='completed':
        salary=salary+Delivery.total_cost*0.1
    return salary