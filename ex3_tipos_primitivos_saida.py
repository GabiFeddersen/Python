n1=int(input('Digite um número: '))
n2=int(input('Digite mais um número: '))
s= n1 + n2
print('A soma vale: ', s)
print('Tipo do primeiro número', type(n1))
print('Tipo do segundo número', type(n2))
print('A soma entre ', n1,'e',n2, 'vale: ', s)
print('Outra forma de concatenação')
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
print(f'A soma entre {n1} e {n2} vale {s}')


