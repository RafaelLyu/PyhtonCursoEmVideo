temp = list()
pessoas = list()
maior = menor = 0
while True:
    temp.append(str(input('Digite seu nome:')))
    temp.append(float(input('Digite seu peso:')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]       
    pessoas.append(temp[:])
    temp.clear()
    


    while True:
        p = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if p not in 'SN':
            print('Erro Digite Novamente...')
        else:
            break    
    if p in 'N':
        break
print(f'No total foram cadrastada {len(pessoas)}, peso de ',)
print(f'O Maior peso foi de {maior}KG Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'O Menor peso foi de {menor}KG. peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')



