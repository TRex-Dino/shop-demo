"""Модуль заказов интернет-магазина."""

DELIVERY_FEE = 300          # доставка, руб.
FREE_DELIVERY_FROM = 5000   # бесплатная доставка от этой суммы
MAX_DISCOUNT = 1000         # купон даёт не больше 1000 руб.


def calculate_total(items, coupon_percent=0):
    """Итоговая сумма заказа с учётом купона и доставки."""
    subtotal = sum(price * qty for price, qty in items)

    total = subtotal
    if coupon_percent:
        discount = min(subtotal * coupon_percent / 100, MAX_DISCOUNT)
        total = subtotal - discount

    if total < FREE_DELIVERY_FROM:
        total += DELIVERY_FEE
    return round(total, 2)
