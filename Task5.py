# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов (нет нулевых кофициентов).

import numpy
# a = np.array([1,2], float)
# b = np.array([3,4,5,6], float)
# c = np.array([7,8,9], float)
# print(np.poly((1, 0, 1, 0, -1, 0, 1)))

# print(np.concatenate((a, b, c)))
# print(np.poly([-1, 1, 1, 10]))


# def str(e):
#     return (lambda f, g, i, j, l: (lambda k: '0' if f(k) == 1 and k[0] == 0 else 
#     (lambda b: ((lambda a: ((l if a.startswith(' + ') else '-') + a[3:]))
#     (b(f(k) - 1, k[-1])) + l.join(b(h, k[h]) for h in range(f(k) - 2, -1, -1))))
#     (((lambda a, b: (l if b == 0 else (' + ' if b.real >= 0 else ' - ') + 
#     (l if g(b) == 1 and a > 0 else i(j(g(b), 3)) if type(b) == float else i(g(b))) + 
#     (l if a == 0 else 'x' if a == 1 else 'x' + l.join({'0': chr(8304), '1': chr(185), 
#     '2': chr(178), '3': chr(179), '4': chr(8308), '5': chr(8309), '6': chr(8310), '7'
#     : chr(8311), '8': chr(8312), '9': chr(8313)}[s] for s in i(a))))))))(e._coeff))(f=len, g=abs, i=str, j=round, l='')

# print (str(5))

n = int(input())
koef = [int(elem) for elem in input().split()]
 
koef.append(koef[-1])
 
for i in range(n, 0, -1):
    koef[i] += koef[i-1]
        
print(*koef)