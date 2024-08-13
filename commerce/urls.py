from django.urls import path
from . views import  ProductHomePage, ProductDetailPage,CreateCartPage, ItemsListPage, AddToCartPage, RemoveCartItemPage, home, shop, detail

urlpatterns = [
    path('products/', ProductHomePage.as_view(), name='all-products'),
    path('cart/', CreateCartPage.as_view(), name='cart'),
    path('cartitems/', ItemsListPage.as_view(), name='cart_items'),
    path('<uuid:id>/addtocart/', AddToCartPage.as_view(), name='cart_add'),
    path('removecartitem/<str:cart_id>/<str:product_id>/', RemoveCartItemPage.as_view(), name='cart_remove'),
    path('<str:id>/', ProductDetailPage.as_view(), name='detail'),
    path('', home, name="home"),
    path('shop/', shop, name="shop"),
    path('detail/', detail, name="detail"),

]