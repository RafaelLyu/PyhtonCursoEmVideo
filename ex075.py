Numeros = (int(input('Digite o primeiro número: ')),
            int(input('Digite o segundo número:')),
            int(input('Digite o terceiro número:')),
            int(input('Digite o quarto número:')))
print(f'Você digitou os números {Numeros}')    
print(f'o Número 9 apareceu {Numeros.count(9)} vezes')
if 3 in Numeros:
    print(f'O Número 3 aparece na {Numeros.index(3)} posição')
else:
    print('O valor três não foi encontrado em nenhuma posição')
for n in Numeros:
    p = (int(input('Digite um valor: ')))
    if p % 2 == 0:
        print(n,end='')

