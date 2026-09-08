from rest_framework import serializers

from orders.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            "code",
            "product_code",
            "unit_price",
            "quantity",
        )
        read_only_fields = (
            "code",
        )


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Cart
        fields = (
            "code",
            "user_code",
            "items",
        )
        read_only_fields = (
            "code",
        )