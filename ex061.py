A1 = int(input('A1:'))  # Primeiro Termo
R = int(input('Razão: '))  # Razão
T = A1  # Termos
cont = 1  # Contador
A10 = A1 + (10 - 1) * R  # Qualquer termo
while cont <= 10:
    print(f'{T}➝ ' , end='')
    T += R
    cont += 1
print('Acabou ')
