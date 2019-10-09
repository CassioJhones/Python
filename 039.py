'''Exercício Python 039: Faça um programa que leia o ano de nascimento, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento, mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date #modulo de data e tempo
atual = date.today().year # mostra ano atual
nasc = int(input('Ano que nasceu: '))
idade = atual - nasc

print('Quem nasceu em {}, tem {} anos em {}...'.format(nasc, idade, atual))

if idade ==18:
    print('Voce precisa se alistar IMEDIATAMENTE!')

elif idade <18:
    saldo = 18 - idade
    print('Voce ainda nao tem 18 anos. Faltam {} anos'.format(saldo))

elif idade > 18:
    saldo  = idade - 18
    print('Voce ja deveria ter se alistado há {} anos'.format(saldo))