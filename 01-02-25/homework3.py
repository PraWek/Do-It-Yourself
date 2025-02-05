# ДЗ 3: функция деления, (/)

def divide(pair):
    head, tail = pair
    return head / tail[0]

# Пример
print(divide((6, (2, ()))))  # -> 3.0
