import time
import random

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання {func.__name__}: {end_time - start_time:.6f} секунд")
        return result
    return wrapper

@timing_decorator
def count_divisors(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    return count

@timing_decorator
def max_divisors_in_range(m, n):
    max_count = 0
    numbers = []
    for i in range(m, n + 1):
        divisors_count = count_divisors(i)
        if divisors_count > max_count:
            max_count = divisors_count
            numbers = [i]
        elif divisors_count == max_count:
            numbers.append(i)
    return numbers

@timing_decorator
def is_simple(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

@timing_decorator
def get_simples(n):
    simples = [i for i in range(2, n + 1) if is_simple(i)]
    return simples

@timing_decorator
def format_output(simples, format_type):
    if format_type == "list":
        return simples
    elif format_type == "column":
        return "\n".join(map(str, simples))
    elif format_type == "count":
        return len(simples)
    else:
        return "Неправильний формат."

@timing_decorator
def filter_list_by_range(numbers, bottom, upper):
    min_val = min(numbers)
    max_val = max(numbers)

    filtered_numbers = []
    for num in numbers:
        if min_val + bottom <= num <= max_val - upper:
            filtered_numbers.append(num)

    return filtered_numbers

print("=== Тестування завдання 6 ===")
for n in [10, 100, 1000, 10000, 100000, 1000000]:
    print(f"Тест для n = {n}")
    m = 1
    max_divisors_in_range(m, n)

print("\n=== Тестування завдання 7 ===")
for n in [10, 100, 1000, 10000, 100000, 1000000]:
    print(f"Тест для n = {n}")
    simples = get_simples(n)
    format_output(simples, "count")

print("\n=== Тестування завдання 8 ===")
for n in [10, 100, 1000, 10000, 100000, 1000000]:
    print(f"Тест для n = {n}")
    numbers = random.sample(range(1, n + 1), min(20, n))  # Генеруємо максимум 20 випадкових чисел
    filter_list_by_range(numbers, 1, 1)
