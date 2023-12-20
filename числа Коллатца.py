# числа Коллатца

x = int(input("Введите стартовое число:"))
s_index = 0

while x!=1:
    if x%2 == 0:
        x = x / 2
    else:
        x = 3 * x + 1
    print(x)
    s_index += 1

print(f"Количество итераций: {s_index}")