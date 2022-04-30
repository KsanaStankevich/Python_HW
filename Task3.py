# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

mass = [int(x) for x in input('Введите числа массива через пробел ').split()]
print(mass)

def unique_mass_num(mass):
    unique = []

    for mass in mass:
        if mass in unique:
            continue
        else:
            unique.append(mass)
    return unique

print(unique_mass_num(mass))