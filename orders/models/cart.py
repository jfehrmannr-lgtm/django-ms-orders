from typing import ClassVar

from django.db import models


class Cart(models.Model):
    code = models.CharField(
        max_length=100,
        unique=True,
    )

    user_code = models.CharField(
        max_length=50,
        unique=True,
    )


class CartItem(models.Model):
    code = models.CharField(
        max_length=200,
        unique=True,
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
    )

    product_code = models.CharField(
        max_length=50,
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    quantity = models.PositiveIntegerField()

    class Meta:
        constraints: ClassVar[list[models.BaseConstraint]] = [
            models.UniqueConstraint(
                fields=["cart", "product_code"],
                name="unique_product_per_cart",
            ),
        ]