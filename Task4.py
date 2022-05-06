# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 1 до 100, можно создать свой генератор случайных чисел или использовать готовый) 
# многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0

k = int(input('Введите степень k: '))

import random
mass = random.sample(range(9), k+1)

print(mass)

file = open('Task4.txt', 'a')
p = k
for i in mass:
    while p > 0:
        file.write(f'{mass[i]}x^{p} +')
        p = p - 1
file.write(f' {mass[k]} = 0' + '\n')
file.close()