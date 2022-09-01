numeros = list()
while True:
    numeros.append(int(input('Digite um Número:')))
    while True:
        p = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if p not in 'SN':
            print('Erro tente novamente')
        else:
            break   
    if p in 'N':
        break 
print(f'Foram digitados {len(numeros)} Números.')
numeros.sort(reverse=True)
print(f'Os números nas ordem descrescente {numeros}.')
if 5 in numeros:
    print('O número 5 apareceu na lista!')
else:
    print('O número 5 não apareceu na lista.')


       
