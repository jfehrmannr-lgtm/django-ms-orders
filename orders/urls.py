from django.urls import URLPattern, URLResolver, path

from .views.cart import CartDetailedView, CartListView

urlpatterns: list[URLPattern | URLResolver] = [
    path("", CartListView.as_view(), name="cart-list"),
    
    path("<str:code_param>/", CartDetailedView.as_view(), name="cart-detail"),
]