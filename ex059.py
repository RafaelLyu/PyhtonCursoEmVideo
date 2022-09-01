V1 = int(input('Digite o Primeiro Valor Número: '))
V2 = int(input('Digite O Segundo Valor Número: '))
opc = 0
sair = False
maior = 0
while not sair:
    print('''
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Escolher Números Novos
    [5]Sair Do Programa
    ''')
    opc = int(input('>>>> Qual a sua escolha? '))
    if opc == 1:
        print(f'A Soma entre  {V1} e {V2} valores é {V1 + V2}')
    if opc == 2:
        print(f'A Multiplicação entre {V1} e {V2} é {V1 * V2}')
    if opc == 3:
        maior = V1
        if V2 > V1:
            maior = V2
        print(f'O Numero {maior} é de maior valor ')
    if opc == 4:
        V1 = int(input('Digite o Primeiro Valor Número'))
        V2 = int(input('Digite O Segundo Valor Número'))
    if opc == 5:
        sair = True


     

