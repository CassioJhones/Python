'''Python 026: Leia uma frase e
mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e
em que posição ela aparece a última vez.'''

frase = str(input('Digite seu frase: ')) #FRASE RECEBE UM INPUT DO TIPO STRING
frase = frase.upper() #FRASE É TRANSFORMADA EM UPPER(MAIUSCULA)
print('A letra A aparece {} vezes'.format(frase.count('A'))) # COUNT CONTA QUANTOS 'A' APARECEM EM FRASE
print('A primeira letra A apareceu na posição: {}'.format(frase.find('A')+1)) #FIND MOSTRA ONDE APARECE PRIMEIRO NO STR
print('A ultima letra A apareceu na posição: {}'.format(frase.rfind('A')+1)) #FIND MOSTRA ONDE APARECE PRIMEIRO NO STR
