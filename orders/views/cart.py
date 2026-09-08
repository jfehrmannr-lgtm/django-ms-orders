from rest_framework.generics import DestroyAPIView, ListAPIView

from ..models.cart import Cart
from ..serializers.cart import CartSerializer


class CartListView(ListAPIView[Cart]):
	serializer_class: CartSerializer
	
class CartDetailedView(DestroyAPIView[Cart]):
    serializer_class: CartSerializer