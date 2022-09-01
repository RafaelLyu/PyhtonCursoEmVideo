while True:
    num = int(input('Digite o numero que deseja saber a tabuada: ')) 
    if num > 0:
        for c in range(1,11):
            print(f'{num} x {c} = {num * c}')
    else:
        break
    