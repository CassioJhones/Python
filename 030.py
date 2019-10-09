from time import sleep

'''Exercício Python 030: leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

num = int(input('Digite um numero: '))
result = num%2
if result == 0:
    print('Numero PAR')
else:
    print('Numero IMPAR')
sleep(3)