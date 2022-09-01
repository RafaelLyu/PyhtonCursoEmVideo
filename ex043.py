N = str(input('Qual é o Seu Nome ?: '))
A = float(input('Qual é a Sua Altura (M)? '))
P = float(input('Qual é o seu peso (KG)?  '))
IMC = P / (A**2) #Calculo IMC
print(f'Seu IMC é {IMC}')
if IMC < 18.5:
    print(f'Senhor(a) {N} está \033[30mabaixo do peso\033[m')
elif 18.5 <= IMC < 25:
    print(f'Senhor(a){N} Está no \033[31mPeso ideal\033[m ')
elif 25 <= IMC <= 30:
    print(f'Senhor(a) {N} Está no \033[32m sobrepeso \033[m')
elif 30 <= IMC < 40:
    print(f'Senhor(a){N} Está \033[33m Obesa \033[m')
else:
    print(f'Senhor(a) está na \033[34m Obesidade Mórbida \033[m')



