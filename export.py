"""Выгрузка истории заказов в CSV."""

import csv
import io

HEADER = ["order_id", "date", "status", "total"]

# BOM в начале файла: без него Excel открывает кириллицу «кракозябрами»
UTF8_BOM = "﻿"


def orders_to_csv(orders):
    buf = io.StringIO()
    buf.write(UTF8_BOM)
    writer = csv.DictWriter(buf, fieldnames=HEADER, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(orders)
    return buf.getvalue()
