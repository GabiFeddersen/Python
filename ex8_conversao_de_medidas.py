# Escreva um programa que leia um valor em metro e faça a coversao para centimetros e milimetros

metros = float(input('Digite a metragem: '))
cm = metros * 100
ml = metros *1000
print(f'{metros:.2f} metros possui {cm:.2f} centimetros')
print(f'{metros:.2f} metros possui {ml:.2f} melimetros')
