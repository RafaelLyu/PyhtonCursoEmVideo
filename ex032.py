from datetime import date
A = int(input('Qual ano Quer Analisar? Coloque 0 para Analisar o Ano atual: '))
if A == 0:
    A = date.today().year
if A % 4 == 0 and A % 100 != 0 or A % 400 == 0:
    print(f'O Ano {A} Digitado é bissexto')
else:
    print(f'O Ano {A} Não é Bissexto')
