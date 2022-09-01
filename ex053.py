f = str(input('Frase: ')).strip().upper()
p = f.split()
junto = ''.join(p)
i = ''
for letra in range(len(junto) - 1, -1, -1):
    i += junto[letra]
print(f'O Inverso de {junto} é {i}')
if i == junto:
    print('Há um palíndromo')
else:
    print('a frase digitada não é um palíndromo')
