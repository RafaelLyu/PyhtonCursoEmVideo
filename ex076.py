papelaria = ('Lapís', 1.50,
            'Borracha', 2,
            'Caderno', 20,
            'Caneta', 3,
            'Mochila', 100,)
print('=-='*13)
print(f'{"PAPELARIA DO LYU":^40}')
print('=-='*13)
for posição in range(0,len(papelaria)):
    if posição % 2 == 0:
        print(f'{papelaria[posição]:.<30}', end='')
    else:
         print(f'R${papelaria[posição]:.>2.2f}')


