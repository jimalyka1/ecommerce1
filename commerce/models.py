from django.db import models
import uuid


PRODUCT_CATEGORY = (
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Children', 'Children'),
)

PRODUCT_STATUS = (
    ('In stock', 'In stock'),
    ('Out of stock', 'Out of stock')
)
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=PRODUCT_CATEGORY)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images')
    other_image = models.ImageField(upload_to='product_images')
    status = status = models.CharField(max_length=100, choices=PRODUCT_STATUS)


    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cart'

    def __str__(self):
        return str(self.id)


class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Cart Items'

    def __str__(self):
        return str(self.cart.id)
    
class Shop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cart Shop'

    def __str__(self):
        return str(self.id)

# Create your models here.
