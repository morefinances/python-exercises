list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
dict_a = {x: x**2 for x in list_a}
print(dict_a)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, -2: 4, -1: 1, 5: 25}

# dict_gen = (x: x**2 for x in list_a)      # SyntaxError: invalid syntax
dict_gen = ((x, x ** 2) for x in list_a)    # Корректный вариант генератора-выражения для словаря
# dict_a = dict(x: x**2 for x in list_a)    # SyntaxError: invalid syntax
dict_a = dict((x, x ** 2) for x in list_a)  # Корректный вариант синтаксиса от @longclaps