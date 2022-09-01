n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
m = (n1 + n2)/2
print(f'A Sua media foi {m:.1f}')
if m>= 6.0:
    print('Sua Média escolar foi boa! PARABENS')
else:
    print('Sua média escolar foi ruim! ESTUDE MAIS')
