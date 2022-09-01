S = 0
for c in range(1, 6 + 1):
    N = int(input('Digite um Número:'))
    if N % 2 == 0:
        S += N
print(f'O Somatario De TODOS os Numeros PARES FOI {S}')
