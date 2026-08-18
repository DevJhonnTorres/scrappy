"""A small REST API to demo Graphify's knowledge graph: orders, users and inventory."""
from __future__ import annotations

from datetime import datetime
from typing import Optional


class User:
    def __init__(self, user_id: int, name: str, email: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email


class Product:
    def __init__(self, sku: str, name: str, price: float, stock: int = 0) -> None:
        self.sku = sku
        self.name = name
        self.price = price
        self.stock = stock

    def in_stock(self) -> bool:
        return self.stock > 0

    def adjust_stock(self, delta: int) -> None:
        self.stock += delta


class Inventory:
    def __init__(self) -> None:
        self._items: dict[str, Product] = {}

    def add(self, product: Product) -> None:
        self._items[product.sku] = product

    def get(self, sku: str) -> Optional[Product]:
        return self._items.get(sku)

    def reserve(self, sku: str, qty: int) -> bool:
        p = self.get(sku)
        if p is None or not p.in_stock() or p.stock < qty:
            return False
        p.adjust_stock(-qty)
        return True


class OrderItem:
    def __init__(self, product: Product, qty: int) -> None:
        self.product = product
        self.qty = qty

    @property
    def subtotal(self) -> float:
        return self.product.price * self.qty


class Order:
    def __init__(self, order_id: int, user: User) -> None:
        self.order_id = order_id
        self.user = user
        self.items: list[OrderItem] = []
        self.created_at = datetime.utcnow()
        self.status = "pending"

    def add_item(self, product: Product, qty: int) -> None:
        self.items.append(OrderItem(product, qty))

    @property
    def total(self) -> float:
        return sum(i.subtotal for i in self.items)

    def complete(self) -> None:
        self.status = "completed"


class OrderService:
    """Coordinates inventory reservation and order fulfilment."""

    def __init__(self, inventory: Inventory) -> None:
        self.inventory = inventory
        self._orders: dict[int, Order] = {}

    def create_order(self, order_id: int, user: User) -> Order:
        order = Order(order_id, user)
        self._orders[order_id] = order
        return order

    def checkout(self, order: Order) -> bool:
        for item in order.items:
            if not self.inventory.reserve(item.product.sku, item.qty):
                return False
        order.complete()
        return True

    def get_order(self, order_id: int) -> Optional[Order]:
        return self._orders.get(order_id)
