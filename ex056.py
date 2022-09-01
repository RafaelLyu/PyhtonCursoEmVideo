SI = 0
MI = 0
MIH = 0
NDV = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'========= {p}ª PESSOA =========')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    SI += idade
    if p == 1 and sexo in 'Mm':
        MIH = idade
        NDV = nome
    if sexo in 'Mm' and idade > MIH:
        MIH = idade
        NDV = nome
    if sexo in 'fF' and idade < 18:
        totmulher20 += 1
MI = SI / 4
print(f'A Media de idade das pessoas é {MI}')
print(f'O Homem mais VELHO Tem {MIH} e se chama {NDV}')
print(f' {totmulher20} Total de mulheres com menos de 18 anos')
