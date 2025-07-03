def validate_user_input(data):
    if not isinstance(data, dict):
        raise TypeError("Ожидался словарь с данными пользователя.")

    try:
        if 'name' not in data or not isinstance(data['name'], str):
            raise ValueError("Отсутствует имя или оно некорректного типа.")
        if 'age' not in data or not (isinstance(data['age'], int) and data['age'] > 0):
            raise ValueError("Возраст должен быть положительным целым числом.")
    except Exception as e:
        raise ValueError("Ошибка валидации данных.") from e

    print("Валидация прошла успешно.")

# Тесты
print("Тест 1: корректные данные")
validate_user_input({"name": "Alice", "age": 30})

print("\nТест 2: отсутствует name")
try:
    validate_user_input({"age": 25})
except Exception as e:
    print(e)

print("\nТест 3: age = -5")
try:
    validate_user_input({"name": "Bob", "age": -5})
except Exception as e:
    print(e)

print("\nТест 4: передан не словарь")
try:
    validate_user_input("не словарь")
except Exception as e:
    print(e)