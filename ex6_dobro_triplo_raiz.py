# Crie um algoritmo que leio o número e mostra o seu dobro, triplo e raiza quadrada 

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n**(1/2)
print(f'O dobro de {n} é {dobro}')
print(f'O triplo de {n} é {triplo}')
print(f'A raiz quadrada de {n} é {raiz:.3f}') 