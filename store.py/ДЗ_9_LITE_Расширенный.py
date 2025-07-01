# Расширенный store.py

from typing import List
from datetime import datetime


# === КЛАСС ТОВАР ===
class Product:
    def __init__(self, name: str, price: float, category: str = "Общее"):
        self.name = name
        self.price = price
        self.category = category  # новый параметр — тип продукта

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price:.2f} руб."

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, category='{self.category}')"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price


# === КЛАСС ЗАКАЗ ===
class Order:
    all_orders = []

    def __init__(self, products: List[Product]):
        self.products = products
        Order.all_orders.append(self)

    def total_price(self):
        return sum(product.price for product in self.products)

    def apply_discount(self, discount):
        return Discount.apply_discount(self.total_price(), discount.discount_percent)

    def __str__(self):
        return f"Заказ на сумму {self.total_price():.2f} руб. с товарами: {[product.name for product in self.products]}"

    @classmethod
    def total_orders_count(cls):
        return len(cls.all_orders)

    @classmethod
    def total_revenue(cls):
        return sum(order.total_price() for order in cls.all_orders)


# === КЛАСС КЛИЕНТ ===
class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def total_spent(self):
        return sum(order.total_price() for order in self.orders)

    def __str__(self):
        return f"Клиент: {self.name}, заказов: {len(self.orders)}, сумма: {self.total_spent():.2f} руб."

    def __repr__(self):
        return f"Customer(name='{self.name}')"


# === КЛАСС СКИДКА ===
class Discount:
    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price: float, percent: float) -> float:
        return price * (1 - percent / 100)

    def __str__(self):
        return f"{self.description}: {self.discount_percent}% скидка"

    def __repr__(self):
        return f"Discount(description='{self.description}', discount_percent={self.discount_percent})"


# === НОВЫЙ КЛАСС КОРЗИНА ПОКУПОК ===
class ShoppingCart:
    def __init__(self, customer: Customer, admin_user: str = "admin"):
        self.customer = customer
        self.admin_user = admin_user
        self.cart_items = []

    def add_product(self, product: Product):
        self.cart_items.append(product)

    def get_details(self):
        product_list = [p.name for p in self.cart_items]
        total = sum(p.price for p in self.cart_items)
        print(f"Покупатель {self.customer.name} приобрел: {product_list}")
        print(f"Общая сумма: {total:.2f} руб.")
        print(f"Зарегистрировал покупки пользователь: {self.admin_user}")
        print(f"Время: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")


# === ПРИМЕР ИСПОЛЬЗОВАНИЯ ===

# Товары разных категорий
p1 = Product("Ноутбук", 50000, "Электроника")
p2 = Product("Футболка", 1500, "Одежда")
p3 = Product("Хлеб", 40, "Продукты")

# Клиент
tanya = Customer("Таня")

# Корзина
cart = ShoppingCart(tanya)
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

# Детали заказа
cart.get_details()
