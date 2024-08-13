from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ProductSerializer, CartSerializer, CartitemsSerializer, DisplayCartItemsSerializer
from .models import Product, Cart, Cartitems
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated


class ProductHomePage(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def get(self, request, format=None, *args, **kwargs):
        all_products = Product.objects.all()
        serialized_products = ProductSerializer(all_products, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        new_product = ProductSerializer(data=request.data)
        new_product.is_valid(raise_exception=True)
        new_product.save()
        return Response({'Success': 'Product has been added successfully!'}, status=status.HTTP_201_CREATED)



class ProductDetailPage(APIView):
    def get(self, request, id):
        single_product = get_object_or_404(Product, id=id)
        serialized_product = ProductSerializer(single_product)
        return Response(serialized_product.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        single_product = get_object_or_404(Product, id=id)
        serialized_product = ProductSerializer(single_product, data=request.data, partial=True)
        serialized_product.is_valid(raise_exception=True)
        serialized_product.save()
        return Response('Update successful', status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        single_product = get_object_or_404(Product, id=id)
        single_product.delete()
        return Response('Product has been successfully deleted', status=status.HTTP_204_NO_CONTENT)


class CreateCartPage(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self, request, format=None):
        new_cart = Cart.objects.create()
        cart_serializer = CartSerializer(new_cart, data=request.data)
        cart_serializer.is_valid(raise_exception=True)
        cart_serializer.save()
        return Response({'Success': 'Your shopping cart has been created successfully!'}, status=status.HTTP_201_CREATED)

class AddToCartPage(APIView):
    permission_classes = ([IsAuthenticated])

    ''' PASS IN THE ID OF A CART THEN PASS IN THE 
    ID OF THE PRODUCT YOU WANT TO ADD AND THE QUANTITY'''

    def post(self, request, id):
        cart_item = Cart.objects.get(id=id)
        print(cart_item)
        new_cartitem = Cartitems(cart=cart_item)
        print(new_cartitem)
        cart_item = CartitemsSerializer(new_cartitem, data=request.data, partial=True)
        cart_item.is_valid(raise_exception=True)
        cart_item.save()
        return Response({'Success': 'Item added to cart successfully!'}, status=status.HTTP_201_CREATED)




class ItemsListPage(APIView):
    permission_classes = ([IsAdminUser])
    def get(self, request, id):
        cart_items = Cartitems.objects.filter(id=id)
        serialized_items = CartitemsSerializer(cart_items, many=True)
        return Response(serialized_items.data, status=status.HTTP_200_OK)


class RemoveCartItemPage(APIView):
    permission_classes = ([IsAdminUser])
    def delete(self, request, id):
        remove_product = get_object_or_404(Cartitems, id=id)
        remove_product.delete()
        return Response('Product has been successfully removed from your cart', status=status.HTTP_204_NO_CONTENT)
       


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Create your views here.
def home(request):
    context = {}
    return render(request, 'commerce/index.html',context)

def shop(request):
    context = {}
    return render(request, 'commerce/shop.html',context)

def detail(request):
    context = {}
    return render(request, 'commerce/detail.html',context)