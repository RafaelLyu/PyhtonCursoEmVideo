N = int(input('Digite o Número a qual deseja saber a tabuada: '))
M = int(input('Até quando a tabuada? '))
print('=-='*10)
for c in range(1, M+1):
    print(f'{N} x {c} = {N * c}')
print('=-='*10)
