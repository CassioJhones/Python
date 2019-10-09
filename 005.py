from time import sleep

'''Exercício 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.'''

x = int(input('Digite um numero: '))
suce = x+1
ante = x-1
print('o Sucessor é {}, o Antecessor é {}'.format(suce, ante))
sleep(3)
