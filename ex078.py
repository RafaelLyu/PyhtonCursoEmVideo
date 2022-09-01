numeros = list()
maior = 0
menor = 0
for n in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {n}: ')))
    if n  == 0:
        maior = menor = numeros[n]
    else:    
        if numeros[n] > maior:
            maior = numeros[n]
        if  numeros[n] < menor:
            menor = numeros[n]
print(F'Você Digitou os valores {numeros}')
print(f'O maior número da lista é {maior} aparecendo nas posições ', end='') 
for  i , v in enumerate(numeros):
    if v == maior:
        print(f'{i}... ', end='')
print(f'O menor número da lista é o {menor} aparecendo nas posições ', end='') 
for  i , v in enumerate(numeros):
    if v == menor:
        print(f'{i}... ', end='')