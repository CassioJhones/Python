import math
from time import sleep
'''Exercício  018: Leia um ângulo qualquer
e mostre o valor do seno, cosseno e tangente'''

x = float(input('Digite um angulo: '))
cos = math.cos(math.radians(x)) #pega x e converte para radianos
sen = math.sin(math.radians(x))
tg = math.tan(math.radians(x))

print('''Seno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'''.format(sen, cos, tg))
sleep(3)