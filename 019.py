import random
from time import sleep

'''Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')
lista = [a1, a2, a3, a4] #lista de alunos
escolhido = random.choice(lista) #escolher na lista aleatoriamente

print('O aluno escolhido foi {}'.format(escolhido))
sleep(3)