matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somarpar = maior = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um Valor Númerico para [{l}, {c}]: '))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somarpar+= matriz[l][c]
    print()
print('=-' * 30)
print(f'a Soma dos valores pares é {somarpar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A Soma da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segunda coluna é {maior}')
