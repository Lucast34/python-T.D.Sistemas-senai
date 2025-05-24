# input
num1 = int(input("Digite um numero >> "))
num2 = int(input("Digite outro numero >> "))
num3 = int(input("Digite mais um numero >> "))

# sim eu sei que é um jeito idiota
if num1 > num2 and num1>num3:
    print(f'O maior numero: {num1}')
    if num2 > num3:
        print(f'Segundo maior: {num2}\nMenor: {num3}')
    else:
        print(f'Segundo maior: {num3}\nMenor: {num2}')
elif num2 > num1 and num2 > num3:
    print(f'O maior numero: {num2}')
    if num1 > num3:
        print(f'Segundo maior: {num1}\nMenor: {num3}')
    else:
        print(f'Segundo maior: {num3}\nMenor: {num1}')
else:
    print(f'O maior numero: {num3}')
    if num1 > num2:
        print(f'Segundo maior: {num1}\nMenor: {num2}')
    else:
        print(f'Segundo maior: {num2}\nMenor: {num1}')