A1 = int(input('A1:')) #Primeiro Termo
R = int(input('R:')) #Razão
T = A1 # Termos
total = 0
cont = 1 #Contador
mais = 10
while mais != 0:
    total = total + mais
    while cont <= 10:
        print(f'{T}➝ ',end='')
        T += R
        cont += 1
    mais = int(input('Quantos termos você quer mostrar a mais ? '))
print(f'Progressão terminado com {total} Termos')