real = float(input('Quanto de dinheiro tenho? R$ '))
dolar = real / 4.87
euro = real / 5.28
peso_arg = real / 0.014 
print(f'Com R$ {real} posso comprar US$ {dolar:.2f}')
print(f'Com R$ {real} posso comprar € {euro:.2f}')
print(f'Com R$ {real} posso comprar $ {peso_arg:.2f}')