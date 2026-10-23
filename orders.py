"""Модуль заказов интернет-магазина."""

DELIVERY_FEE = 300          # доставка, руб.
FREE_DELIVERY_FROM = 5000   # бесплатная доставка от этой суммы


def coupon_discount(subtotal, coupon_percent):
    """Размер скидки по купону в рублях."""
    if not coupon_percent:
        return 0
    return subtotal * coupon_percent / 100


def calculate_total(items, coupon_percent=0):
    """Итоговая сумма заказа с учётом купона и доставки."""
    subtotal = sum(price * qty for price, qty in items)

    discount = coupon_discount(subtotal, coupon_percent)
    total = subtotal - discount

    if total < FREE_DELIVERY_FROM:
        total += DELIVERY_FEE
    return round(total, 2)
