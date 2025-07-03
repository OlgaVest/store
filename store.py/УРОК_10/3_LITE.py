# Пользовательское исключение
class NegativeNumberError(Exception):
    def __init__(self, value, message="Число не должно быть отрицательным."):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} Получено: {self.value}"

# Функция проверки числа
def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError(num)
    print(f"Число {num} положительное.")

# Тесты
print("Тест 1: число -10")
try:
    check_positive_number(-10)
except NegativeNumberError as e:
    print("Ошибка:", e)

print("\nТест 2: число 5")
try:
    check_positive_number(5)
except NegativeNumberError as e:
    print("Ошибка:", e)