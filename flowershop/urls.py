"""flowershop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from account import views as account_views
from shop import views as shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('api1/v1/register/', account_views.RegisterAPIView.as_view()),
    path('api1/v1/registerstaff/', account_views.RegisterStaffAPIView.as_view()),
    path('api1/v1/login/', account_views.LoginAPIView.as_view()),

    path('api/products/', shop_views.ProductView.as_view()),
    path('api/categories/', shop_views.CategoryView.as_view()),
    path('api/cart/', shop_views.CartView.as_view()),
    path('api/cart_detail/', shop_views.Cart_detailView.as_view()),
    path('api/order/', shop_views.OrderView.as_view()),
    path('api/order_detail/', shop_views.Order_detailView.as_view()),
    path('api/favorites/', shop_views.FavoritesView.as_view()),
    path('api/delivery/', shop_views.DeliveryView.as_view()),
    #path('products/<int:pk>', shop_views.ProductView.as_view(), name='product')
]