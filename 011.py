from time import sleep
'''Exercício 011: Faça um programa que leia a largura e a altura de uma parede e calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

alt = float(input('Altura da parede: '))
lar = float(input('Largura da parede: '))
area = alt*lar
litro = area / 2
print('Para pintar uma area de {:.2f}m² será necessario {:.2f}L de tinta'.format(area, litro))
sleep(3)