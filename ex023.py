Num = int(input('Digite Um Numero De 0 A 9999: '))
u = Num // 1 % 10
d = Num // 10 % 10
c = Num // 100 % 10
m = Num // 1000 % 10
print(f'Analisando o seu numero : {Num}')
print(m , 'Milhares')
print(c, 'Centenas')
print(d, 'Dezenas')
print(u, 'Unidades')

