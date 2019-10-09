from time import sleep

'''Exercício 013: Leia o salário atual e mostre o novo salário com 15% de aumento.'''
salario = float(input('Salário Atual: R$ '))
cento = salario * 0.15
aumento = salario + cento
print('Salário com 15% de Aumento: R$ {}'.format(aumento))

sleep(3)

