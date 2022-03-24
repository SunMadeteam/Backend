from account.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
import datetime
from django.utils import timezone
         
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.TextField(default=None, null=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    image = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    CHOICES = (('easy','easy'),('middle','middle'), ('hard','hard'))
    complexity_of_care= models.CharField(choices=CHOICES, default=None, null=True, max_length=20)
    florist = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    hight= models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True, blank=True)
    quantity= models.IntegerField(null=True, default=None)
    #def get_absolute_url(self):
    #    return reverse('shop:product_list_by_category', args=[self.slug])

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'name'),)

    def str(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_sum=models.IntegerField(default=0)
    
    @property
    def total_sum(self):
        Cart.objects.filter(pk=cart_detail.pk).aggregate(total_sum=sum(cart_detail__product.price*quantity))
        print(total_sum)
        total_sum=2
        return total_sum

class Cart_detail(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    CHOICES = (('new','new'),('processed','processed'), ('completed','completed'))
    status=models.CharField(choices=CHOICES, default=None, null=True, max_length=20)
    total_sum=models.IntegerField(default=0)
    date=models.DateField(auto_now_add=True, null=True)
    

class Order_detail(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, default=None, null=True)
    quantity= models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Delivery(models.Model):
    adress = models.TextField()
    runner = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost= models.IntegerField(default=None, null=True)
    CHOICES = (('accepted','accepted'), ('took','took'), ('completed','completed'), ('on the way', 'on the way'), ('delivered','delivered'), ('completed', 'completed'))
    status=models.CharField(choices=CHOICES, default=None, null=True,max_length=20)
    date=models.DateField(auto_now_add=True, null=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, default=None, null=True)
    number = models.CharField(max_length=13, blank=True, null=True)

class Favorites(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)