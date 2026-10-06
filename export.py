"""Выгрузка истории заказов в CSV."""

import csv
import io

HEADER = ["order_id", "date", "status", "total"]


def orders_to_csv(orders):
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=HEADER, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(orders)
    return buf.getvalue()
