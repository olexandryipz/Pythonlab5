import math

def hypotenuse(a, b):
    try:
        a = float(a)
        b = float(b)
        if a <= 0 or b <= 0:
            raise ValueError("Катети повинні бути додатніми числами.")
        return math.sqrt(a**2 + b**2)
    except ValueError as e:
        return f"Помилка введення: {e}"

a1 = input("Введіть перший катет для першого трикутника: ")
b1 = input("Введіть другий катет для першого трикутника: ")
a2 = input("Введіть перший катет для другого трикутника: ")
b2 = input("Введіть другий катет для другого трикутника: ")

hyp1 = hypotenuse(a1, b1)
hyp2 = hypotenuse(a2, b2)

if isinstance(hyp1, float) and isinstance(hyp2, float):
    print(f"Гіпотенуза першого трикутника: {hyp1}")
    print(f"Гіпотенуза другого трикутника: {hyp2}")
    if hyp1 > hyp2:
        print("Перша гіпотенуза більша за другу.")
    elif hyp1 < hyp2:
        print("Друга гіпотенуза більша за першу.")
    else:
        print("Гіпотенузи рівні.")
else:
    print(f"Помилка: {hyp1}, {hyp2}")