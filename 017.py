from math import hypot
from time import sleep
'''Exercício 017: Leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre a hipotenusa.'''

co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = hypot(co, ca)
print('Hipotenusa vale {:.2f}'.format(hi))

sleep(3)
