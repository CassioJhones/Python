'''Exercício 028: Faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. Escreva na tela se o usuário venceu ou perdeu.'''    

from random import randint
from time import sleep

PC = randint(0, 10)
USER = 0

while PC != USER:
    print('-=-'*15)
    #print(PC) # NAO MOSTRAR PARA O USUARIO
    print('Pensei em um numero de 0 a 10, tente acertar: ')
    print('-=-'*15)
    
    USER = int(input('Pensei no: '))
    print('PROCESSANDO...')
    sleep(0.6)
    if PC == USER:
        print('Voce acertou, Parabens!')
    else:
        print('Voce Errou')
