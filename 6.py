def count_divisors(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    return count

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

while True:
    m = input("Введіть початок інтервалу M: ")
    n = input("Введіть кінець інтервалу N: ")
    if m.isdigit() and n.isdigit() and int(m) < int(n):
        m, n = int(m), int(n)
        break
    print("Введіть цілі числа, де M < N.")

print("Числа з максимальною кількістю дільників:", max_divisors_in_range(m, n))