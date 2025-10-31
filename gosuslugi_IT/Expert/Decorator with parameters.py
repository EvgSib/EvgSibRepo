# -*- coding: utf-8 -*-

# Определяем декоратор
def log_method_call(func):
    """Декоратор для логирования вызовов методов."""
    # Внутренняя функция-обёртка принимает все аргументы, включая 'self'
    def wrapper(self, *args, **kwargs):
        print(f"Вызов метода '{func.__name__}' с аргументами: {args}, {kwargs}")
        result = func(self, *args, **kwargs) # Вызов исходного метода
        print(f"Метод '{func.__name__}' завершён. Результат: {result}")
        return result
    return wrapper

# Определяем класс и применяем декоратор к методу
class Calculator:
    def __init__(self, value):
        self.value = value

    @log_method_call
    def add(self, other):
        """Метод для сложения чисел."""
        self.value += other
        return self.value

# Создаём экземпляр класса и вызываем декорированный метод
calc = Calculator(10)
result = calc.add(5)

print(f"Итоговое значение: {result}")






















