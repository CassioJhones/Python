from time import sleep

'''Exercício 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto'''

preço = float(input('Preço do produto: R$ '))
cento = preço * 0.05
desconto = preço - cento
print('Produto com 5% de Desconto: R$ {}'.format(desconto))
sleep(3)