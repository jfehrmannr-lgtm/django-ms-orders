from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from ..models import CartItem
from ..serializers.cart import CartItemSerializer


class CartItemListView(ListCreateAPIView[CartItem]):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
	
class CartItemDetailedView(RetrieveUpdateDestroyAPIView[CartItem]):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
    lookup_field = "code"
    lookup_url_kwarg = "code_param"
    
    http_method_names = (
        "get",
        "patch",
        "delete",
        "head",
        "options",
    )