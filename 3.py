def is_point_inside_circle(x, y, a, b, R):
    try:
        R = float(R)
        if R <= 0:
            raise ValueError("Радіус повинен бути додатнім числом.")
        return (x - a)**2 + (y - b)**2 < R**2
    except ValueError as e:
        return f"Помилка введення: {e}"

a = float(input("Введіть координату a (центр кола по x): "))
b = float(input("Введіть координату b (центр кола по y): "))
R = input("Введіть радіус кола: ")

points = [("P", float(input("Введіть р1: ")), float(input("Введіть р2: "))),
          ("F", float(input("Введіть f1: ")), float(input("Введіть f2: "))),
          ("L", float(input("Введіть l1: ")), float(input("Введіть l2: ")))]

count_inside = sum(1 for name, x, y in points if is_point_inside_circle(x, y, a, b, R) == True)
print(f"Кількість точок, що лежать всередині кола: {count_inside}")
