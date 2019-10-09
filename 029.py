#  Created by Cássio Jhones on 15/03/19 17:15.
#  Last Modified 15/03/19 17:14.

'''Exercício 27: Leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
from time import sleep

velo = int(input('Qual sua velocidade: '))
if velo > 80:
    print('\nVoce esta acima do limite!')

    multa = (velo-80) * 7

    print('Pagará R$ 7,00 para cada KM acima do limite')
    print('Total a pagar: R$', multa)
else:
    print('\nMuito bem, Continue Assim')
sleep(3)