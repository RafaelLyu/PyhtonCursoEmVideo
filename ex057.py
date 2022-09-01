str(input('Digite o nome da pessoa:'))
S = str(input('Digite o sexo da pessoa [M/F]:')).strip().upper()[0]
while S not in 'MF':
    print('Sexo Incorreto')
    S = str(input('Digite o sexo da pessoa novamente [M/F]:')).strip().upper()
print('Sexo Correto')
