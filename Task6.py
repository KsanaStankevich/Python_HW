# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# 1. Самый простой
# import random

# PlayerOne = input('Введите имя первого игрока ')
# PlayerTwo = input('Введите имя второго игрока ')

# OneTossNumber = random.randint(1, 100)
# TwoTossNumber = random.randint(1, 100)

# if( OneTossNumber > TwoTossNumber): print(f'{PlayerOne} ходит первый')
# else: print(f'{PlayerTwo} ходит первый')

# num2 = 2021
# n = 0
# while num2 > 0:
#     num1 = int(input('Введите число до 28: '))
#     if num1 > 28: print('Атата, число должно быть меньше 28!')
#     else: 
#         num2 -= num1
#         print(f'Осталось {num2} конфет')
#         n = n+1
# if(n%2==0): print(f'Выиграл {PlayerTwo}')
# else: print(f'Выиграл {PlayerOne}')

# 2. Против бота

import random

Player = input('Введите имя игрока ')
PlayerTossNumber = random.randint(1, 100)
CompTossNumber = random.randint(1, 100)

if( PlayerTossNumber > CompTossNumber): print(f'{Player} ходит первый')
else: print('Компьютер ходит первый')

num2 = 40
while num2 > 0:
    num1 = int(input('Введите число до 28: '))
    if num1 > 28: print('Атата, число должно быть меньше 28!')
    else: 
        num2 -= num1
        if num2 <= 0: print('Вы выиграли!')
        else: 
            comp = random.randint(1, 28)
            print(f'Компьютер выбрал {comp}')
            num2 -= comp
            if num2 <= 0: print('Выиграл компьютер :с')
            print(f'Осталось {num2} конфет')

# 3. Против умного бота