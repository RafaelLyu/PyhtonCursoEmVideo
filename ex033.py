P =int(input('Digite o Primeiro Número: '))
S =int(input('Digite o Segundo Número:'))
T =int(input('Digite o Terceiro Número: '))
#Verificando quem é o menor
menor = P
if S < P and S < T:
    menor = S
if T < P and T < S:
    menor = T
#Verificando Quem é o maior
maior = P
if  S > P and S > T:
    maior = S
if T > P and T >S :
    maior = T
print('-=-'*15)
print(f'O Menor valor digitado foi {menor}')
print(f'O Maior valor digitado foi {maior}')
print('-=-'*15)



