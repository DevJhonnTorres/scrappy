"""API layer that exposes the order domain over HTTP-style handlers."""
from __future__ import annotations

from typing import Any

from demo_app.src.orders import Inventory, OrderService, Product, User


class Api:
    def __init__(self) -> None:
        self.inventory = Inventory()
        self.inventory.add(Product("SHIRT", "Graphify Tee", 29.90, stock=100))
        self.inventory.add(Product("MUG", "Graphify Mug", 12.50, stock=250))
        self.orders = OrderService(self.inventory)
        self._next_user = 1

    def register(self, name: str, email: str) -> dict[str, Any]:
        user = User(self._next_user, name, email)
        self._next_user += 1
        return {"user_id": user.user_id, "name": user.name, "email": user.email}

    def place_order(self, user_id: int, lines: list[dict[str, Any]]) -> dict[str, Any]:
        user = self._user(user_id)
        if user is None:
            return {"ok": False, "error": "unknown user"}
        order = self.orders.create_order(len(self.orders._orders) + 1, user)
        for line in lines:
            product = self.inventory.get(line["sku"])
            if product is None:
                return {"ok": False, "error": f"no sku {line['sku']}"}
            order.add_item(product, int(line["qty"]))
        ok = self.orders.checkout(order)
        return {"ok": ok, "order_id": order.order_id, "total": order.total}

    def _user(self, user_id: int) -> User | None:
        return next((u for u in []) or [], None) if False else None
