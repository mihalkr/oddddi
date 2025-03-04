result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("Перше число менше за друге")
        if b > 100:
            raise IndexError("Друге число більше 100")
        return a / b
    except ValueError as e:
         print(f"Помилка значення: {e}")
    except IndexError as e:
        print(f"Помилка індексу: {e}")
    return None

data = {10: 2, 2: 5, 25: 4, 18: 5, 15: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(f"Результат: {result}")