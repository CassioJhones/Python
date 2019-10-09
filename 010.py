from time import sleep

'''Exercício 010: Crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos dólares ela pode comprar'''
real = float(input('\nQuantos reais voce tem: R$ '))
dolar = real / 3.84
euro = real / 4.33
peso = real * 5.05
print('Dolar: Voce pode comprar U$ {:.2f}'.format(dolar))
print('Euro: Voce pode comprar €$ {:.2f}'.format(euro))
print('Peso: Voce pode comprar $ {:.2f}'.format(peso))

sleep(3)