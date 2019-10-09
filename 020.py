import random
from time import sleep

'''Python – Exercício 020 – Sorteando uma ordem
Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')
lista = [a1, a2, a3, a4] #lista de alunos
random.shuffle(lista) #EMBARALHA A LISTA

print('A Ordem escolhida foi {}'.format(lista))
sleep(3)