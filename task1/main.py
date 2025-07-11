def caching_fibonacci():
    # Словник для збереження вже обчислених значень чисел Фібоначчі
    cache = {}

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        # Якщо значення вже є в кеші, повертаємо його одразу
        if n in cache:
            return cache[n]

        # Інакше обчислюємо рекурсивно
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Приклад використання:
# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610