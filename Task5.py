# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов (нет нулевых кофициентов).

import re
import numpy

def ReadFile(path):
    data = open(path, 'r')
    dataString = data.read()
    data.close()
    dataString = re.sub(r'\*x\^\d*', '', dataString)
    dataString = re.sub(r'\*x', '', dataString)
    dataString = re.sub(r'\s\+', '', dataString)
    dataString = re.sub(r'\s\=\s0', '', dataString)
    dataString = re.sub(r'\s\-\s', ' -', dataString)
    dataList = dataString.split(' ')
    for i in range(0, len(dataList)):
        dataList[i] = int(dataList[i])
    return dataList

def writeFile(path, dataWrite):
    data = open(path, 'w')

    for i in range(0, len(dataWrite)):
        if(i == 0):
            if(dataWrite[i + 1] > 0):
                data.write(f'{dataWrite[i]}*x^{len(dataWrite)-i} + ')
        elif(i < (len(dataWrite) - 2)):
            if(dataWrite[i + 1] > 0):
                if(dataWrite[i] > 0):
                    data.write(f'{dataWrite[i]}*x^{len(dataWrite)-i} + ')
                else:
                    data.write(f'{dataWrite[i]*(-1)}*x^{len(dataWrite)-i} + ')
            else:
                data.write(f'{dataWrite[i]}*x^{len(dataWrite)-i} - ')
        if(i == (len(dataWrite) - 2)):
            if(dataWrite[len(dataWrite) - 1] > 0):
                data.write(f'{dataWrite[i]}*x + {dataWrite[len(dataWrite) - 1]} = 0')
            else:
                data.write(f'{dataWrite[i]}*x - {dataWrite[len(dataWrite) - 1] * (-1)} = 0')
    data.close()

first_path = 'Task5.txt'
second_path = 'Task51.txt'

first_data = ReadFile(first_path)
second_data = ReadFile(second_path)
resultData = numpy.polyadd(first_data, second_data)
writeFile('Task5Res.txt', resultData)


# Решение 2:
# from sympy import parse_expr, symbols
# path1 = 'Polynom1.txt'
# path2 = 'Polynom2.txt'
# with open(path1, 'r') as file:
#     mNumber = file.read()
# with open(path2, 'r') as file:
#     mNumber2 = file.read()
# print(f'({mNumber}) + ({mNumber2})')
# x = symbols('x')
# mNumber = parse_expr(mNumber.replace('^', '**'), local_dict={'x': x})
# mNumber2 = parse_expr(mNumber2.replace('^', '**'), local_dict={'x': x})
# sumMNumbers = mNumber + mNumber2
# print(f'({mNumber}) + ({mNumber2})')
# print(f'{mNumber} + {mNumber2}')
# print(sumMNumbers)

# Решение на дз:
# str_1 = "2*x^2 + 4*x + 5".split(' ')
# str_2 = "3x^2 + 5*x + 0".split(' ')
# print(str_1)
# print(str_2)

# a1 = str_1[0].split('*')
# a2 = str_2[0].split('*')
# print(a1, a2)
