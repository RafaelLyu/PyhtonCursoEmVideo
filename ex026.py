frase = str(input('Digite Uma frase: ')).lower().strip()
print('Apareceu', frase.count('a'), 'Vezes')
print('Apareceu na posição', frase.find('a')+1), 'a primeira vez'
print('A Ultima letra A  Apareceu na posição {}'.format(frase.rfind('a')+1))
