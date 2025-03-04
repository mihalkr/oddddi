result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("Перше число менше за друге")
        if b > 100:
            raise IndexError("Друге число більше 100")
        return a / b
    except TypeError as e:
        print(f"Помилка типу: {e}")
    except ValueError as e:
         print(f"Помилка значення: {e}")
    except IndexError as e:
        print(f"Помилка індексу: {e}")
    except ZeroDivisionError as e:
        print(f"Ділення на нуль: {e}")
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, (1, 2, 3): 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(f"Результат: {result}")