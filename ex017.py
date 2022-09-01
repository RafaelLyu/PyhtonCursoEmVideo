from math import hypot
A = float(input('Digite o valor do cateto adjacente: '))
O = float(input('Digite o valor do cateto opostos: '))
H = hypot(O, A)
print(f'O Comprimento da Hipotenusa desse triangulo é {H:.2f}')
