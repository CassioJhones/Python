'''Exercício 27: Leia o nome completo de uma pessoa, mostrando em seguida o primeiro
 e o último nome separadamente.Primeiro e último nome'''
from time import sleep

nome = input('Digite seu nome completo: ')
separado = nome.split() # Separa a variavel nome em lista

print('Bom dia, {}'.format(separado[0])) #mostra posição 0 da lista
print('Seu ultimo nome é {}'.format(separado[len(separado)-1]))
# LEN CONTA QUANTOS ITENS TEM NA LISTA 'SEPARADO' E -1 TIRA 1 PARA OLHAR O ULTIMO ITEM

sleep(3)