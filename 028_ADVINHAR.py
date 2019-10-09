#  Created by Cássio Jhones on 15/03/19 16:46.

'''Exercício 028: Faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. Escreva na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
PC = randint(0, 5)
print('-=-'*15)
print('Pensei em um numero de 0 a 5, tente acertar: ')
print('-=-'*15)

USER = int(input('Pensei no: '))
print('\nPROCESSANDO...')
sleep(0.5)
if PC == USER:
    print('Voce acertou, Parabens!')
else:
    print('Voce Errou')