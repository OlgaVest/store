from typing import List

# Класс Товар
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price:.2f} руб."

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price


# Класс Заказ
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


# Класс Клиент
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


# Класс Скидка
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


# Пример использования

# Создаем продукты
p1 = Product("Ноутбук", 50000)
p2 = Product("Мышь", 1500)
p3 = Product("Клавиатура", 3000)

# Сравнение продуктов
print(p1 > p2)  # True

# Создаем скидки
seasonal = Discount("Сезонная распродажа", 10)
promo = Discount("Промокод ЛЕТО25", 25)

# Создаем заказы
order1 = Order([p1, p2])
order2 = Order([p2, p3])

# Применение скидки
print(f"Итог заказа1 без скидки: {order1.total_price():.2f} руб.")
print(f"Со скидкой {seasonal.description}: {order1.apply_discount(seasonal):.2f} руб.")

# Создаем клиентов
alice = Customer("Алиса")
bob = Customer("Боб")

# Добавляем заказы клиентам
alice.add_order(order1)
bob.add_order(order2)

# Информация о клиентах
print(alice)
print(bob)

# Общая информация по заказам
print("Общее количество заказов:", Order.total_orders_count())
print("Общая сумма всех заказов:", Order.total_revenue(), "руб.")

# Вывод с дандер методами
print("\nПодробная информация:")
print("Продукты:", p1, repr(p2))
print("Заказ:", str(order1))
print("Скидка:", repr(seasonal))