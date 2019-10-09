from time import sleep

'''Exercício 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

m = float(input('Digite quantos metros: '))
cm = m * 100
mm = m * 1000
dm = m * 10
km = m / 1000
print('Centimetros {}'.format(cm))
print('Milimetros {}'.format(mm))
print('Decametro {}'.format(dm))
print('Kilometro {}'.format(km))

sleep(3)