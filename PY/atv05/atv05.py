# função

def multiplacao(*numeros):
    resultado = 1

    for numero in numeros:
        resultado *= numero
    
    return f'O resultado foi {resultado}'

print(multiplacao(2,2))
