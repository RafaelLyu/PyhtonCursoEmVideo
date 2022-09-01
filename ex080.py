numeros = list()
for n in range (0,5):
    v = int(input('Digite um valor: '))
    if n == 0 or v > numeros[-1]:
        numeros.append(v)
    else:
        pos = 0
        while pos < len(numeros):
            if v <= numeros[pos]:
                numeros.insert(pos, v)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {numeros}')     
    

