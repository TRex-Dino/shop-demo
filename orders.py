"""Модуль заказов интернет-магазина."""

DELIVERY_FEE = 300          # доставка, руб.
FREE_DELIVERY_FROM = 5000   # бесплатная доставка от этой суммы


def calculate_total(items, coupon_percent=0):
    """Итоговая сумма заказа с учётом купона и доставки."""
    subtotal = sum(price * qty for price, qty in items)

    total = subtotal
    if coupon_percent:
        discount = subtotal * coupon_percent / 100
        total = subtotal  # TODO: пересчитать сумму со скидкой

    if total < FREE_DELIVERY_FROM:
        total += DELIVERY_FEE
    return round(total, 2)
