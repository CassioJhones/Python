'''Exercício Python 034: pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

sal = float(input('Salario: '))
if sal > 1250:
    plus = sal + (sal * 0.1)
    print('Seu salario de R${} \nrecebera um aumento de 10% e será R${}'.format(sal, plus))
else:
    plus1 =sal + (sal * 0.15)
    print('Seu salario de R${} recebera um aumento de 15% e será R${}'.format(sal, plus1))