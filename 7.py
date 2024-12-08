def is_simple(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_simples(n):
    simples = [i for i in range(2, n + 1) if is_simple(i)]
    return simples

def format_output(simples, format_type):
    if format_type == "list":
        return simples
    elif format_type == "column":
        return "\n".join(map(str, simples))
    elif format_type == "count":
        return len(simples)
    else:
        return "Неправильний формат."

while True:
    n = input("Введіть максимальне число N: ")
    if n.isdigit() and int(n) > 1:
        n = int(n)
        break
    print("Введіть ціле число більше 1.")

while True:
    format_type = input("Виберіть формат виводу (list, column, count): ")
    if format_type in ["list", "column", "count"]:
        break
    print("Виберіть правильний формат.")

print("Прості числа:", format_output(get_simples(n), format_type))