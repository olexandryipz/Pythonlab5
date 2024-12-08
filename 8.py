def filter_list_by_range(numbers, bottom, upper):
    min_val = min(numbers)
    max_val = max(numbers)

    filtered_numbers = []
    for num in numbers:
        if min_val + bottom <= num <= max_val - upper:
            filtered_numbers.append(num)

    return filtered_numbers


import random
numbers = random.sample(range(1, 100), 20)

print("Список чисел:", numbers)
while True:
    bottom = input("Введіть нижню межу: ")
    upper = input("Введіть верхню межу: ")
    if bottom.isdigit() and upper.isdigit() and int(bottom) >= 0 and int(upper) >= 0:
        bottom, upper = int(bottom), int(upper)
        break
    print("Введіть додатні значення для нижньої та верхньої меж.")

filtered_list = filter_list_by_range(numbers, bottom, upper)
print("Новий список:", filtered_list)