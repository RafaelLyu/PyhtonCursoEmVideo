Nome = str(input('Qual é seu nome completo?  ')).strip()
Primeiro = Nome.split()
print('Seu Nome é Minicuslo é', Nome.lower())
print('Seu Nome em Maisculo é', Nome.upper())
print('Seu Nome tem ', len(Nome)- Nome.count(' '), 'No total de letras')
print('Seu Primeiro Nome tem', len(Primeiro[0]), 'Letras')
