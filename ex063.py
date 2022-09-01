from ex061 import T


print('~'*30)
print('Sequência de Fibonacci')
print('~'*30)
N = int(input('Quantos termos você quer mostrar? ')) #Número real
N1 = 0 
N2 = 1
print('~'*30)
print(f'{N1} ➝ {N2}')
cont = 3
while cont <=  N:
    N3 = N1 + N2
    print(f'{N3} ➝', end='')
    N1 = N2
    N2 = N3
    cont += 1
    print('Concluida a sequencia de fibonnaci ')
