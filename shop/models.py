from account.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

         
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
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
    CHOICES = ((1,'easy'),(2,'middle'), (3,'hard'))
    complexity_of_care= models.IntegerField(choices=CHOICES, default=None, null=True)
    florist = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hight= models.DecimalField(decimal_places=1, max_digits=1)
    
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
        

class Cart_detail(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Delivery(models.Model):
    adress = models.TextField()
    runner = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost= models.IntegerField(default=None, null=True)
    CHOICES = ((1,'accepted'),(2,'took'), (3,'completed'), (4, 'on the way'), (5,'delivered'), (6, 'completed'))
    status=models.IntegerField(choices=CHOICES, default=None, null=True)
    CHOICES_del = ((1,'delivery'),(2,'pickup'))
    delivery_type=models.IntegerField(choices=CHOICES, default=None, null=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = ((1,'new'),(2,'processed'), (3,'completed'))
    status=models.IntegerField(choices=CHOICES, default=1)
    total_sum=models.IntegerField(default=0)
    delivery=models.ForeignKey(Delivery, on_delete=models.CASCADE, default=None, null=True)

class Order_detail(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Favorites(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)

