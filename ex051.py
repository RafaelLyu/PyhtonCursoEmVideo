A1 = int(input('A1: '))
R = int(input('R: '))
A10 = A1 + (10 - 1) * R
for c in range(A1, A10 + R, R):
    print(c, end='➔ ')
print('FINALIZADO')
