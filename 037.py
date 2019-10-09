'''Exercício Python 037: leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input('UM NUMERO: '))
print('''Escolha uma das bases: 
1 - Para Binario
2 - Para Octal
3 - Para Hexacimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} em BINARIO fica {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} em OCTAL fica {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} em HEXADECIMAL fica {}'.format(num, hex(num)[2:]))
else:
    print('OPCAO INVALIDA')