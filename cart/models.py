from django.db import models
from shop.models import Product

# Create your models here.
class Cart(models.Model) :
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta :
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self) :
        return self.cart_id

class CartItem(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default = True)

    class Meta :
        db_table = 'CartItem'

    def sub_total(self) :
        return self.product.price * self.quantity
    
    def __str__(self) :
        return self.product

class Post(models.Model):
    realname = models.CharField(max_length=10)
    artist_name = models.CharField(max_length=30)
    team = models.CharField(max_length=64)
    email = models.EmailField()
    artist_intro = models.TextField(max_length=300)
    post_intro = models.TextField(max_length=300)
    post_plan = models.TextField()
    # 전시 장소 추가 필요

    def __str__(self):
        return self.artist_name

    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'post'