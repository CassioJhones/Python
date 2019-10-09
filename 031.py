from time import sleep
'''Exercício Python 31: pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.'''

x = int(input('Qual a distancia da viagem: '))
if x <= 200:
    preco = 0.50 * x
    print('Voce pagará R${} na passagem'.format(preco))
else:
    preco = 0.45 * x
    print('Voce pagara R${} na passagem'.format(preco))
sleep(3)