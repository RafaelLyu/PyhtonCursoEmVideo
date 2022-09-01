numeros = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)   
    while True:
        p = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if p not in 'SN':
            print('Erro tente novamente')
        else:
            break   
    if p in 'N':
        break 
print(f'Os Números Foram {numeros}')  
print(f'Os Números IMPARES foram {impar}')  
print(f'Os Números PARES foram {par}')