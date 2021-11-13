#расчет случайного квадрата для упражнения по извлечению корня в уме

import random
square = 10
while square%10 == 0:
    square = random.randint(16, 99)
print( square**2 )
