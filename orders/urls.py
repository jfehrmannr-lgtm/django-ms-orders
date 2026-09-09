from django.urls import URLPattern, URLResolver, path

from .views.cart import CartDetailedView, CartListView
from .views.cart_item import CartItemDetailedView, CartItemListView

urlpatterns: list[URLPattern | URLResolver] = [
    path("cart/", CartListView.as_view(), name="cart-list"),
    path("cart_item/", CartItemListView.as_view(), name="cart_item-list"),
    
    path("cart/<str:code_param>/", CartDetailedView.as_view(), name="cart-detail"),
    path("cart_item/<str:code_param>/", CartItemDetailedView.as_view(), name="cart_item-detail"),
]