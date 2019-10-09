from time import sleep
from math import trunc

'''Exercício 016: Leia um número Real qualquer pelo teclado e mostre na tela a sua parte Inteira.'''

x = float(input('Digite um numero: '))
print('O numero digitado foi {}, sua parte inteira é {}'.format(x, trunc(x)))
#trunc corta os decimais e mostra só o inteiro
sleep(3)