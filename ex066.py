N = S = 0
cont = 0
while True:
    N = int(input('Digite um Número: '))
    if N == 999:
        break
    cont += 1
    S += N
print(f'a soma dos Números Foi {S}')
