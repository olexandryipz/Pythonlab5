def calculate_quadrilateral_area(X, Y, Z, T):
    try:
        X, Y, Z, T = float(X), float(Y), float(Z), float(T)
        if X <= 0 or Y <= 0 or Z <= 0 or T <= 0:
            raise ValueError("Сторони повинні бути додатніми числами.")
        return (X * Y) / 2 + (Z * T) / 2
    except ValueError as e:
        return f"Помилка введення: {e}"

X = input("Введіть X: ")
Y = input("Введіть Y: ")
Z = input("Введіть Z: ")
T = input("Введіть T: ")

print(f"Площа чотирикутника: {calculate_quadrilateral_area(X, Y, Z, T)}")
