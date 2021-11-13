# Расчет квадратного корня через ряды Тейлора (взят до 5й степени включительно).
# Изначальное число приводится к виду (1 + х), чтобы воспользоваться формулой ряда.
# Если корень целочисленный ответ выдаётся сразу

def my_square(numb):
  return (1 + 0.5 * (numb - 1) - ((numb - 1)**2) / 8 + ((numb - 1)**3 ) / 16 - (5 / 128) * ((numb - 1))**4 + (7 / 258) * (numb - 1)**5 )

number = 0
while number<=0 or number>1000:
    number = float(input("Введите положительное число [1;1000] для расчета кв.корня: "))
    if number<=0 or number>1000:
        print()
        print("Повнимательнее, диапазон числа должен быть в пределах:[1;1000]")
        print()
        print("Попробуем еще раз:)")
pre_square = 0
result = False

for i in range(1001):
  if i**2 == number:
    print(f"Корень квадратный от {number} равен {i}")
    result=True
    break
  if i**2 > number:
    break
  pre_square = i

if not result:
  print(f'Ближайший целый корень "снизу": {pre_square}')
  print(f"Корень квадратный от {number} равен = {(pre_square * my_square(number / pre_square**2))}")
