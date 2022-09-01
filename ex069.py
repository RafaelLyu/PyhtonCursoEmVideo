print('~'*20)
print('CADASTRO DE PESSOAS')
print('~'*20)
contI = 0
contF1 = 0
contM = 0
contF2 = 0
while True:
    idade = int(input('Qual é a sua idade? '))
    if idade > 18:
        contI += 1
    sexo = str(input('Qual o seu sexo? [M/F] '))
    if sexo not in 'MmFf':
        sexo = str(input('Qual o seu sexo? [M/F] '))
    if sexo in 'Ff' and idade >= 20:
        contF1 += 1
    if sexo in 'Mm' and idade <=20:
        contM += 1
    pergunta = str(input('Deseja continuar? [S/N]? ')).upper().strip()[0]
    if pergunta not in 'NnSs':
        pergunta = str(input('Deseja continuar? [S/N]? ')).upper().strip()[0]
    if pergunta in 'Nn':
            break
print(f'Tiveram {contM} Homens {contF1}, Mulheres com mais de 20 anos,{contF2} com menos de 20 anos e Deu {contI} De Maior ')