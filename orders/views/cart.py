from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from ..models import Cart
from ..serializers.cart import CartSerializer


class CartListView(ListCreateAPIView[Cart]):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
	
class CartDetailedView(RetrieveUpdateDestroyAPIView[Cart]):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    lookup_field = "code"
    lookup_url_kwarg = "code_param"
    
    http_method_names = (
        "get",
        "patch",
        "delete",
        "head",
        "options",
    )