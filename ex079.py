numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n in numeros:
        print('Número já existente na lista')
    else: 
        print('Número adicionado')
        numeros.append(n)  
    while True:
        p = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
        if p not in 'SN':
            print('Erro Digite Novamente...')
        else:
            break    
    if p in 'N':
        break
numeros.sort()
print(f'Os valores digitados foram {numeros} ')    
