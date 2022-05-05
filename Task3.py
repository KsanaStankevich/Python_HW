# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности. (только 1 раз)

mass = [int(i) for i in input('Введите числа массива через пробел ').split()]
print(mass)

def unique_mass_num(mass):
    unique = []

    for i in mass:
        if mass.count(i) != 1:
            continue
        else:
            unique.append(i)
    return unique

print(unique_mass_num(mass))