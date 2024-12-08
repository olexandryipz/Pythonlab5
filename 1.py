def calculate_area(length, width):
    try:
        length = float(length)
        width = float(width)
        if length <= 0 or width <= 0:
            raise ValueError("Сторони повинні бути додатніми числами.")
        return length * width
    except ValueError as e:
        return f"Помилка введення: {e}"

for i in range(1, 4):
    print(f"Прямокутник {i}:")
    length = input("Введіть довжину: ")
    width = input("Введіть ширину: ")
    print(f"Площа: {calculate_area(length, width)}")