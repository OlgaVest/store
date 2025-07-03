def convert_to_int(value):
    try:
        result = int(value)
        print(f"Преобразовано успешно: {result}")
        return result
    except ValueError:
        print("Ошибка: невозможно преобразовать значение в целое число.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        print("Завершена попытка преобразования.")

# Тесты
print("Тест 1: корректная строка '123'")
convert_to_int("123")
print("\nТест 2: некорректная строка 'abc'")
convert_to_int("abc")
print("\nТест 3: список [1, 2, 3]")
convert_to_int([1, 2, 3])