def find_numbers(n, divisors):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError("n повинно бути натуральним числом.")
        divisors = [int(d) for d in divisors if int(d) > 0]

        return [i for i in range(1, n + 1) if all(i % d == 0 for d in divisors)]
    except ValueError as e:
        return f"Помилка введення: {e}"


n = input("Введіть верхню межу (n): ")
divisors = input("Введіть числа через пробіл, на які має ділитися n: ").split()
print(f"Числа, що відповідають умовам: {find_numbers(n, divisors)}")
